from django.urls import path

from .import views

urlpatterns = [
    path('user/', views.register_by_access_token)
]
