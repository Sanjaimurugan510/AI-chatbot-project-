from django.shortcuts import render
from django.conf import settings


def chat_home(request):
    return render(request, "chat/index.html", {"api_base_url": settings.FASTAPI_BASE_URL})
