from django.db import models
from django.contrib.auth.models import User

class Bank(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255 , null=True)
    address = models.CharField(max_length=255 , null=True)
    swift_code =models.IntegerField(null=True)
    inst_num = models.IntegerField(null=True)
    description = models.CharField(max_length=200 , null=True)
    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=255)
    transit_num = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    capacity = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

