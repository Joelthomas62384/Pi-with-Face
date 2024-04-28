from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import logging
import pywhatkit as pw
from datetime import datetime
from file_opener import openfile
import time
from face_checker import main
from brian import Speak2 as Speak
from speech import SpeechRecognitionModel
from brian import find_audio


ScriptDir = pathlib.Path().absolute()
logging.basicConfig(level=logging.WARNING)
warnings.simplefilter("ignore")

url = ""
with open('passkey.txt','r') as f:
    url = f.read()
    
user_name = main()
user_name = "Roshan" if user_name == None else user_name 


text_area = r"/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea"
submit_button = r"/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button"
reply_element = r"/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]"

def problem_solve():
    print("Error Raised")
    print("Solving Automatically...")

    try:
         WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div/div/div/div[2]/button"))).click()
         WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div/div/div/div/div[2]/button"))).click()
    except:
        pass

    try:
        current_url = driver.current_url
        if "https://pi.ai/talk" in current_url or "https://pi.ai/discover" in current_url or "https://pi.ai/profile" in current_url:
            driver.get("https://pi.ai/talk")


    except :
        pass
    print("Problem Solved...")
def first_time(user_name):
    try:
        while True:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div[2]/div[2]/div/button"))).click()
    except:
        pass

    try:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div/div[2]/div[3]/div/div/div/div/textarea"))).send_keys(user_name)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div/div[2]/div[3]/div/div/div/button"))).click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div/div[2]/div[3]/div/div/div[2]/button[2]"))).click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div/div[2]/div[2]/div[2]/button"))).click()


    except:
        pass


def entry_animations(user_name):
    try:
        # first_time(user_name)
        first_time(user_name)
    except:

        pass
    finally:
        # input()
        

        Speak(f"{chat_with_py(f'Hello Jarvis I am {user_name} speaking to you ')}")
        # reply = chat_with_py("Hello Jarvis")
        # print(reply)
        # Enable Audio
        # WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button"))).click()
        # try:
        #      WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[6]"))).click()
        # except:
        #     pass



def response_taker():
    text_element_locator = (By.XPATH, reply_element)

    response_element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(text_element_locator)
    )


    response_text = response_element.text
    return response_text
        
def find_enabled():
    try:
        while True:
            driver.find_element(by=By.XPATH,value=text_area).send_keys("h")
            submit_enabled = driver.find_element(by=By.XPATH,value=submit_button).is_enabled()
            if submit_enabled:
                driver.find_element(by=By.XPATH,value=text_area).clear()
                break
            else:

                pass
    except:
        pass
def chat_with_py(text):
    try:
        input_element =  WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,text_area)))
        input_element.send_keys(text)
        input_element.clear()

        
        button_element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,submit_button)))
        button_element.click()
        find_enabled()
        response_text  = response_taker()
    except:
        problem_solve()
        input_element =  WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,text_area)))
        input_element.send_keys(text)
        input_element.clear()
        button_element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,submit_button)))
        button_element.click()
        find_enabled()
        response_text  = response_taker()

    return response_text

def find_audio():
    is_audio_playing = driver.execute_script("""
    var audioElements = document.querySelectorAll('audio');
    var isPlaying = false;
    for (var i = 0; i < audioElements.length; i++) {
        if (!audioElements[i].paused) {
            isPlaying = true;
            break;
        }
    }
    return isPlaying;
""")
    return is_audio_playing

def wait_for_audio():
    while find_audio():
        time.sleep(1) 






chrome_option = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_option.add_argument("user-agent={user_agent}")
# chrome_option.add_argument("--profile-directory=Default")
# chrome_option.add_argument(f"user-data-dir={ScriptDir}\\Brain\\DataBase\\user-data")
chrome_option.headless=True
chrome_option.add_argument("--headless=new")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option )
driver.get(url)
driver.maximize_window()
entry_animations(user_name)

while True:
    prompt = ""
    if not find_audio():
    # prompt = input("Enter your query : ")
        prompt = SpeechRecognitionModel()
        print(f"{user_name} : {prompt}")
        prompt = str(prompt).lower()


    if prompt !="":

        if "youtube" in prompt and "play" in prompt:
            prompt = prompt
            prompt = prompt.replace("youtube","")
            prompt = prompt.replace("jarvis","")
            prompt = prompt.replace("play","")
            prompt = prompt.replace("can","")
            prompt = prompt.replace("you","")
            prompt = prompt.replace("for","")
            prompt = prompt.replace("me","")
            Speak(f"Playing {prompt} on Youtube") 
            pw.playonyt(prompt)

        elif "what" in prompt and "time" in prompt:
            time_now = datetime.now().strftime("%I:%M:%p")
        
            Speak(f"The time is {time_now}")
        
        elif "open" in prompt:
            prompt = prompt.replace("open","")
            prompt = prompt.replace("jarvis","")
            prompt = prompt.replace("please","")
            prompt = prompt.replace("can","")
            prompt = prompt.replace("you","")
            prompt = prompt.replace("for","")
            prompt = prompt.replace("me","")

            Speak(f"Opening {prompt}")
            openfile(prompt)


            

        else:
            wait_for_audio()
            try:
                problem_solve(user_name)
                reply = chat_with_py(prompt)

            except:
                reply = chat_with_py(prompt)

            # print(reply)
                

        
            print("")
            Speak(reply)
            print("")