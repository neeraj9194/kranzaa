from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin
from .models import Location

# Register your models here.


from .models import RegStore,Category,Comments

class RegStoreAdmin(admin.ModelAdmin):
    list_display=["__str__","date_added"]
    prepopulated_fields={ 'storeslug': ('name',)}
    class Meta:
        model=RegStore

class CategoryAdmin(admin.ModelAdmin):
    list_display=["__str__"]
    prepopulated_fields={ 'slug': ('cat_title',)}
    class Meta:
        model=Category

class LocationAdmin(GeoModelAdmin):
    meta=Location
    list_display=["__str__"]

class CommentsAdmin(admin.ModelAdmin):
    meta=Comments
    list_display=['user', "__str__",'created','store','pos_score_comment','neg_score_comment' ]
    #readonly_fields=('user','comment','ratings','store')

admin.site.register(Category,CategoryAdmin)
admin.site.register(RegStore,RegStoreAdmin)
admin.site.register(Location)
admin.site.register(Comments,CommentsAdmin)
