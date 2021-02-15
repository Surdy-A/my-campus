from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.timezone import now
from django.utils import timezone
from django_countries.fields import CountryField
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/courses')
    image_thumbnail = ImageSpecField(source='image',processors=[ResizeToFill(350, 200)], format='JPEG',
        options={'quality': 60})
    date = models.DateTimeField(default=timezone.now)
    location = CountryField(default='')
    description = models.CharField(max_length=500)
    

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def str(self):
        return self.name

    def getabsoluteurl(self):
        return reverse("event_detail", kwargs={"pk": self.pk})
