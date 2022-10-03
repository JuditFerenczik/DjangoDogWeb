from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator, MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.


class Breed(models.Model):
    name = models.CharField(max_length=50, default="mixture")

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=50, default="John Doe")
    age = models.IntegerField()

    class Meta:
        ordering = ['name', 'age']

    def get_absolute_url(self):
        return reverse('owner_detail', kwargs={"pk":self.pk})

    def __str__(self):
        return f"{self.name} "


class Doggo(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
    name = models.CharField(max_length=30, validators=[MinLengthValidator(1)], default="Boglárka")
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)], default=3)
    color = models.CharField(max_length=20, validators=[MinLengthValidator(1)], default="Black")
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True)
    isBiting = models.BooleanField(default=False)
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
        default=Sex.MALE
    )
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('doggo_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} is a {self.age} years old {self.breed} dog with owner {self.owner}\n"