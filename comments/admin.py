from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display =  ['name','email','url','text','created_time','post']

admin.site.register(Comment,CommentAdmin)