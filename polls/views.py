from .models import Poll, Choice
from rest_framework.exceptions import PermissionDenied
from .serializers import ChoiceSerializer, VoteSerializer
from rest_framework import generics, views, response, status


class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])
        return queryset

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])
        if not request.user == poll.created_by:
            raise PermissionDenied("You can not create choice for this poll.")
        return super().post(request, *args, **kwargs)


class CreateVote(views.APIView):
    def post(self, request, pk, choice_id):
        voted_by = request.data.get('voted_by')
        data = {"choice":choice_id, 'poll':pk, 'voted_by':voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


