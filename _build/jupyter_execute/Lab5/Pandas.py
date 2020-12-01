#!/usr/bin/env python
# coding: utf-8

# # Pandas

# **CS1302 Introduction to Computer Programming**
# ___

# In this lab, we will analyze COVID19 data using a powerful package called [`pandas`](https://pandas.pydata.org/docs/user_guide/index.html).  
# The package name comes from *panel data* and *Python for data analysis*.

# ## Loading CSV Files with Pandas 

# [DATA.GOV.HK](https://data.gov.hk/en-data/dataset/hk-dh-chpsebcddr-novel-infectious-agent) provides an [API](https://data.gov.hk/en/help/api-spec#historicalAPI) to retrieve historical data on COVID-19 cases in Hong Kong.

# The following uses the `urlencode` function to create the url that links to a csv file containing probable and confirmed cases of COVID-19 by Aug 1st, 2020.

# In[ ]:


from urllib.parse import urlencode

url_data_gov_hk_get = 'https://api.data.gov.hk/v1/historical-archive/get-file'
url_covid_csv = 'http://www.chp.gov.hk/files/misc/enhanced_sur_covid_19_eng.csv'
time = '20200801-1204'
url_covid = url_data_gov_hk_get + '?' + urlencode({
    'url': url_covid_csv,
    'time': time
})

print(url_covid)


# `urlencode` creates a string `'url=<...>&time=<...>'` with some [special symbols encoded](https://www.w3schools.com/tags/ref_urlencode.ASP), e.g.:
# - `:` is replaced by `%3A`, and
# - `/` is replaced by `%2F`.

# **Exercise** Write a function `simple_encode` that takes in a string and return a string with `:` and `/` encoded as described above.  
# *Hint:* Use the `replace` method of `str`.

# In[ ]:


def simple_encode(string):
    '''Returns the string with : and / encoded to %3A and %2F respectively.'''
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert simple_encode(
    'http://www.chp.gov.hk/files/misc/enhanced_sur_covid_19_eng.csv'
) == 'http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Fenhanced_sur_covid_19_eng.csv'


# Like the function `open` that loads a file into memory, `pandas` has a function `read_csv` that loads a csv file.   
# The csv file can even reside on the web.

# In[ ]:


import pandas as pd
df_covid = pd.read_csv(url_covid)

print(type(df_covid))
df_covid


# The above creates a [`DataFrame` object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame). The content of the csv file is displayed as an HTML table conveniently.   
# (We can control how much information to show by setting the [display options](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html).)

# **Exercise** Using the function `pd.read_csv`, load `building_list_eng.csv` as `df_building` from the url `url_building`.  

# In[ ]:


url_building_csv = 'http://www.chp.gov.hk/files/misc/building_list_eng.csv'
time = '20200801-1203'
url_building = url_data_gov_hk_get + '?' + urlencode({
    'url': url_building_csv,
    'time': time
})

# YOUR CODE HERE
raise NotImplementedError()
df_building


# In[ ]:


# tests
assert all(df_building.columns == ['District', 'Building name', 'Last date of residence of the case(s)',
       'Related probable/confirmed cases'])  # check column names


# ## Selecting and Removing columns

# We can obtain the column labels of a `Dataframe` using its `columns` attribute.

# In[ ]:


df_covid.columns


# Using the indexing operator `[]`, a column of a `DataFrame` can be returned as a [`Series` object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html), which is essentially a named array.   
# We can further use the method `value_counts` to return the counts of different values in another `Series` object.

# In[ ]:


series_gender_counts = df_covid['Gender'].value_counts()  # return the number of male and female cases

print(type(series_gender_counts))
series_gender_counts


# **Exercise** For `df_building`, use the operator `[]` and method `value_counts` to assign `series_district_counts` to a `Series` object that stores the counts of buildings in different district.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()
series_district_counts


# In[ ]:


# tests
assert all(series_district_counts[['Wong Tai Sin', 'Kwun Tong']] == [313, 212])


# In `df_covid`, it appears that the column `Name of hospital admitted` contains no information. We can confirm this by:
# 1. Returning the column as a `Series` with `df_covid_cases['Name of hospital admitted']`, and
# 1. printing an array of unique column values using the method `unique`.

# In[ ]:


df_covid['Name of hospital admitted'].unique()


# **Exercise** Drop the column `Name of hospital admitted` using the `drop` method of the DataFrame. 
# 
# Use the keyword argument `inplace=True`, so that the method will 
# - mutate the original DataFrame in place instead of 
# - creating a copy of the DataFrame with the column dropped.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()
df_covid


# In[ ]:


# tests
assert all(df_covid.columns == ['Case no.', 'Report date', 'Date of onset', 'Gender', 'Age',
       'Hospitalised/Discharged/Deceased', 'HK/Non-HK resident',
       'Case classification*', 'Confirmed/probable'])


# ## Selecting Rows of DataFrame

# We can select the confirmed male cases using the attribute [`.loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) and the indexing operator `[]`.  
# `.loc` implements an advanced indexing method `__getitem__` that can take a boolean vector.

# In[ ]:


df_confirmed_male = df_covid.loc[(df_covid['Confirmed/probable']=='Confirmed') & (df_covid['Gender']=='M')]
df_confirmed_male


# **Exercise** Assign `df_confirmed_local` to a `DataFrame` of confirmed cases that are local or epidemiologically linked with a local case.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()

df_confirmed_local


# In[ ]:


# tests
assert set(df_confirmed_local['Case classification*'].unique()) == {
    'Epidemiologically linked with local case', 'Local case'
}


# ## Challenge

# **Exercise** Write a function `case_counts` that 
# - takes an argument `district`, and
# - returns the number of cases in `district`. 
# 
# *Hint:* Be careful that there can be more than one case for each building and there may be multiple buildings associated with one case.  
# You may want to use the `split` and `strip` methods of `str` to obtain a list of cases from the `Dataframe`.

# In[ ]:


def case_counts(district):
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert case_counts('Kwai Tsing') == 109

