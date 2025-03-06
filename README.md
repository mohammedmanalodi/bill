# bill
This project uses PaddleOCR to extract text from invoice images and an LLM (Large Language Model) for smart invoice parsing. It processes the extracted text to identify the crucial points in a bill and structures the data accordingly.


# Invoice OCR Parsing with PaddleOCR and Mistral-7B

This project uses PaddleOCR to extract text from invoice images and Mistral-7B for smart invoice parsing to extract structured data such as:
- Invoice Number
- Invoice Date
- Customer Name
- Customer Address
- Purchased Items (Item Names, Quantity, Price)
- SGST, CGST, Tax Total, Full Total

## Requirements
- PaddleOCR
- Transformers
- PyTorch
- Pandas
- Pillow

## Installation
To install the necessary dependencies, run the following:

```
pip install -r requirements.txt
```

## Usage
1. Place your invoice image (e.g., `invoice.png`) in the project directory.
2. Run the `invoice_parsing.py` script:
```
python invoice_parsing.py
```
This will extract and parse the invoice details, saving them as `invoice_extracted_data.json` and `invoice_extracted_data.csv`.

## License
This project is licensed under the MIT License.
