from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE, SET_NULL
from rest_framework.authtoken.models import Token
import uuid
from django.core.validators import MinLengthValidator

class roles(models.Model):
    roleId =  models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False,unique=True)
    roleName = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    createdBy = models.UUIDField()


class employee(AbstractUser):
    first_name = None
    last_name = None
    #username (emaild + role)
    email = models.EmailField(_('email address'))
    empId =  models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    empCbid = models.CharField(max_length=255,null = True,default=None)
    empFname = models.CharField(max_length=255)
    empLname = models.CharField(max_length=255)
    empPhone = models.CharField(max_length=10,default="0000000000",validators=[MinLengthValidator(10)])
    createdAt = models.DateTimeField(auto_now_add=True,editable=False)
    roleId = models.ForeignKey(roles,CASCADE,related_name="roles" ,null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def tokenGenerator(sender, instance = None,created = False,**kwargs):

    if created:
        token = Token.objects.create(user=instance)
        print(token.key)
