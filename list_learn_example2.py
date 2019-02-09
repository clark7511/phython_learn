#!/usr/bin/env python
# coding: utf-8

# In[1]:


TIOBE_list=['Java','C','C++','C#','Python','Objective-C']


# In[2]:


TIOBE_list[-1]='Swift'


# In[3]:


TIOBE_list


# In[4]:


top3_list=TIOBE_list[0:3]


# In[5]:


top3_list


# In[6]:


inverse_list=TIOBE_list[::-1]


# In[7]:


inverse_list


# In[8]:


TIOBE_list.append('php')


# In[9]:


TIOBE_list


# In[10]:


other_language=['javascript','T-SQL']


# In[11]:


TIOBE_list.extend(other_language)


# In[12]:


TIOBE_list


# In[13]:


other_language_2=['ruby','perl']


# In[14]:


TIOBE_list+=other_language_2


# In[15]:


TIOBE_list


# In[16]:


TIOBE_list.insert(1,'lisp')


# In[17]:


TIOBE_list


# In[18]:


TIOBE_list.insert(88,'Go')


# In[19]:


TIOBE_list


# In[20]:


TIOBE_list.remove('php')


# In[21]:


TIOBE_list


# In[22]:


catch_pop=TIOBE_list.pop()


# In[23]:


TIOBE_list


# In[24]:


catch_pop


# In[25]:


catch_pop2=TIOBE_list.pop(2)


# In[27]:


catch_pop2


# In[28]:


TIOBE_list


# In[29]:


position_of_Python=TIOBE_list.index('Python')+1


# In[30]:


print('position of Python',position_of_Python)


# In[31]:


'Go' in TIOBE_list


# In[32]:


'lisp' in TIOBE_list


# In[33]:


TIOBE_str=', '.join(TIOBE_list) 


# In[34]:


TIOBE_str


# In[37]:


TIOBE_str2=' / '.join(TIOBE_list) 


# In[38]:


TIOBE_str2


# In[39]:


language=['C#','Java','SQL']


# In[40]:


separator='*'


# In[41]:


joined=separator.join(language) 


# In[42]:


joined


# In[43]:


separated=joined.split('*')


# In[44]:


separated


# In[45]:


sorted_T_list=sorted(TIOBE_list)


# In[46]:


TIOBE_list


# In[47]:


sorted_T_list


# In[48]:


TIOBE_list.sort()


# In[49]:


TIOBE_list


# In[50]:


R_S_list=TIOBE_list.sort(reverse=True)


# In[52]:


R_S_list #不會回傳值


# In[53]:


TIOBE_list


# In[54]:


sorted_list_2=sorted(TIOBE_list)


# In[55]:


sorted_list_2


# In[56]:


list99=['aaa','bbbbb','dd','a']


# In[57]:


list99.sort(key=len,reverse=True)


# In[58]:


list99


# In[66]:


a=[1,2,3]


# In[67]:


a


# In[68]:


b=a.copy()


# In[69]:


b


# In[70]:


b[1]=999


# In[71]:


a


# In[72]:


b


# In[ ]:




