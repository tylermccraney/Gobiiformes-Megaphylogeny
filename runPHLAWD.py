#!/usr/bin/python

from __future__ import division
from __future__ import print_function

import glob
import re
import os

# Tyler McCraney
# February 25, 2015

def PHLAWDrunner(): # This function automates PHLAWD to analyze multiple genes
    configfiles = glob.glob("*.configfile") # Create list of configfiles
    print(str(len(configfiles)) + " genes will be analyzed by PHLAWD") # Print message and run PHLAWD    
    for configfile in configfiles:
        os.system("PHLAWD assemble " + configfile)
        gene_name = configfile.replace(".configfile", "")
        print(gene_name + " sequences aligned")
    print("Finished " + str(len(configfiles)) + " PHLAWDs!") # Print message that everything is finished

PHLAWDrunner() # Call function
