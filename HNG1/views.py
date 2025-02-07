from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def classify_number(request):
    number = request.GET.get('number', None)

    # Input validation
    if not number:
        return JsonResponse({"number": "Invalid input", "error": True}, status=400)
    
    try:
        # Try converting to a float to catch decimals
        num_float = float(number)

        # Check for decimals
        if not num_float.is_integer():
            return JsonResponse({"number": "decimal", "error": True}, status=400)

        # Convert to integer
        num_int = int(num_float)

        # Check for negative numbers
        if num_int < 0:
            return JsonResponse({"number": "negative", "error": True}, status=400)

    except ValueError:
        # Handle alphabets or other non-numeric inputs
        return JsonResponse({"number": "alphabet", "error": True}, status=400)

    # Prime check
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Perfect number check
    def is_perfect(n):
        if n < 2:
            return False
        divisors_sum = sum([i for i in range(1, n // 2 + 1) if n % i == 0])
        return divisors_sum == n

    # Armstrong number check
    def is_armstrong(n):
        num_str = str(n)
        return n == sum(int(digit) ** len(num_str) for digit in num_str)

    # Calculate digit sum
    digit_sum = sum(int(d) for d in str(num_int))

    # Properties
    properties = []
    if is_prime(num_int):
        properties.append("prime")
    if is_perfect(num_int):
        properties.append("perfect")
    if is_armstrong(num_int):
        properties.append("armstrong")
    if num_int % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Fetching fun fact from Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{num_int}")
        fun_fact = response.text if response.status_code == 200 else "No fun fact available"
    except:
        fun_fact = "No fun fact available"

    # JSON response
    return JsonResponse({
        "number": num_int,
        "is_prime": is_prime(num_int),
        "is_perfect": is_perfect(num_int),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }, status=200)
