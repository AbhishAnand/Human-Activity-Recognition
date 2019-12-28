import pandas as pd
temp=[line.rstrip() for line in open('features.txt','r').read().split('\n')]
print(len(temp))
data=pd.read_csv('X_test.txt',names=temp,delim_whitespace=True)
print(len(data))
print(data.shape)
#print(data)
y_testdata=[line.rstrip() for line in open('y_test.txt','r').read().split()]
print(len(y_testdata))
subject_id=[line.rstrip() for line in open('subject_id_test.txt','r').read().split()]
print(len(subject_id))
data['Sub_ID']=subject_id
data['Action']=y_testdata
print(data.shape)
print(data.columns)
data.to_csv(r'C:\Users\KIIT\PycharmProjects\MLProject\Test_csv\test.csv',index=False)













