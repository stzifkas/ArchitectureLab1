# Εργαστήριο 1
##### Μακρή Ελένη ( 8087 ) , Τζίφκας Σωκράτης ( 7026 )

## α) Αρχείο starter_se.py
 Το αρχείο starter_se.py είναι παραμετροποιήσιμο και κατά την εκτέλεσή του μπορούν να καθοριστούν η συχνότητα του
 επεξεργαστή, ο αριθμός των πυρήνων, το μέγεθος, ο τύπος και τα κανάλια της μνήμης. Οι προκαθορισμένες
 τιμές είναι: 
 * 4GHz (--cpu-freq)
 * 1 (--cpu-core)
 * DDR3_1600_8x8 (--mem-type)
 * 2 (--mem-channels)
 * 2GB (--mem-size)
 
 
 
 Επίσης, μπορούμε να αλλάξουμε τη συχνότητα και τη τάση του ρολογιού του επεξεργαστή (clk_domain, voltage_domain), 
 για τα οποία οι προκαθορισμένες τιμές είναι 1GHz και 3.3V, αντίστοιχα.
 
## β) Αρχεία config.ini και config.json
* Το μέγεθος μνήμης επαληθεύεται από το πεδίο "mem_ranges": ["0:2147483647"] που αντιστοιχεί στα 2GB 
* To cache line size από το πεδίο "cache_line_size": 64MB
* Η συχνότητα του ρολογιού εντοπίζεται στο πεδίο "clk_domain.clock" του system και αντιστοιχεί σε 1000 ticks per period

## γ) In-order CPU μοντέλα 
#### SimpleCPU
Η SimpleCPU είναι αμιγώς λειτουργική και κατάλληλη για περιπτώσεις στις οποίες ένα λεπτομερές μοντέλο δεν είναι απαραίτητο.
#### BaseSimpleCPU
H BaseSimpleCPU εξυπηρετεί διάφορους σκοπούς.
Διατηρεί την αρχική κατάσταση και τα δεδομένα που είναι κοινά σε όλα τα μοντέλα της SimpleCPU.
Ορίζει τις λειτουργίες που ελέγχουν τυχόν διακοπές, μεταφέρει εντολές στον επεξεργαστή, χειρίζεται λειτουργίες πριν και μετά την εκτέλεση εντολών.
Εφαρμόζει την ExecContext διεπιφάνεια.
Η BaseCPU δεν μπορεί να τεθεί σε λειτουργία μόνη της
#### AtomicSimpleCPU
Η AtomicSimpleCPU είναι η μορφή της SimpleCPU η οποία χρησιμοποιεί προσβάσεις ατομικής μνήμης. Χρησιμοποιεί τις εκτιμούμενες καθυστερήσεις μεταφοράς για να προβλέψει τον χρόνο προσβασης στη μνήμη cache. H AtomicSimpleCPU διαθέτει λειτουργίες για την ανάγνωση και εγγραφή μνήμης, ενώ επίσης ελέγχει τι συμβαίνει σε κάθε κύκλο CPU.
#### TimingSimpleCPU
Η TimingSimpleCPU είναι μια μορφή της SimpleCPU που χρησιμοποιεί προσβάσεις χρονικής μνήμης. Καθυστερεί την πρόσβαση στη μνήμη cache ούτως ώστε το σύστημα μνήμης να ανταποκριθεί πριν προχωρήσει μία ενέργεια. Όπως η AtomicSimpleCPU, έτσι και αυτή προέρχεται από την BaseSimpleCPU και έχει τις ίδιες λειτουργίες. Ορίζει την πύλη που συνδέεται με τη μνήμη και συνδέει τη CPU με την cache.
#### Minor
Πρόκειται για έναν pipelined επεξεργαστή 4 σταδίων (fetch1-fetch2-decode-execute). Η προσκόμιση της εντολής από την κύρια μνήμη πραγματοποιείται στο fetch1 στάδιο ενώ στο fetch2 αποκωδικοποιείται. Στο στάδιο execute εκτός από την εκτέλεση της εντολής πραγματοποιείται και η εγγραφή. 

## δ) Συγκριτική εκτέλεση C προγράμματος σε minor CPU και TimingSimpleCPU
Το `roots.c` υπολογίζει τις ρίζες μίας 2βάθμιας εξίσωσης. Για το compile χρησιμοποιούμε την παρακάτω εντολή:

`arm-linux-gnueabihf-gcc -o arm_program --static roots.c -lm`

| CPU    | sim_seconds  | sim_ticks | 
| ------ | ------------ | --------- |
|MinorCPU| 0.000040     | 40412000  |
|TimingSimpleCPU| 0.000045 | 44748000 | 


Η καθυστέρηση που εμφανίζεται στην περίπτωση του TimingSimpleCPU είναι αναμενόμενη δεδομένου ότι το συγκεκριμένο μοντέλο υλοποιεί ένα Timing Memory Access, που πρακτικά σημαίνει πως αναμένει μέχρι να επιστραφεί η πρόσβαση στην μνήμη. Κάθε αριθμητική εντολή εκτελείται σε ένα κύκλο ενώ η πρόσβαση στην μνήμη σε περισσότερους. Στον αντίποδα το Minor CPU υλοποιεί ένα pipeline όπως προαναφέρεται με αποτέλεσμα να προσομοιώνει ταχύτερο επεξεργαστή.