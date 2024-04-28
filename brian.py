from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from jarvis import Jarvis_Base_Operations
import warnings
import logging
import time

ScriptDir = pathlib.Path().absolute()
logging.basicConfig(level=logging.WARNING)
warnings.simplefilter("ignore")

website = r"F:\train announcement\Small Ai\brian.html" # Enter path to your html file
model_option = Options()
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
model_option.add_argument("user-agent={user_agent}")
# model_option.add_argument("--profile-directory=Default")
# model_option.add_argument(f"user-data-dir={ScriptDir}\\Voicdata")
model_option.headless=True
model_option.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=model_option )
driver.get(website)
driver.maximize_window()
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

def wait_audi():
    while find_audio():
        time.sleep(1) 

def Speak2(txt):
    length = len(str(txt))
    if length == 0:
        pass
    else:
        # Encode the text to remove non-BMP characters
        Data = str(txt).encode('ascii', 'ignore').decode('ascii')
        # Send the encoded text to the element
        print(f"Jarvis : {Data}")
        driver.find_element(By.XPATH, value='/html/body/div/textarea').send_keys(Data)
        driver.find_element(By.XPATH, value='/html/body/div/button').click()
        driver.find_element(By.XPATH, value='/html/body/div/textarea').clear()
        sleep(1)


if __name__ == "__main__":
    while True:
        if not find_audio():
            Speak2(input("Enter your Words : "))