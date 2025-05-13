from django.core.management.base import BaseCommand
from auditors.models import IsoStandard

class Command(BaseCommand):
    help = 'Populate IsoStandard model with initial ISO standards'

    def handle(self, *args, **kwargs):
        standards = [
            {'code': '9001', 'description': 'ISO 9001 (Quality Management)'},
            {'code': '14001', 'description': 'ISO 14001 (Environmental Management)'},
            {'code': '45001', 'description': 'ISO 45001 (Occupational Health & Safety)'},
            {'code': '27001', 'description': 'ISO 27001 (Information Security)'},
            {'code': '50001', 'description': 'ISO 50001 (Energy Management)'},
            {'code': '22301', 'description': 'ISO 22301 (Business Continuity)'},
            {'code': '37001', 'description': 'ISO 37001 (Anti-Bribery Management)'},
        ]
        for standard in standards:
            IsoStandard.objects.get_or_create(
                code=standard['code'],
                defaults={'description': standard['description']}
            )
            self.stdout.write(self.style.SUCCESS(f"Added {standard['code']}"))