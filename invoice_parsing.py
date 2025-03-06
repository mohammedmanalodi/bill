
import os
import re
import json
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from paddleocr import PaddleOCR
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

# ---------------- STEP 1: RUN OCR WITH PADDLEOCR ---------------- #

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")

# Load Invoice Image
image_path = "/path/to/your/invoice.png"  # Replace with actual path
ocr_results = ocr.ocr(image_path, cls=True)

# Extract text from OCR results
extracted_text = "\n".join([word[1][0] for line in ocr_results for word in line])

# Clean OCR text: Remove multiple spaces and unnecessary characters
extracted_text = re.sub(r"\s+", " ", extracted_text).strip()

# Print extracted text for debugging
print("Extracted Text:\n", extracted_text)

# ---------------- STEP 2: USE MISTRAL-7B MODEL FOR INVOICE PARSING ---------------- #

# Load Mistral-7B Model & Tokenizer
model_id = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Set device to CPU (or CUDA if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Function to Use Mistral AI for Smart Invoice Parsing
def parse_invoice_with_mistral(raw_text):
    prompt = f'''
    Extract structured invoice details in JSON format with fields:
    - Invoice Number, Invoice Date, Customer Name, Customer Address
    - Purchased Items (Item Names, Quantity, Price)
    - SGST, CGST, Tax Total, Full Total

    Extracted Invoice Text:
    {raw_text}

    Return structured JSON output.
    '''

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(device)

    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=500, do_sample=True, temperature=0.5)

    structured_json = tokenizer.decode(output[0], skip_special_tokens=True)

    try:
        structured_invoice = json.loads(structured_json)
    except json.JSONDecodeError:
        print("\n⚠️ AI Parsing Failed! Returning raw text instead.")
        return {"error": "Mistral AI failed to structure the data", "raw_text": raw_text}

    return structured_invoice

# Use Mistral AI for final structuring
structured_invoice = parse_invoice_with_mistral(extracted_text)

# ---------------- STEP 3: SAVE RESULTS ---------------- #

# Print Final Extracted Invoice
print("\n🧾 Final Extracted Invoice:")
print(json.dumps(structured_invoice, indent=4))

# Save extracted data to a JSON file
output_file = "invoice_extracted_data.json"
with open(output_file, "w") as f:
    json.dump(structured_invoice, f, indent=4)

# Convert extracted data to a Pandas DataFrame for visualization
df_invoice = pd.DataFrame.from_dict(structured_invoice, orient="index", columns=["Extracted Value"])

# Save as CSV
df_invoice.to_csv("invoice_extracted_data.csv")

print(f"Extracted invoice data saved to: {output_file} and invoice_extracted_data.csv")
