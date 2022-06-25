from django.db import models
from django.core.validators import MaxLengthValidator


class Quote(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=4096, validators=[MaxLengthValidator(4096)])
