from django.db import models


# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to="img_file/", blank=True, null=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"
