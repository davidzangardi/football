import feedparser
import urllib.parse


def lookup(school):
    """Look up articles for school"""

    # Check cache
    try:
        if school in lookup.cache:
            return lookup.cache[school]
    except AttributeError:
        lookup.cache = {}

    # Replace special characters
    escaped = urllib.parse.quote(school, safe="")

    # Get feed from Google
    feed = feedparser.parse(
        f"https://news.google.com/rss/search?q=football+{escaped}?ned=us&gl=US&hl=en")

    if not feed["items"]:
        feed = feedparser.parse("http://www.espn.com/espn/rss/ncf/news")

    # Cache results
    lookup.cache[school] = [{"link": item["link"],
                             "title": item["title"]} for item in feed["items"]]

    # Return results
    return lookup.cache[school]
