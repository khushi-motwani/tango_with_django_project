#suppose to be an include statement here? page 85

from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)

