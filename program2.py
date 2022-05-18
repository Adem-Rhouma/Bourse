import urllib.request
import re
with open('C:\DOCs\Bourse\PYTHON\yachatstxt.txt', 'r') as file:
    read = file.read()
option = input('check 1cours or all?')
if option == '1cours' :
    code = input('code: ')
    ur1 = 'https://www.boursorama.com/cours/consensus/%s' % (code, )
    res = urllib.request.urlopen(ur1)
    cours = re.findall(r'</div><div><span class="c-instrument c-instrument--last" data-ist-last>(.*?)</span></div>', str(res.read()))



    
    searcher = bool(re.search(code, read))
    if searcher:
        pod = re.findall(r'"Code": "(.*?)"', read)            
        pos1 = pod.index(code)
        caurse= re.findall(r'"Cours": (.*?),', read)
    if float(cours[0]) > float(caurse[pos1])+(float(caurse[pos1])*5)/100:
        read = read.replace(f'"Cours": {caurse[pos1]},', f'"Cours": {cours[0]},')
        with open('C:\DOCs\Bourse\PYTHON\yachatstxt.txt', 'w') as file:
            file.write(read)
elif option == 'all':
    pod = re.findall(r'"Code": "(.*?)"', read)
    for eachURL in pod:           
        caurse= re.findall(r'"Cours": (.*?),', read)

        ur1 = 'https://www.boursorama.com/cours/consensus/%s'% (eachURL)
        res = urllib.request.urlopen(ur1)
        cours = re.findall(r'</div><div><span class="c-instrument c-instrument--last" data-ist-last>(.*?)</span></div>', str(res.read()))

        try:
            if float(cours[0]) > float(caurse[pod.index(eachURL)]) + (float(caurse[pod.index(eachURL)])*5)/100:
                read = read.replace(f'"Cours": {caurse[pod.index(eachURL)]},', f'"Cours": {cours[0]},')
                print(f'Attention {eachURL} has been promoted check it out!!!!!')
                with open('C:\DOCs\Bourse\PYTHON\yachatstxt.txt', 'w') as file:
                    file.write(read)
            else:
                print('all good here')
        except:

            print('exception for', eachURL)
