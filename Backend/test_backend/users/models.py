from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class User(models.Model):
    username = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(to=Group, on_delete=models.deletion.CASCADE)






