
# Bill Extraction Using LLM Models

## Overview

This project combines Optical Character Recognition (OCR) and Large Language Models (LLMs) to automate the process of extracting and structuring data from invoices. The primary goal of the project is to extract relevant information from invoices (such as invoice number, date, customer details, and purchased items) and store this data in a structured JSON and CSV format.

The OCR component of the project uses **PaddleOCR**, which is responsible for converting the text from the invoice image into raw text. After that, the **Mistral-7B** language model is used to intelligently parse the extracted text and identify key fields from the invoice.

This system can be particularly useful for automating the extraction of data from invoices for use in accounting, data analysis, or other business applications.

---

## Key Features

- **OCR with PaddleOCR**: The system extracts raw text from scanned or photographed invoices using **PaddleOCR**. This includes text with various fonts, orientations, and layouts.
  
- **Smart Parsing with Mistral-7B**: The raw text is then processed by the **Mistral-7B** language model to intelligently extract structured data, including:
  - Invoice Number
  - Invoice Date
  - Customer Name
  - Customer Address
  - Purchased Items (Item Names, Quantity, Price)
  - SGST, CGST, Tax Total, Full Total
  
- **Output**: The extracted invoice data is saved in both **JSON** and **CSV** formats for easy integration into other systems or for further analysis.

---

## Requirements

The following Python libraries are required to run the project:

- **PaddleOCR**: A powerful OCR library for extracting text from images.
- **Transformers**: A library from Hugging Face to work with pre-trained language models, including Mistral-7B.
- **PyTorch**: Deep learning framework used to run the Mistral-7B model.
- **Pandas**: A data manipulation library to manage and save the extracted data in tabular form.
- **Pillow**: Python Imaging Library (PIL) for handling image processing.

### Installation

To install all the necessary dependencies, you can create a virtual environment and then install the requirements by running:

1. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv env
   ```

2. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source env/bin/activate
     ```

3. **Install the dependencies**:
   Download or clone this repository, and then install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Installation Requirements (`requirements.txt`)

The `requirements.txt` file includes all the necessary dependencies for the project. Here is its content:

```txt
torch
paddlepaddle
transformers
pandas
opencv-python
Pillow
```

---

## Usage

### Step 1: Prepare Your Invoice Image

Ensure that the invoice image is available in the project directory. The script is designed to handle images in common formats such as `.png`, `.jpg`, `.jpeg`. Make sure the image is clear, with legible text for better OCR accuracy.

### Step 2: Run the Invoice Parsing Script

1. **Place your invoice image** (e.g., `invoice.png`) in the root directory of this project.

2. **Run the Invoice Parsing Script**: The script `invoice_parsing.py` is designed to process the invoice image, extract the text, and parse it using the Mistral-7B model. You can run the script using the following command:

   ```bash
   python invoice_parsing.py
   ```

3. **Result**: The script will perform the following operations:
   - Extract text from the image using **PaddleOCR**.
   - Parse the extracted text using **Mistral-7B** to identify key fields from the invoice.
   - Save the structured invoice data in **JSON** format in a file named `invoice_extracted_data.json`.
   - Save the same data in **CSV** format in a file named `invoice_extracted_data.csv`.

### Example of Extracted JSON Output

The final JSON structure for an invoice might look like this:

```json
{
  "Invoice Number": "12345",
  "Invoice Date": "2025-03-07",
  "Customer Name": "John Doe",
  "Customer Address": "123 Main Street, City, Country",
  "Purchased Items": [
    {"Item Name": "Laptop", "Quantity": 1, "Price": 1000},
    {"Item Name": "Mouse", "Quantity": 2, "Price": 20}
  ],
  "SGST": 18,
  "CGST": 18,
  "Tax Total": 36,
  "Full Total": 1056
}
```

### Example of Extracted CSV Output

The data will also be saved in a CSV file, which will look something like this:

| Field                | Extracted Value                |
|----------------------|--------------------------------|
| Invoice Number       | 12345                          |
| Invoice Date         | 2025-03-07                     |
| Customer Name        | John Doe                       |
| Customer Address     | 123 Main Street, City, Country |
| Item 1 Name          | Laptop                         |
| Item 1 Quantity      | 1                              |
| Item 1 Price         | 1000                           |
| Item 2 Name          | Mouse                          |
| Item 2 Quantity      | 2                              |
| Item 2 Price         | 20                             |
| SGST                 | 18                             |
| CGST                 | 18                             |
| Tax Total            | 36                             |
| Full Total           | 1056                           |

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgements

- **PaddleOCR**: [PaddleOCR GitHub](https://github.com/PaddlePaddle/PaddleOCR) – Optical character recognition library used to extract text from images.
  
- **Mistral-7B**: [Mistral-7B Model](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) – Large language model used to parse extracted text into structured data.

- **Hugging Face**: [Transformers](https://huggingface.co/transformers/) – Library for pre-trained transformers models.

- **OpenAI**: For the original inspiration behind utilizing language models for parsing tasks.

---

## Contact Information

If you have any questions or suggestions regarding this project, feel free to reach out to me at mohammedmanalodi@gmail.com.

---

