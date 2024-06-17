# Placeholder script for  OCR model
import argparse
from PIL import Image
import pytesseract

def predict(image_path):
    image = Image.open(image_path)
    employee_id = pytesseract.image_to_string(image)
    print(f"Predicted Employee ID: {employee_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict Employee ID from image")
    parser.add_argument("--image_path", type=str, required=True, help="Path to the image")

    args = parser.parse_args()
    predict(args.image_path)
