from django.contrib import admin
from .models import FeedBack
# Register your models here.
@admin.register(FeedBack)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['user','emoji','body','ratings']

