from django.urls import path
from .views import ChatMessageListCreateView

urlpatterns = [
    path('', ChatMessageListCreateView.as_view(), name='chat-message-list-create'),
]
