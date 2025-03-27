from django.conf import settings
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Open SQLite database using sqlite3 command-line tool'

    def handle(self, *args, **kwargs):
        # Dynamically fetch the database file path from settings
        db_path = settings.DATABASES['default']['NAME']
        
        # Check if the SQLite database file exists
        if not os.path.exists(db_path):
            self.stdout.write(self.style.ERROR(f"Database file not found at: {db_path}"))
            return
        
        # Run the sqlite3 command
        os.system(f"sqlite3 {db_path}")
        self.stdout.write(self.style.SUCCESS("Exited SQLite shell."))