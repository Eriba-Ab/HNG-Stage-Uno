from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def digit_sum(n):
    return sum(int(d) for d in str(n))

@require_GET
def classify_number(request):
    try:
        number = int(request.GET.get('number', ''))
    except ValueError:
        return JsonResponse({"number": request.GET.get('number'), "error": True}, status=400)
    
    properties = []
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")

    # Fetch fun fact from Numbers API
    fun_fact_url = f"http://numbersapi.com/{number}/math"
    fun_fact_response = requests.get(fun_fact_url)
    fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact available."

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }
    return JsonResponse(response, status=200)
