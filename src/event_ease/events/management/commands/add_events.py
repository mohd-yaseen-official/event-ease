import csv
import datetime
import random

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from authentication.models import Customer

from events.models import Event, EventType



class Command(BaseCommand):
    help = 'This command creates a new events'
    def handle(self, *args, **options):
        Event.objects.all().delete()
        EventType.objects.all().delete()

        file = open(settings.BASE_DIR / "events.csv", encoding='utf-8')

        csv_reader = csv.reader(file)

        next(csv_reader)
        
        customers = list(Customer.objects.all())

        for row in csv_reader:
            title  = row[0]
            description = row[1]
            venue = row[3]
            type = row[2]
            
            type = EventType.objects.get_or_create(name=type)
            date_and_time = datetime.datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S')
            
            event = Event.objects.create(
                title=title,
                description=description,
                date_and_time=date_and_time,
                type=type[0],
                venue=venue,
                customer=random.choice(customers),

            )

            
        print("Proccess Completed......Success!")