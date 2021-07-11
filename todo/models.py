from django.db import models


# Create your models here.
class ToDo(models.Model):
    # data fields for the ToDo model
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    # toString function for ToDo models
    def __str__(self):
        return self.title
