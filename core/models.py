from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskTicket(models.Model):
    STATUS_CHOICES = (
        (1, 'Resolved'),
        (2, 'Unresolved'),
        (3, 'Frozen'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name='статус', choices=STATUS_CHOICES, default=2)
    task_text = models.TextField(verbose_name='Задание')

    def __str__(self):
        return self.task_text


class Answer(models.Model):
    task_ticket = models.ForeignKey(TaskTicket, on_delete=models.CASCADE, related_name='support_answer')
    answer_text = models.TextField(verbose_name='Ответ')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return self.answer_text
