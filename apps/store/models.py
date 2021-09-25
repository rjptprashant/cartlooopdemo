import pytz
import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Store(models.Model):
    """
    Model for application store
    """
    TIME_ZONE_CHOICES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    name = models.CharField(max_length=255)
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
    def store_timezone_hour(self):
        return datetime.datetime.now(pytz.timezone(self.timezone)).hour


class DiscountCode(models.Model):
    """
    Model for application store discount
    """
    store = models.ForeignKey(Store, models.CASCADE, related_name='store_discount_codes')
    discount_code = models.CharField(_("discount code"), max_length=255, unique=True)

    def __str__(self):
        return str(self.id)
