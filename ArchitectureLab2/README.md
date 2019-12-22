
# Εργαστήριο 2
 *Τζίφκας Σωκράτης (7026) , Μακρή Ελένη (8087)*

 ### Βήμα 1ο

 #### α) Παράμετροι επεξεργαστή και υποσυστήματος μνήμης

  Σε όλες τις προσομοιώσεις οι παράμετροι που μας ενδιαφέρουν ήταν:

*  L1 instruction cache size: 32768 bytes
*  L1 data cache size: 65536 bytes
* L2 cache size: 2097152 bytes
* L1 instruction cache associativity: 2
* L1 data cache associativity: 2
* L2 associativity: 8

#### β) Simulation Results

| Benchmarks |	sim_seconds |	system.cpu.cpi |	system.cpu.dcache.overall_miss_rate::total |	system.cpu.icache.overall_miss_rate::total |	system.l2.overall_miss_rate::total |
| --- | --- | --- | --- | --- | --- |
spechmmer |	0.059368	| 1.187362	| 0.001645 | 	0.000205	| 0.082246 |
speclibm	| 0.174681 |	3.493611	| 0.060971 |	0.000099	| 0.999927 |
specmcf |	0.055477	| 1.109538	| 0.002051	| 0.000037	| 0.724040 |
specsjeng | 	0.513541 |	10.270810 |	0.121829 |	0.000020	| 0.999979 |
specbzip |	0.084159	| 1.683172 |	0.014840 | 	0.000074	| 0.281708 |


#### γ) Προσομοίωση στα 1GHz

Οι παράμετροι που χρονίζονται στα 1GHz:

```
system.clk_domain.clock                          1000                       # Clock period in ticks

system.cpu_clk_domain.clock                      1000                       # Clock period in ticks
```

Κατά κανόνα, όσο μεγαλύτερη η συχνότητα ρολογιού και η τάση, τόσο μικρότερο είναι το CPI. Παρ' όλα αυτά, όσο μεγαλύτερη η συχνότητα ρολογιού, τόσο μεγαλύτερη και η κατανάλωση ενέργειας. Συνεπώς, δεν μπορεί να υπάρξει βέλτίστο scaling υπό την έννοια πως υπάρχει trade-off.


```
system.mem_ctrls.rank1.averagePower   505.014591 # Core power per rank (mW)
system.mem_ctrls.rank0.averagePower 505.121577  # Core power per rank (mW)

```

### Βήμα 2ο

#### Βελτιστοποίηση Απόδοσης

Για την αναζήτηση των παραμέτρων που θα βελτιστοποιήσουν την απόδοση χρησιμοποιήσαμε το `scripts/simulator.py` . Οι πιθανές τιμές των ζητούμενων παραμέτρων ορίζονται σε lists

Για τις προσομοιώσεις μας χρησιμοποιήσαμε τα:
```
l1i_size = ['8kB','16kB','32kB','64kB'] #L1 instcution cache size
l1i_assoc = ['1','2','4','8','16'] #L1 instcution cache associativity
l1d_size = ['8kB','16kB','32kB','64kB'] # L1 data cache size
l1d_assoc = ['1','2','4','8','16'] #L1 data cache associativity
l2_size = ['128kB', '256kB', '512kB', '1MB','2MB'] #L2 cache size
l2_assoc = ['1','2','4','8','16'] #L2 cache associativity
cacheline_size = ['128','64','32'] #cache line size
```

Το αρχείο `scripts/findmincpi.py` εκτυπώνει τον βέλτιστο συνδυασμό παραμέτρων . Στην περίπτωσή το αποτέλεσμα ήταν

```
min cpi: 1.969293
l1d_size 8kB
l1i_size 8kB
l2_size 256kB
l1i_assoc 1
l1d_assoc 4
l2_assoc 16
cache_line_size 32
```

#### Επίδραση παραμέτρων

Για να μελετήσουμε την επίδραση κάθε παραμέτρου στο CPI δημιουργούμε ένα CSV αρχείο της μορφής:

```
CPI, l1i_size, l1d_size, l2size, l1i_assoc, l1d_assoc, l2_assoc
```

Με βάση αυτό, μπορούμε να διατηρήσουμε σταθερές τις τιμές των υπολοίπων παραμέτρων, σε τυχαία τιμή -κάθε φορά- και να παρατηρήσουμε την στατιστική επίδραση της μεταβαλώμενης παραμέτρου στο CPI.




#### Συνάρτηση Κόστους

Η συνάρτηση κόστους που υλοποιήσαμε για είναι η παρακάτω (σε Python).
```
c = (int(l2_a) + int(l1i_a) + int(l1d_a))*(10*float(l2_s) + 50*float(l1i_s) + 50*float(l1d_s) ) + float(cachesize)
```

Ουσιαστικά, το κόστος, για κάθε συνδυασμό προκείπτει ως το γινόμενο της αθροιστικής περιπλοκότητας, επί το άθροισμα του κόστους/μέγεθος της κάθε μνήμης cache (θεωρήσαμε ότι οι l1 έχουν 5πλάσιο κόστος από τις l2). Στο τελικό κόστος προσθέτουμε και το μέγεθος του cache line.


```
Cost = (instruction_assoc + data_assoc +
   l2_assoc)*(10*l2_size + 50*(instruction_size
     + data_size)) + cache_line_size
```

Το script `scripts/cost_csv_producer.py` δημιουργεί ένα csv αρχείο που αντιστοιχεί στο CPI το αντίστοιχο κόστος του συνδυασμού των παραμέτρων.

##### Γράφημα Κέρδους (cpi) - Κόστους (με βάση τη συνάρτηση)
<img src="cpi_cost.png">

Παρατηρούμε ότι υπάρχουν σημεία στα οποία το CPI ελαχιστοποιείται για μικρό κόστος.

## Βιβλιογραφία

##### Bιβλια
* ΑΡΧΙΤΕΚΤΟΝΙΚΗ ΥΠΟΛΟΓΙΣΤΩΝ
HENNESSY L. JOHN, PATTERSON A. DAVID

##### Φυλλαδιο εργασιας 2
* https://www.spec.org/cpu2006/

##### Ηλεκτρονικες Πηγές
* http://gem5.org/
* https://www.watelectronics.com/arm-processor-architecture-working/
* https://extremetech.com/extreme/188776-how-l1-and-l2-cpu-caches-work-and-why-theyre-an-essential-part-of-modern-chips
* https://www.economics.utoronto.ca/osborne/2x3/tutorial/COST2IN.HTM
* https://en.wikipedia.org/wiki/Benchmark_(computing)
* https://www.kernel.org/doc/html/v4.15/admin-guide/pm/cpufreq.html
