from rest_framework import viewsets
from rest_framework import generics
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework.exceptions import PermissionDenied


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs['pk'])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not delete this poll")
        return super().destroy(request, *args, **kwargs)

