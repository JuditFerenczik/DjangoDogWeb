from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
# Create your models here


class Dog(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
    name = models.CharField(max_length=30, validators=[MinLengthValidator(1)],default="Boglárka")
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)], default=3)
    color = models.CharField(max_length=20, validators=[MinLengthValidator(1)],default="Black")
    breed = models.CharField(max_length=20, validators=[MinLengthValidator(1)], default="dashound")
    isBiting = models.BooleanField(default=False)
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
        default=Sex.MALE
    )

    def __str__(self):
        return f"{self.name} is a {self.breed} doggo and {self.age} years old\n"

