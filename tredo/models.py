from django.db import models

class Email(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    message = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name