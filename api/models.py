from django.db import models


class Custom_Model(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.title}"
