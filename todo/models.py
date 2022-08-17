from django.db import models

class Writing(models.Model):
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.content

