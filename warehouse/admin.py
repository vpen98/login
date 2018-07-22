from django.contrib import admin
from .models import good
# Register your models here.
class goodAdmin(admin.ModelAdmin):
    list_display = ('author','price','introduce','pub_date')

admin.site.register(good,goodAdmin)