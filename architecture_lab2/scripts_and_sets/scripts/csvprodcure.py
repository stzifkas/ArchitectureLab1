cost_line_number = 0
with open('cost-time.csv','a+') as f:
	with open('cost.txt','r') as f2:
		lines = f2.readlines()
		with open('results.txt','r') as f3:
			for line in f3:
				time = line.split('\t')[2]
				cost = lines[cost_line_number]
				f.write('%s,%s'%(time,cost))
				cost_line_number += 1	
