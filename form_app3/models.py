from django.db import models


# Create your models here.
class Tasks(models.Model):
    task_title = models.TextField(max_length=150, unique=True)
    task_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.task_title}: {self.task_text}'
