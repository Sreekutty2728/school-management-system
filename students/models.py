from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    register_number = models.CharField(
    max_length=20,
    null=True,
    blank=True
)
    roll_number = models.IntegerField(
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    address = models.TextField(
        null=True,
        blank=True
    )

    student_class = models.CharField(
        max_length=50
    )

    profile_image = models.ImageField(
        upload_to='students/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
