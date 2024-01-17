from django.db import models


class Image(models.Model):
    original_image = models.ImageField(upload_to='images/original/')
    optimized_image = models.ImageField(
        upload_to='images/optimized/', blank=True, null=True)
    image_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
