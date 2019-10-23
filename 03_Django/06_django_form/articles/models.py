from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)  # related_name 필수

    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # 외래키로 연결, 게시글 삭제되면 모든 댓글 삭제(required한 option)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ('-pk', )

    def __str__(self):  # 표현식
        return self.content

# 모델링 후
# $ python manage.py makemigrations
# $ python manage.py showmigrations
# $ python manage.py migrate