#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import glob
import re

# Tyler McCraney
# February 26, 2015

def mkconfigs(taxa): # This function makes configuration files for PHLAWD
    knownfiles = glob.glob("*.keep") # Create list of knownfiles
    print("Made PHLAWD configuration files for the following " + str(len(knownfiles)) + " genes:") # Print message about which genes will be used
    for knownfile in knownfiles:
        gene_name = knownfile.replace(".keep", "")
        print(gene_name)    
    for knownfile in knownfiles: # Write configuration files
        gene_name = knownfile.replace(".keep", "")
        configfile = open(gene_name + ".configfile", "w")
        configfile.write( \
            "clade = " + taxa + "\n" 
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
        
clade = "Gobiaria"
mkconfigs(clade) # Call function