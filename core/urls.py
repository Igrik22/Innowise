from django.urls import path
from core.views import TaskTicketCreateView, TaskTicketListView, TaskTicketUpdateView, \
    TaskTicketUpdateStatusView, AnswerCreateView, AnswerUpdateView

urlpatterns = [
    path('create/', TaskTicketCreateView.as_view(), name='create'),
    path('list/', TaskTicketListView.as_view(), name='list'),
    path('update/<int:pk>/', TaskTicketUpdateView.as_view(), name='update'),
    path('update/status/<int:pk>/', TaskTicketUpdateStatusView.as_view(), name='update_status'),
    path('create-answer/', AnswerCreateView.as_view(), name='create_answer'),
    path('update-answer/<int:pk>/', AnswerUpdateView.as_view(), name='update_answer'),
]
