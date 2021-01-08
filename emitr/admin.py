from django.contrib import admin
from .models import LatestUpdate, Service, SubService, UsefulLink

# Register your models here.
class LatestUpdateAdmin(admin.ModelAdmin):
    list_display = ('headline', 'date')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'isExclusive')

class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('name', "service" , 'fee')

class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ('text', 'url',)

admin.site.register(LatestUpdate, LatestUpdateAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(UsefulLink, UsefulLinkAdmin)
