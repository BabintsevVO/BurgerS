from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    form = ProductAdminForm
    save_as = True
    save_on_top = True
    list_display = ('name', 'id', 'slug', 'get_image', 'category', 'price', 'rating')
    list_display_links = ('name', 'slug', 'get_image')
    search_fields = ('name',)
    list_filter = ('category',)
    readonly_fields = ('rating',)
    fields = (
        ('name', 'slug'), 'image', 'description', 'short_desription', ('price', 'quantity'), 'category',
    'rating')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'Image'


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
