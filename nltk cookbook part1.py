
# coding: utf-8

# In[1]:

1 + 5 * 2 - 3


# In[2]:

1 +


# In[3]:

import nltk


# In[4]:

nltk.download()


# In[5]:

from nltk.book import *


# In[7]:

text1


# In[8]:

text2


# In[9]:

text1.concordance("monstrous")


# In[10]:

text1.similar("monstrous")


# In[11]:

text2.similar("monstrous")


# In[12]:

text2.common_contexts(["monstrous","very"])


# In[13]:

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])


# In[14]:

len(text3)


# In[15]:

sorted(set(text3))


# In[16]:

len(set(text3))


# In[17]:

len(set(text3)) / len(text3)


# In[18]:

text3.count("smote")


# In[19]:

100 * text4.count('a') / len(text4)


# In[20]:

def lexical_diversity(text):
    return len(set(text)) / len(text)


# In[21]:

def percentage(count,total):
    return 100 * count / total


# In[22]:

lexical_diversity(text3)


# In[23]:

lexical_diversity(text5)


# In[24]:

percentage(4, 5)


# In[25]:

percentage(text4.count('a'), len(text4))


# In[26]:

#2   A Closer Look at Python: Texts as Lists of Words

#2.1   Lists

sent1 = ['Call', 'me', 'Ishmael', '.']


# In[27]:

sent1


# In[28]:

len(sent1)


# In[29]:

lexical_diversity(sent1)


# In[30]:

sent2


# In[31]:

sent3


# In[32]:

['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail']


# In[33]:

sent4 + sent1


# In[34]:

sent1.append("Some")
sent1


# In[35]:

#2.2   Indexing Lists

text4[173]


# In[36]:

text4.index('awaken')


# In[37]:

text5[16715:16735]


# In[38]:

text6[1600:1625]


# In[39]:

sent = ['word1', 'word2', 'word3', 'word4', 'word5',
        'word6', 'word7', 'word8', 'word9', 'word10']


# In[40]:

sent[0]


# In[41]:

sent[9]


# In[42]:

sent[10]


# In[43]:

sent[5:8]


# In[44]:

sent[5]


# In[45]:

sent[6]


# In[46]:

sent[7]


# In[47]:

sent[:3]


# In[48]:

text2[141525:]


# In[49]:

sent[0]='First'
sent[9] = 'Last'


# In[50]:

len(sent)


# In[51]:

sent[1:9] = ['Second', 'Third']


# In[52]:

sent


# In[53]:

sent[9]


# In[54]:

len(sent)


# In[55]:

#2.3   Variables

sent1 = ['Call', 'me', 'Ishmael', '.']


# In[56]:

my_sent = ['Bravely', 'bold', 'Sir', 'Robin', ',', 'rode',
 'forth', 'from', 'Camelot', '.']


# In[57]:

noun_phrase = my_sent[1:4]
noun_phrase


# In[58]:

wOrDs = sorted(noun_phrase)
wOrDs


# In[59]:

not = 'Camelot'


# In[60]:

vocab = set(text1)
vocab_size = len(vocab)
vocab_size


# In[61]:

#2.4   Strings

name = 'Monty'
name[0]


# In[62]:

name[:4]


# In[63]:

name * 2


# In[64]:

name+'!'


# In[65]:

' '.join(['Monty', 'Python'])


# In[66]:

'Monty Python'.split()


# In[67]:

#3   Computing with Language: Simple Statistics

saying = ['After', 'all', 'is', 'said', 'and', 'done',
           'more', 'is', 'said', 'than', 'done']


# In[68]:

tokens = set(saying)


# In[69]:

tokens = sorted(tokens)


# In[70]:

tokens[-2:]


# In[72]:

#3.1   Frequency Distributions

fdist1 = FreqDist(text1)
print(fdist1)


# In[73]:

fdist1.most_common(50)


# In[74]:

fdist1['whale']


# In[75]:

#3.2   Fine-grained Selection of Words

V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)


# In[76]:

fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)


# In[77]:

#3.3   Collocations and Bigrams

list(bigrams(['more', 'is', 'said', 'than', 'done']))
#?????


# In[78]:

text4.collocations()


# In[79]:

text8.collocations()


# In[80]:

#3.4   Counting Other Things

[len(w) for w in text1]


# In[82]:

fdist = FreqDist(len(w) for w in text1) 
print(fdist)


# In[83]:

fdist


# In[84]:

fdist.most_common()


# In[85]:

fdist.max()


# In[86]:

fdist[3]


# In[87]:

fdist.freq(3)
#????


# In[89]:

#4   Back to Python: Making Decisions and Taking Control

#4.1   Conditionals
sent7


# In[90]:

[w for w in sent7 if len(w) < 4]


# In[91]:

[w for w in sent7 if len(w) <= 4]


# In[92]:

[w for w in sent7 if len(w) == 4]


# In[93]:

[w for w in sent7 if len(w) != 4]


# In[94]:

sorted(w for w in set(text1) if w.endswith('ableness'))


# In[95]:

sorted(term for term in set(text4) if 'gnt' in term)


# In[96]:

sorted(item for item in set(text6) if item.istitle())


# In[97]:

sorted(item for item in set(sent7) if item.isdigit())


# In[ ]:



