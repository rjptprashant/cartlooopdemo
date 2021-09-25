import pytz
import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class OperatorGroup(models.Model):
    """
    Model to store operator group names
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)


class Operator(models.Model):
    """
    Model to store the application operators
    """

    user = models.OneToOneField(User, models.CASCADE)
    operator_group = models.ManyToManyField(OperatorGroup)

    def __str__(self):
        return str(self.id)


class Client(models.Model):
    """
    Model to store the application clients
    """
    import pytz
    TIME_ZONE_CHOICES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    user = models.OneToOneField(User, models.CASCADE)
    timezone = models.CharField(
        choices=TIME_ZONE_CHOICES,
        max_length=32,
        default=settings.TIME_ZONE,
        help_text=_('All times for this event are in this time zone. If you change it, '
                    'be sure all the times are correct for the new time zone.')
    )

    def __str__(self):
        return str(self.id)

    @property
    def user_timezone_hour(self):
        return datetime.datetime.now(pytz.timezone(self.timezone)).hour

