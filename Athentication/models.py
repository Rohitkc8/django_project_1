from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username