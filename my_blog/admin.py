from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    list_display=('title','slug','short_des','status','created_on','updated_on')
    list_filter=("status","tags",)
    summernote_fields=('content',)
    search_fields=['title','content']
    prepopulated_fields={'slug':('title',)}


admin.site.register(Post,PostAdmin)