from django.urls import path
from .views import register, user_login, user_logout,home, dashboard


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),  # Homepage URL
    path('dashboard/', dashboard, name='dashboard'),

]
from .views import book_bus

urlpatterns += [
    path('book/', book_bus, name='book_bus'),
]
