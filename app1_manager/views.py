from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from .forms import PostForm

def simple_page(request):
    form=PostForm()
    if request.method =='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'simple-page.html',context)

class simple_api(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
