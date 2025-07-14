from django.urls import path
from .views import LoginAPIView, FormAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('forms/', FormAPIView.as_view()),
]
