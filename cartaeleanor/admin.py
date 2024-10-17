from django.contrib import admin
from cartaeleanor.models import Index, IndexText, IndexImage, IndexBackground, IndexPseudoImage

class IndexAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class IndexTextAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class IndexImageAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class IndexBackgroundAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

class IndexPseudoImageAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)

admin.site.register(Index, IndexAdmin)
admin.site.register(IndexText, IndexTextAdmin)
admin.site.register(IndexImage, IndexImageAdmin)
admin.site.register(IndexBackground, IndexBackgroundAdmin)
admin.site.register(IndexPseudoImage, IndexPseudoImageAdmin)
