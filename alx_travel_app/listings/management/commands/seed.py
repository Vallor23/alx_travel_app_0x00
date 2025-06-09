from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Populates the database with sample listing data.'
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # Your data seeding logic will go here
        # For now, let's just print a message

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))