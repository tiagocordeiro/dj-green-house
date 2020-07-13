from django.contrib import admin

# Register your models here.
from grow.models import Lampada, Relay


class LampadaAdmin(admin.ModelAdmin):
    list_display = ('pin', 'name', 'time_on', 'time_off')


class RelayAdmin(admin.ModelAdmin):
    list_display = ('pin', 'name')


admin.site.register(Lampada, LampadaAdmin)
admin.site.register(Relay, RelayAdmin)
