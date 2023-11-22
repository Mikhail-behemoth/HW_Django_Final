from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name')
    list_display_links = ('pk', 'username',)
    list_filter = ('email', 'username')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.site_header = 'Foodgram'
admin.site.site_title = 'Foodgram'
