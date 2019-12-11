import os

l1i_size = ['8kB','16kB','32kB','64kB'] #L1 instcution cache size
l1i_assoc = ['1','2','4','8','16'] #L1 instcution cache associativity
l1d_size = ['8kB','16kB','32kB','64kB'] # L1 data cache size
l1d_assoc = ['1','2','4','8','16'] #L1 data cache associativity
l2_size = ['128kB', '256kB', '512kB', '1MB','2MB'] #L2 cache size
l2_assoc = ['1','2','4','8','16'] #L2 cache associativity
cacheline_size = ['128','64','32'] #cache line size
directory_number = 0

for l1i_s in l1i_size:
    for l1i_a in l1i_assoc:
        for l1d_s in l1d_size:
            for l1d_a in l1d_assoc:
                for l2_s in l2_size:
                    for l2_a in l2_assoc:
                        for cachesize in cacheline_size:
                            command = './build/ARM/gem5.opt -d spec_results/speclibm_{} configs/example/se.py --cpu-type=MinorCPU --caches --l2cache --l1d_size={} --l1i_size={} --l2_size={} --l1i_assoc={} --l1d_assoc={} --l2_assoc={} --cacheline_size={} --cpu-clock=1GHz -c spec_cpu2006/470.lbm/src/speclibm -o "20 spec_cpu2006/470.lbm/data/lbm.in 0 1 spec_cpu2006/470.lbm/data/100_100_130_cf_a.of" -I 1000000'.format(directory_number,l1d_s,l1i_s,l2_s,l1i_a,l1d_a,l2_a,cachesize)
                            directory_number += 1
                            print(command)
                            os.system(command)
