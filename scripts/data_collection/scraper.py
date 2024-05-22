from utils import scrape_news_page, scrape_news_more, scrape_telegram
import json
from pathlib import Path

def update_json_file(sources):
    Path('.')
    with open('news_sources.json', 'w') as f:
        json.dump({"sources":sources} , f , indent=4)

def main():
    Path('.')
    with open('news_sources.json',) as f:
        sources = json.load(f)["sources"]

        for source in sources:

            if not source["is_scraped"]:
                if source['type'] == 'page number':
                    scrape_new(source["url"], 
                            source["num_pages"], 
                            source["title_selector"],
                            source["article_selector"],
                            source["content_selector"],
                            source["class_selector"],
                            source["date_selector"])


                elif source['type'] == 'telegram':
                    scrape_telegram(source["channel_username"], source["url"])

                
                elif source['type'] == 'more':
                    scrape_news_more(source['url'], 
                                     source['more_button_selector'], 
                                     source['title_selector'], 
                                     source['content_selector'], 
                                     source['article_link_selector'], 
                                     source['date_selector'])

                    
                source["is_scraped"] = True
                update_json_file(sources)
   
if __name__ == "__main__":
    main()