import MetaTrader5 as mt5
import re
import urllib.request
import re
from datetime import datetime, date,timedelta
import pandas as pd

result = ''
Names = []
names2 =[]
Exp= []
reader = open('C:\DOCs\Bourse\PYTHON\AcACTIONS.txt', 'r')
read = reader.read()
reader.close()
url = re.findall(r'"URL": "(.*?)"', read)
pot = re.findall(r'"Potentiel": (.*?),', read)
cours = re.findall(r'"cours": (.*?),', read)
Ac = re.findall(r'"Ac": (.*?),',read)
Na = re.findall(r'"Na": (.*?),',read)
today= date.today()
today = today - timedelta(days=365)
today2 = today + timedelta(days=1)
print(today)
print(today2)
cours1y = []
TDate = date.today()
esDate = TDate - timedelta(days=365)
for i in range(len(Ac)):
    s = f'{Ac[i]}/{Na[i]}'
    Exp.append(s)
    
    res = urllib.request.urlopen(url[i])
    cod = re.findall(r'https://www.boursorama.com/cours/consensus/(.*?)/"', str(res.read()))
    
    res = urllib.request.urlopen(url[i])
    names1 = re.findall(fr'<a class="c-faceplate__company-link" href="/cours/{cod[0]}/" title="Cours (.*?)"', str(res.read()))
    print(names1)
    names2.append(names1[0])
    nvda = pd.DataFrame(mt5.copy_rates_from(names1[0].lower(),mt5.TIMEFRAME_H1,datetime(esDate.year,esDate.month,esDate.day),1))["close"]
    nvda = str(nvda)[5:]
    cours1y.append(nvda)
for a in range(len(Exp)):

    code = f'\n\t\t\t<tr>\n\t\t\t\t<td><a href="{url[a]}">{names2[a].lower()}</a></td>\n\t\t\t\t<td>{pot[a]}</td>\n\t\t\t\t<td>{cours[a]}</td>\n\t\t\t\t<td>{cours1y[a]}</td>\n\t\t\t\t<td>{Exp[a]}</td>'
    result = result + code




part1 = '<DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<style>\n\t\t\ttable {\n\t\t\t\tfont-family: arial, sans-serif;\n\t\t\t\tborder-collapse: collapse;\n\t\t\t\twidth: 100%\n\t\t\t}\n\t\t\ttd, th {\n\t\t\t\tborder: 1px solid #dddddd;\n\t\t\t\ttext-align: left;\n\t\t\t\tpadding: 8px;\n\t\t\t}\n\t\t\ttr:nth-child(even) {\n\t\t\t\tbackground-color: #dddddd;\n\t\t\t}\n\t\t</style>\n\t</head>\n\t<body>\n\t\t<table>\n\t\t\t<tr>\n\t\t\t\t<th>Name</th>\n\t\t\t\t<th>testPot</th>\n\t\t\t\t<th>Cours</th>\n\t\t\t\t<th>cours (1Year)</th>\n\t\t\t\t<th>Experts</th>\n\t\t\t</tr>'
part2 = '\n\t\t</table>\n\t</body>\n</html>'











# for i in range(a):
#     code = f""
#     result = result + code


index = open('about.html', 'w')
index.write(part1+result+part2)
index.close()
