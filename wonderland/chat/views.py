from django.shortcuts import render


# Create your views here.
def chat_index(request):
    return render(request, "chat/index.html")
