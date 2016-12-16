
# coding: utf-8

# In[30]:

# This program paints histograms
# It needs as input two files 
# file1 : DSK output of fsY reads 
# file2 : DSK output of trusted single copy genes 


# In[31]:

from __future__ import division
from collections import defaultdict


# In[32]:

def reverse_complement(seq):
    seq_dict = {'A':'T','T':'A','G':'C','C':'G','N':'N'}
    return "".join([seq_dict[base] for base in reversed(seq)])


# In[33]:

# function that kmerizes an input_string and returns a list of kmers
def kmerize (ip_string, kmer_size) :
    return [ip_string[i:i+kmer_size] for i in range(0, len(ip_string)-kmer_size+1, 1)]


# In[34]:

# function that settifies a large file with kmers and count
# file looks like : ATGCT 101
# the set created is NOT twice as large as DSK kmer set
# it does NOT have both forward and revcomp kmers

def make_set_from_kmer_abundance (ip_file, kmer_size) :
    with open(ip_file,'r') as file_handle1 :
        list1 = [line[:kmer_size] for line in file_handle1]
    #with open(ip_file,'r') as file_handle2 :
    #    list2 = [reverse_complement(line[:kmer_size]) for line in file_handle2]   
    #list1.extend(list2)
    return set (list1)

def test_make_set () :    
    ip_file = 'test/trusted_DSK'
    single_copy_assembled_kmers = make_set_from_kmer_abundance(ip_file, 25)
    print single_copy_assembled_kmers


# In[35]:

def make_dict_from_kmer_abundance (ip_file, kmer_size) : 
    kmer_dicts = defaultdict(int)
    with open(ip_file,'r') as file_handle1 :
        for line in file_handle1 :
            current_abundance = int(line.split(' ')[1])
            kmer_dicts[line[:kmer_size]] = current_abundance
            kmer_dicts[reverse_complement(line[:kmer_size])] = current_abundance
    return kmer_dicts
            
def test_make_dict () :    
    ip_file = 'test/fsY_DSK'
    single_copy_assembled_kmers = make_dict_from_kmer_abundance(ip_file, 5)
    print single_copy_assembled_kmers
            

#test_make_dict()


# In[46]:

def main () :
    trusted_kmers = "data/single_copy_gene_kmers"
    fsY_kmers = "data/fsY_kmers"
    kmer_size = 25
    
    print "Started Painter"
    
    trusted_kmers_set = make_set_from_kmer_abundance(trusted_kmers, kmer_size)
    #print trusted_kmers_set
    fsY_kmers_dict = make_dict_from_kmer_abundance(fsY_kmers, kmer_size)
    
    print "Created trusted set and fsY dict"
    print "Now going to find coverage by looking at mean abundance of trusted kmers"
    
    trusted_dict_from_fsY_dict = defaultdict(int)
    for trusted in trusted_kmers_set :
        trusted_dict_from_fsY_dict[trusted] = fsY_kmers_dict[trusted]
    
    print "Found abundances for all trusted kmers"
    
    #for k,v in trusted_dict_from_fsY_dict.iteritems() :
    #    print k,v 
    
    count = 0
    total_abundance = 0
    for k,v in trusted_dict_from_fsY_dict.iteritems() :
        count+=1 
        total_abundance+=v
    print "Average = ", total_abundance/count 
    
    #with open("trusted_DSK_counts_acc_to_fsY","w") as output_handle :
    #    for k,v in trusted_dict_from_fsY_dict.iteritems() :
    #        to_write = str(k)+' '+str(v)+'\n'
    #        output_handle.write(to_write)
    

if __name__ == "__main__": main()


# In[47]:


