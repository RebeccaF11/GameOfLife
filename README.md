"# GameOfLife" by John Conway
=============================

There is a very clean working implementation and description on the page:

https://bitstorm.org/gameoflife/

As detailed on this page, given an initial state, you update each 'populated tile' based on following rules: 

For a space that is 'populated':

i) Each cell with one or no neighbors dies, as if by solitude.
ii) Each cell with four or more neighbors dies, as if by overpopulation.
iii) Each cell with two or three neighbors survives.
iv For a space that is 'empty' or 'unpopulated'. Each cell with three neighbors becomes populated.

Extenstion:
===========

What are the interesting initial stage, it would be an interest task to just randomly set the tiles within the space the store
all the "interesting" examples, where at first thought I would describe interesting as states which tend to some equilibrium
for a given period. 

