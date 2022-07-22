from django.contrib import admin
from .models import Booklet
from django.contrib.auth.models import Group

class BookletAdmin(admin.ModelAdmin):
    list_display=('title','uploaded','updated')
admin.site.unregister(Group)
admin.site.register(Booklet,BookletAdmin)