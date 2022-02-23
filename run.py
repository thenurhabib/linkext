#!/usr/bin python3

# Import Functions From Modules
from requests import get
from colorama import Fore
from bs4 import BeautifulSoup

# Important Variables
singleLineBreck = "\n"
blue = Fore.BLUE
yellow = Fore.YELLOW
green = Fore.GREEN
cyan = Fore.CYAN
red = Fore.RED


# Main Class
class ExtractorClass:
    def __init__(self, geturlFromUser: str):
        self.__geturlFromUser = geturlFromUser

    def sendRequestFunction(self) -> BeautifulSoup:
        try:
            reqs = get(self.__geturlFromUser)
            soup = BeautifulSoup(reqs.text, "html.parser")
            return soup
        except Exception as error:
            pass

        
    def cliPrinterFunction(self, mainResponse: BeautifulSoup) -> None:
        try:
            geturlFromUsers = []
            for link in mainResponse.find_all('a'):
                print(f"[*] Link: {link.get('href')}")
        except AttributeError:
            print(f"{red}{singleLineBreck}Enter geturlFromUser With https:// [ - example: https://{geturlFromUser} -] ")
            

if __name__ == '__main__':
    
    geturlFromUser = input(f"{blue} [habib{yellow}@{blue}linux]─ {yellow}$ {cyan}Enter here: {green}")
    extractor = ExtractorClass(geturlFromUser)
    mainResponse = extractor.sendRequestFunction()
    extractor.cliPrinterFunction(mainResponse)
