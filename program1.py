from textwrap import indent
import urllib.request
import re
import json
import operator


def urlread(web):
  global res
  res = urllib.request.urlopen(web)


def sorter(e):
  return e['Potentiel']

def sorter2(r):
  return r['Ac'] / r['Na'] 

def rapp(r):
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
counter=0

for eachURL in allURLS:
  urlread(eachURL)
  x = re.findall(r'href="(.*?)"', str(res.read()))

  for eachX in x:
    if '/cours/' in eachX and 7<len(eachX) <22:
      U = re.findall(r'/cours/(.*?)/', eachX)
      for eachT in U:
        if eachT not in realT:
          realT.append(eachT)
          URL = 'https://www.boursorama.com/cours/consensus/%s' % (eachT,)


headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML,like Gecko) Chrome/24.0.1312.27 Safari/537.17'
req = urllib.request.Request('https://www.xm.com/fr/stocks', headers= headers)


res = urllib.request.urlopen(req)
read = str(res.read())

for ur1 in range(len(realT)):

  res = urllib.request.urlopen(f'https://www.boursorama.com/cours/{realT[ur1]}/')
  name = re.findall(fr'<a class="c-faceplate__company-link" href="/cours/{realT[ur1]}/" title="Cours (.*?)"', str(res.read()))
  print(realT[ur1])
  print(name[0].lower())

  if name[0].lower() in read:
      print('test in')

    #for ur1 in range(160):
      counter +=1
      print('C O U N T E R  :   ',counter)
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
          res = urllib.request.urlopen(url)
          x = re.findall(r'Acheter</span></div> (.*?) <div class="o-vertical-interval-bottom-large"></div>' , str(res.read()))
          for eachX in x: 
            print('dsadas')   
            Table = re.findall(r'<span class="c-table__content">(.*?)</span>', eachX)
            Ac = str(Table[4])
            Na = str(Table[34])
            Eur = str(Table[46])                          
            res = urllib.request.urlopen(url)
            Pot = re.findall(r'<span class="c-table-analyst-goal__potential-value">(.*?)%</span>', str(res.read()))
            res = urllib.request.urlopen(url)
            name = re.findall(r'<a class="c-faceplate__company-link" href="/cours/1rPAB/" title="Cours (.*?)">AB SCIENCE</a>', str(res.read()))
            if float(Ac) > float(Na)/2:
              if (float(cours1[0]) > 10.00) and (int(Ac)>4):
                if url not in d or url not in info:
                  print('testy testy')

                  val1=int(Ac) / int(Na)
                  info.append({"Ac":int(Ac),"Na":int(Na), "Potentiel":float(Pot[0]), "cours": float(cours1[0]), "URL": url})
                
                  d.append({"val1":val1,"Ac":int(Ac),"Na":int(Na), "Potentiel":float(Pot[0]), "cours": float(cours1[0]), "URL": url})
              
                  #info.sort(key=sorter, reverse=True)
                  #pprint.pprint(sorted(info, key=operator.itemgetter('Ac', 'Na')))
          
                  #d.sort(key=sorter2, reverse=True)        
            
            print(Ac,'/',Na,'Potentiel',Pot[0], 'cours:', cours1[0],   realT[ur1])
        else:
          print('invalid', realT[ur1])
      except:
        print('exception occured %s' % (realT[ur1],)) 
  else:
    print('test not in')

#a_list=info
#a_list=sorted(info, key=operator.itemgetter('Ac', 'Na'))
info.sort(key=sorter, reverse=True)
    

with open('C:\DOCs\Bourse\PYTHON\AcACTIONS.txt', 'w') as f:
  for i in range(len(info)):
    f.write(json.dumps(info[i], indent=2))

print(info)

a_list=d
a_list=sorted(d, key=operator.itemgetter('val1','Ac', 'Potentiel'),reverse=True)
print(a_list)

with open('C:\DOCs\Bourse\PYTHON\Experts123.txt', 'w') as f:
  for i in range(len(a_list)):
    f.write(json.dumps(a_list[i], indent=2))