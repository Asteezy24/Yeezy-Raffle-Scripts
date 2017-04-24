import requests
from random import getrandbits
url = 'https://www.boutique1.com/competition/yeezy'

UserAgent = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def raffle():
    for number in range(1, 10000): #change to any number you want
        mail = 'ENTER_YOUR_EMAIL_HERE+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'competition_name' : '', #first and last name only
            'surname' : '', # last name only
            'competition_email': mail, #do not change
            'mobile' : '', # phone number no spaces
            'shoe_size' : '8', #shoe size in number format
            'tc':'terms' #do not change
        }
        r = requests.post(url, data=payload, headers=UserAgent, timeout=10)

        if r.status_code == 200:
            print('Entered Boutique1 Raffle ' + str(number) + ' Times. ')
        else:
            print('Boutique1 Raffle Entry Unsuccessful.')

if __name__ == "__main__":
    raffle()
