from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import registeration_view, logout_view
urlpatterns = [
    # path('login/', obtain_auth_token, name='login'),
    path('register/', registeration_view, name='register'),
    path('logout/', logout_view, name='logout'),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
