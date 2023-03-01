from django.urls import path
from .views import *



urlpatterns = [
    path('polls/<int:pk>/choices/', ChoiceList.as_view()),
    path('polls/<int:pk>/choices/<int:choice_id>/vote/', CreateVote.as_view())
]