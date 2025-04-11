from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    type = models.ForeignKey("events.EventType", on_delete=models.CASCADE)

    date_and_time = models.DateTimeField()
    venue = models.CharField(max_length=200)

    customer = models.ForeignKey('authentication.Customer', on_delete=models.CASCADE)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-date_and_time']
        
    def __str__(self):
        return self.title


class EventType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Event Type'
        verbose_name_plural = 'Event Types'
        ordering = ['-id']
        
    def __str__(self):
        return self.name



class Dummy(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Dummy'
        verbose_name_plural = 'Dummys'
        ordering = ['-id']
        
    def __str__(self):
        return self.title