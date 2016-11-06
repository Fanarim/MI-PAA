# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal svg size 400,300 enhanced fname 'arial'  fsize 10 butt solid
set output 'out.svg'

# Key means label...
set key inside top left
set xlabel 'Number of items'
set ylabel 'Execution time [s]'
set title 'Average execution time'
plot  "data.txt" using 1:2 title 'e=0.6' with lines, "data.txt" using 1:3 title 'e=0.2' with lines, "data.txt" using 1:4 title 'e=0.05' with lines

n/eps	0.6	0.2	0.05
4	0.000252	0.000468	0.000666
10	0.002257	0.003262	0.006318
15	0.010069	0.019773	0.046599
20	0.034394	0.074433	0.208158
22	0.050216	0.110930	0.339883
25	0.092035	0.220328	0.679378
27	0.130317	0.313222	0.965425
30	0.216223	0.514596	1.686521
32	0.265535	0.665607	2.185783
35	0.423465	1.012181	3.676685
37	0.541886	1.328059	4.762713
40	0.756932	1.964903	6.769749
