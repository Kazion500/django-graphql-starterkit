from django.db import models

class Fruit(models.Model):
    """A tasty treat"""
    name = models.CharField(max_length=20)
    color = models.ForeignKey('Color', blank=True, null=True,
            related_name='fruits', on_delete=models.CASCADE)

class Color(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="field description",
    )