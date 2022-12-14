from django.shortcuts import render
from inspect import GEN_CLOSED
from rest_framework.decorators import api_view #데코레이터
from .serializers import MovieListSerializer, MovieSerializer,CommentListSerializer,CommentSerializer, ActorListSerializer,ActorSerializer
from rest_framework import status
from .models import Movie,Actor,Comment
from rest_framework.response import Response # drf 형태로 response
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from articles.models import Article
from django.http import JsonResponse


# Create your views here.
@api_view(['GET']) # GET이 기본값이긴 하나 명시하는 게 좋음
def index(request):
     if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)
     

@api_view(['GET']) # GET이 기본값이긴 하나 명시하는 게 좋음
def detail(request, movie_id):
   movie = get_object_or_404(Movie,pk=movie_id)
   if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data) # drf 형태로 반환
     
@api_view(['GET']) 
def actor(request):
      if request.method == 'GET':
         actors = Actor.objects.all()
         serializer = ActorListSerializer(actors, many=True)
         return Response(serializer.data) 
     
@api_view(['GET']) 
def detail_actor(request, movie_id):

   if request.method == 'GET':
      actor = Actor.objects.filter(movie_id=movie_id)
      serializer = ActorSerializer(actor, many=True)
      return Response(serializer.data)
   
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(),username=request.user)  
   #  print(user)
    print(user.point,'확인')
    user.point= user.point+10
    user.save()
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
     
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def comment_list(request,movie_id):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment, movie=movie_id)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
    person = get_object_or_404(get_user_model(), username=request.user)
    articles = Article.objects.filter(user=request.user).last()
    recent= articles.getgenre
   

    if recent != None:
        movies = Movie.objects.filter(genres=recent).order_by('popularity')[:20]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('아직 데이터가 없는 상태', status=status.HTTP_200_OK)