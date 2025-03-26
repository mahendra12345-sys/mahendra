from django.urls import path
from .views import login_page, home_page

urlpatterns = [
    path('', home_page, name='home'),  # Home page
    path('login/', login_page, name='login'),  # Login page
]
