
# coding: utf-8

# In[5]:


def ngram(sequence, n):
    '''
    sequence:array
    n :int
    '''
    i = 0
    ngram_list = []
    while i+n <= len(sequence):
        ngram_list.append(sequence[i:i+n])
        i=i+1
    return ngram_list

