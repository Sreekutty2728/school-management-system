from django.db import models
# from .validators import validate_teacher_name

class Teachers(models.Model):
    name = models.CharField(
        max_length=100,
        # validators=[validate_teacher_name]
    )

    email = models.EmailField()

    def __str__(self):
        return self.name