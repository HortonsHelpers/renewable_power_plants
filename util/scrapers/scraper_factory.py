from .cz_eru_scraper import CZ_ERU_Scraper

class ScraperFactory(object):
	"""docstring for ScraperFactory"""
	def __init__(self):
		super(ScraperFactory, self).__init__()

	def getScraper(self, source_name, url):
		if self == 'CZ' and source_name == 'ERU':
			return CZ_ERU_Scraper(url)