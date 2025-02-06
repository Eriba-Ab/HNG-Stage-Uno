from django.urls import path
from .views import classify_number

urlpatterns = [
    path('api/classify-number', classify_number),
]
git add <conflicting_file>