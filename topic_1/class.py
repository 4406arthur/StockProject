import numpy as np
from sklearn.svm import SVC
import json
import unicodedata


x = np.loadtxt('data.out',usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12))
y = np.loadtxt('data.out',usecols=(13,))



 
clf = SVC()
print 'training'
clf.fit(x, y)
print 'done'




while(1):
  s = raw_input("enter your test data vector\n")
  data = map(float, s.split())
  print (clf.predict(data))  
  


