
from collections import defaultdict
from bs4 import BeautifulSoup
import requests


def scraper():
    team_page = requests.get("http://games.crossfit.com/team/4666")
    athletes = parse_athlete_data(team_page.content)
    for athlete_name, data in athletes.iteritems():
        stats = scrape_athlete_data(data['profile_url'])
        athletes[athlete_name].update(stats)
    print 'Loaded data for %s Athletes.' % len(athletes)
    return athletes


def parse_athlete_data(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    roster_block = soup.find(id="block-search-athlete-affiliate-team-blocks-team-roster")

    roster_map = defaultdict(dict)

    for item in roster_block.find_all('li'):
        athlete_name = item.span.text
        athlete_data = {'profile_url': item.a['href'], 'image_url': item.img['src']}
        roster_map[athlete_name] = athlete_data
    return roster_map


def scrape_athlete_data(profile_url):

    athlete_page = requests.get("http://games.crossfit.com" + profile_url)
    soup = BeautifulSoup(athlete_page.content, "html.parser")
    athlete_data = {}

    stats = soup.find_all('dd')
    athlete_data['age'] = stats[4].text
    athlete_data['hieght'] = stats[5].text
    athlete_data['wieght'] = stats[6].text

    for row in soup.find_all("tr"):
        if row.th is None:
            stats = row.find_all('td')
            stat = stats[0].text
            metric = stats[1].text
            if metric == '--':
                metric = None
            athlete_data[stat] = metric
    return athlete_data



if __name__ == '__main__':
    scraper()