from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions
# Create your views here.
from socialnet_api.models import *
from .permissions import IsOwnerOrReadOnly
from .serializer import *


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

def add_like(request):
    answer_id = None
    print(request)
    if request.method == 'GET':
        answer_id = request.GET.get('answer_id')
    likes = 0

    if answer_id:

        answer = Post.objects.get(id=int(answer_id))
        if answer:
            likes = answer.likes + 1
            answer.likes = likes
            answer.save()
    return HttpResponse(likes)
