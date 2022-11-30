from django.db import models
import uuid
from employee.models import *



class product(models.Model):
    prodId = models.UUIDField(primary_key=True,default = uuid.uuid4,editable = False)
    prodNumber = models.CharField(max_length=255, unique=True, null=True, default=None)
    prodName = models.CharField(max_length = 100)
    amount = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10,null=True, blank=True,default='0')
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)


    def __str__(self):
        return self.prodName