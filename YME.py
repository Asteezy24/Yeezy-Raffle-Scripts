import requests
from random import getrandbits

url = 'https://mailchimp.sleeknote.com/'

User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

def raffle():
    for number in range(1 , 100000): #Change the 100,000 to however many times you want to enter the raffle.

        mail = 'ENTER_YOUR_EMAIL_HERE+{}@gmail.com'.format(getrandbits(25))

        data = {
            'name' : '', #enter first and last name
            'email' : mail, #do not change
            'Kid 20-27 or Unisex UK 4-12' : '8', # enter shoe size in number form
            'Enter City' : '', # enter in City, State form
            'SleeknoteId' :'24494', #do not change
            'CustomerId' : '3096', #do not change
            'SignupPage' : 'https://www.ymeuniverse.com/en/blog/2017/04/21/yeezy-boost-350-v2-cream-white/', #do not change
            'UserAgent' : User_Agent #do not change
        }

        r = requests.get(url, params=data, timeout = 10) #10 second timeout

        if r.status_code == 200:
            print('Entered Raffle ' + str(number) + ' Times. ')
        else:
            print('Raffle Entry Unsuccessful.')

if __name__ == "__main__":
    raffle()
