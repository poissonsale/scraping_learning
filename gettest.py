from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def gettest(urlstring):
    try:
        html = urlopen(urlstring)
        bs0bj = BeautifulSoup(html,'lxml')
        try:
            #class_values = set()
            class_values = []
            for item in bs0bj.body.find_all("",{"class":re.compile("^.*")}):
                if len(item['class'])==1:
                        #class_values.add(item['class'][0])
                        class_values.append(item['class'][0])
                else:
                        for i in item['class']:
                            #class_values.add(i)
                            class_values.append(i)
            #print('get testset')
            test=[]
            origin=[]
            for value in class_values:
                origin.append(value)
                if '-' in value:
                    s = value.split('-')
                    d = ' '
                    value=d.join(s)
                if '_' in value:
                    s = value.split('_')
                    d = ' '
                    value = d.join(s)
                test.append(value)
            testset=test
            #testset=print(test)
            return (origin,testset)
        except IOError :
            print('IOError')
            pass
    except  :#or error.HTTPError :#or HTTPError or error.URLError:
        print('Error')
        pass
    print('done')
