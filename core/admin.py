from django.contrib import admin

# Register your models here.

from .models import Quiz,UserAnswer

admin.site.register(Quiz)
admin.site.register(UserAnswer)
