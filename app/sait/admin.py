from django.contrib import admin
from .models import Settings, Statics, Imgaes

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'facebook', 'twitter', 'github', 'google')


admin.site.register(Statics)
admin.site.register(Imgaes)