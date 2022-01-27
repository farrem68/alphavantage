from django.contrib import admin
from django.urls import path

from rest_framework.authtoken import views
import quotes.views as quote_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path("api/v1/quotes/", quote_views.quotes )
]
