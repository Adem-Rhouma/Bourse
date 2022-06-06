from math import floor
import urllib.request
import re

import smtplib
try:

    msg = ''
    stringer = False
    with open('yachatstxt.txt', 'r') as file:
        read = file.read()

        
    pod = re.findall(r'"Code": "(.*?)"', read)
    for eachURL in pod:        
        pot1 = re.findall(r'"Potentiel": (.*?),', read)   
        caurse= re.findall(r'"Cours": (.*?),', read)
        
        ur1 = 'https://www.boursorama.com/cours/consensus/%s'% (eachURL)
        res = urllib.request.urlopen(ur1)
        pot = re.findall(r'<span class="c-table-analyst-goal__potential-value">(.*?)%</span>', str(res.read()))
        res = urllib.request.urlopen(ur1)
        cours = re.findall(r'</div><div><span class="c-instrument c-instrument--last" data-ist-last>(.*?)</span></div>', str(res.read()))
        read = read.replace(f'"Potentiel": {pot1[pod.index(eachURL)]},', f'"Potentiel": {pot[0]},')
        oldcours = re.findall(r'"old cours": (.*?),', read)
        #print(cours[0])

        try:
            read = read.replace(f'"Cours": {caurse[pod.index(eachURL)]},', f'"Cours": {cours[0]},')
            # print(caurse)
            
            with open('yachatstxt.txt', 'w') as file:
                file.write(read)
            if float(cours[0]) > float(oldcours[pod.index(eachURL)]) + (float(oldcours[pod.index(eachURL)])*5)/100:
                stringer = True
                newPot = floor(((float(cours[0])-float(oldcours[pod.index(eachURL)]))*100)/float(float(cours[0])))
                msg = msg + f'\n({eachURL}) has been promoted for {newPot}%, your old cours was {oldcours[pod.index(eachURL)]}, and now it costs {cours[0]}'+'\n---------------------------------------------'
            elif float(oldcours[pod.index(eachURL)]) > float(cours[0]) + float(cours[0]) *(5/100):
                stringer = True
                newPot1 = floor((float(oldcours[pod.index(eachURL)])-float(cours[0]))*(100/float(oldcours[pod.index(eachURL)])))
                msg = msg + f'\nthe prooduct: {eachURL} is down for {newPot1}%'+'\n---------------------------------------------'
            else:
                print('all good here')
        except:
            stringer = True
            msg = msg +f'\n{eachURL} has a problem... or your code'+'\n---------------------------------------------'
except:
    stringer= True
    msg = 'there is something wrong with your code'
if stringer:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('ademrhouma866@gmail.com', 'mqzy uigj uaox vban')
        smtp.sendmail('ademrhouma866@gmail.com', 'm.n.rhouma@gmail.com', msg)    


