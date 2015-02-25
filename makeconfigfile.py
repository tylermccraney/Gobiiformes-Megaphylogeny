#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import glob
import re

# Tyler McCraney
# February 24, 2015

# This program makes configuration files for PHLAWD

# Create list of knownfiles
knownfiles = glob.glob("*.keep")

# Print message about which genes will be used
print("Made PHLAWD configuration files for the following " + str(len(knownfiles)) + " genes:")
for knownfile in knownfiles:
    gene_name = knownfile.replace(".keep", "")
    print(gene_name)

# Write configuration files    
for knownfile in knownfiles:
    gene_name = knownfile.replace(".keep", "")
    configfile = open(gene_name + ".configfile", "w")
    configfile.write( \
        "clade = Gobiaria" + "\n" 
        "search = " + gene_name + "\n"
        "gene = " + gene_name + "\n"
        "mad =  0.01" + "\n"
        "coverage = 0.2" + "\n"
        "identity = 0.2" + "\n"
        "db = /home/analysis/PHLAWD/vrt.db" + "\n"
        "knownfile = " + knownfile + "\n"
        "numthreads = 4" + "\n"
        "excludelistfile = exclude" + "\n")
    configfile.close()

    


