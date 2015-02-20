#!/bin/bash

## Tyler McCraney
## February 20, 2015

## This shell script builds a GenBank database for PHLAWD.
## db.setup names the output file and intructs PHLAWD to only download vertebrate data  

# Initialize and load data into the database
PHLAWD setupdb db.setup