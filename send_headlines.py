import feedparser
import requests
from datetime import datetime
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
RSS_URL = "https://moxie.foxnews.com/google-publisher/latest.xml"

feed = feedparser.parse(RSS_URL)
headlines = feed.entries[:10]

message = f"🦊 **FOX NEWS TOP HEADLINES**\n**{datetime.now().strftime('%Y-%m-%d')}**\n\n"

for i, a in enumerate(headlines, start=1):
    title = a.title
    link = a.link

    message += f"**{i}. {title}**\n{link}\n\n"

requests.post(
    WEBHOOK_URL,
    json={"content": message}
)
