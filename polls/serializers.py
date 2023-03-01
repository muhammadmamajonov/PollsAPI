from rest_framework import serializers
from .models import Vote, Choice, Poll


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    vote = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'

    
class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'
