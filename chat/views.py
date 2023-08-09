from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
  return render(request, 'chat/base.html')

def about(request):
  return render(request, 'chat/about.html')

def chatRoom(request):
   return render(request, "chat/chatRoom.html")

def messages(request):
   return render(request, "chat/messages.html")

def message_detail(request, message_id):
   message = Message.objects.get(id=message_id)
   return render(request, 'message/detail.html', {
    'message': message
  })

class MessageCreate(LoginRequiredMixin,CreateView):
  model = Message
  fields = ['Content', 'SentAt']

class MessageUpdate(LoginRequiredMixin,UpdateView):
  model = Message
  fields = ['Content', 'SentAt']

class MessageDelete(LoginRequiredMixin,DeleteView):
  model = Message
  success_url = '/messageDelete'