# imports
import discord ,discord.message,env,random,time
from selenium import webdriver
from selenium.webdriver.common.by import By

# discord init
intents = discord.Intents.default()
intents.message_content = True
Client = discord.Client(intents=intents)

# selenium init
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# when bot is ready (Bot start)
@Client.event 
async def on_ready():
    print("Bot is Ready and Online")

# when user types the command in discord 
@Client.event
async def on_message(message):
    if message.author == Client.user:
        return
    msg = str(message.content).split() 
    if msg[0] == ">meme":
        randomArticle = random.randint(1,80)
        await message.channel.send(env.DEFAULT)
        x = ""
        try:
            meme = getImgUrl(driver=driver , tag=msg[1] , article=str(randomArticle))
            await message.channel.send(meme)
        except:
            await message.channel.send(env.ERROR)
            

# gets the image url from the website  
def getImgUrl(driver,tag,article=1,):
    def scrollDown(driver):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    # check if tag exists or not 
    try:
        driver.get(env.SOURCE + tag)
    except:
        print("Something went wrong")

    scrollDown(driver=driver)
    memeUrl = ""
    # checks if generated article number exists or not 
    try:
        memeUrl = driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div/div[2]/section/div[2]/article[{article}]/div[1]/a/picture/img')
    except:
        # checks if next (+1) article exists or not
        scrollDown(driver=driver)
        try: 
            aboveArticle = int(article) + 1 
            x = str(aboveArticle)
            memeUrl = driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div/div[2]/section/div[2]/article[{x}]/div[1]/a/picture/img')
        except:
            # from the original article number , this randomly boils down to 1st article 
            belowArticle = int(article) - 1
            while belowArticle < int(article):
                print(belowArticle)
                try:
                    x = str(belowArticle)
                    memeUrl = driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div/div[2]/section/div[2]/article[{x}]/div[1]/a/picture/img')
                except:
                    if belowArticle == 1:
                        print(env.ERROR)
                        break
                    else:
                        belowArticle = random.randint(1,belowArticle)
                else:
                    x = str(belowArticle)
                    memeUrl = driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div/div[2]/section/div[2]/article[{x}]/div[1]/a/picture/img')
                    break


    #print(memeUrl.get_attribute('alt')) -- debug code
    return memeUrl.get_attribute('src')

# runs disord bot
Client.run(env.TOKEN) 
