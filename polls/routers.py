from rest_framework.routers import DefaultRouter
from .viewsets import PollViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')
