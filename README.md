# SCSN-Earthquake-Catalog-to-CSV
A collection of Python scripts to convert CalTech's SCSN .catalog files from ASCII to CSV. 
 
I'm by no means a programmer, so there is almost certainly a cleaner way to do all this.  But it worked for me, hopefully it'll work for you too.
___
## CatalogSingle.py
This script takes a SCSN .catalog file (usually a specific year) and brute-force converts it to a .csv with the same name.
* The argument is the filename without the file extension: "2000" will look for the file "2000.catalog" and will produce a file called "2000.csv"
______

## CatalogRange.py
This script takes a starting year and ending year as arguments and iterates through all the files within that range, inclusively.
* So "CatalogRange.py 1993 2003" will start with 1993.catalog, create a 1993.csv, move on to 1994, and continue until it has processed 2003.catalog and made a 2003.csv file.
____
## CatalogeConcatenate.py
This script will build a single .csv file ("concatenate.csv") from an inclusive range of dates, similar to CatalogRange.py