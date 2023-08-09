from django.contrib import admin
from django.urls import path
from chat import views

# from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    path("chat/", views.chatRoom, name="chatRoom"),
    path("messages/", views.messages, name="message"),
    path('messages/<int:messages_id>/', views.message_detail, name='messageDetail'),
    path('messages/create/', views.MessageCreate.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', views.MessageUpdate.as_view(), name='messages_update'),
    path('messages/<int:pk>/delete/', views.MessageDelete.as_view(), name='messages_delete')
]
