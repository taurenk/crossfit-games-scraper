# crossfit-games-scraper
Web scraper and relational data loader for affiliates athlete stats. 

##Scraper - webscraper.py
Given a team id (taken from your games.crossfit.com url i.e. http://games.crossfit.com/team/4666), scrape all of athletes data and stats into a nested dictionary.

##Postgresql Data Loader - db_loader.py
import data from the webscraper to a postgresql database.


## Coming soon:
- Adding Crossfit Open 2016 Scores
- Command Line Interface to grab targeted team/athelete data.
- More docs
