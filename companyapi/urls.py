from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home_page),  # Home page route
    path('', home_page),  # Root URL redirects to home page
    path("api/v1/", include("api.urls")),  # API routes
    path('', include('function.urls')),  # Include function app URLs
]
