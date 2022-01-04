import pathlib
import uuid
from django.db import models

# Create your models here.


def shop_image(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())  # uuid + timestamps
    return f"shop/image/{new_fname}{fpath.suffix}"


class ShopItems(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=shop_image)
    price = models.DecimalField(decimal_places=2)
    discount = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True
    )
