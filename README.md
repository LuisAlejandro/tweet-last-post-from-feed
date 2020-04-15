<p align='center'>
  <h3 align="center">tweet-last-post-from-feed</h3>
  <p align="center">GitHub Action for tweeting the latest entry from an atom feed</p>
</p>

---

Current version: 0.1.2

## 🎒 Prep Work
1. [Create a twitter app](https://github.com/gr2m/twitter-together/blob/master/docs/01-create-twitter-app.md) with the twitter account where you want to share the tweets.
2. Find the atom feed URL that contains the posts that you wish to share.

## 🖥 Project Setup
1. Fork this repo.
2. Go to your fork's `Settings` > `Secrets` > `Add a new secret` for each environment secret (below).
3. Activate github workflows on `Actions` > `I understand my workflows, go ahead and run them`.
4. Star your own fork to trigger the initial build. The feed is checked hourly, if you haven't posted anything on your blog on the last hour, nothing will be posted on the initial build.

## 🤫 Environment Secrets

- **TWITTER_CONSUMER_KEY**: API key
- **TWITTER_CONSUMER_SECRET**: API secret key
- **TWITTER_OAUTH_TOKEN**: Access token
- **TWITTER_OAUTH_SECRET**: Access token secret
- **FEED_URL**: Atom feed URL
