from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'created_at')
    search_fields = ('headline', 'content')
    filter_horizontal = ('categories',)  # Add this line if you want a horizontal filter for categories
    # readonly_fields = ('image_preview',)

    # def has_image(self, obj):
    #     return bool(obj.image)
    # has_image.boolean = True
    # has_image.short_description = 'Has Image'

    # def image_preview(self, obj):
    #     if obj.image:
    #         return format_html('<a href="{0}" target="_blank"><img src="{0}" style="max-height:200px;max-width:200px;" /></a>', obj.image.url)
    #     else:
    #         return 'No image'
    # image_preview.allow_tags = True
    # image_preview.short_description = 'Image Preview'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Add a comma here to make it a tuple
    class Meta:
        verbose_name = 'Category'  # Specify the verbose name
