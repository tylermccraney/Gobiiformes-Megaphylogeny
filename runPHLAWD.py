#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import glob
import re
import os

# Tyler McCraney
# February 25, 2015

# This program automates PHLAWD to analyze multiple genes

# Create list of configfiles
configfiles = glob.glob("*.configfile")

# Print message and run PHLAWD
print(str(len(configfiles)) + " genes will be analyzed by PHLAWD")    
for configfile in configfiles:
    os.system("PHLAWD assemble " + configfile)
    gene_name = configfile.replace(".configfile", "")
    print(gene_name + " sequences aligned")
    
# Print message that everything is finished
print("Finished " + str(len(configfiles)) + " PHLAWDs!")
