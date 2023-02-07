from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

def simple_page(request):
    return render(request,'simple-page.html')

class simple_api(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
