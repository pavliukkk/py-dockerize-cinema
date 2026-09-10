import time

from django.core.management.base import BaseCommand
from django.db import OperationalError, connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            "Wait for db connection"
        )
        db_connection = None
        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True
            except OperationalError:
                self.stdout.write("Database unavailable...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
