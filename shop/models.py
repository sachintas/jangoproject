from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default='0')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to="images", null=True, width_field="image_width",
                              height_field="image_height")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False)
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name