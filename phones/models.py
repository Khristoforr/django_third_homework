from django.db import models

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    price = models.FloatField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.TextField()
    slug = models.TextField()

    def __str__(self):
        return f"{self.name}: цена {self.price}"
