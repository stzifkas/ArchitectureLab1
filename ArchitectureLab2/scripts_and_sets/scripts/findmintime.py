l1i_size = ['8kB','16kB','32kB','64kB'] #L1 instcution cache size
l1i_assoc = ['1','2','4','8','16'] #L1 instcution cache associativity
l1d_size = ['8kB','16kB','32kB','64kB'] # L1 data cache size
l1d_assoc = ['1','2','4','8','16'] #L1 data cache associativity
l2_size = ['128kB', '256kB', '512kB', '1MB','2MB'] #L2 cache size
l2_assoc = ['1','2','4','8','16'] #L2 cache associativity
cacheline_size = ['128','64','32'] #cache line size
directory_number = 0


min = 10000
min_filename = ''
with open('results.txt') as f:
	for line in f:
		filename = line.split('\t')[0]
		time = line.split('\t')[1]
		if time == 'NaN' or time == 'sim_seconds':
			time = '1000'
		time = float(time)
		if time < min:
			min = time
			min_filename = filename
print(min_filename)
print(min)	

for l1i_s in l1i_size:
    for l1i_a in l1i_assoc:
        for l1d_s in l1d_size:
            for l1d_a in l1d_assoc:
                for l2_s in l2_size:
                    for l2_a in l2_assoc:
                        for cachesize in cacheline_size:
                            filename = 'speclibm_{}'.format(directory_number)
                            directory_number += 1
			    if filename == min_filename:
			    	result = 'l1d_size {} , l1i_size {} , l2_size {} , l1i_assoc {} , l1d_assoc {} , l2_assoc {} , cache_line_size {}'.format(l1d_s,l1i_s,l2_s,l1i_a,l1d_a,l2_a,cachesize)
                            	print(result)
				exit()
