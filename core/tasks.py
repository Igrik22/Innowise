from celery import shared_task
from core.models import TaskTicket


@shared_task
def count_task_ticket():
    return TaskTicket.objects.count()
