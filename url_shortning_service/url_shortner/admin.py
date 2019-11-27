from django.contrib import admin
from url_shortner.models import UrlDetail
 
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_url_id','http_main_url','pub_date', 'count')
    ordering = ('-pub_date',)
 
admin.site.register(UrlDetail, UrlsAdmin)