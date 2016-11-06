# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal svg size 400,300 enhanced fname 'arial'  fsize 10 butt solid
set output 'out.svg'

# Key means label...
set key inside top right
set xlabel 'Number of items'
set ylabel 'Average error [%/100]'
set title 'Average error'
plot  "data.txt" using 1:2 title 'e=0.6' with lines, "data.txt" using 1:3 title 'e=0.2' with lines, "data.txt" using 1:4 title 'e=0.05' with lines


n/eps	0.6	0.2	0.05
4	0.010307	0.000326	0
10	0.001031	0.000319	0.000033
15	0.000877	0.000178	0
20	0.000301	0	0
22	0.000191	0.000008	0
25	0.000221	0.000021	0
27	0.000137	0.000008	0
30	0.000234	0.000006	0
32	0.000107	0.000016	0
35	0.000093	0	0
37	0.000059	0.000006	0
40	0.000084	0.000009	0
