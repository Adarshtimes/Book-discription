from django.db import models

# Create your models here.
class Receipe(models.Model):
    Book_name = models.CharField(max_length=100)
    Book_description=models.TextField()
    Book_image = models.ImageField(upload_to="receipe", null=True, blank=True)
      

    def __str__(self):
        return self.Book_name