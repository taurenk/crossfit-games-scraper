# crossfit-games-scraper
Web scraper and relational data loader for affliates athelete stats. 

##Scraper - webscraper.py
Given a team id (taken from your games.crossfit.com url i.e. http://games.crossfit.com/team/4666), scrape all of atheletes data and stats into a nested dictionary.

##Postgresql Data Loader - db_loader.py
import data from the webscraper to a postgresql database.


## Coming soon:
- Command Line Interface to grab targeted team/athelete data.
- More docs
