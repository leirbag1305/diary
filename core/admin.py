from django.contrib import admin
from core.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'dt_event', 'dt_creation')
    list_filter = ('title', 'dt_event',)


admin.site.register(Event, EventAdmin)
