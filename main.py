from scraper.smmbind_com import Smmbind
from scraper.likesoutlet_com import Likesoutlet
from scraper.godofpanel_com import Godofpanel
from scraper.postlikes_com import Postlikes
from db.core import IsDbCreated, IsDbTable

def main():
    Smmbind().scrape()
    Likesoutlet().scrape()
    Godofpanel().scrape()
    Postlikes().scrape()

def check_db():
    IsDbCreated().check()
    IsDbTable().check()

if __name__ == "__main__":
    check_db()
    main()