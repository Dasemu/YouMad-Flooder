import platform
from time import sleep
from termcolor import colored, cprint
import os

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def init():
    if platform.system() == "Windows":
        windows()
    elif platform.system() == "Linux":
        linux()
    elif platform.system() == "MacIS":
        mac_os()


def windows():
    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def init():
        driver.get("https://web.whatsapp.com")
        driver.minimize_window()

        try:
            WebDriverWait(driver, 600).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas")))
        finally:
            pass

        cprint("|--> Please, login with your Whatsapp Account.", color="red", attrs=['bold'])
        input(colored("$--> Press return to continue ", color="red", attrs=['bold']))

        driver.maximize_window()

        while check_exists_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span") is False:
            if check_exists_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/span/button") is True:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[2]/div/span/button").click()
            sleep(1)

        driver.minimize_window()

        main()

    def main():
        def user():
            victim = input(colored("$--> Victim's Phone Number (with country code). ", color="red", attrs=['bold']))
            invalid_chars = ['+', ' ', '-']
            for i in invalid_chars:
                victim = victim.replace(i, '')

            reptxt = input(colored('    |-$ Word/Sentence that you want to send Multiple Times > ', color="red", attrs=['bold']))
            repcount = int(input(colored('    |-$ How many times ? > ', color="red", attrs=['bold'])))

            driver.get(f'https://web.whatsapp.com/send?phone={victim}&text&source&data&app_absent')

            driver.maximize_window()

            try:
                WebDriverWait(driver, 600).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span")))
            finally:
                pass

            sleep(3)

            if check_exists_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]") is False:
                driver.minimize_window()
                cprint("|-->Invalid phone number, restarting.", color="red", attrs=['bold'])
                sleep(3)
                os.system('cls||clear')
                victim()
            else:
                driver.maximize_window()
                for i in range(repcount):
                    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]").send_keys(reptxt + Keys.ENTER)
                    
            driver.close()


        def group():
            victim = input(colored("$--> Group name (you have to be alredy in). ", color="red", attrs=['bold']))

            reptxt = input(colored('    |-$ Word/Sentence that you want to send Multiple Times > ', color="red", attrs=['bold']))
            repcount = int(input(colored('    |-$ How many times ? > ', color="red", attrs=['bold'])))

            driver.maximize_window()

            if check_exists_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]"):
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]").send_keys(victim + Keys.ENTER)
                
            

            try:
                WebDriverWait(driver, 600).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span")))
            finally:
                pass

            sleep(3)

            if check_exists_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]") is False:
                driver.minimize_window()
                cprint("|-->Invalid phone number, restarting.", color="red", attrs=['bold'])
                sleep(3)
                os.system('cls||clear')
                main()
            else:
                driver.maximize_window()
                for i in range(repcount):
                    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]").send_keys(reptxt + Keys.ENTER)
                    
            driver.close()

        cprint("|--> Choose the mode you want to use.", color="red", attrs=['bold'])
        cprint("    1.--> User.", color="red", attrs=['bold'])
        cprint("    2.--> Group.", color="red", attrs=['bold'])
        mode = input(colored("$-->  ", color="red", attrs=['bold']))

        invalid_chars = ['+', ' ', '-']
        for i in invalid_chars:
            mode = mode.replace(i, '')

        if mode.isdigit():
            if int(mode) == 1:
                user()
            if int(mode) == 2:
                group()
            else:
                cprint("|-->Invalid mode chosed, restarting.", color="red", attrs=['bold'])
                sleep(3)
                os.system('cls||clear')
                main()
        elif mode.lower() == "user":
            user()
        elif mode.lower() == "group":
            group()
        else:
            cprint("|-->Invalid mode chosed, restarting.", color="red", attrs=['bold'])
            sleep(3)
            os.system('cls||clear')
            main()


    r = requests.get("https://chromedriver.storage.googleapis.com/95.0.4638.54/chromedriver_win32.zip", allow_redirects=True)
    open('driver.zip', 'wb').write(r.content)
    # with zipfile.ZipFile('driver.zip', 'r') as zip_ref:
    #   zip_ref.extractall('driver.zip')

    driver = webdriver.Chrome()

    init()


def linux():
    cprint("linux", color="red", attrs=['bold'])


def mac_os():
    cprint("macOS", color="red", attrs=['bold'])
