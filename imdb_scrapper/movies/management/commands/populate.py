from django.core.management.base import BaseCommand
from movies.models import Movie
import scrapy
from scrapy.crawler import CrawlerProcess
from imdb_scrapy.spiders.movie_spider import MovieSpider
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
    help = 'Clear and populate table via scrapy'
    def handle(self, *args, **options):
        Movie.objects.all().delete()
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(MovieSpider)
        process.start()

