import numpy as np
from sklearn.neighbors.nearest_centroid import NearestCentroid
import json



tokens = open('data').read().split()
with open('data.out','w') as output:
	i = 0
	j = 13
	for k in range(len(tokens)/13):
		data = []
		a = tokens[i+3]
		b = tokens[i+6]
		c = tokens[i+8]
		d = tokens[i+10]
		if (a == '--') | (c == '--') | (d == '--') :
			i+=13
			j+=13
			continue	
		
		if (float(a) - float(b) > 0):
			label = '0'
		else:
			label = '1'
				
		for item in tokens[i:j]:
			output.write("%s " % item)
		output.write(" "+label+'\n')


		i+=13
		j+=13

# with open('final.json', 'w') as outfile:
#     json.dump(data, outfile)



# train = np.array(data)


#print train[:,1].shape

# #main
# clf = NearestCentroid()
# clf.fit(train[:,0],train[:,1])


# # while(1):
# #   s = raw_input("enter your test data vector\n")
# #   data = map(float, s.split())
# #   print (clf.predict(data))  
