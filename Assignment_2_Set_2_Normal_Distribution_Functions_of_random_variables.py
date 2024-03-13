#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import statsmodels.api as smf
import warnings
warnings.filterwarnings('ignore')


# # SET 2  

# ### Question 1 

# In[4]:


"""the serving work will began after 10 min of drop off so 45+10 
which will now take more than the usual time so new mew is 55 minutes 
and the porbbaility that it will take more than 1 hour to complete"""
mew = 55
std = 8
q1 = stats.norm.sf(60, loc = mew, scale = std)
print("""The probability that the service manager cannot meet his 
      commitment is""",np.round(q1,5))


# ### Question 2 

# In[8]:


mean = 38
std1 = 6
q2_lessthan_38 = stats.norm.cdf(38, loc = mean, scale = std1)


q2_less_than_44 = stats.norm.cdf(44, loc = mean,  scale = std1)


q2_betweeen_38_and_44 = (q2_less_than_44 - q2_lessthan_38)
print('The probability of employee age betweeen 38 and 44 is',np.round(q2_betweeen_38_and_44*100,2),'%') 

q2_morethan_44 = 1-stats.norm.cdf(44, loc = mean, scale = std1)
print('The probability of employee age more than 44 is',np.round(q2_morethan_44*100,2),'%')

true_or_false = (q2_morethan_44 > q2_betweeen_38_and_44)
print('Answer:',true_or_false)

q2b = stats.norm.cdf(30, loc = mean, scale = std1)
print("""A training program for employees under the age of 30 at the center would be expected to attract about"""
      ,np.round((q2b*400),0),'employees')


# ### Question 4

# <b>Let X ~ N(100, 202). Find two values, a and b, symmetric 
#         about the mean, such that the probability of the random variable 
#         taking a value between them is 0.99.</b>
# + A.90.5, 105.9 
# + B.80.2, 119.8
# + C.22, 78 
# + D.48.5, 151.5
# + E.90.1, 109.9

# In[13]:


# Given
mew = 100
std = 20
# p(a<x<b)
#To Find = 
""" two values, a and b, symmetric about the mean, such that the 
probability of the random variable taking a value between them is 0.99""" 
# Solution
""" From the above details,we have to exclude .005% area from each
left and right tails. Hence, we want to find the .005th and the 
.995th percentiles Z score values"""

# Z value for .005 percentiles 
z_005_ = np.round(stats.norm.ppf(0.005),4)
z_005_

# Z value for .99 percentiles 
z_99_ = np.round(stats.norm.ppf(0.995),4)
z_99_

#z = (x_bar - mew) / std
#x_bar = (z*std) + mew
a = np.round((z_005_*std) + mew,1)
b = np.round((z_99_*std) + mew,1)
print("""The two values of a and b, symmetric about the mean, 
      are such that the probability of the random variable 
      taking a value between them is 0.99:""",a,b)


# # Or Simply

# In[12]:


print("""The two values of a and b, symmetric about the mean, 
      are such that the probability of the random variable 
      taking a value between them is 0.99:""",np.round(stats.norm.interval(0.99, loc = 100, scale = 20),1))


# ### Question 5 
# 
# 

# 5.Consider a company that has two different divisions. The annual profits from the two divisions are independent and have distributions Profit1 ~ N(5, 32) and Profit2 ~ N(7, 42) respectively. Both the profits are in USD Million. Answer the following questions about the total profit of the company in Rupees. Assume that 1USD = Rs. 45
# 
# 

# In[15]:


# Combine Mean Profit of both division for Company= mean1 + mean2
mean1 = 5
mean2 = 7
Mean = (mean1+mean2) # 1 USD = 45 rupees
print('The Mean Profit of both division:',Mean, 'Million$')
print('The Mean Profit of both division:',(Mean*45)/10, 'Crore Rupees')

# Combine standard Deviation = (Std1^2 + Std2^2)^1/2
std1 = 3**2
std2 = 4**2
Std = np.sqrt(std1 + std2)
print('The Standard Deviation of both division:', Std, 'Million$')
print('The Standard Deviation of both division:', (Std*45)/10, 'Crore Rupees')


#  A. Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
# 

# In[16]:


r1, r2 = np.round(stats.norm.interval(0.95, Mean, Std),2)
print('Rupee Ranges from',r1,'to',r2,'Million$ in Annual profit of the Company 95% of the time')
print('Rupee Ranges from',np.divide(np.multiply(r1,45),10),'to',np.divide(np.multiply(r2,45),10),'Crore Rupees in Annual profit of the Company 95% of the time')


# B.	Specify the 5th percentile of profit (in Rupees) for the company
# 

# In[18]:


# Z value  = X_bar - Mew / Std pop 
# for percentile, X_percentile = (Zvalue * Std pop) + Mew
Z_05_ = stats.norm.ppf(0.05)
Fifth_percentile = (Z_05_ * Std) + Mean
print('The 5th percentile of Profit for the company is',np.round(Fifth_percentile,2),'Million$')
print('The 5th percentile of Profit for the company is',np.round((Fifth_percentile*45)/10,),'Crore Rupees')


# C.	Which of the two divisions has a larger probability of making a loss in a given year?
# 
# 

# In[19]:


# The probability of Division #1 making a loss
print('The Probability of Division #1 making a loss is',np.round((stats.norm.cdf(0,5,3))*100,2),'%')

# The probability of Division #2 making a loss
print('The Probability of Division #2 making a loss is',np.round((stats.norm.cdf(0,7,4))*100,2),'%')

Division_1 = (stats.norm.cdf(0,5,3))*100
Division_2 = (stats.norm.cdf(0,7,4))*100

if Division_1>Division_2:
    print('The Division 1 has a larger Probability of making a loss')
else:
          print('The Division 2 has a larger Porbability of making a loss')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




