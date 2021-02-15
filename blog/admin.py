from mptt.admin import DraggableMPTTAdmin
# from mptt.admin import MPTTModelAdmin

from django import forms
from django import CKEditorUploadingWidget
from ckeditor.widgets.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class PostAdminForm(forms.ModelForm):
    content=forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model=Post
        fields='__all__'
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    form=PostAdminForm
    save_as = True
    list_display=('id','title','slug','category','created_at','get_photo','views')
    list_display_links = ('id', 'title')
    search_fields=('title')
    list_filter = ('category','tags')
    readonly_fields=('views','created_at','get_photo')
    fields=('title','slug','categeory','tags','content','photo','get_photo','views','created_at')
    def get_photo(self,obj,):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'
    get_photo.short_description='фото'
        
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
# admin.site.register(Post,MPTTModelAdmin)

# Register your models here.
