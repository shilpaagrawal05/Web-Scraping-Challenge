from splinter import Browser
from bs4 import BeautifulSoup as bs

def init_browser():
    executable_path = {"executable_path": '/users/shilpaagrawal/Downloads/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_collection = {}

    #Mars Latest News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_collection["news_title"] = soup.find('div',class_ = 'list_text').find('div',class_= 'content_title').get_text()
    mars_collection["news_paragraph"] = soup.find('div',class_ = 'list_text').find('div',class_= 'article_teaser_body').get_text()


    # Mars featured Image
    url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    images = soup.find('a',class_ = 'button fancybox')
    featured_image = images['data-fancybox-href']
    
    mars_collection["featured_image_url"] = 'https://www.jpl.nasa.gov' + featured_image
    
    # Mars Weather Tweet
    url = ('https://twitter.com/marswxreport?lang=en')
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    mars_collection["mars_weather"] = soup.find('div',class_ = 'js-tweet-text-container').p.get_text()
    
    # Mars Facts
    mars_facts_url = "https://space-facts.com/mars/"
    table = pd.read_html(mars_facts_url)
    table[1]
    df = table[1]
    df.columns = ["Facts", "Value"]
    df.set_index(["Facts"])
    facts_html = df.to_html()
    facts_html = facts_html.replace("\n","")
    mars_collection["fact_table"] = facts_html
    
    # Mars Hemisphere

    return mars_collection

   