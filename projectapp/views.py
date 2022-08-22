
from django.shortcuts import get_object_or_404, render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Review
from .serializers import  MovieListSerializer, ReviewListSerializer

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) #로그인시 이용
def movie_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)

        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated]) #로그인시 이용
def movie_detail_update_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializers = MovieListSerializer(movie)
        return Response(serializers.data)

    elif request.method == 'PATCH':
        serializers = MovieListSerializer(instance=movie, data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

    elif request.method == 'DELETE':
        movie.delete()
        data ={
            'movie':movie_pk
        }
        return Response(data)


# review
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) #로그인시 이용
def review_list_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)

        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer = ReviewListSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated]) #로그인시 이용
def review_detail_update_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'GET':
        serializers = ReviewListSerializer(review)
        return Response(serializers.data)

    elif request.method == 'PATCH':
        serializers = ReviewListSerializer(instance=review, data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)

    elif request.method == 'DELETE':
        review.delete()
        data ={
            'review':pk
        }
        return Response(data)