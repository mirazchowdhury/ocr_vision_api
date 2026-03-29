import os
import base64
import requests
import json
from dotenv import load_dotenv

# 1. Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env file.")
    exit()


def perform_google_ocr(image_path):
    """
    Sends image to Google Cloud Vision API using the REST endpoint.
    Best for: Handwriting, Papers, E-cards.
    """
    # URL for the Google Vision API
    url = f"https://vision.googleapis.com/v1/images:annotate?key={API_KEY}"

    # 2. Load and Encode Image
    try:
        with open(image_path, "rb") as image_file:
            # Google requires the image to be Base64 encoded strings
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        return f"Error: File '{image_path}' not found."

    # 3. Create the JSON Payload
    # We use 'DOCUMENT_TEXT_DETECTION' because it is better for handwriting
    # and dense text than standard 'TEXT_DETECTION'.
    payload = {
        "requests": [
            {
                "image": {
                    "content": base64_image
                },
                "features": [
                    {
                        "type": "DOCUMENT_TEXT_DETECTION"
                    }
                ]
            }
        ]
    }

    # 4. Send the Request
    print(f"Scanning '{image_path}'...")
    response = requests.post(url, json=payload)

    # 5. Parse the Response
    if response.status_code == 200:
        result = response.json()

        # Google returns a list of responses (one per image sent)
        responses = result.get("responses", [])
        if responses:
            # The 'fullTextAnnotation' field contains the complete string
            full_text = responses[0].get("fullTextAnnotation", {}).get("text", "")

            if full_text:
                return full_text
            else:
                return "No text detected in this image."
        else:
            return "Empty response from Google."
    else:
        return f"API Error: {response.status_code} - {response.text}"


# --- Test the Script ---
if __name__ == "__main__":
    # The 'r' tells Python to ignore escape characters
    my_image = r"C:\D drive\OCR_VISION_API\sources_data\WhatsApp Image 2026-02-09 at 6.02.31 PM.jpeg"

    extracted_text = perform_google_ocr(my_image)

    print("-" * 40)
    print("EXTRACTED TEXT:")
    print("-" * 40)
    print(extracted_text)
    print("-" * 40)