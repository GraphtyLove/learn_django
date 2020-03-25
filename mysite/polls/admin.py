from django.contrib import admin
from .models import Question

# Register your models here.
# Add the object Question to the admin interface
admin.site.register(Question)