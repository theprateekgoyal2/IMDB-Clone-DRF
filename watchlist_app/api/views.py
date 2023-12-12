from watchlist_app.models import Watchlist, StreamingPlatform, Review
from .serializers import (
    WatchlistSerializer,
    StreamingPlatformSerializer,
    ReviewsSerializer,
)
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from .pagination import WatchlistPagination, WatchlistLimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User

class WatchlistView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchlistV2(generics.ListAPIView):
    pagination_class = WatchlistLimitOffsetPagination
    serializer_class = WatchlistSerializer
    queryset = Watchlist.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'platform__name']


class WatchlistDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except:
            return Response(
                {"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        print(request.data)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Success")
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamingPlatformListView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        platforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamingPlatformDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except:
            return Response(
                {"Error": "Platform not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamingPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ReviewList(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewsSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movie=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer

class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = Watchlist.objects.get(pk=pk)

        reviewer = self.request.user
        review_queryset = Review.objects.filter(reviewer=reviewer, movie=movie)

        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie')
        
        if movie.total_ratings == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else: 
            movie.avg_rating = (movie.avg_rating * movie.total_ratings + serializer.validated_data['rating']) / (movie.total_ratings + 1)
        movie.total_ratings += 1
        movie.save()
        serializer.save(movie=movie, reviewer=reviewer)

class UserReviews(generics.ListAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Review.objects.filter(reviewer__username=username)