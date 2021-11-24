from rest_framework import generics, permissions
from core.models import TaskTicket, Answer
from core import serializers
from core.permissions import IsOwnerOrReadOnly


class TaskTicketCreateView(generics.CreateAPIView):
    """Create task ticket"""
    queryset = TaskTicket.objects.all()
    serializer_class = serializers.TaskTicketDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class TaskTicketListView(generics.ListAPIView):
    """ Show Task Ticket"""
    queryset = TaskTicket.objects.all().order_by('-id')
    serializer_class = serializers.TaskTicketListSerializer


class TaskTicketUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """ Update task text (only for user, who created this task)"""
    queryset = TaskTicket.objects.all()
    serializer_class = serializers.TaskTicketDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class TaskTicketUpdateStatusView(generics.UpdateAPIView):
    """ Update status task (only for admins)"""
    queryset = TaskTicket.objects.all()
    serializer_class = serializers.TaskTicketListSerializer
    permission_classes = [permissions.IsAdminUser, ]


class AnswerCreateView(generics.CreateAPIView):
    """Answer create view"""
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class AnswerUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """ Update Answer (only for user, who created this task, and admins)"""
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAdminUser]
