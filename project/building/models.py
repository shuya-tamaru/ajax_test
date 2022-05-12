from django.db import models
from django.utils import timezone

class Comment(models.Model):
    title = models.CharField('タイトル',max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
    cordinate = models.TextField('座標',blank = True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = 'コメント情報'