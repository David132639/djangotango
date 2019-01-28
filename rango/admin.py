from django.contrib import admin
from rango.models import Category,Page

# Register your models here.
class Page(admin.ModelAdmin):
    fields = ["title","category","url"]

admin.site.register(Category)
admin.site.register(Page)
