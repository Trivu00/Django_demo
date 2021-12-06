from django.db import models
from django.conf import settings

# Create your models here.
class idiom4Day(models.Model):
    idiom_sentence = models.CharField(max_length=100)
    idiom_meaning = models.CharField(max_length=1000)
    def __str__(self):
       return self.idiom_sentence

class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Thể loại của bài đọc')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categores'



class ReadingBook(models.Model):
    name = models.CharField(max_length=200, help_text='Tên bài đọc')
    content_reading = models.TextField(help_text='Nội dung bài đọc')
    reading_translate = models.TextField(help_text='Nội dung bài đọc', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    views = models.IntegerField(null=True, blank=True, default=0)
    
    def __str__(self):
        return self.name


class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    name_read = models.ForeignKey(ReadingBook, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = 'Questions'

class Vocabulary(models.Model):
    vocabulary = models.CharField(max_length=20)
    translate = models.CharField(max_length=100, null = True)
    name_read = models.ForeignKey(ReadingBook, on_delete=models.PROTECT)

    def __str__(self):
        return self.vocabulary

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_read = models.ForeignKey(ReadingBook, on_delete=models.PROTECT)
    note = models.TextField(help_text='Nội dung cần ghi nhớ !')
    

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(help_text='Nội dung bình luận')
    date = models.DateTimeField(auto_now_add=True)
    