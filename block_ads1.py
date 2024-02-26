import requests
import re

def block_ads(url):
    # fetch the web page
    response = requests.get(url)
    if response.status_code == 200:
        # extract URLs from the HTML content
        urls = re.findall(r'href=["\']?(https?://[^"\'>]+)', response.text)
        
        # filter ad URLs
        ad_urls = [url for url in urls if "ad" in url or "ads" in url or "banner" in url]
        
        # block ads by printing their urls or redirecting the request
        for ad_url in ad_urls:
            print(f"Blocking ad: {ad_url}")
            # you can take action to the ad here
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        

# testing
block_ads("https://timesofindia.indiatimes.com/city/kanpur/iit-kanpur-class-of-1974-pledges-rs-10-11-crore-to-set-up-class-of-1974-batch-legacy-fund/articleshow/108016826.cms")