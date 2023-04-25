import imp
from django.core.management.base import BaseCommand
from core.utils import result
# from core.utils import execWebCrawler

class Command(BaseCommand):
    help = 'Model has been run, spiders have been released'
    def handle(self, *args, **options):

        result()
        
            
