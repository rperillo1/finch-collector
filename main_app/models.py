from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('T', 'Treat'),
    ('M', 'Meal')
)


class Toy(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
