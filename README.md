docker-compose.yml


```
version: '2.0'
services:
  annoucementbot:
    image: dgc1980/annoucementbot
    environment:
      REDDIT_USER: YOUR_REDDIT_BOT_USERNAME
      REDDIT_PASS: YOUR_REDDIT_BOT_PASS
      # get your Client_ID and Secret from https://www.reddit.com/prefs/apps
      REDDIT_CID: YOURCLIENTID
      REDDIT_SECRET: YOURSECRET
      # you can monitor multiple subreddits using subreddit1+subreddit2+subreddit3
      REDDIT_SUBREDDIT: SubReddit

      WIKIPAGE: config-annoucementbot
    volumes:
      - ./data:/data
    restart: always
```



example of wikipage config

```
slots: 1
run-time: 00:00
posts:
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
    - https://www.reddit.com/r/xxxx/comments/xxxx/comments
```
