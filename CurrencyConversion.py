# -*- coding: utf-8 -*-
"""



"""

import requests
from bs4 import BeautifulSoup
import datetime
class Rates:
    def __init__(self, amount, exchangeDate, newCurrency):
        amount= amount.replace(' ', '')
        amount = amount.replace(',', '.')
        newCurrency= newCurrency.replace(' ', '')
        exchangeDate = exchangeDate.replace(' ', '')
        exchangeDate = exchangeDate.replace('/', '-')
        self.baseCurrency = amount[-3:].upper()
        self.newCurrency = newCurrency.upper()
        try:
             self.amount = float(amount.replace(self.baseCurrency, ''))
        except ValueError:
            print("Wrong value was entered")
            self.amount = 0
        self.exchangeDate = exchangeDate
        if(exchangeDate=='x'):
             self.newRate = Rates.GetData(self,'https://free.currconv.com/api/v7/convert?q='
                                                                 +self.baseCurrency+'_'+self.newCurrency+'&compact=ultra&apiKey=12dd2742035017a68711')
        else:
            try :
                year,month,day = exchangeDate.split('-')
                datetime.datetime(int(year),int(month),int(day))
                self.newRate = Rates.GetData(self,'https://free.currconv.com/api/v7/convert?q='
                                                                 +self.baseCurrency+'_'+self.newCurrency+'&compact=ultra&date='+self.exchangeDate+'&apiKey=12dd2742035017a68711')
            except ValueError :
                print("Wrong date entered, program will use current date instead")
                self.newRate = Rates.GetData(self,'https://free.currconv.com/api/v7/convert?q='
                                                                 +self.baseCurrency+'_'+self.newCurrency+'&compact=ultra&apiKey=12dd2742035017a68711')
     
    @staticmethod
    def GetData(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        soup_string = str(soup)        
        soup_string =soup_string.replace('}','')
        soup_string =soup_string.replace('_','')    
        soup_string =soup_string.replace('{','')         
        soup_string =soup_string.replace(':','')
        soup_string =soup_string.replace('"','')
        soup_string =soup_string.replace(self.exchangeDate,'')
        soup_string =soup_string.replace(self.baseCurrency,'')
        soup_string =soup_string.replace(self.newCurrency,'')
        return soup_string
    

        
    def GetValue(self):        
        result = round( self.amount * float(self.newRate), 2)
        return result
    
    
def GetDataEbay(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_string = str(soup.find("span", itemprop="price").text)
    tab = soup_string.split(' ')
    newString = tab[1]+tab[0]
    return newString
        


def printMenu():
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Currency conversion")
    print ("2. Currency conversion from Ebay")
    print ("3. Exit")
    print (30 * '-')
    

choice = 0
while choice != 3:
    
    printMenu()
 
    choice = input('Pick an option : ')
 
    choice = int(choice)
 
    if choice == 1:
            amount = input("Input the amount with the currency sign, example: 5.37USD  ")
            exchangeDate = input("Input the date in the format RRRR-MM-DD or enter x for current date  ")
            newCurrency = input( "Input the new currency, example: PLN   ")
            v = Rates(amount,exchangeDate, newCurrency)
            print(v.GetValue(),newCurrency)
            input("Press any key to continue")
    elif choice == 2:
            url = input("Podaj adres strony")
            exchangeDate = input("Input the date in the format RRRR-MM-DD or enter x for current date  ")
            newCurrency = input( "Input the new currency, example: PLN   ")
            amount = GetDataEbay(url)
            v = Rates(amount,exchangeDate,newCurrency)
            print(v.GetValue(),newCurrency)
            input("Press any key to continue")
    elif choice == 3:
            print ("Exiting...")

    else:    
            print ("Enter the correct number")
            choice = 0