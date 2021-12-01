from rest_framework import serializers

from core.models import TaskTicket, Answer


class TaskTicketDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaskTicket
        fields = '__all__'
        read_only_fields = ['status']


class TaskTicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTicket
        fields = '__all__'


class TaskTicketUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTicket
        fields = ['status']


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Answer
        fields = '__all__'
