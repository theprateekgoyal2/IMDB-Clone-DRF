from django.contrib import admin
from .models import Watchlist, StreamingPlatform, Review

# Register your models here.
admin.site.register(Watchlist)
admin.site.register(StreamingPlatform)
admin.site.register(Review)