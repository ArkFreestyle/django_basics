from django.core.management.base import BaseCommand
import time

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("\n\nCommand chal gaye! Time:\n\n", time.time())