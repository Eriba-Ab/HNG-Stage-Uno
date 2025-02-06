# Number Classification API

## Project Description
The Number Classification API is a Django-based RESTful API that accepts a number as input and returns interesting mathematical properties about it, along with a fun fact sourced from the Numbers API.

---

## Features
- Checks if the number is prime, perfect, or an Armstrong number.
- Calculates the digit sum of the number.
- Fetches a fun fact about the number using the Numbers API.
- Handles invalid inputs gracefully with appropriate error responses.
- CORS-enabled for cross-origin requests.

---

## Technology Stack
- **Backend**: Django (Python)
- **CORS Handling**: django-cors-headers
- **External API**: [Numbers API](http://numbersapi.com/)

---

## API Specification

### Endpoint
`GET https://hng-stage-uno.onrender.com/api/classify-number?number=put a number here`

### Query Parameters
- `number` (required): An integer value to classify.

### Response Formats

#### Success (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

---

## Installation and Setup

### Prerequisites
- Python 3.8+
- Pip
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

The API will be accessible at `http://127.0.0.1:8000/api/classify-number`.

---

## Deployment

To deploy the API to a production environment:

1. Choose a hosting platform (e.g., Heroku, AWS, PythonAnywhere).
2. Configure the Django settings for production.
3. Set up a WSGI server (e.g., Gunicorn) and reverse proxy (e.g., Nginx).
4. Ensure the API is accessible and CORS is enabled.

---

## Example Usage

### Request
```http
GET http://127.0.0.1:8000/api/classify-number?number=371
```

### Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

---

## Error Handling
- If the `number` parameter is missing or invalid, the API responds with a `400 Bad Request` error.

Example:
```http
GET http://127.0.0.1:8000/api/classify-number?number=abc
```
Response:
```json
{
    "number": "alphabet",
    "error": true
}
```

---

## Testing
Run the test suite to ensure functionality:
```bash
python manage.py test
```

---

## License
This project is licensed under the MIT License. Feel free to use and modify it.

---

## Acknowledgments
- [Numbers API](http://numbersapi.com/) for providing fun facts.
- Django documentation for guidance.

---

## Contact
For questions or feedback, feel free to reach out at [your-email@example.com].

