import numpy as np
import sys
from sklearn.neighbors.nearest_centroid import NearestCentroid


x = np.loadtxt(str(sys.argv[1]),usecols=(3,4,5,6))
y = np.loadtxt(str(sys.argv[1]),usecols=(7,))

clf = NearestCentroid()
clf.fit(x, y)

while(1):
  s = raw_input("enter your test data vector\n")
  data = map(float, s.split())
  print (clf.predict(data))  
  





