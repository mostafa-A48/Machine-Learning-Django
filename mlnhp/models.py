from django.db import models

# Create your models here.


class News(models.Model):
    headline = models.CharField(max_length=1000)
    predicted_category = models.CharField(max_length=1000)

    def __str__(self):
        return self.headline + ' ------> ' + self.predicted_category