def predict(testval):
    file = open('rewCV.txt', 'r')#训练集
    lines = file.readlines()
    attribute = []
    trainval = []
    IFM = [];ifm = []
    TIT = [];tit = [];USR = [];usr = [];DAT = [];dat = [];CNT = [];cnt = []
    RUS = [];rus = [];RDT = [];rdt = [];RTI = [];rti = [];RCT = [];rct = []
    for tag in lines:
        tag = tag.strip('\n')
        separate = tag.split(' ')
        joint = ' '
        trainval.append(joint.join(separate[1:]))
        attribute.append(separate[0])
        #a, b = tag.split(' ', 1)
        #trainval.append(b)
        #attribute.append(a)

    allval = testval + trainval  # 合并列表同时向量化

    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()
    vecval = vectorizer.fit_transform(allval).todense()

    #randomforest分类
    from sklearn.ensemble import RandomForestClassifier
    test_data = vecval[:-len(trainval)]
    rf = RandomForestClassifier()

    train_data = vecval[-len(trainval):]
    train_target = attribute
    rf.fit(train_data, train_target)
    #rf.predict(test_data)

    for i in range(len(test_data)):
        P = rf.predict(test_data[i])
        if P == 'IFM':
            ifm += [i]

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
    ''''''
    for j in ifm:
        IMF.append(testval[j])

    for j in tit:
        TIT.append(testval[j])  # TIT.add(tsval[i])
    for j in usr:
        USR.append(testval[j])
    for j in dat:
        DAT.append(testval[j])
    for j in cnt:
        CNT.append(testval[j])

    for j in rti:
        RTI.append(testval[j])
    for j in rus:
        RUS.append(testval[j])
    for j in rdt:
        RDT.append(testval[j])
    for j in rct:
        RCT.append(testval[j])
    ''''''
    print('IMF:',len(IFM),IFM)
    print('USR:', len(USR),USR);print('DAT:',len(DAT),DAT);print('TIT:',len(TIT),TIT);print('CNT:',len(CNT),CNT )
    print('RUS:', len(RUS),RUS);print('RDT:',len(RDT), RDT);print('RTI:',len(RTI),RTI);print('RCT:',len(RCT),RCT)

    #return USR,DAT,TIT,CNT,RUS,RDT,RTI,RCT,IMF


'''#用来验证结果
file = open('rewCV.txt','r')
lines = file.readlines()
attribute=[]
value=[]


for tag in lines:
    tag=tag.strip('\n')
    separate = tag.split(' ')
    joint = ' '
    value.append(joint.join(separate[1:]))
    attribute.append(separate[0])
#print(attribute)
#print(value)
tsval=value#需要替换*testval 由测试页面导入的结果
'''
''''''
from gettest import gettest
tsval=gettest('http://bbs.tianya.cn/post-no05-447563-1.shtml')
predict(tsval)


