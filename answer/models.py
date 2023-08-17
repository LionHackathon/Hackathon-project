from django.db import models

# Create your models here.
from question.models import Question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()