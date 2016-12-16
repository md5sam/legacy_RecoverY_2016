# RecoverY and kmerPaint

This is the implementation of the RecoverY and kmerPaint modules. 

### Usage  

    python paint_histo.py

    ./recoverY_main.sh    	
	
### Dependencies 

Biopython

    pip install biopython


### Input

Data for kmerPaint is in kmerPaint/data folder 


### Output 

The output for kmerPaint is :
*trusted_DSK_counts_acc_to_fsY

This file looks like :

>CTTTCTATTTTTGTAACAATATGAA 35
>TATATTTGAATATGTGAATTCATGC 45
>ATATTATTTCGAAGCAGTCAAAAAC 73

The first part of the line is the kmer, followed by kmer abundance 

### Notebook 

The ipynb notebook for this analysis is in ./notebook folder


### License
This program is released under the MIT License. Please see LICENSE.txt for details


### Citation
Please cite this github repo if you use this tool in your research. Thanks !
https://github.com/md5sam/
