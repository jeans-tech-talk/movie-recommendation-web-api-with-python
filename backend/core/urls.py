from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.authentication.views import UserViewSet
from core.recommendation.views import GenreViewSet, MovieViewSet, WatchlistViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register('genres', GenreViewSet)
router.register('movies', MovieViewSet)
router.register('reviews', ReviewViewSet)
router.register('users', UserViewSet)
router.register('watchlists', WatchlistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
