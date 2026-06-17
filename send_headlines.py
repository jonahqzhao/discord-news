import feedparser
import requests
from datetime import datetime
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
RSS_URL = "https://moxie.foxnews.com/google-publisher/latest.xml"

feed = feedparser.parse(RSS_URL)
headlines = feed.entries[:10]

description = "\n\n".join(
    f"**{i+1}. [{a.title}]({a.link})**"
    for i, a in enumerate(headlines)
)
payload = {
    "username": "PATRIOT NEWS",
    "embeds": [{
        "title": "AMERICA'S BIGGEST HEADLINES",
        "description": description,
        "footer": {
            "text": datetime.utcnow().strftime("%Y-%m-%d")
        }
    }]
}
requests.post(WEBHOOK_URL, json=payload)
