from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Page Title', max_length=200)
    content = models.TextField(verbose_name='Page Content')
    created = models.DateTimeField(auto_now_add= True, verbose_name='Info added on')
    updated = models.DateTimeField(auto_now= True, verbose_name='Info updated on')

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ['title']

    def __str__(self):
        return self.title
