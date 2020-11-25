from django.contrib import admin

# Models
from .models import Visitor, Survey

admin.site.register(Visitor)
admin.site.register(Survey)