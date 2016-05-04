from django.contrib import admin
from .models import Review
# Register your models here.

from django.utils.html import format_html

class ReviewAdmin(admin.ModelAdmin):
    meta=Review
    list_display=['store', "pos_score",'neg_score','polarity' ,'created','show_chart_url']
    readonly_fields=('store', "pos_score",'neg_score','polarity','no_of_comments')
    
    def show_chart_url(self, obj):
        return format_html("<a href='/chart/{url}'>{url}</a>", url=obj.store.storeslug)
    show_chart_url.short_description = "Chart URL"
    show_chart_url.allow_tags = True
admin.site.register(Review,ReviewAdmin)
