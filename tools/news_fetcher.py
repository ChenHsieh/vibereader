import feedparser

def fetch_guardian_headlines():
    url = "https://www.theguardian.com/world/rss"
    feed = feedparser.parse(url)
    return [entry.title for entry in feed.entries[:5]]