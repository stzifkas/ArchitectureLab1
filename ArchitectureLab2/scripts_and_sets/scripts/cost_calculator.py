import os

l1i_size = ['8000','16000','32000','64000'] #L1 instcution cache size
l1i_assoc = ['1','2','4','8','16'] #L1 instcution cache associativity
l1d_size = ['8000','16000','32000','64000'] # L1 data cache size
l1d_assoc = ['1','2','4','8','16'] #L1 data cache associativity
l2_size = ['128000', '256000', '512000', '1000000','2000000'] #L2 cache size
l2_assoc = ['1','2','4','8','16'] #L2 cache associativity
cacheline_size = ['128','64','32'] #cache line size
directory_number = 0
cost = []
with open('cost.txt','a+') as f:
	for l1i_s in l1i_size:
	    for l1i_a in l1i_assoc:
		for l1d_s in l1d_size:
		    for l1d_a in l1d_assoc:
		        for l2_s in l2_size:
		            for l2_a in l2_assoc:
		                for cachesize in cacheline_size:
				    c = (int(l2_a) + int(l1i_a) + int(l1d_a))*(10*float(l2_s) + 50*float(l1i_s) + 50*float(l1d_s) ) + float(cachesize)
				    cost.append(c)
			            f.write('%s\n' % str(c))		
		                    filename = 'speclibm_{}'.format(directory_number)
		                    print(filename)
				    print(cost[directory_number])
				    directory_number += 1

