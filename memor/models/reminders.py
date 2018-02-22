from django.db import models


class Reminder(models.Model):
    remind_on = models.DateTimeField()
    