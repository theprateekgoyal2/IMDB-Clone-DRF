from django.contrib.auth.models import User
from django.urls import reverse
from .models import StreamingPlatform, Watchlist, Review
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

class StreamingPlatformsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ str(token.access_token))
        self.stream = StreamingPlatform.objects.create(name='Netflix', website='http://netflix.com', about='#1 streaming platform')

    def test_platforms_list_create(self):
        data = {
            'name': 'primevideo',
            'website': 'http://primevideo.com',
            'about': 'OTT by Amazon'
        }
        response = self.client.post(reverse('platforms_list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_platforms_list(self):
        response = self.client.get(reverse('platforms_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_platforms_ind(self):
        response = self.client.get(reverse('platform_detail', args=(self.stream.id, )))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_platforms_ind_edit(self):
        data = {
            'name': 'Zee5',
            'website': 'http://zee5.com',
            'about': 'Indias Ott Platform'
        }
        response = self.client.put(reverse('platform_detail', args=(self.stream.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_platforms_ind_delete(self):
        response = self.client.delete(reverse('platform_detail', args=(self.stream.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
class WatchlistTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ str(token.access_token))
        self.watch = Watchlist.objects.create(title='Testing V1', storyline='testing for watchlist')

    def test_movies_list_create(self):
        data = {
            "title": "Testing",
            "storyline": "just testing"
        }
        response = self.client.post(reverse('movies_list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_movies_list(self):
        response = self.client.get(reverse('movies_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_movies_list_edit(self):
        data = {
            "title": "Testing",
            "storyline": "just testing"
        }
        response = self.client.put(reverse('movies_details', args=(self.watch.id, )), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_movies_list_del(self):
        response = self.client.delete(reverse('movies_details', args=(self.watch.id, )))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ReviewTestCase(APITestCase):
    def setUp(self):
        pass

    # 