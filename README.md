<p align='center'>
  <img src="https://github.com/LuisAlejandro/tweet-last-post-from-feed/blob/develop/branding/banner.svg">
  <h3 align="center">Tweet last post from feed</h3>
  <p align="center">GitHub Action for tweeting the latest entry from an atom feed</p>
</p>

---

Current version: 0.2.2

## 🎒 Prep Work

1. Create an app with the twitter account where you want to share the tweets (https://developer.twitter.com/apps). You might need to fill an application form before being able to create an app. More info [here](https://github.com/gr2m/twitter-together/blob/main/docs/01-create-twitter-app.md).
2. Find the atom feed URL that contains the posts that you wish to share.

## 🖥 Workflow Usage

Configure your workflow to use `LuisAlejandro/tweet-last-post-from-feed@0.2.2`,
and provide the atom feed URL you want to use as the `FEED_URL` env variable.

Provide the authentication keys and tokens for your Twitter app
as the `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`,
`TWITTER_OAUTH_TOKEN`, and `TWITTER_OAUTH_SECRET` env variables
(as secrets). Remember, to add secrets go to your repository
`Settings` > `Secrets` > `Actions` > `New repository secret`
for each secret.

For example, create a file `.github/workflows/schedule.yml` on
a github repository with the following content:

```yml
name: Tweet last post of feed hourly
on:
  schedule:
    - cron: '0 * * * *'
jobs:
  tweet:
    runs-on: ubuntu-20.04
    steps:
      - uses: LuisAlejandro/tweet-last-post-from-feed@0.2.2
        env:
          TWITTER_CONSUMER_KEY: ${{ secrets.TWITTER_CONSUMER_KEY }}
          TWITTER_CONSUMER_SECRET: ${{ secrets.TWITTER_CONSUMER_SECRET }}
          TWITTER_OAUTH_TOKEN: ${{ secrets.TWITTER_OAUTH_TOKEN }}
          TWITTER_OAUTH_SECRET: ${{ secrets.TWITTER_OAUTH_SECRET }}
          FEED_URL: https://hnrss.org/newest?points=300&count=3
```

Publish your changes, activate your actions if disabled and enjoy.

## ❗ Important notes

* The action is designed to publish a maximum of 1 post per batch, regardless of the actual
number of new posts since the last run. You can alter this behavior by setting a `MAX_COUNT` env
variable with your new value.
* For this action to work properly, it should be run with an hourly cron (`0 * * * *`).
The script is designed to look back and publish all posts (set by `MAX_COUNT`)
since the **last hour**. If you want to change the frecuency of execution, modify the cron
expression and then set a `POST_LOOKBACK` env variable with the cron interval in seconds. For example,
for a `*/5 * * * *` cron (every 5 min), set env `POST_LOOKBACK: 300`.

## 🕵🏾 Hacking suggestions

- You can test the script locally with Docker Compose:

  * Install [Docker Community Edition](https://docs.docker.com/install/#supported-platforms) according with your operating system
  * Install [Docker Compose](https://docs.docker.com/compose/install/) according with your operating system.

      - [Linux](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)
      - [Mac](https://docs.docker.com/compose/install/#install-compose-on-macos)
      - [Windows](https://docs.docker.com/compose/install/#install-compose-on-windows-desktop-systems)

  * Install a git client.
  * Fork this repo.
  * Clone your fork of the repository into your local computer.
  * Open a terminal and navigate to the newly created folder.
  * Change to the `develop` branch.

          git checkout develop

  * Create a `.env` file with the content of the environment secrets as variables, like this (with real values):

          FEED_URL=xxxx
          TWITTER_CONSUMER_KEY=xxxx
          TWITTER_CONSUMER_SECRET=xxxx
          TWITTER_OAUTH_TOKEN=xxxx
          TWITTER_OAUTH_SECRET=xxxx

  * Execute the following command to create the docker image (first time only):

          make image

  * You can execute the tweet script with this command:

          make publish

  * Or, alternatively, open a console where you can manually execute the script and debug any errors:

          make console
          python3 entrypoint.py

  * You can stop the docker container with:
  
          make stop

  * Or, destroy it completely:
  
          make destroy
  

## Made with :heart: and :hamburger:

![Banner](https://github.com/LuisAlejandro/tweet-last-post-from-feed/blob/develop/branding/author-banner.svg)

> Web [luisalejandro.org](http://luisalejandro.org/) · GitHub [@LuisAlejandro](https://github.com/LuisAlejandro) · Twitter [@LuisAlejandro](https://twitter.com/LuisAlejandro)