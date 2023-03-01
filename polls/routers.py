from rest_framework.routers import DefaultRouter
from .viewsets import PollViewSet, ChoiceList


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')
