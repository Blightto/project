from django.contrib import admin

# Register your models here.

from .models import Yazi

class BlogAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    readonly_fields = ("slug",)
admin.site.register(Yazi, BlogAdmin)