from django.contrib import admin
from cedatest_control.models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'email')
    fields = ('name', 'email')
    search_fields = ('name', 'email')
admin.site.register(User, UserAdmin)
