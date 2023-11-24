from django.contrib import admin
from .models import Menu, Option


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)
    

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('menu', 'title', 'parent_option')