from django.db import models


# Create your models here.
class Tasks(models.Model):
    task_title = models.CharField(max_length=150, unique=True)
    task_text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.task_title} - {self.task_text}'
