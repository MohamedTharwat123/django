from django.urls import path
from .views import payment_view


app_name = "payment"  # payment:pay
urlpatterns = [
    path("", payment_view, name="pay"),
]
