from django.urls import path
from .views import HomePageBaseView

urlpatterns = [
    path('', HomePageBaseView.as_view(), name='base'),
]