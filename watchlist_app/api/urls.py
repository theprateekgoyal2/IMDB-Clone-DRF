from django.contrib import admin
from django.urls import path
from .views import (
    WatchlistView,
    WatchlistDetailView,
    StreamingPlatformListView,
    StreamingPlatformDetailView,
    ReviewList,
    ReviewDetail,
    ReviewCreate, 
    UserReviews,
    WatchlistV2
)

urlpatterns = [
    path("", WatchlistView.as_view(), name="movies_list"),
    path("<int:pk>/", WatchlistDetailView.as_view(), name="movies_details"),
    path("platforms_list/", StreamingPlatformListView.as_view(), name="platforms_list"),
    path("platform_detail/<int:pk>", StreamingPlatformDetailView.as_view(), name="platform_detail"),
    # path("review", ReviewList.as_view(), name="review_list"),
    # path("review/<int:pk>", ReviewDetail.as_view(), name="review_detail"),
    path("<int:pk>/review/", ReviewList.as_view(), name="review_list"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review_detail"),
    path("<int:pk>/review_create", ReviewCreate.as_view(), name="review_create"),
    path("reviews/<str:username>/", UserReviews.as_view(), name="user_reviews"),
    path("watchlist/", WatchlistV2.as_view(), name="watchlist") 
]
