from django.db import models


class Feature(models.Model):
    feature_image = models.ImageField(upload_to='features')
    
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = ("Feature")
        verbose_name_plural = ("Features")

    def __str__(self):
        return self.title
