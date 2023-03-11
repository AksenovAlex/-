from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CustomMPTTModelAdmin(CategoryAdmin):
    mptt_level_indent = 20


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(
    Post,
    PostAdmin
)