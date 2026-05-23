# OCR Vision API

A Python project for extracting text from images using Google Cloud Vision API. The project reads an image from local storage, converts it into Base64 format, sends it to the Google Vision REST endpoint, and returns the extracted text from the image.

## Project Overview

This repository is focused on optical character recognition using Google Cloud Vision. The main OCR script is `google_ocr.py`. It loads a Google API key from a `.env` file, reads an image, sends the encoded image to Google Vision API, and prints the detected text.

The repository also contains supporting files such as customer sample data and an experimental office monitoring script. The office monitoring script is separate from the OCR workflow and uses camera input, YOLO, tracking, and pose estimation ideas.

## Repository Link

```text
https://github.com/mirazchowdhury/ocr_vision_api
```

## Main Features

1. Reads API key from environment variables.
2. Loads local image files from a given path.
3. Converts image files into Base64 encoded strings.
4. Sends image data to Google Cloud Vision API.
5. Uses `DOCUMENT_TEXT_DETECTION` for better dense text and handwritten document extraction.
6. Returns full extracted text from the `fullTextAnnotation` response.
7. Handles missing image files with a clear error message.
8. Handles empty OCR responses.
9. Handles API request errors.
10. Includes sample customer sales data in JSON format.
11. Includes an experimental office activity monitoring script using YOLO pose tracking.

## Repository Structure

```text
ocr_vision_api/
    .env
    Vision API.txt
    customer_data.json
    google_ocr.py
    office_monitoring.txt
    requirements.txt

    sources_data/
        image files used for OCR testing

    .idea/
        IDE project files
```

## File Description

## google_ocr.py

This is the main OCR script.

Main responsibilities:

1. Loads the Google API key from `.env`.
2. Opens a local image file in binary mode.
3. Encodes the image content into Base64.
4. Creates a Google Vision API request payload.
5. Sends the request to the Google Vision API endpoint.
6. Reads extracted text from the response.
7. Prints the final OCR result in the terminal.

Core function:

```python
perform_google_ocr(image_path)
```

The function receives an image path and returns the detected text.

## requirements.txt

The repository dependency file contains:

```text
python-dotenv
requests
```

These two packages are enough for the main OCR script.

## customer_data.json

This file contains sample retail customer order data. Each record includes customer id, customer name, item name, item id, item code, quantity, order date, and discount information.

This file is not required for the OCR script, but it may be useful for future integration where extracted OCR text is connected with customer or sales records.

## office_monitoring.txt

This file contains an experimental computer vision script for office monitoring. It includes ideas such as:

1. Connecting to an RTSP camera stream.
2. Loading a YOLO pose model.
3. Detecting people in a room.
4. Tracking people using BoT SORT.
5. Estimating simple activities such as walking, standing, sitting, and using a computer.
6. Displaying people count on live camera frames.

This script is separate from the OCR pipeline.

## Vision API.txt

This file appears to contain a Google Vision API key. For security reasons, API keys should not be stored in public repositories. Revoke the exposed key from Google Cloud Console, create a new key, and keep the new key only in a local `.env` file.

## Important Security Warning

The repository includes sensitive credentials in visible files. Before using this project with real accounts or cloud billing, do the following:

1. Revoke the exposed Google Vision API key.
2. Create a new API key in Google Cloud Console.
3. Store the new key inside `.env`.
4. Never commit `.env` to GitHub.
5. Add `.env` to `.gitignore`.
6. Remove `Vision API.txt` from version control.
7. Do not commit RTSP camera usernames, passwords, or local network addresses.
8. Rotate any camera password that was committed publicly.

Recommended `.gitignore` entries:

```text
.env
Vision API.txt
__pycache__/
*.pyc
.idea/
sources_data/
```

## Prerequisites

Before running the project, make sure you have:

1. Python 3.10 or higher.
2. A Google Cloud project.
3. Google Cloud Vision API enabled.
4. A valid Google Vision API key.
5. A local image file for OCR testing.
6. Internet connection for calling Google Vision API.

## Google Cloud Vision Setup

Follow these steps:

1. Open Google Cloud Console.
2. Create a new project or choose an existing project.
3. Enable Cloud Vision API.
4. Create an API key from the credentials section.
5. Restrict the API key to Cloud Vision API.
6. Copy the API key.
7. Store it inside a local `.env` file.

Example `.env` file:

```env
GOOGLE_API_KEY=your_google_vision_api_key_here
```

## Installation

Clone the repository.

```bash
git clone https://github.com/mirazchowdhury/ocr_vision_api.git
cd ocr_vision_api
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment on Windows.

```bash
.venv\Scripts\activate
```

Activate the virtual environment on Linux or macOS.

```bash
source .venv/bin/activate
```

Upgrade pip.

```bash
python -m pip install --upgrade pip
```

Install dependencies.

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_vision_api_key_here
```

Update the image path inside `google_ocr.py`.

Example:

```python
my_image = r"sources_data/sample_image.jpeg"
```

For Windows absolute path:

```python
my_image = r"C:\Users\YourName\Pictures\sample_image.jpeg"
```

For Linux or macOS path:

```python
my_image = "sources_data/sample_image.jpeg"
```

## How to Run OCR

Run the main script.

```bash
python google_ocr.py
```

Expected terminal output:

```text
Scanning 'sources_data/sample_image.jpeg'
----------------------------------------
EXTRACTED TEXT:
----------------------------------------
Detected text will appear here
----------------------------------------
```

## How the OCR Function Works

The OCR process follows this flow:

```text
Image file
    Read image in binary mode
        Encode image with Base64
            Create Google Vision request payload
                Send request to images annotate endpoint
                    Parse fullTextAnnotation
                        Return extracted text
```

## Example Function Usage

You can also import and use the OCR function in another Python file.

```python
from google_ocr import perform_google_ocr

image_path = "sources_data/sample_image.jpeg"
text = perform_google_ocr(image_path)

print(text)
```

## Google Vision Request Type

The script uses:

```text
DOCUMENT_TEXT_DETECTION
```

This request type is suitable for:

1. Documents.
2. Dense printed text.
3. Handwritten notes.
4. Paper based forms.
5. Cards and notices.
6. Images where full text extraction is needed.

## Error Handling

The script handles the following cases:

1. API key missing from `.env`.
2. Image file not found.
3. Empty response from Google Vision API.
4. No text detected in the image.
5. API request failure with status code and response text.

## Current Code Formatting Note

The visible source may need line formatting cleanup before execution if it appears as one collapsed line in an editor. The logic is clear, but Python import statements and function blocks must be placed on separate lines.

A clean starter structure should look like this:

```python
import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
```

## Suggested Clean Version of google_ocr.py

```python
import os
import base64
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found in .env file.")


def perform_google_ocr(image_path: str) -> str:
    url = f"https://vision.googleapis.com/v1/images:annotate?key={API_KEY}"

    try:
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        return f"Error: File '{image_path}' not found."

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

    response = requests.post(url, json=payload, timeout=60)

    if response.status_code != 200:
        return f"API Error: {response.status_code} {response.text}"

    result = response.json()
    responses = result.get("responses", [])

    if not responses:
        return "Empty response from Google."

    full_text = responses[0].get("fullTextAnnotation", {}).get("text", "")

    if not full_text:
        return "No text detected in this image."

    return full_text


if __name__ == "__main__":
    image_path = "sources_data/sample_image.jpeg"
    extracted_text = perform_google_ocr(image_path)

    print("=" * 40)
    print("EXTRACTED TEXT")
    print("=" * 40)
    print(extracted_text)
```

## Turning This Script Into a Web API

The repository name says API, but the current OCR logic is mainly a Python script that calls Google Vision API. To expose it as a local API, FastAPI can be added.

Suggested endpoint:

```text
POST /ocr
```

Suggested request:

```json
{
    "image_path": "sources_data/sample_image.jpeg"
}
```

Suggested response:

```json
{
    "success": true,
    "text": "Detected text from the image"
}
```

## Optional FastAPI Example

Install FastAPI and Uvicorn.

```bash
pip install fastapi uvicorn python-multipart
```

Create a file named `app.py`.

```python
from fastapi import FastAPI
from pydantic import BaseModel
from google_ocr import perform_google_ocr


app = FastAPI(title="OCR Vision API")


class OCRRequest(BaseModel):
    image_path: str


@app.get("/")
def root():
    return {"message": "OCR Vision API is running"}


@app.post("/ocr")
def extract_text(request: OCRRequest):
    text = perform_google_ocr(request.image_path)
    return {
        "success": True,
        "text": text
    }
```

Run the API.

```bash
uvicorn app:app --reload
```

Open the API documentation.

```text
http://127.0.0.1:8000/docs
```

## Optional Office Monitoring Setup

The `office_monitoring.txt` file can be converted into a Python file if you want to test the camera monitoring experiment.

Suggested file name:

```text
office_monitoring.py
```

Extra dependencies may be needed:

```bash
pip install opencv-python ultralytics cvzone
```

The script uses:

1. OpenCV for camera stream reading.
2. Ultralytics YOLO for person detection and pose estimation.
3. BoT SORT for tracking.
4. cvzone for drawing labels on frames.

Security note:

Do not write camera username, password, and IP address directly in code. Use environment variables instead.

Example `.env` values:

```env
CAMERA_USER=your_camera_user
CAMERA_PASSWORD=your_camera_password
CAMERA_IP=192.168.1.10
```

## Sample Customer Data Use

The `customer_data.json` file can be used later to connect OCR extracted receipts or invoices with sales records.

Possible future use cases:

1. Extract product names from receipts.
2. Match extracted product names with item catalog.
3. Match customer information from scanned documents.
4. Create purchase history from image based receipts.
5. Combine OCR results with recommendation systems.

## Common Issues and Fixes

## API key not found

Cause:

`.env` file is missing or `GOOGLE_API_KEY` is not set.

Fix:

Create `.env` in the project root and add:

```env
GOOGLE_API_KEY=your_google_vision_api_key_here
```

## Image file not found

Cause:

The image path is wrong.

Fix:

Use a correct relative or absolute image path.

```python
my_image = "sources_data/sample_image.jpeg"
```

## API returns permission error

Cause:

Cloud Vision API is not enabled or the API key is restricted incorrectly.

Fix:

Enable Cloud Vision API in Google Cloud Console and check API key restrictions.

## No text detected

Cause:

The image may be blurry, dark, rotated, cropped, or contain very small text.

Fix:

Use a clearer image with higher resolution and proper lighting.

## Syntax error in google_ocr.py

Cause:

The file may have collapsed code formatting.

Fix:

Reformat the file using the clean version shown in this README.

## Limitations

1. The current project does not include a running Flask or FastAPI server by default.
2. The OCR script reads a local file path rather than uploaded files.
3. The exposed API key must be revoked and replaced.
4. The OCR output is raw text only.
5. No post processing is applied to clean extracted text.
6. No language selection is added in the request.
7. No batch OCR endpoint is included.
8. No automated tests are included.
9. The office monitoring code is mixed into a text file and should be separated from the OCR project.

## Recommended Improvements

1. Add a proper FastAPI service.
2. Add image upload support.
3. Add batch OCR support.
4. Add JSON response formatting.
5. Add OCR text cleanup.
6. Add confidence score extraction.
7. Add support for Bangla and English document workflows.
8. Add request logging.
9. Add exception logging.
10. Add Docker support.
11. Move sample images into a separate ignored data folder.
12. Remove all secrets from Git history.
13. Add unit tests for OCR response parsing.
14. Add a clear API documentation page.
15. Add a sample image and sample response without private data.

## Suggested Production Structure

```text
ocr_vision_api/
    app/
        api/
            routes.py
        core/
            config.py
        services/
            google_vision_service.py
        schemas/
            ocr_schema.py

    samples/
    tests/
    .env.example
    .gitignore
    requirements.txt
    README.md
```

## License

No license file was visible in the repository at the time this README was prepared. Add a license file before public reuse or commercial use.

## Author

Miraj Uddin Chowdhury

Repository:

```text
https://github.com/mirazchowdhury/ocr_vision_api
```
