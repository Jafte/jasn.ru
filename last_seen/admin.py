
from django.contrib import admin

from last_seen.models import LastSeen


class LastSeenAdmin(admin.ModelAdmin):
    list_filter = ('site', 'module', 'last_seen')
    search_fields = ('user__username',)
    list_display = ('site', 'module', 'user', 'last_seen')


admin.site.register(LastSeen, LastSeenAdmin)
