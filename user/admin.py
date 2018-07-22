from django.contrib import admin
from user.models import Register
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username','password','register_time')

admin.site.register(Register,RegisterAdmin)