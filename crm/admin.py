from django.contrib import admin

# Register your models here.
from .models import Record

admin.site.register(model_or_iterable=Record)
