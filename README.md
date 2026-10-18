# Pincode Lookup API

A REST API built with Python and FastAPI to look up Indian PIN codes and support bulk PIN code lookups.

## Features

- Look up a single PIN code
- Bulk PIN code lookup (up to 20 codes per request)
- Validate six-digit PIN code format
- Custom error handling for invalid or unavailable PIN codes
- Interactive API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Run Locally

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the API:

   ```bash
   uvicorn main:app --reload
   ```

5. Open `http://127.0.0.1:8000/docs` in your browser.

## Endpoints

- `GET /pincode/{code}` — Look up one PIN code.
- `POST /pincode/bulk` — Look up multiple PIN codes.

## Purpose

This project demonstrates REST API development, input validation, bulk processing, and error handling using FastAPI.