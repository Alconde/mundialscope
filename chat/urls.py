from django.urls import path
from .views import ChatConversationListView, ChatConversationDetailView

app_name = "chat"

urlpatterns = [
    path("", ChatConversationListView.as_view(), name="chat-list"),
    path("<int:pk>/", ChatConversationDetailView.as_view(), name="chat-detail"),
]