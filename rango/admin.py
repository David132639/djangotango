from django.contrib import admin
from rango.models import Category,Page

# Register your models here.
class PageClass(admin.ModelAdmin):
    list_display = ("title","category","url")

#admin.site.register(Category)
admin.site.register(Page,PageClass)

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
