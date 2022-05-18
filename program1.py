from textwrap import indent
import urllib.request
import re
import json


def urlread(web):
  global res
  res = urllib.request.urlopen(web)


def sorter(e):
  return e['Potentiel']

def sorter2(r):
  return r['Ac'] / r['Na']

d =[]

# def sorter2(c):
#   return abs(float(c['Ac']) / float(c['Na']))


Url_1 = 'https://www.boursorama.com/bourse/actions/cotations/'

allURLS = ['https://www.boursorama.com/bourse/actions/cotations/']



urlread(Url_1)
y = re.findall(r'href="/bourse/actions/cotations/(.*?)"', str(res.read()))
for eachY in y:
  URL_1 = 'https://www.boursorama.com/bourse/actions/cotations/%s' % (eachY,)
  if 'page' in eachY and URL_1 not in allURLS:
    allURLS.append(URL_1)	

realT = []
info=[]
OutPut=[]

for eachURL in allURLS:
  urlread(eachURL)
  x = re.findall(r'href="(.*?)"', str(res.read()))

  for eachX in x:
    if '/cours/' in eachX and 7<len(eachX) <22:
      U = re.findall(r'/cours/(.*?)/', eachX)
      for eachT in U:
        realT.append(eachT)
        URL = 'https://www.boursorama.com/cours/consensus/%s' % (eachT,)

for ur1 in range(len(realT)-1):
  url = 'https://www.boursorama.com/cours/consensus/%s/' % (realT[ur1],)

  res = urllib.request.urlopen(url)
  try:
    cours1 = re.findall(r'</div><div><span class="c-instrument c-instrument--last" data-ist-last>(.*?)</span></div>', str(res.read()))
    urlread(url)
    paragraph = re.findall(r'<td class="c-table__cell(.*?)Acheter</span>', str(res.read()))
    urlread(url)
    test = bool(re.search('<div class="c-table__decorator">', paragraph[0]))
    if test:
      print('valid')
      x = re.findall(r'Acheter</span></div> (.*?) <div class="o-vertical-interval-bottom-large"></div>' , str(res.read()))
      for eachX in x:    
        Table = re.findall(r'<span class="c-table__content">(.*?)</span>', eachX)
        Ac = str(Table[4])
        Na = str(Table[34])
        Eur = str(Table[46])                          
        res = urllib.request.urlopen(url)
        Pot = re.findall(r'<span class="c-table-analyst-goal__potential-value">(.*?)%</span>', str(res.read()))
        if float(Ac) > float(Na)/2:
          if float(cours1[0]) > 10.00:
            info.append({"Ac":int(Ac),"Na":int(Na), "Potentiel":float(Pot[0],), "cours": float(cours1[0]), "Code":"%s" % (realT[ur1],)})
            info.sort(key=sorter, reverse=True)    
            d.append({"Ac":int(Ac),"Na":int(Na), "Potentiel":float(Pot[0],), "cours": float(cours1[0]), "Code":"%s" % (realT[ur1],)})
            d.sort(key=sorter2, reverse=True)        
        
        print(Ac,'/',Na,'Potentiel',Pot[0], 'cours:', cours1[0],   realT[ur1])
    else:
      print('invalid', realT[ur1])
  except:
    print('exception occured %s' % (realT[ur1],)) 

print(info)

with open('C:\DOCs\Bourse\PYTHON\AcACTIONS.txt', 'w') as f:
  for i in range(30):
    f.write(json.dumps(info[i], indent=2))

with open('C:\DOCs\Bourse\PYTHON\Experts123.txt', 'w') as f:
  for i in range(30):
    f.write(json.dumps(d[i], indent=2))



















