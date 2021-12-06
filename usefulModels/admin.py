from django import contrib
from django.contrib import admin
from django.contrib.admin.filters import ListFilter

# Register your models here.
from .models import Comment, Post, Vocabulary, idiom4Day, Category, ReadingBook, QuesModel

admin.site.register(idiom4Day) # lệnh này để hiển thị phần chỉnh sửa DB trong site admin

# tùy chỉnh các phần sẽ hiển thị
class idiom4DayAdmin(admin.ModelAdmin):
    list_display = ('idiom_sentence', 'idiom_meaning')


@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ReadingBook)
class ReadBookAdmin(admin.ModelAdmin):
    list_display = ('name','content_reading')
    search_fields = ('name',)
    
@admin.register(QuesModel)
class QuesMoldelAdmin(admin.ModelAdmin):
    list_display = ('question','name_read',)

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('name_read',)
    
@admin.register(Comment)    
class CommentInline(admin.ModelAdmin):
    list_display = ('author','body','date')

@admin.register(Vocabulary)    
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('vocabulary','translate','name_read')