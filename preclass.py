from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def preclass(urlstring,traintxt):
    INFO = []
    TIT = [];USR = [];DAT = [];CNT = []
    RUS = [];RDT = [];RTI = [];RCT = []

    #gettest
    def gettest(urlstring):
        try:
            html = urlopen(urlstring)
            bs0bj = BeautifulSoup(html, 'lxml')
            try:
                # class_values = set()
                class_values = []
                for item in bs0bj.body.find_all("", {"class": re.compile("^.*")}):
                    if len(item['class']) == 1:
                        # class_values.add(item['class'][0])
                        class_values.append(item['class'][0])
                    else:
                        for i in item['class']:
                            # class_values.add(i)
                            class_values.append(i)
                # print('get testset')
                test = []
                originval = []
                for value in class_values:
                    originval.append(value)
                    if '-' in value:
                        s = value.split('-')
                        d = ' '
                        value = d.join(s)
                    if '_' in value:
                        s = value.split('_')
                        d = ' '
                        value = d.join(s)
                    test.append(value)
                testset = test
                # testset=print(test)
                return (originval, testset)
            except IOError:
                print('IOError')
                pass
        except:  # or error.HTTPError :#or HTTPError or error.URLError:
            print('Error')
            pass
        print('done')

    (originval, testval)=gettest(urlstring)

    #predict
    def predict(testval,traintxt):
        with open(traintxt) as f:
            file = open(traintxt, 'r')  # 训练集
            lines = file.readlines()
            attribute = []
            trainval = []
            info = []
            tit = [];usr = [];dat = [];cnt = []
            rus = [];rdt = [];rti = [];rct = []

            for tag in lines:
                tag = tag.strip('\n')
                separate = tag.split(' ')
                joint = ' '
                trainval.append(joint.join(separate[1:]))
                attribute.append(separate[0])

            allval = testval + trainval  # 合并列表同时向量化

            from sklearn.feature_extraction.text import CountVectorizer
            vectorizer = CountVectorizer()
            vecval = vectorizer.fit_transform(allval).todense()

            # randomforest分类
            from sklearn.ensemble import RandomForestClassifier
            test_data = vecval[:-len(trainval)]
            rf = RandomForestClassifier()

            train_data = vecval[-len(trainval):]
            train_target = attribute
            rf.fit(train_data, train_target)
            # rf.predict(test_data)

            for i in range(len(test_data)):
                P = rf.predict(test_data[i])
                if P == 'INFO':
                    info += [i]

                if P == 'TIT':
                    tit += [i]
                if P == 'USR':
                    usr += [i]
                if P == 'DAT':
                    dat += [i]
                if P == 'CNT':
                    cnt += [i]

                if P == 'RUS':
                    rus += [i]
                if P == 'RDT':
                    rdt += [i]
                if P == 'RTI':
                    rti += [i]
                if P == 'RCT':
                    rct += [i]
            info = info
            usr = usr;tit = tit;dat = dat;cnt = cnt
            rus = rus;rdt = rdt;rti = rti;rct = rct
            return (info, usr, dat, tit, cnt, rus, rdt, rti, rct)

    (info, usr, dat, tit, cnt, rus, rdt, rti, rct)=predict(testval,traintxt)

    for j in info:
        INFO.append(originval[j])
    for j in tit:
        TIT.append(originval[j])  # TIT.add(tsval[i])
    for j in usr:
        USR.append(originval[j])
    for j in dat:
        DAT.append(originval[j])
    for j in cnt:
        CNT.append(originval[j])
    for j in rti:
        RTI.append(originval[j])
    for j in rus:
        RUS.append(originval[j])
    for j in rdt:
        RDT.append(originval[j])
    for j in rct:
        RCT.append(originval[j])
    print('INFO:',INFO)
    print('USR:', USR);print('DAT:', DAT);print('TIT:', TIT);print('CNT:', CNT)
    print('RUS:', RUS);print('RDT:', RDT);print('RTI:',RTI);print('RCT:',  RCT)
    return (INFO,USR,DAT,TIT,CNT,RUS,RDT,RTI,RCT)

(INFO,USR,DAT,TIT,CNT,RUS,RDT,RTI,RCT)=preclass('http://forum.home.news.cn/detail/140821643/1.html','class_values.txt')
