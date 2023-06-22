import discord ,discord.message,env,random
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

# discord init
intents = discord.Intents.default()
intents.message_content = True
Client = discord.Client(intents=intents)
# selenium init
#chromeDriver = "chromedriver.exe"
# chromeDriver = Service(executable_path="D:\\Coding\\Projects\\Python\\Discord Bot\\chromedriver.exe")
options = webdriver.ChromeOptions().add_argument("--ignore-certificate-errors")
# driver = webdriver.Chrome(service=chromeDriver, options=options)
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
        randomArticle = random.randint(1,20)
        await message.channel.send("Just a second...")
        meme = getImgUrl(driver=driver , tag=msg[1] , article=str(randomArticle),dismsg=message)
        await message.channel.send(meme)
    

# gets the image url from the website  
def getImgUrl(driver,tag,dismsg,article=1,):
    def scrollDown(driver):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    print(f'tag is {tag}')
    print(f'article number is {article}')
    num = 1
    scrollDown(driver=driver)

    # check if tag exists or not 
    try:
        driver.get(f"https://www.memedroid.com/memes/tag/{tag}")
    except:
        #await dismsg.channel.send(f"could not find meme on {tag}")
        print(f"could not find meme on {tag}")

    # checks if article exists or not 
    try:
        memeUrl = driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div/div[2]/section/div[2]/article[{article}]/div[1]/a/picture/img')
    except:
        while num < int(article):
            num += 1
            try:
                memeUrl = driver.find_element(by=By.XPATH,value=f'/html/body/div[5]/div/div[2]/section/div[2]/article[{num}]/div[1]/a/picture/img')
                break
            except:
                if num == 1:
                    #await dismsg.channel.send("There was some problem :(")
                    print("There was some problem :(")
                    break
                else:
                    continue

    print(memeUrl.get_attribute('src'))
    return memeUrl.get_attribute('src')



# runs disord bot
Client.run(env.TOKEN) 
