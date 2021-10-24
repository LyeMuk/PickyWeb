from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Tags)
# admin.site.register(models.Links)


# from django.contrib import admin

# the module name is app_name.models
from .models import Tags, Links

# this class define which department columns will be shown in the department admin web site.
class LinkAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'name', 'tag']

admin.site.register(Links, LinkAdmin)