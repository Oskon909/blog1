from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    foto = models.ImageField(height_field=100,width_field=100,verbose_name='фото')
    create_date = models.DateTimeField(auto_now_add=False,auto_now=False)

    def __str__(self):
        return self.title
