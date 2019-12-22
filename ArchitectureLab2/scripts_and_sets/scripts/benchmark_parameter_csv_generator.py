import os
l1i_size = ['8000','16000','32000','64000'] #L1 instcution cache size
l1i_assoc = ['1','2','4','8','16'] #L1 instcution cache associativity
l1d_size = ['8000','16000','32000','64000'] # L1 data cache size
l1d_assoc = ['1','2','4','8','16'] #L1 data cache associativity
l2_size = ['128000', '256000', '512000', '1000000','2000000'] #L2 cache size
l2_assoc = ['1','2','4','8','16'] #L2 cache associativity
cacheline_size = ['128','64','32'] #cache line size
directory_number = 0
i = 0
with open('results.txt','r') as f:
	lines = f.readlines()
	for l1i_s in l1i_size:
	    for l1i_a in l1i_assoc:
		for l1d_s in l1d_size:
		    for l1d_a in l1d_assoc:
		        for l2_s in l2_size:
		            for l2_a in l2_assoc:
		                for cachesize in cacheline_size:
				    csv_line = '%s,%s,%s,%s,%s,%s,%s,%s\n' % (lines[i].split('\t')[1],l1i_s,l1i_a,l1d_s,l1d_a,l2_s,l2_a,cachesize)
				    with open('parameters.csv','a+') as f1:
					f1.write(csv_line)
				    i += 1
				    if (i>3204):
					exit()


