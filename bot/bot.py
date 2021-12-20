import sqlite3

import time
import praw
import prawcore
import requests

import logging
import os
import random

import schedule

import yaml

os.environ['TZ'] = 'UTC'


reddit_cid = os.environ['REDDIT_CID']
reddit_secret = os.environ['REDDIT_SECRET']

reddit_user = os.environ['REDDIT_USER']
reddit_pass = os.environ['REDDIT_PASS']

reddit_subreddit = os.environ['REDDIT_SUBREDDIT']
reddit_wikipage = os.environ['REDDIT_WIKIPAGE']

web_useragent = 'python:announcementbot (by dgc1980)'

reddit = praw.Reddit(client_id=reddit_cid,
                     client_secret=reddit_secret,
                     password=reddit_pass,
                     user_agent=web_useragent,
                     username=reddit_user)
subreddit = reddit.subreddit(reddit_subreddit)

apppath='./'


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=apppath+'affiliatebot.log',
                    filemode='a')



console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
os.environ['TZ'] = 'UTC'

f = open(apppath+"current.txt","a+")
f.close()

wikistring = reddit.subreddit(reddit_subreddit).wiki[reddit_wikipage].content_md
wikiconfig = next(yaml.safe_load_all( wikistring ))


def run_schedule():
    logging.info("Running Schedule")
    wikistring = reddit.subreddit(reddit_subreddit).wiki[reddit_wikipage].content_md
    wikiconfig = next(yaml.safe_load_all( wikistring ))
    if 'current' in wikiconfig:
      currentsticky = wikiconfig['current']
    else:
      currentsticky = []
    for stickyid in currentsticky:
      submission =  reddit.submission(stickyid.rstrip())
      logging.info("Removing Sticky on https://redd.it/"+submission.id)
      submission.mod.sticky(state=False)

    #print( yaml.dump(wikiconfig) )
    currentsticky = []
    for i in range(int(wikiconfig['slots'])):
        submission = reddit.submission(url=wikiconfig['posts'][i])
        wikiconfig['posts'].append( wikiconfig['posts'][i] )
        del wikiconfig['posts'][i]
        logging.info("Applying Sticky on https://redd.it/"+submission.id)
        submission.mod.sticky(state=True,bottom=True)
        currentsticky.append( submission.id )
    wikiconfig['current'] = currentsticky
    logging.info("Schedule Done.")
    reddit.subreddit(reddit_subreddit).wiki[reddit_wikipage].edit(yaml.dump(wikiconfig))
    #print( yaml.dump(wikiconfig) )

#run_schedule()
schedule.every().day.at( wikiconfig['run-time'] ).do(run_schedule)
logging.info("bot initialized...." )
while True:
  schedule.run_pending()
  time.sleep(1)


