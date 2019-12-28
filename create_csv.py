import pandas as pd
temp=[line.rstrip() for line in open('features.txt','r').read().split('\n')]
print(len(temp))
data=pd.read_csv('X_test.txt',names=temp,delim_whitespace=True)
print(data.shape)
print(data)
data.to_csv(r'C:\Users\KIIT\PycharmProjects\MLProject\Test_csv\test.csv',index=False)













