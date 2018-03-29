from django.db import models
from django.utils.six import python_2_unicode_compatible
# Create your models here
# coding: utf-8
# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100,verbose_name='姓名')
    email = models.EmailField(max_length=255,verbose_name='邮箱')
    url = models.URLField(blank=True,verbose_name='浏览页面')
    text = models.TextField(verbose_name='评论')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')

    post = models.ForeignKey('blog.Post',verbose_name='评论POST')

    def __str__(self):
        return self.text[:20]
