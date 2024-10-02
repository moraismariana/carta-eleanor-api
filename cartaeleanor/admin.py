from django.contrib import admin
from cartaeleanor.models import Index

class IndexAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(Index, IndexAdmin)
