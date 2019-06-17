from django.contrib import admin
from .models import Question

# Make the poll app modifiable by admin
admin.site.register(Question)
