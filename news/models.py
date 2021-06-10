from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anouns = models.CharField('Anouns', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Published date')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

