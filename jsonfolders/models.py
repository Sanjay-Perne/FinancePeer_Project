from django.db import models

# Create your models here.
class folder(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField(max_length=1000)
    class Meta:
        db_table="folder"
        verbose_name_plural="folder"
