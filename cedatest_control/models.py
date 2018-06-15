from django.db import models

# Create your models here.

class User(models.Model):
    """User of the test app
    """

    name = models.CharField(
        max_length=256,
        unique=True,
        help_text="Name of user"
    )

    email = models.EmailField(
        max_length=256,
        help_text="Email of user"
    )

    def __str__(self):
        return "%s (%s)" % (self.name, self.email)
