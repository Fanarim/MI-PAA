# Scale font and line width (dpi) by changing the size! It will always display stretched.
set terminal svg size 400,300 enhanced fname 'arial'  fsize 10 butt solid
set output 'out.svg'

# Key means label...
set key inside top right
set xlabel 'Number of items'
set ylabel 'Max error [%/100]'
set title 'Maximal error'
plot  "data.txt" using 1:2 title 'e=0.6' with lines, "data.txt" using 1:3 title 'e=0.2' with lines, "data.txt" using 1:4 title 'e=0.05' with lines


n/eps	0.6	0.2	0.05
4	0.099567	0.016304	0
10	0.013761	0.010810	0.000837
15	0.005387	0.001834	0
20	0.003426	0	0
22	0.003842	0.000390	0
25	0.003427	0.000369	0
27	0.001426	0.000395	0
30	0.001686	0.000276	0
32	0.001305	0.000519	0
35	0.001092	0	0
37	0.000831	0.000284	0
40	0.000712	0.000221	0
