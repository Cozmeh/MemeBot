# MemeBot
* This is a basic Discord meme bot that scrapes memes from a website and sends them to a Discord channel based on a user's tag input. The bot is implemented using the Discord.py library and Selenium for web scraping.
* This bot runs `Locally` in your system
* The selenium webdriver (Chrome) runs headlessly 

## Setup

To set up and run the bot, follow these steps:

1. Install the required dependencies:
   - discord.py
   - selenium

2. Install the necessary modules and libraries:
```
pip install selenium
pip install discord 
```

## Usage

To use the bot, follow these steps:

1. Goto https://discord.com/developers and setup a bot and make sure it has the necessary permissions

2. Invite the bot to your Discord server using the `auth` section in `developer` portal.

3. In a Discord channel, type the command `>meme` followed by a tag. For example, `>meme cat` will fetch a random meme with the "cat" tag.

The bot will then scrape the website for a meme based on the provided tag and send it as a message in the Discord channel.

### Optional 
* If you are familiar with selenium and discord in python , feel free to change the source of website from which the bot is scraping and also specify the right `xPath` for the html element
* You can use https://github.com/trembacz/xpath-finder to find the xpath of an element.
* [xPath Finder](https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph) - Chrome web store 

### Note
* Make sure to replace `env.DEFAULT`, `env.ERROR`, `env.SOURCE`, and `env.TOKEN` with the appropriate values for your environment.
* Currently this bot uses [Memedroid](https://www.memedroid.com/) as source for memes 
