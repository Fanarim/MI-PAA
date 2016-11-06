# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal svg size 400,300 enhanced fname 'arial'  fsize 10 butt solid
set output 'out.svg'
set datafile separator "|"

# Key means label...
set key inside top left
set xlabel 'Number of items'
set ylabel 'Execution time [s]'
set title 'Average execution time'
plot  "data.txt" using 1:2 title 'Bruteforce' with lines, "data.txt" using 1:3 title 'Branch and Bounds' with lines, "data.txt" using 1:4 title 'Dynamic' with lines, "data.txt" using 1:5 title 'FPTAS (eps=0.1)' with lines



n/time[s] | bruteforce | branch&bound | dynamic    | FPTAS=0.1
     4    | 0.00005854 |  0.00005436  | 0.00111556 | 0.00042206
     10   | 0.00103532 |  0.00018346  | 0.00668096 | 0.00471038
     15   | 0.03728424 |  0.00094774  | 0.03752692 | 0.02826282
     20   | 1.158171   |  0.02660638  | 0.13431106 | 0.11697322
     22   | 4.60866762 |  0.1089643   | 0.1932481  | 0.18902064
     25   |     NaN    |  0.81157176  | 0.36002596 | 0.36664684
     27   |     NaN    |  3.08290996  | 0.4794965  | 0.52861026
     30   |     NaN    |      NaN     | 0.78171244 | 0.89571224
     32   |     NaN    |      NaN     | 0.9066391  | 1.12906768
     35   |     NaN    |      NaN     | 1.3737256  | 1.85080732
     37   |     NaN    |      NaN     | 1.71947062 | 2.42695326
     40   |     NaN    |      NaN     | 2.4233144  | 3.64695372
