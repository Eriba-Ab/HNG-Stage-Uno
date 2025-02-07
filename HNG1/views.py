from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def classify_number(request):
    number = request.GET.get('number', None)

    # Input validation
    if not number:
        return HttpResponse('{"number": "Invalid input", "error": true}', content_type="application/json", status=400)

    try:
        # Attempt to parse the input into an integer
        num_int = int(number)
    except ValueError:
        # Handle non-numeric inputs
        return HttpResponse('{"number": "alphabet", "error": true}', content_type="application/json", status=400)

    # Prime check
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(abs(n) ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Armstrong number check
    def is_armstrong(n):
        num_str = str(abs(n))  # Use absolute value for Armstrong check
        return n == sum(int(digit) ** len(num_str) for digit in num_str)

    # Calculate digit sum
    digit_sum = sum(int(d) for d in str(abs(num_int)))  # Sum of digits for absolute value

    # Fetching fun fact from Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{num_int}")
        fun_fact = response.text if response.status_code == 200 else "No fun fact available"
    except:
        fun_fact = "No fun fact available"

    # Constructing the response
    response_data = {
        "number": num_int,
        "is_prime": is_prime(num_int),
        "is_armstrong": is_armstrong(num_int),
        "digit_sum": digit_sum,  # sum of its digits
        "fun_fact": fun_fact  # gotten from the Numbers API
    }

    # Return the response
    return JsonResponse(response_data)