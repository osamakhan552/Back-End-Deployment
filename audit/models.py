from django.db import models
import uuid
from employee.models import employee
from customer.models import customer


class auditType(models.Model):
    auditTypeId = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    auditType = models.CharField(max_length=100)

    def __str__(self):
        return self.auditType

class audit(models.Model):
    auditId = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    auditType = models.ForeignKey(auditType,on_delete=models.CASCADE)
    employee = models.ForeignKey(employee,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    date = models.DateField()
    isActive = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.customer.custFname

