
from math import floor
import MetaTrader5 as mt5
import re
import pandas as pd
from datetime import datetime, date,timedelta
import smtplib
a=0
msg = ''
mt5.initialize(login=26904062, server="XM.COM-MT5",password="demo0Naceur")
if not mt5.initialize():
    print(mt5.last_error())
    quit()

login = 26904062
password = 'demo0Naceur'
server = 'XM.COM-MT5'
mt5.login(login,password,server)
account_info = mt5.account_info()
ords = mt5.positions_get()
positions = str(mt5.positions_get())
TDate = date.today()
esDate = TDate - timedelta(days=365)
Names = re.findall(r"symbol='(.*?)'", positions)
print(Names)
current_price = re.findall(r"price_current=(.*?),", positions)
Bought_price = re.findall(r"price_open=(.*?),",positions)
for i in range(len(Names)):
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1500) 
    My_data = pd.DataFrame(mt5.copy_rates_from(Names[i],
                                            mt5.TIMEFRAME_H1,
                                            datetime(esDate.year ,esDate.month, esDate.day),
                                            1))["close"]
    print(My_data)
    price = str(My_data)[5:]

    if float(current_price[i]) > float(Bought_price[i]) + (float(Bought_price[i])*5)/100:
        a+=1
        pot = floor(((float(current_price[i]))-float(Bought_price[i])))*100/float(float(Bought_price[i]))
        msg = msg+ f'\n{Names[i]}has been promoted for {pot}%, bought at {Bought_price[i]}$ current price is {current_price[i]}\n --------------------------'
    elif float(Bought_price[i]) > float(current_price[i]) + float(current_price[i]) *(5/100):
        a+=1
        pot = floor((float(Bought_price[i])-float(current_price[i]))*(100/float(Bought_price[i])))
        msg = msg + f'\n{Names[i]}has been demoted for {pot}%, bought at {Bought_price[i]}$ current price is {current_price[i]}\n -------------------------'

    print(float(Bought_price[i]))
    print(float(current_price[i]))
    print(float(Bought_price[i])+(float(Bought_price[i])*5)/100)
if a == 0:
    msg = 'nothing new'


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('ademrhouma866@gmail.com', 'mqzy uigj uaox vban')
    smtp.sendmail('ademrhouma866@gmail.com', 'ademrhouma077@gmail.com',msg) 
    #smtp.sendmail('ademrhouma866@gmail.com', 'm.n.rhouma@gmail.com', msg)



