from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'balance')
    list_display_links = ('username',)
    search_fields = ('username',)
    filter_horizontal = ('category',)


class InfotmationTransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'costs_sum', 'time_operation',
                    'category', 'organization', 'description')
    list_display_links = ('user', 'costs_sum')
    search_fields = ('user',)
    list_editable = ('category',)
    list_filter = ('user', 'time_operation')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_cat',)
    list_display_links = ('name_cat',)


admin.site.register(User, UserAdmin)
admin.site.register(InfotmationTransaction, InfotmationTransactionAdmin)
admin.site.register(Category, CategoryAdmin)
