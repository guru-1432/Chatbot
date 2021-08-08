from django.db import models

# Create your models here.
class UserCalls(models.Model):
    Username = models.CharField(max_length=101,primary_key=True)
    count = models.IntegerField()