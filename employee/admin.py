from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from employee.models import *

class UserAdmin(UserAdmin):
   
    model = employee
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'empFname', 'username')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password','roleId','empCbid','username','empFname','empLname','empPhone')}),
        ('Permissions', {'fields': ('is_staff','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','roleId','empCbid','username','empFname','empLname','empPhone')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
   

admin.site.register(employee, UserAdmin)
admin.site.register(roles)
# Register your models here.
