#!/usr/bin/env python
# coding: utf-8

# # PANDAS FUNCTIONALITIES HERE:
PANDAS:-> Panel data -> Tabular Structure....

Row Data :-> By Using Pandas -> Read The DataSet, data Cleaning....
    
    
                              DATA STRUCTURE IN PANDAS
                              ------------------------
                      There are Basically Two Types Of Data
            
            (1) Series : "A single Column of data is Called Series"
                
                
                
            (2) DataFrame : "Collection of multiple series is called dataFrame"
                   
# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[49]:


#How To Create Series
import pandas as pd
S = [10,20,30,40,50]
S1 = pd.Series(S)
print(S1)
print()
print(type(S1))


# In[54]:


#How To Create DataFrame
#import pandas as pd
D = {"Date":["12/12/2022","10/08/2023","06/08/2024"],
    "Temp":[35.6,40.2,44.1],
    "Humidity":[20,38,27]}

df = pd.DataFrame(D)
df


# # Mini_Project On Video_Games:

# In[ ]:


Reading Files 


# In[1]:


import pandas as pd


# In[2]:


video_games = pd.read_csv("C:/Users/Ranje/OneDrive/Desktop/PYTHON_CS/video_games_sales.csv")


# In[3]:


video_games


# In[4]:


video_games.sample


# In[5]:


video_games.sample(3)


# In[6]:


#head() :It's returns a top 5 data of our dataset...
video_games.head()


# In[7]:


video_games.head(10)


# In[8]:


video_games.head(n=15)


# In[9]:


#tail() : It's returns a bottom 5 Data Of our datasets ....
video_games.tail()


# In[10]:


video_games.tail(10)


# In[11]:


video_games.tail(n=12)


# In[12]:


#Method-1
#Access the column name by using Column_Name...
video_games.Name


# In[13]:


#Method-2
#Access the column name by using Column_Name...
video_games['Name']


# In[14]:


video_games['Platform']


# In[ ]:





# # DAY-25

# In[ ]:





# # Reading Files loc/iloc:
There are two ways to access data in pandas:-
    
1) loc :- Allow you to access row & column by using their name.
                       OR
          Access a group of row & col by column name.
    
    Syn:
        loc(col name)
        

2) iloc :- Allow you to access row & column by using their index.
                              OR
           Access a group of row & column by it's index.
    
    syn:
        iloc(col index)
        iloc[row,col]
        iloc[0,]  -----> For single row.
        iloc[15:20]  -----> For range of record.
# In[15]:


video_games.iloc[4]  #it's represent the all data row number 'Four'


# In[16]:


video_games.iloc[0:4]            #it's represents b/w [0-4] data of row & col...


# In[17]:


video_games.iloc[25:50]


# In[18]:


# Access 'Name','Genre' & 'Developers' of all games using iloc
video_games.iloc[:,[0,3,14]]


# In[19]:


# Access 'Name','Genre' & 'Developers' of all games using iloc
video_games.iloc[:,[0,3,-2]]


# In[20]:


# Access 'EU_Sales','Global_Sales' & 'Critic_Count' for range 20 to 40 games by using iloc..
video_games.iloc[20:40,[6,9,11]]


# In[21]:


# Access 'Name','Genre' & 'Developers' of all games using loc
video_games.loc[:,['Name','Genre','Developer']]


# In[22]:


# Access a particular row using iloc..
video_games.iloc[[15,25,35]]                #it will give us row number 15,25,35 accordly...


# In[23]:


#3:8 --> Represent row & 5:12 --> Represenr Column
video_games.iloc[3:8,5:12]    # it will give us range of row & col..


# In[ ]:





# # DAY-26

# In[ ]:





# # Search/Filter Operation:

# In[24]:


# i want all racing games
video_games.Genre == 'Racing'


# In[25]:


racing_games = video_games.loc[video_games.Genre == 'Racing']


# In[26]:


racing_games


# In[27]:


racing_games = video_games.loc[video_games.Genre == 'Shooter']


# In[28]:


racing_games


# In[29]:


# i want Genre Only 'Shooter' & Publisher Only 'Activision' of all Data
racing_games = video_games.loc[(video_games.Genre == 'Shooter')&(video_games.Publisher == 'Activision')]


# In[30]:


racing_games


# In[31]:


#i want all racing games witch have Critic_Score >= 95
racing_games = video_games.loc[video_games.Critic_Score >= 95]


# In[32]:


racing_games


# In[33]:


#i want all 'Racing' or 'Action' Games with Critic_Score >=9
racing_games = video_games.loc[((video_games.Genre == 'Racing')|(video_games.Genre == 'Action'))&(video_games.Critic_Score >=95)]


# In[34]:


racing_games


# In[35]:


# i need all 'Racing','Action' & 'Sports' games with Critic_Score >=9
gaming_action = video_games.loc[(video_games.Genre.isin(['Racing','Action','Sports']))&(video_games.Critic_Score>=95)]


# In[36]:


gaming_action


# In[37]:


# i need all 'Racing','Action' & 'Sports' games with Publisher 'Nintendo'
gaming_action = video_games.loc[(video_games.Genre.isin(['Racing','Action','Sports']))&(video_games.Publisher == 'Nintendo')]


# In[38]:


gaming_action


# In[39]:


gaming_action = video_games.loc[(video_games.Genre.isin((['Racing','Action','Sports']))|(video_games.Publisher == 'Nintendo'))&(video_games.User_Score>=95)]


# In[40]:


gaming_action


# In[ ]:





# # DAY-27

# In[ ]:





# # Handlinh Missing Values:

# In[41]:


#i want all video_games whole User_Score>9
good_games = video_games.loc[(video_games.User_Score>9)]


# In[42]:


video_games.User_Score


# In[43]:


video_games.dtypes

astype():

-> To change the datatype of each column.
-> It's all about type casting.

  syn:
        astype(Col_Name:DataType)
# In[44]:


video_games.astype({"User_Score":Float})


# In[45]:


video_games['User_Score'].unique()


# In[46]:


video_games['User_Score'] = video_games['User_Score'].replace('tbd',0.0)


# In[47]:


video_games['User_Score'].unique()


# In[48]:


video_games = video_games.astype({'User_Score':float})


# In[49]:


video_games['User_Score'].unique()


# In[50]:


video_games.dtypes


# In[51]:


good_games = video_games.loc[(video_games.User_Score>9)]


# In[52]:


good_games


# In[53]:


good_games.head()


# In[54]:


good_games = good_games.reset_index()


# In[55]:


good_games


# In[ ]:





# # DAY-28

# In[ ]:





# In[56]:


good_games.drop('index',axis=1,inplace=True)


# In[57]:


good_games.head(10)

contains():
    It is a case sensitive
# In[58]:


mario_games = video_games.loc[(video_games.Name.str.contains('mario',case=False,na=False))]


# In[59]:


mario_games


# In[60]:


mario_games = video_games.loc[(video_games.Name.notnull())&(video_games.Name.str.contains('mario',case=False))]


# In[61]:


mario_games


# In[62]:


print(video_games.shape)

dropna(): It is remove only missing value like na,NAN....
# In[63]:


video_games_User_Score = video_games.dropna(subset=['User_Score'])


# In[64]:


print(video_games_User_Score)


# In[65]:


print(video_games_User_Score.shape)


# In[ ]:





# # DAY-29

# In[ ]:





# # Transformation Function:
Basically There are two kind s of Functions described in below :-
    
    1) map():It is used for small changes[Like One lines of code]...
    2) apply():It is used for largers/Big changes[Like more than one code]...
# In[67]:


add = lambda x:x+5
add(20)


# In[70]:


mul = lambda a:a*3
mul(3)


# In[71]:


mul = lambda a:a-3
mul(3)


# In[72]:


video_games.head()


# In[ ]:





# In[73]:


#we increased values of specified column using lambda function...
video_games.NA_Sales = video_games.NA_Sales.map(lambda x:x+5)


# In[74]:


video_games.NA_Sales


# In[75]:


video_games.head(2)


# In[81]:


#we increased values of specified column using lambda function...
video_games.EU_Sales = video_games.EU_Sales.map(lambda z:z-10)


# In[82]:


video_games.EU_Sales


# In[83]:


video_games.JP_Sales = video_games.JP_Sales.map(lambda l:l*2)
video_games.JP_Sales


# In[87]:


#NA_Sales & EU_Sales both must be reduced by 5

def sub5(row):
    row.NA_Sales -=5
    row.EU_Sales -=5
    return row
video_games = video_games.apply(sub5,axis=1)


# In[88]:


video_games.head()


# In[ ]:





# # DAY-30

# In[ ]:





# # GROUPING AND SORTING:

# In[90]:


#i want know which 'Genre' has how many games which Genre has most games....
video_games.groupby('Genre').Genre.count()


# In[91]:


#Which 'Developer' has most games sold..
dev_games_count = video_games.groupby('Developer').Name.count()
dev_games_count


# In[92]:


#Sorting
dev_games_count.sort_values(ascending = False)


# In[93]:


video_games.head()


# In[96]:


#Which 'Developer' has sale how much sale in USD Globally
video_games.groupby('Developer').Global_Sales.sum().sort_values(ascending = False)


# In[99]:


#Sort games based on their 'Genre'
video_games.sort_values('Genre')


# In[98]:


#Sort games based on their 'Genre'
video_games.sort_values('Genre',ascending = False)


# In[103]:


#sort games by 'Genre' and under each 'Genre',we need to have games in alphabetical order..
video_games.sort_values(['Genre','Name'])


# In[102]:


#sort games by 'Genre' and under each 'Genre',we need to have games in alphabetical order..
video_games.sort_values(['Genre','Name'],ascending=[False,True])


# In[104]:


video_games.head(100)


# In[ ]:





# # DAY-31

# In[ ]:





# In[105]:


Fill_Critic_Score = video_games['Critic_Score'].fillna(75)


# In[106]:


Fill_Critic_Score


# In[107]:


video_games.head(2)


# # Replace Only for Specified column:

# In[109]:


#Replace Null value on the specific column...
Fill_Critic_Score = video_games['Critic_Score'].fillna(75,inplace=True)


# In[110]:


Fill_Critic_Score


# In[111]:


video_games.head()


# # Replace Using 'Mean',"Median" and "Mode":

# In[115]:


#Calculate the mean & replace any empty values with it...
fill_mean = video_games['Critic_Count'].mean()
video_games['Critic_Count'].fillna(fill_mean,inplace = True)


# In[116]:


fill_mean


# In[117]:


video_games.head()


# In[130]:


#Calculate the mode & replace any empty values with it...
fill_mode = video_games['User_Score'].mode()
video_games['User_Score'].fillna(fill_mode,inplace = True)


# In[131]:


fill_mode


# In[123]:


#Calculate the median & replace any empty values with it...
fill_median = video_games['User_Count'].median()
video_games['User_Count'].fillna(fill_median,inplace = True)


# In[124]:


fill_median


# In[125]:


video_games.head(50)


# In[132]:


#FReplace 'Developer' empty cell with the value of 'Nintendo' with it...
fill_developer = video_games['Developer'].fillna('Nintendo',inplace = True)


# In[133]:


fill_developer


# In[135]:


#Count Rating...
video_games.groupby('Rating').count()


# In[138]:


#FReplace 'Rating' empty cell with the value of 'M' with it...
fill_Rating = video_games['Rating'].fillna('M',inplace = True)


# In[139]:


fill_Rating


# In[140]:


video_games.head(100)


# In[141]:


#Calculate the median & replace any empty values with it...
fill_median = video_games['User_Score'].median()
video_games['User_Score'].fillna(fill_median,inplace = True)


# In[142]:


fill_median


# In[143]:


video_games.head(100)


# In[144]:


video_games.to_excel("video_games.xlsx")


# In[ ]:





# # DAY-32

# # NUMPY:
Nnmpy :- Numerical Python
    
    -> Numpy is a python library
    -> Numpy is used for working with array
    -> Numpy is short for numerical python
# # Create A Numpy ndArray Object:
-> We can create a Numpy ndArray obj by Using the array() function.

  NOTE:
        To Create An ndArray we can pass a[List,Tuple Or Any Array like obj...]
# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3,4,5])
print(a)


# In[3]:


print(type(a))


# In[4]:


print(a[3])


# In[9]:


print(a[4])


# In[10]:


# Use a Tuple to create a Numpy Array...
arr = np.array([11,22,33,44,55,66])
print(arr)


# # Dimensions In Arrays:
-> Dimensions in arrays is one level of arrays depth(Nested Arrays)...
-> Nested Array are always that have array as their element...
# # 0-D Array:
-> 0-D Array are the elements in an array.
-> Each value in an array is a 0-D Array..
# In[11]:


#Create a-D Array with values of 42..

arr = np.array(42)
print(arr)


# # 1-D Array:
-> An Array that has 0-D Arrays as it's elements is called uni_Dimensions Array or 1-D Arrays.
-> These are the most common & Basic Arrays.
# In[12]:


#Create A 1-D array Containds the values.

arr = np.array([1,2,3,4,5,6])
print(arr)


# # 2-D Array:

# In[13]:


#Create A 2-D array Containds the values.

arr = np.array([[1,2,3],[4,5,6]])
print(arr)


# In[14]:


arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.shape)


# # 3-D Array:

# In[15]:


#Create A 2-D array Containds the values.

arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr)


# In[16]:


arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr.shape)

Note:
    Numpy Array provide the 'ndim' attribute that return an integer that tell us how many dimensions the array have...
# In[18]:


#Check how many dimensions array have...

a = np.array(42)
b = np.array([1,2,3])
c = np.array([[11,22,33],[44,55,66]])
d = np.array([[[99,88,77],[66,55,44],[33,22,11]]])

print('Dimensions of a :',a.ndim)
print('Dimensions of b :',b.ndim)
print('Dimensions of c :',c.ndim)
print('Dimensions of d :',d.ndim)


# # Numpy Array Index:

# In[19]:


arr = np.array([1,3,5,7,9])
print(arr[3])


# In[20]:


#Get the second element from the following array...

arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1])


# In[21]:


#Get the third & Four element from the following array...

arr = np.array([1,2,3,4,5,6,7,8])
print(arr[3],arr[4])


# In[22]:


#Get the third & Four element of sum from the following array...

arr = np.array([1,2,3,4,5,6,7,8])
print(arr[3]+arr[4])


# # Access 2-D Array:

# In[24]:


#Access the element on the 1st row & 2nd Column..

arr = np.array([[1,2,3],[5,6,7]])
print(arr[0,1])


# In[25]:


#2nd row 3rd column

print(arr[1,2])


# In[26]:


#2nd row 1st column
print(arr[1,0])


# # DAY-33

# # Access 3-D Array:
Note:
    To access elements from 3-D Array we can use comma separated integers represent the dimensions and index of the element... 
# In[29]:


#Access the 3rd elements of the second array of the 1st array...
arr = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr[0,1,2])


# In[31]:


#Access the 2nd elements of the 3rd array of the 1st array
print(arr[0,2,1])


# In[32]:


#Access the 2nd elements of the 2nd array of the 1st array
print(arr[0,1,1])


# # Negative Indexing:

# In[34]:


# Use negative indexing to access array from the end

arr = np.array([[1,2,3],[4,5,6]])
print(arr[1,-1])


# # Numpy Array Slicing:
-> Slicing in python means taking element from one given index to another given index.

  syn:
        [start:end:step]
        
        Step:
             Use to step value to determine the step of the slicing.
        
  Note:
      -> if we don't pass "start" it's considerd 0
      -> if we don't pass "step" it's considerd 1
      -> if we don't pass "end
      " it's considerd "Length of the array that dimensions"
# In[35]:


#Slicing index from index 1 to 5 from the following arrays...
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])

Note:
    The results includes the start index, But exclude the end index
# In[39]:


#Slice index from index 4 to the end of the array

arr = np.array([11,22,33,44,55,66,77,88,99])
print(arr[4:])


# In[40]:


#Slice index from start to the 4 array index
print(arr[:4])


# In[41]:


#slice from the index 3 from the end to index 1 from the end
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[-3:-1])


# In[42]:


#Return every other element from index 1 to index 5

arr = np.array([2,4,6,8,10,12,14,16,18,20])
print(arr[1:5:2])


# In[43]:


#Return every other elements from the entire array
arr = np.array([2,4,6,8,10,12,14,16,18,20])
print(arr[::2])


# # Slicing In 2-D Array:

# In[44]:


#From the 2nd elements slicing from index 1 to index 4 (Not included)

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])


# In[45]:


#From the 1nd elements slicing from index 1 to index 4 (Not included)

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1:4])


# In[46]:


#From the 2nd elements slicing from index 1 to index 4 (Not included) with step 1

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4:2])


# In[47]:


#From both element return index 2

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,2:2])


# In[48]:


#From both elements slicing from index 1 to index 4 (Not included)

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:4,1:4])


# In[ ]:





# # DAY-34 [Data_Types In Numpy]
Data Types in Python

By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"

integer - used to represent integer numbers. e.g. -1, -2, -3

float - used to represent real numbers. e.g. 1.2, 42.42

boolean - used to represent True or False.

complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# # Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer

b - boolean

u - unsigned integer

f - float

c - complex float

m - timedelta

M - datetime

O - object

S - string

U - unicode string

V - fixed chunk of memory for other type ( void )

# # **Checking** the Data Type of an Array
The NumPy array object has a property called dtype that returns the data type of the array:

# In[3]:


#Get the data type of an array object:
arr = np.array([1, 2, 3, 4])

print(arr.dtype)


# In[4]:


#Get the data type of an array containing strings:
arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

**Explanation**

The code creates a NumPy array containing three strings: "apple", "banana", and "cherry".

It then prints the data type of the array using the dtype attribute.

The output <U6 signifies:

<U: Indicates that the array elements are Unicode strings. Unicode is a standard encoding system that represents text from different writing systems.

6: Represents the maximum length of the strings in the array. In this case, the longest string is "banana" with 6 characters.

Therefore, <U6 tells us that the array holds Unicode strings with a maximum length of 6 characters.
# In[ ]:





# # Creating Arrays With a Defined Data Type
-> We use the array() function to create arrays, this function can take an optional argument:
    dtype that allows us to define the expected data type of the array elements:
# In[5]:


#Create an array with data type string:
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

When you create a NumPy array with **dtype='S'**, the numerical values (1, 2, 3, 4) are converted into **byte strings**. 
Since the maximum **length** of the strings in this case is **1**, each element is represented as a **byte string of length 1** (e.g., b'1', b'2').




The code creates a NumPy array with a specified data type of 'S', which represents strings.

Array Creation:

arr = np.array([1, 2, 3, 4], dtype='S') creates a NumPy array from the list [1, 2, 3, 4] and sets the data type of its elements to strings using dtype='S'.

Output:

print(arr) displays the array elements: [b'1' b'2' b'3' b'4']

The 'b' prefix before each element indicates that they are byte strings. This is because the 'S' data type in NumPy represents byte strings.

print(arr.dtype) prints the data type of the array: '|S1'

'|S1' indicates a byte string data type with a maximum length of 1 character.
# In[6]:


# create an array of Unicode strings
arr = np.array([1, 2, 3, 4], dtype='U')
print(arr)
print(arr.dtype)

This will create an array of Unicode strings with a maximum length of 1 character.


***For i, u, f, S and U we can define size as well.***
# In[7]:


#Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


# # Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.
# In[8]:


#Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


# In[9]:


#Change data type from integer to boolean:
arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)


# In[ ]:





# # NumPy Array Copy vs View
**The Difference Between Copy and View**

The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
# In[10]:


#COPY:
#Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5]) #created array
x = arr.copy() # created a copy of existing array
arr[0] = 42 # origibal array -> changes arr[0]=42

print(arr)
print(x)


# # **The copy SHOULD NOT be affected by the changes made to the original array.**

# In[11]:


#VIEW:
#Make a view, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# # **The view SHOULD be affected by the changes made to the original array.**

# In[12]:


#Make Changes in the VIEW:
#Make a view, change the view, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)


# # **The original array SHOULD be affected by the changes made to the view.**

# # Check if Array Owns its Data
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.
# In[13]:


#Print the value of the base attribute to check if an array owns it's data or not:
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)


#  **The copy returns None.
# The view returns the original array.**

# # NumPy Array Shape

# Shape of an Array
# 
# The shape of an array is the number of elements in each dimension.
# 
# Get the Shape of an Array
# 
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
# 
# 
# 

# In[14]:


#Print the shape of a 2-D array:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)


# The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.
# 
# 

# In[15]:


#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)
print(arr[0,0,0,0,3])


# What does the shape tuple represent?
# 
# Integers at every index tells about the number of elements the corresponding dimension has.
# 
# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.

# **Explanation:**
# 
# **Creating a 5D array:** np.array([1, 2, 3, 4], ndmin=5) creates a NumPy array from the list [1, 2, 3, 4] with a minimum of 5 dimensions. NumPy adds additional dimensions as "singleton dimensions" (dimensions with size 1) to achieve the desired dimensionality.
# 
# **Printing the array:** print(arr) displays the 5D array, showing its nested structure with multiple sets of brackets representing each dimension.
# 
# **Shape of the array:** print('shape of array :', arr.shape) prints the shape of the array as a tuple. The output (1, 1, 1, 1, 4) indicates that the array has five dimensions, with the first four dimensions having a size of 1 and the last dimension having a size of 4.
# 
# **Verifying the last element:** print(arr[0,0,0,0,3]) accesses and prints the element at index 3 in the last dimension. The output 4 confirms that the last dimension contains the value 4.

# # NumPy Array Reshaping
# 

# Reshaping arrays
# 
# Reshaping means changing the shape of an array.
# 
# The shape of an array is the number of elements in each dimension.
# 
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# **Reshape From 1-D to 2-D**

# In[16]:


#Convert the following 1-D array with 12 elements into a 2-D array.

#The outermost dimension will have 4 arrays, each with 3 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)


# In[17]:


arr1=arr.reshape(2,6)
arr1


# In[ ]:


#Convert the following 1-D array with 12 elements into a 3-D array.
#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# Can We Reshape Into any Shape?
# 
# Yes, as long as the elements required for reshaping are **equal in both shapes**.
# 
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
# 

# In[ ]:


#Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(3, 3)

print(newarr)


# **Returns Copy or View?**

# In[ ]:


#Check if the returned array is a copy or a view:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)


# The example above returns the original array, so it is a view.

# **Flattening the arrays**
# 
# Flattening array means converting a multidimensional array into a 1D array.
# 
# We can use reshape(-1) to do this.
# 

# In[ ]:


#Convert the array into a 1D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


# In[ ]:


arr2=arr.ravel()
arr2


# In[ ]:


arr3=arr.flatten()
arr3


# # NumPy Array Iterating

# Iterating Arrays
# 
# Iterating means going through elements one by one.
# 
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# 
# If we iterate on a 1-D array it will go through each element one by one.
# 

# In[ ]:


#Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])

for x in arr:
  print(x)


# **Iterating 2-D Arrays**
# 
# In a 2-D array it will go through all the rows.
# 

# In[ ]:


#Iterate on the elements of the following 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)


# **If we iterate on a n-D array it will go through n-1th dimension one by one.**

# In[ ]:


#To return the actual values, the scalars, we have to iterate the arrays in each dimension.

#Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)


# **Iterating 3-D Arrays**
# 
# In a 3-D array it will go through all the 2-D arrays.
# 

# In[ ]:


#Iterate on the elements of the following 3-D array:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)


# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# In[ ]:


#Iterate down to the scalars:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


# ### **Iterating Arrays Using nditer()**
# 
# The function nditer() is a helping function that can be used from very basic to very advanced iterations.
# 
# It solves some basic issues which we face in iteration, lets go through it with examples.
# 
# Iterating on Each Scalar Element
# 
# In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.
# 

# In[ ]:


#Iterate through the following 3-D array:

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# In[ ]:





# # DAY-35   LinkedIn Optimization

# # DAY-36:

# # NumPy Joining Array

# Joining NumPy Arrays
# 
# Joining means putting contents of two or more arrays in a single array.
# 
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# 
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

# In[ ]:


#Join two arrays
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


# In[ ]:


#Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# ## Joining Arrays Using Stack Functions
# 
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# 
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# 
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

# In[ ]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)


# Stacking Along Rows
# 
# NumPy provides a helper function: hstack() to stack along rows.

# In[ ]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


# Stacking Along Columns
# 
# NumPy provides a helper function: vstack()  to stack along columns.

# In[ ]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)


# Stacking Along Height (depth)
# 
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
# 
# 

# In[ ]:


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)


# # NumPy Splitting Array
# 

# 
# Splitting NumPy Arrays
# 
# Splitting is reverse operation of Joining.
# 
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# 
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# In[ ]:


arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


# **Note**: The return value is a list containing three arrays.

# If the array has less elements than required, it will adjust from the end accordingly.

# In[ ]:


#Split the array in 4 parts:

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)


# Note: We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.
# 
# 

# ## Split Into Arrays
# 
# The return value of the array_split() method is an array containing each of the split as an array.
# 
# If you split an array into 3 arrays, you can access them from the result just like any array element:

# In[ ]:


#Access the splitted arrays:
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# ## Splitting 2-D Arrays
# 
# Use the same syntax when splitting 2-D arrays.
# 
# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

# In[ ]:


#Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)


# The example above returns three 2-D arrays.
# 
# Let's look at another example, this time each element in the 2-D arrays contains 3 elements.

# In[ ]:


#Split the 2-D array into three 2-D arrays.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)


# The example above returns three 2-D arrays.
# 
# In addition, you can specify which axis you want to do the split around.
# 
# The example below also returns three 2-D arrays, but they are split along the row (axis=1).

# In[ ]:


#Split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


# An alternate solution is using hsplit() opposite of hstack()
# 
# 

# In[ ]:


#Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)

print(newarr)


# Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().

# # NumPy Searching Arrays
# Searching Arrays
# 
# You can search an array for a certain value, and return the indexes that get a match.
# 
# To search an array, use the where() method.

# In[ ]:


#Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


# The example above will return a tuple: (array([3, 5, 6],)
# 
# Which means that the value 4 is present at index 3, 5, and 6.

# In[ ]:


#Find the indexes where the values are even:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)


# In[ ]:


#Find the indexes where the values are odd:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 1)

print(x)


# ## Search Sorted
# 
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

# In[ ]:


#Find the indexes where the value 7 should be inserted:

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)


# Example explained: The number 7 should be inserted on index 1 to remain the sort order.
# 
# The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.

# ## Search From the Right Side
# 
# By default the left most index is returned, but we can give side='right' to return the right most index instead.

# In[ ]:


#Find the indexes where the value 7 should be inserted, starting from the right:

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)


# Example explained: The number 7 should be inserted on index 2 to remain the sort order.
# 
# The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.

# ### **Multiple Values**
# 
# To search for more than one value, use an array with the specified values.

# In[ ]:


#Find the indexes where the values 2, 4, and 6 should be inserted:

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)


# The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.
# 
# 

# # DAY-37

# # NumPy Sorting Arrays

# Sorting Arrays
# 
# Sorting means putting elements in an ordered sequence.
# 
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
# 
# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# In[ ]:


#Sort the array:

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))


# Note: This method returns a copy of the array, leaving the original array unchanged.

# In[ ]:


#You can also sort arrays of strings, or any other data type:
#Sort the array alphabetically:

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))


# In[ ]:


#Sort a boolean array:

arr = np.array([True, False, True])

print(np.sort(arr))


# When you sort a boolean array, False is considered smaller than True. Therefore, when you sort the array [True, False, True], it arranges the elements in ascending order, resulting in the output: [False, True, True].

# ## Sorting a 2-D Array
# 
# If you use the sort() method on a 2-D array, both arrays will be sorted:
# 

# In[ ]:


#Sort a 2-D array:

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


# # NumPy Filter Array

# Filtering Arrays
# 
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# 
# In NumPy, you filter an array using a boolean index list.

# A boolean index list is a list of booleans corresponding to indexes in the array.

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

# In[ ]:


#Create an array from the elements on index 0 and 2:

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False] # filter array

newarr = arr[x]

print(newarr)


# The example above will return [41, 43], why?
# 
# Because the new array contains only the values where the filter array had the value True, in this case, index 0 and 2.

# ## Creating the Filter Array
# 
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

# In[ ]:


#Create a filter array that will return only values higher than 42:

#import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
    else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# Creating Filter Directly From Array
# 
# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
# 
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

# In[ ]:


#Create a filter array that will return only values higher than 42:

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# In[ ]:


#Create a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# #  Numpy Functionalities

# In[ ]:


a1=np.zeros((3,4))
print(a1)


# In[ ]:


a1=np.ones((3,4))
print(a1)


# In[ ]:


a=range(0,5)
print(a)


# In[ ]:


print(np.arange(0,5))


# In[ ]:


print(np.arange(0,5,3))


# In[ ]:


print(np.linspace(0,5,10))


# In[ ]:


print(arr)


# In[ ]:


arr.min()


# In[ ]:


arr.max()


# In[ ]:


arr.sum()


# In[ ]:





# # DAY-38:

# # START MATPLOTLIB IN PYTHON:

# # What is Matplotlib?
# 
# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# 
# Matplotlib was created by John D. Hunter.
# 
# Matplotlib is open source and we can use it freely.
# 
# Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

# # Matplotlib Pyplot
# 
# ## Pyplot
# Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
# 

# In[1]:


import matplotlib.pyplot as plt

#Now the Pyplot package can be referred to as plt.


# In[2]:


#Draw a line in a diagram from position (0,0) to position (6,250):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()


# # Matplotlib Plotting

# Plotting x and y points
# 
# The plot() function is used to draw points (markers) in a diagram.
# 
# By default, the plot() function draws a line from point to point.
# 
# The function takes parameters for specifying points in the diagram.
# 
# Parameter 1 is an array containing the points on the x-axis.
# 
# Parameter 2 is an array containing the points on the y-axis.
# 
# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

# In[3]:


#Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


# The x-axis is the horizontal axis.
# 
# The y-axis is the vertical axis.

# # Plotting Without Line
# 
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
# 

# In[4]:


#Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()


# ## Multiple Points
# 
# You can plot as many points as you like, just make sure you have the same number of points in both axis.

# In[5]:


#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# # Default X-Points
# 
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
# 
# So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

# In[6]:


#Plotting without x-points:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()


# The x-points in the example above are [0, 1, 2, 3, 4, 5].

# # Matplotlib Markers

# ### Markers
# 
# You can use the keyword argument marker to emphasize each point with a specified marker:

# In[7]:


#Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()


# In[8]:


#Mark each point with a star :

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()


# Marker Reference
# 
# You can choose any of these markers:
# 
# 
# Marker	Description
# 
# 'o'	Circle
# 
# '*'	Star
# 
# '.'	Point
# 
# ','	Pixel
# 
# 'x'	X
# 
# 'X'	X (filled)
# 
# '+'	Plus
# 
# 'P'	Plus (filled)
# 
# 's'	Square
# 
# 'D'	Diamond
# 
# 'd'	Diamond (thin)
# 
# 'p'	Pentagon
# 
# 'H'	Hexagon
# 
# 'h'	Hexagon
# 
# 'v'	Triangle Down
# 
# '^'	Triangle Up
# 
# '<'	Triangle Left
# 
# '>'	Triangle Right
# 
# '1'	Tri Down
# 
# '2'	Tri Up
# 
# '3'	Tri Left
# 
# '4'	Tri Right
# 
# '|'	Vline
# 
# '_'	Hline

# ## Format Strings fmt
# You can also use the shortcut string notation parameter to specify the marker.
# 
# This parameter is also called **fmt**, and is written with this syntax:
# 
# **marker**|**line**|**color**

# In[9]:


#Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()


# The marker value can be anything from the Marker Reference above.
# 
# The line value can be one of the following:
# 
# Line Reference
# 
# Line Syntax	Description
# 
# '-'	Solid line
# 
# ':'	Dotted line
# 
# '--'	Dashed line
# 
# '-.'	Dashed/dotted line

# Note: If you leave out the line value in the fmt parameter, no line will be plotted.

# The short color value can be one of the following:
# 
# Color Reference
# 
# Color Syntax	Description
# 
# 'r'	Red
# 
# 'g'	Green
# 
# 'b'	Blue
# 
# 'c'	Cyan
# 
# 'm'	Magenta
# 
# 'y'	Yellow
# 
# 'k'	Black
# 
# 'w'	White

# ## Marker Size
# 
# You can use the keyword argument markersize or the shorter version, **ms** to set the size of the markers:
# 

# In[10]:


#Set the size of the markers to 20:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()


# ## Marker Color
# 
# You can use the keyword argument markeredgecolor or the shorter **mec** to set the color of the edge of the markers:

# In[11]:


#Set the EDGE color to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()


# You can use the keyword argument markerfacecolor or the shorter **mfc** to set the color inside the edge of the markers:
# 

# In[12]:


#Set the FACE color to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()


# Use both the mec and mfc arguments to color the entire marker:

# In[13]:


#Set the color of both the edge and the face to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()


# # Matplotlib Line

# ## Linestyle
# 
# You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

# In[14]:


#Use a dotted line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()


# In[15]:


#Use a dashed line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')
plt.show()


# ## Shorter Syntax
# 
# The line style can be written in a shorter syntax:
# 
# linestyle can be written as ls.
# 
# dotted can be written as :.
# 
# dashed can be written as --.

# In[17]:


#Shorter syntax:

plt.plot(ypoints, ls = ':')


# **Line Styles**
# 
# You can choose any of these styles:
# 
# Style	Or
# 
# 'solid' (default)	'-'
# 
# 'dotted'	':'
# 
# 'dashed'	'--'
# 
# 'dashdot'	'-.'
# 
# 'None'	'' or ' '

# ## Line Color
# 
# You can use the keyword argument color or the shorter c to set the color of the line:

# In[18]:


#Set the line color to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()


# ## Line Width
# 
# You can use the keyword argument linewidth or the shorter lw to change the width of the line.
# 
# The value is a floating number, in points:

# In[19]:


#Plot with a 20.5pt wide line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()


# ## Multiple Lines
# 
# You can plot as many lines as you like by simply adding more plt.plot() functions:

# In[20]:


#Draw two lines by specifying a plt.plot() function for each line:

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()


# You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.
# 
# (In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)
# 
# The x- and y- values come in pairs:

# In[21]:


#Draw two lines by specifiyng the x- and y-point values for both lines:

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()


# In[ ]:





# # DAY-39

# In[ ]:





# # Matplotlib Labels and Title

# ## Create Labels for a Plot
# 
# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

# In[22]:


#Add labels to the x- and y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()


# ## Create a Title for a Plot
# 
# With Pyplot, you can use the title() function to set a title for the plot.

# In[23]:


#Add a plot title and labels for the x- and y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()


# ## Set Font Properties for Title and Labels
# 
# You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.

# In[24]:


#Set font properties for the title and labels:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()


# ## Position the Title
# 
# You can use the loc parameter in title() to position the title.
# 
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

# In[26]:


#Position the title to the left:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()


# # Matplotlib Adding Grid Lines

# Add Grid Lines to a Plot
# 
# With Pyplot, you can use the grid() function to add grid lines to the plot.

# In[28]:


#Add grid lines to the plot:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()


# ## Specify Which Grid Lines to Display
# 
# You can use the axis parameter in the grid() function to specify which grid lines to display.
# 
# Legal values are: 'x', 'y', and 'both'. Default value is 'both'.

# In[29]:


#Display only grid lines for the x-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()


# In[30]:


#Display only grid lines for the y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()


# ## Set Line Properties for the Grid
# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

# In[31]:


#Set the line properties of the grid:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()


# # Matplotlib Subplot

# ## Display Multiple Plots
# 
# With the subplot() function you can draw multiple plots in one figure:

# In[32]:


#Draw 2 plots:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()


# ## **The subplot() Function**
# 
# The subplot() function takes three arguments that describes the layout of the figure.
# 
# The layout is organized in rows and columns, which are represented by the first and second argument.
# 
# The third argument represents the index of the current plot.
# 
# plt.subplot(1, 2, 1)
# 
# the figure has 1 row, 2 columns, and this plot is the first plot.
# 
# plt.subplot(1, 2, 2)
# 
# the figure has 1 row, 2 columns, and this plot is the second plot.
# 
# So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:

# In[33]:


#Draw 2 plots on top of each other:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()


# You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.

# In[35]:


#Draw 6 plots:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()


# ## Title
# You can add a title to each plot with the title() function:

# In[36]:


#2 plots, with titles:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()


# ## Super Title
# You can add a title to the entire figure with the suptitle() function:

# In[37]:


#Add a title for the entire figure:

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()


# # Matplotlib Scatter

# ## Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot.
# 
# The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:

# In[38]:


#A simple scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()


# The observation in the example above is the result of 13 cars passing by.
# 
# The X-axis shows how old the car is.
# 
# The Y-axis shows the speed of the car when it passes.
# 
# Are there any relationships between the observations?
# 
# It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.

# ## Compare Plots
# 
# In the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?

# In[39]:


#Draw two plots on the same figure:

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()


# Note: The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter.

# By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives.

# ## Colors
# You can set your own color for each scatter plot with the color or the c argument:

# In[40]:


#Set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()


# ## Color Each Dot
# You can even set a specific color for each dot by using an array of colors as value for the c argument:

# Note: You cannot use the color argument for this, only the c argument.

# In[41]:


#Set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()


# ## ColorMap
# The Matplotlib module has a number of available colormaps.
# 
# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.
# 
# Here is an example of a colormap:
# 
# ![image.png](data:image/png;base64,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)
# 
# This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, up to 100, which is a yellow color.
# 
# 

# ## How to Use the ColorMap
# You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.
# 
# In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot:

# In[43]:


#Create a color array, and specify a colormap in the scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()


# You can include the colormap in the drawing by including the plt.colorbar() statement:

# In[44]:


#Include the actual colormap:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='summer')

plt.colorbar()

plt.show()


# Available ColorMaps
# You can choose any of the built-in colormaps:
# 
# Name
# 
# Reverse
# 
# Accent
# 
# Accent_r
# 
# Blues
# 
# Blues_r
# 
# BrBG
# 
# BrBG_r
# 
# BuGn
# 
# BuGn_r
# 
# BuPu
# 
# BuPu_r
# 
# CMRmap
# 
# CMRmap_r
# 
# Dark2
# 
# Dark2_r
# 
# GnBu
# 
# GnBu_r
# 
# Greens
# 
# Greens_r
# 
# Greys
# 
# Greys_r
# 
# OrRd
# 
# OrRd_r
# 
# Oranges
# 
# Oranges_r
# 
# PRGn
# 
# PRGn_r
# 
# Paired
# 
# Paired_r
# 
# Pastel1
# 
# Pastel1_r
# 
# Pastel2
# 
# Pastel2_r
# 
# PiYG
# 
# PiYG_r
# 
# PuBu
# 
# PuBu_r
# 
# PuBuGn
# 
# PuBuGn_r
# 
# PuOr
# 
# PuOr_r
# 
# PuRd
# 
# PuRd_r
# 
# Purples
# 
# Purples_r
# 
# RdBu
# 
# RdBu_r
# 
# RdGy
# 
# RdGy_r
# 
# RdPu
# 
# RdPu_r
# 
# RdYlBu
# 
# RdYlBu_r
# 
# RdYlGn
# 
# RdYlGn_r
# 
# Reds
# 
# Reds_r
# 
# Set1
# 
# Set1_r
# 
# Set2
# 
# Set2_r
# 
# Set3
# 
# Set3_r
# 
# Spectral
# 
# Spectral_r
# 
# Wistia
# 
# Wistia_r
# 
# YlGn
# 
# YlGn_r
# 
# YlGnBu
# 
# YlGnBu_r
# 
# YlOrBr
# 
# YlOrBr_r
# 
# YlOrRd
# 
# YlOrRd_r
# 
# afmhot
# 
# afmhot_r
# 
# autumn
# 
# autumn_r
# 
# binary
# 
# binary_r
# 
# bone
# 
# bone_r
# 
# brg
# 
# brg_r
# 
# bwr
# 
# bwr_r
# 
# cividis
# 
# cividis_r
# 
# cool
# 
# cool_r
# 
# coolwarm
# 
# coolwarm_r
# 
# copper
# 
# copper_r
# 
# cubehelix
# 
# cubehelix_r
# 
# flag
# 
# flag_r
# 
# gist_earth
# 
# gist_earth_r
# 
# gist_gray
# 
# gist_gray_r
# 
# gist_heat
# 
# gist_heat_r
# 
# gist_ncar
# 
# gist_ncar_r
# 
# gist_rainbow
# 
# gist_rainbow_r
# 
# gist_stern
# 
# gist_stern_r
# 
# gist_yarg
# 
# gist_yarg_r
# 
# gnuplot
# 
# gnuplot_r
# 
# gnuplot2
# 
# gnuplot2_r
# 
# gray
# 
# gray_r
# 
# hot
# 
# hot_r
# 
# hsv
# 
# hsv_r
# 
# inferno
# 
# inferno_r
# 
# jet
# 
# jet_r
# 
# magma
# 
# magma_r
# 
# nipy_spectral
# 
# nipy_spectral_r
# 
# ocean
# 
# ocean_r
# 
# pink
# 
# pink_r
# 
# plasma
# 
# plasma_r
# 
# prism
# 
# prism_r
# 
# rainbow
# 
# rainbow_r
# 
# seismic
# 
# seismic_r
# 
# spring
# 
# spring_r
# 
# summer
# 
# summer_r
# 
# tab10
# 
# tab10_r
# 
# tab20
# 
# tab20_r
# 
# tab20b
# 
# tab20b_r
# 
# tab20c
# 
# tab20c_r
# 
# terrain
# 
# terrain_r
# 
# twilight
# 
# twilight_r
# 
# twilight_shifted
# 
# twilight_shifted_r
# 
# viridis
# 
# viridis_r
# 
# winter
# 
# winter_r

# 
# ## Size
# You can change the size of the dots with the s argument.
# 
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# In[45]:


#Set your own size for the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()


# ## Alpha
# You can adjust the transparency of the dots with the alpha argument.
# 
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# In[46]:


#Set your own size for the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()


# # Matplotlib Bars

# ## Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs:

# In[47]:


#Draw 4 bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


# The bar() function takes arguments that describes the layout of the bars.
# 
# The categories and their values represented by the first and second argument as arrays.

# In[48]:


x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)


# # Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

# In[49]:


#Draw 4 horizontal bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()


# ## Bar Color
# The bar() and barh() take the keyword argument color to set the color of the bars:

# In[50]:


#Draw 4 red bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()


# ## Bar Width
# The bar() takes the keyword argument width to set the width of the bars:

# In[51]:


#Draw 4 very thin bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()


# The default width value is 0.8

# Note: For horizontal bars, use height instead of width.

# ## Bar Height
# The barh() takes the keyword argument height to set the height of the bars:

# In[52]:


#Draw 4 very thin bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()


# The default height value is 0.8
# 
# 

# # Matplotlib Histograms

# ## Histogram
# A histogram is a graph showing frequency distributions.
# 
# It is a graph showing the number of observations within each given interval.
# 
# Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
# 
# ![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAuwAAAJDCAYAAABQakHHAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAADpRSURBVHhe7d0HuB1VvTfgFRJIaKEJoTcp0qSDKEKUIt0AIoIgXkFUREFRucqnXq+KVxRvABEVIk2UIoiISFdQpEsXKSH0GiAQetrHb7k3xniSCwY8Kyfv+zzjOXvvOSc468ys36z5z5p+k15WAACAJs3S+QoAADRIYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBh/Sa9rPP9TCn/9ydMmFD69etXFwAA2jNx4sTSv3//mTKvzdSBvRvWR48eXWabbbYyYMAAoR0AoCHJa1mee+65Mu+885ZBgwbNdHltpg7sL730Uhk1alQ54IADylNPPSWsAwA0KoOsBx10UNl4443LnHPO2Xl35jDTB/bbbrutbL755rXxV1pppTrKDgBAGxLUn3zyyTJixIhy1FFHle23377MMcccnU9nDjN1YB8/fnwZOXJkGTp0aDnkkEPKtttuWwYOHNj5FACA3pa8dtddd5UtttiiDB8+vAwbNmymy2sCeyewz6x/AAAALZPXTOsIAABNE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBh/Sa9rPP9TGf8+PFl5MiRZejQoWX48OFl2LBhZeDAgZ1PAWZML4ybUH5326Mvf53YeafveduyC5RF5hnUeQX0ZfKawC6wA33OI0+/ULb7/mX1a181Yo91yiYrDem8AvoyeU1JDAAANE1gBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGG9HtifeeaZcu+995Ybb7zxH5abbrqp3HHHHWX8+PGdNUt58cUXy0MPPVRuu+22cvPNN9evDzzwQH1/0qRJnbUAAKDv6PXAfu2115aDDjqorLPOOv+wvP3tby+77LJLefzxxztrlnLPPfeUww47rAwbNqxsvPHG9et3vvOd+v6ECRM6awEAQN/R64E9I+MDBw4sq6yySjnuuOPKL3/5y7qcdtppZfjw4WXeeeet691www3lpz/9aTnvvPPKrrvuWg499NDyvve9r9x111018D/88MNCOwAAfU4TNez9+/cv888/f9lwww3Lu971rrpstNFGdaR9ttlmq+ukRObPf/5zWWuttcq2225bttxyy7LTTjuV9ddfv1x//fXlyiuvLE8++WRdFwAA+oomAntGxkePHl3OPffccvbZZ5ff/e53tT69W7/+3HPPlZEjR5YxY8aUrbbaqqy44oplyJAhZdVVV62Bfa655qqlNU888URdHwAA+opeD+yzzjprmX322Ws4T0nMEUccUZcTTzyxXHPNNeX555+vQTyBfsCAAbV0Jl9jlllmqSUzb37zm8vdd99db2CdlpTfTJw4sZ4gdJe8BgCAVvV6YF9ooYXK5ptvXr7+9a+Xww8/vH5dd911yx/+8Iey//771xlkEtgT3FMek4CeoN6V9+aZZ546+v7SSy913v1nCeaZTebZZ5/9hyWj92aYAQCgVb0e2JdYYonyzne+s9atr7TSSmXttdcue+65Z/nIRz5Sw/SFF15YHnnkkVdCdb9+/erXrryfZcr3p3TfffeVH/7wh2WbbbYpm2yySV1yovDhD39YKQ0AAM3q9cA+aNCgOmo+33zzlTnnnLPMPffcZckllyxvectbygILLFBr11O6kvVSNpOyl8lHxPNegn1+NuU1UzN48OCy5ppr1htVM11klg984ANl6623riU5AADQol4P7D3JaHnKXrKMGzeulrwk1Of7UaNGvXIzaoJ7ylry8KRFFllkmsE7P5+5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APqCXg3sGdnOFI2Z/WXyJfXqGRHP14yK52ume9xxxx1r+UpG3b/61a+WX//612XIkCFlv/32qyPwWQ8AAPqSJu+2XHnllWs5zAYbbFADfOTpp5tssknZZZddarlMSmA23HDDsv3225fNNttsmvXrAAAwo2oysK+33nplzz33LFtsscUrQTwj7gntO++8cx1dzw2jBx54YNl6663LPPPMY6YXAAD6JCkXAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQsH6TXtb5fqYzfvz4MnLkyDJ06NAyfPjwMmzYsDJw4MDOpzDzunv0s2XU4892XvU91983phx24R2dV9Ce/Tdd/uVlhc4rmLnJawK7wA49GH7h7S8vAi30FoEd/k5eUxIDAABN6/XAfuedd5YTTjihfOpTnyq77bZb2XXXXcvHP/7xcthhh5WbbrqpjBs3rq43ceLEctddd5Ujjzyy7LXXXmWXXXYp++23XznppJPKk08+WT8HAIC+ptcD+3PPPVfGjh1bBgwYUBZccMGy8MILlwkTJpSrrrqqHHPMMeXee+8tL730UrnjjjvK2WefXZdU8cw777zl0UcfLeeee2455ZRTyrPP9t16WwAAZl69HtgXWGCBsu6665bdd9+9fOYznykHHHBA+dCHPlQWWWSRcvrpp5dbbrmlPPXUU+Xqq6+u4XyOOeaon++///5lu+22q+H+2GOPrcH+xRdf7PxWAADoG3o9sC+22GJlvfXWK2uttVZZcskl6+sNNtigbLzxxnXU/Z577imPPfZYDe4pfUk5zPrrr19WXHHFsu2225atttqqhvVrr722jBkzpvNbAQCgb2juptPUoqf85Zprrql3Bb/lLW+pI+wpfxk8eHBZe+21y6yzzlrXnXPOOcuiiy5al9tvv708/fTT9X0AAOgrmgjszz//fL3B9KMf/WjZaaedamlMXqfsZdVVV603nqbWfdCgQWW++eYrs8zyt//sfv36vfLeE088Mc2SmNS95/fk38rv6i4vvPBC/QwAAFrURGBP8M58mqlbHzJkSJl77rnr6PrDDz9cA3aCeGrV+/fvX0fXs35Xwnvey42p05op5vHHHy8XXnhh+c53vlO++c1v1uVb3/pW+eEPf+iGVQAAmtVEYE9YX3rppcsnP/nJ8vnPf7584hOfKKuttlq5+OKLyxVXXFEDdcJ6QnuC/OQj4gnpCeuzzTbbKyPvPclI+n333Veuu+66Wu/eXW6++eZXpo4EAIDWNDPCnsCd0fVlllmmvPvd7y7bbLNNnebxoosuqqPss88+ew3dufG0G9jzNe+lxj1lMdN66lXq3PfYY49y4oknltNOO60umQ4y871nikgAAGhRE4F9arp155k5JmE+N5X++c9/riPqkRr0lM088MADZYUVVqg3pU5NRt9zUpAbVeeaa6665PtMEzl5iQ0AALSk1wP7DTfcUM4666zy17/+tYbvlK1ceuml9b082TSzwmS6x5VXXrmOoo8YMaLOyZ5ZYfIQpXPOOacsscQSdb3/a6Q8wXzyJSFeWAcAoGW9HtgffPDBWqv+4x//uHz3u98thx9+eDn55JPr++95z3vqfOwLLbRQfbjS5ptvXkfZTzjhhLpeQn1G4VPqklA/rZIYAACYEfV6YJ9//vnr005Tmz5q1Kg6wp6R7zxMKTefrrLKKrVsZfnll3/lQUkpk3nkkUfqiHpC/S677FJLXAAAoK/pN6l7B+dMKDPOjBw5sgwdOrQMHz68DBs2zCg9vGz4hbe/vNzReQX8u+2/6fIvLyt0XsHMTV5r/KZTAACY2QnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANMyDkzw4Cf6JBydB79pu9UXLdmss2nnV97xproFljSXm7byCaZPXBHaBHXogsANvpE1WWqiM2GPdziuYNnlNSQwAADRNYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADSs1wP7qFGjyq9+9asyfPjw8pWvfKV89atfLYcddlj57W9/Wx5//PEyceLEzpqlTJo0qTzzzDPl3HPPLd/73vfKl7/85XLwwQeXk08+uTz88MNl3LhxnTUBAKBv6PXAfvvtt5fzzjuvXHnlleWWW24pf/nLX8oll1xSzjjjjHLOOefUgJ6gHmPGjCmXX355Oemkk+o6N9xwQ3192mmnld/85jflkUceeWVdAADoC3o9sL/wwgtlnnnmKbvsskv5xje+UZett966jpgfeuih5cEHH6wj5wnid911Vzn66KPLX//617LVVluV//qv/yp77bVXmWWWWeqo/I033miUHQCAPqXXA3uCd0phttxyy7LCCiuU5ZZbruy4445lhx12qGH9tttuq6PsL730Ui2fueyyy8ruu+9etthii7L66quXTTbZpHz2s5+t5TPXXXdduf/++zu/GQAAZny9HthnnXXWMvvss9ev/fv3r0t0a9fzWd4bPXp0ue++++r76667bnnTm95U359jjjnKEkssUZZccslaEpMFAAD6il4P7D259dZba3360ksvXcN4QvvYsWPLE088UQYMGFAWWWSR+l6kHGbQoEFlyJAhdZ2nn366vj+llNSMHz++vPjii7UMp7tk5B4AAFrV7+Ug29RdmnfccUc59dRTy1VXXVXWW2+98qlPfaoMHjy43HTTTeXEE0+sn+VG04T2rpTD7LvvvjXM77zzzmWbbbbpfPJ3Tz31VC2vydKtc58wYUJ57LHHyiGHHFJ+9KMflWHDhpWBAwfWz2BmNvzC219e7ui8Anh9rbrYPGXvjZbtvOp7Bg2YpWy0woJl0Kx/qxpg+mTAdeTIkWXo0KF1VsGZMa81E9hT6pIR9BEjRtQ69WWXXbZ86UtfqqUvGUXPDDIJ7D//+c/r54sttljp169f/dkE9o9//OO1PCaBPXXxU0r9e6Z/POWUU8qzzz5b38v/9YT3Bx54oM48I7DD3wjsAP+6IYMHlbP2fUf9yvQT2BsqicmNpUcddVSdk3211VarN5IuuOCCNaxHSmDmmmuuGrCzbhqvK2E/Uz6m8bqlMlNKac0+++xT53fPlJBZLr744noSsMACC3TWAgCAtjQR2DNd45FHHlnnXU85S0bJF1544VdG0CMj7QndKWNJfXsCeqQGPTek3n333TXgL7TQQvX9KeUG1bnnnrt+PvnSHcEHAIAW9XpSzYOSfvGLX9SHJ62//vplww03rGE9N4d2p3NM6cqcc85ZllpqqbLSSiuVM888s9a4J6Rff/31ta49oTufLbroop3f/I8S/rNOgntq3btLd1YaAABoUa8H9muuuaYG7gT3BOprr722nH766eWnP/1prTfPQ5JSc55gnbr27bffvjz66KO1tCV153nKacL7pptuWudln3feeTu/GQAAZny9HtgzDWNG0ueff/5aEpPZWvLU0iz5Pg9DynSNsfjii5fddtutls3ce++95YwzzqiBf+WVVy777bdfffDS5GU0AAAwo+v1WWJS8jK1udATvmebbbZautIN4t2ZXXLTafc/PaPvWe+11qK76xh6ZpYYgH+dWWJeX/JaAyPsCdqZ/aWnJXXreQLq5KPm3RCfKRzzeZY8OMmNowAA9EVSLgAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA3rN+llne9nOuPHjy8jR44sQ4cOLcOHDy/Dhg0rAwcO7HwKU3fZnaPLQ0+90HnV95x/y8Pl/L880nkFwGsxZPCgcta+76hfmX7ymsAusPMv2fP4q8tFtz7aeQUAfyewv77kNSUxAADQNIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQsF4P7M8880y57bbbym9/+9vys5/9rIwYMaJcdNFF5dFHH+2s8XdjxowpV155ZTn55JPLcccdV79edtll5amnnioTJ07srAUAAH1Hrwf20aNHl8svv7wcc8wx5cgjjyyf+9znytFHH13uuuuuzhp/k2B/ww031M+y3hFHHFGXBPf8/PPPP18mTZrUWRsAAPqGXg/s48aNK7POOmt561vfWj796U+X5ZZbrvPJP7r++uvLiSeeWM4///zyH//xHzW0f/CDHyx33313+c///M/y8MMPlwkTJnTWBgCAvqHXA/uSSy5Zttxyy7L33nuXzTffvLzpTW/qfPJ3GTm/6aabyqhRo8oee+xRNttss7LaaquVHXbYoXzgAx+oJTEXX3xxj2U0AAAwI+v1wD5w4MAy//zzl0UWWaTMN998dbR9Sk8//XS5//77y0svvVQ22mijsuCCC5Y555yzDBkypI7IL7bYYuWWW26pNe4AANCX9HpgfzUSxLMkzC+zzDJlwIAB9f1+/fqVueaaqyy++OLlwQcfrHXsU5NR+pTMpAQnwb+75DUAALRqhgjszz33XHnhhRdqUJ977rlrUO9KiM9oe25KnVb4TphPvXtmmclNqlmuuOKKct1119XgDgAALZohAvu0ZOQ8S0L85EF+SimpOeqoo8rWW29d3vWud9Vl0003rTXxTzzxRGctAABoywwR2AcPHlzmmGOOOhL+5JNP/sOc6xlVT437PPPM02P9e9cSSyxR9tlnnzrf+yWXXFKX3KiamWcWWGCBzloAANCWGSKw52bUzB6TGvS//OUvZfz48fX9BPfMEJM525daaqlazz41gwYNquusu+66Zf3116/LeuutV9ZYY41pBn0AAOhNvR7YE7pTX54HKGXp3gyaIP7444+XsWPHltlmm60su+yydRT93HPPLbfffnudwjHh/aqrrqrrrL322nW2malJuUz//v1rOM/v6y7dG1gBAKBFvR7YE9YzQn7eeefVJUH8oYceqjeEXnDBBfXppgnkebDSmmuuWa655ppy9tln1+B+2mmn1ZtH81lGzDMSDwAAfUmvB/bHHnusnHXWWWX33XevS55omplcvva1r5W99tqrHHHEEeWee+6poXy33XarN4oee+yxZd999y0nnXRSffDSwQcfXOdxzwg6AAD0Jf0mZYqVXpTyl8zSknnUpzTLLLPUMpiFF164zD777HVqx5TJZE721LGnnCU3pOZBSnkA07RmielJfsfIkSPL0KFDy/Dhw8uwYcPq74H/y57HX10uutWTdQH4Z0MGDypn7fuO+pXpJ681MMKeOvIE8rXWWuufltwQmgclJaxHbhzNU01XWWWVsvrqq9evmf0l77/WsA4AADOCGWKWGAAAmFkJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBhAjsAADRMYAcAgIYJ7AAA0DCBHQAAGiawAwBAwwR2AABomMAOAAANE9gBAKBh/Sa9rPP9TGf8+PFl5MiRZejQoWX48OFl2LBhZeDAgZ1P+VeNmzCx3PrQ0+WlCX33T+t/zrm1XHPPk51XAPB3QwYPKmft+476leknrwnsAvsb4JGnXyjbff+y+hUAZjYC++tLXlMSAwAATRPYAQCgYQI7AAA0TGAHAICGCewAANAwgR0AABpmWkfTOr7uTOsIwMxs0Kz9y7vfstDLX/vuuOieGy5bVll0cOfVG0teE9gF9jeAwA4AfduIPdYpm6w0pPPqjSWvKYkBAICmCewAANAwgR0AABomsAMAQMMEdgAAaJjADgAADRPYAQCgYQI7AAA0TGAHAICGCewAANAwgR0AABomsAMAQMMEdgAAaJjADgAADes36WWd72c648ePLyNHjixDhw4tw4cPL8OGDSsDBw7sfPrGufeJ58r5tzzSedX3PPPiuDLij6PK2BfGd94BAPqSEXusUzZZaUjn1Rurt/JaSwT2XvgDuOjWR8qex1/TeQUAMGMR2P+9lMQAAEDDBHYAAGiYwA4AAA0T2AEAoGECOwAANExgBwCAhgnsAADQMIEdAAAaJrADAEDDZrjAPmHChPLwww+X66+/vvzxj3+sS75//PHHy7hx4zprAQBA3zBDBfZJkyaVsWPHll/96lflC1/4Qtl1113r8rnPfa787ne/K0888URdBwAA+ooZKrA/9thj5ZxzzimHH354efOb31y+/vWvl//+7/8uiy++eP2a0fZnnnmmszYAAMz4ZqjA/sADD9TAvuSSS5b3vOc9ZfPNN69fd9ttt9K/f/9y1VVXlTvvvLOzNgAAzPj6TZpBakjyn3nhhReW/fffv+y4447lQx/6UFluueXqZ6lf//SnP13r23feeeey/fbb1/cnl5/P5xMnTuy8U2rN+1133VWD/3e/+92y3XbblYEDB3Y+feNc/NdHy8dOvKbzCgBgxvKj3dcp737LQp1Xb6zktVGjRpXNNtusDB8+vAwbNuzfktdaMsME9pdeeqmcddZZ5ROf+ET53ve+V0P2kCFD6mdPP/10Oeyww8oVV1xRw/pee+1V35/cs88+W+65555y3333lfHjx9f38vWhhx4qX/rSl8pHP/rRssEGG5RZZ521fvZGuv6+MeXwi+7ovAIAmLF8epPlyxpLzNt59cbKgGvy2he/+MXy/e9/v2a92WefvfPpzGGGCey52fSMM86oN5iOGDGivPOd7yzzzTdf/Sx16z/5yU9qoH/ve99bPvWpT9X3J3fHHXeUY489thx33HH/VOeeTdCvX7/OqzdG/o0XXnihzDLLLDPdWWHLXnzxxXrVZdCgQW/43wCvTk6ks6/MMcccdX+hd2mP9uSY9dxzz9Xj1oABAzrv0pv08f8e2c5HHXVUzXpzzz13592ZwwwZ2BPON9xww1cCez5LGE9gz2WSfffdt74/uQSz0aNH1/KZnKl15fsE+JypzTbbbJ13X1/ZxDm4HnjggWXFFVeso/k50NK7cnA9+uijy2233Va+/e1v10AitPeuXEn7/e9/X0vUfvzjH9cbygWS3qM92pMTqPvvv7/svffetT8cOnToG9Z38ero4/89cqL6/PPPlxVWWKEssMAC9d7FmckMVRKT6Rz32WefWr+UOqaFFvpb7VRKYjJzzJ/+9Keyww479FgSk/+baezJa9gj76c2Kp3QGzV6lH8jJTm77LJLWX311WsJTsIhvSsH2IMPPrjccMMN5ec//3mZ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)
# 
# 

# You can read from the histogram that there are approximately:
# 
# 2 people from 140 to 145cm
# 
# 5 people from 145 to 150cm
# 
# 15 people from 151 to 156cm
# 
# 31 people from 157 to 162cm
# 
# 46 people from 163 to 168cm
# 
# 53 people from 168 to 173cm
# 
# 45 people from 173 to 178cm
# 
# 28 people from 179 to 184cm
# 
# 21 people from 185 to 190cm
# 
# 4 people from 190 to 195cm

# ## Create Histogram
# In Matplotlib, we use the hist() function to create histograms.
# 
# The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

# The hist() function will read the array and produce a histogram:

# In[53]:


#A simple histogram:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()


# x = np.random.normal(170, 10, 250): Generates 250 random numbers following a normal distribution.
# 
# 170: Mean of the distribution.
# 
# 10: Standard deviation of the distribution.
# 
# 250: Number of samples to generate.

# # Matplotlib Pie Charts

# ## Creating Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts:

# In[54]:


#A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()


# As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).
# 
# By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:
# 
# ![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAp0AAAH8CAYAAACTlRRcAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAGYjSURBVHhe7d0HYBzXfS76b2a2d/QOECDYexOpQlK9W5Ily5Jj39iJY+fmOr43Tnt2+ouT6+ckTuI4dtybLFm2eu+USJEixd4rCBC9Yxfb28y8meXIkiKSYsEutnw/eo2d/1lQJLg7++2ZUwRVAyIiIiKiLBKNr0REREREWcPQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWcfQSURERERZx9BJRERERFnH0ElEREREWSeoGuM+EeWhtJxGPJVGJKloXwFVVRAKR09/1Y5DSeOBmolwDAntsRfLZbPAbbcaR6e5LdrNrJ0sBBFulyPz1aYdu20mOCxaIxER0Xlg6CSaRoqiIJqSEYmnEUskENQCpP6KjOkhU0uY0aTWltDaUimEtdAZS6na96ha6AxnvuqPDybffQlPhGKZgHqx9MDptr8/SHosgnYDRFHQQqcr89Vu1u5bTVpItcImAXaLBKeWRO1mkxZK9e/RalatTavbzCKsJpPxuxERUali6CTKMj0c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)

# Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:
# 
# The value divided by the sum of all values: x/sum(x)

# ## Labels
# Add labels to the pie chart with the labels parameter.
# 
# The labels parameter must be an array with one label for each wedge:

# In[55]:


#A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()


# ## Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
# 
# The startangle parameter is defined with an angle in degrees, default angle is 0:
# 
# ![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAroAAAIvCAYAAACbVnjpAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAHxbSURBVHhe7f3pk6Pped97XtiX3Nfa96qu3vdmk2zuLVGkFBIZirDH9olxeBl7PC/0P9iv/NYxET4RZ2IcJ86JOKGQjy1Z2xlR4s5uspvNXqq7q2tfs6py3xOZWB/M87sBNFEoZFVlFTITePD9UFBmIrMAZCeA54cL133dobLPAAAAgIAJVz8CAAAAgULQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCCFyr7q5wCABp7nuZOeKvWxmUgkYuFw2EKhkDs9rtp11a632dO0rrP2sRXXCQBBRNAFgPu4fPmyzczM2OzsrN24caN6boXCbTqdtqeeesrGxsbcaWBgoPrdR6Nwu7i4aNPT03br1i2bmpqypaWl6ncr+vr67NixY9bT02NPPPHEY18nAAQVQRcAGqytrdn169ddyJ2fn7eNjQ3LZrPu/HqqpEajURscHLRkMmmjo6N29OhRO3XqlKVSqS1VWkulki0sLNiFCxdsYmLCXVcmk7H19XXL5/PVn6qIxWIu7Opjf3+/u86TJ0/anj17qj8BABCCLgBUKWyqenvlyhV3UuAsFovV7z6Ywq3CpoLu008/7UJorcXgfhSiVb29dOmSXb161YXrzdokmlEl+fTp0/bMM8/Y+Pj4Q10nAHQDgi4AVKld4KOPPrKzZ8/ayspK9dytUTtDb2+vvfHGG66lQWH3fhSkVT3+4IMP7OLFi1sK1vXUvqBw/dJLL9nQ0JCr9gJAt2PqAgD4VM1V2Pzkk0/uCblqQVCVNB6PWyKRcG0K+qgwqWBbT5VYtR28/fbbrjp8v8qsvre8vGzvvvtu05Cry9Z11K5TJ92GZhVbXY5uv4K6PgcAUNEFACsUCnbu3Dl755133OKvxnCqaunhw4fdwq+9e/e6oKn+2Tt37tj58+ebtjgopL766qv24osv2v79+6vn3k0tCz/+8Y/dZayurt4zXWHfvn2uKqxWCAVcBW5dpyrOur2NdJ3q3f3d3/1d928UkAGgm0X+va/6OQB0pVwuZ7/4xS9c64JCbz0tMHvuuedcS4CCp0KvJi1o4oE+HxkZcSFVobU+7Cq0qko8PDzswnEjXadC9a9//WtXQW4M1+q5VUhWuNZl6PrUA6y2CC1+U0uEbq+uo0bXqdugyq++/6C2CQAIOloXAHQ1TTSYm5tzoVNhtZEmGih0qiqrsFmbpKBpC7VK77PPPusqqY00JkyTFJpdrirCmuqgkFsfVlWV1eIyVXI1SUH9tvWtCgrZhw4dcuFbt03ht54uSxVmtU3UXy4AdCOCLoCuphA6OTnpKqz1rQMKtGoXOHLkiAuem1EPraqujYFUdJmagds4B1fXo4CrKQuNLQ+6PAVrBWhVb5tRyNb1vfDCC+5j4xgzhWuFd41FA4BuRtAF0NUUNLV4rLE/VpVVtQzo7X8F3s0oZKrSqxYGfWykQKtxYfV0nTq/sfWgFq5VzW1WIa6nsKsQrtvXGLB1+QrXjdcLAN2GoAsAm1DoVOB9GArFzcKpNnxQqK3XLPyKemvVIqGWCAXZ+1GYVeuDAm2zFgVdL9MXAHQ7gi4AbEIV1sa2gM0opDabXatAqhaGeurPbRZCdRla8KbL2ex61VOszSV+8pOf2Hvvvef6gBur0aLraAzYANBtCLoA0ITCo8KigurDUDhtVoVVMG0MuptVW1VBVs/tZlVkVW+1RbACrub9atRY42XXqPdYtx8AuhlBF0BXU+W0WUBV0FUY1anZ1IRGCqfNqrDNKrpaJKa+4Ea6HVqAVn85uh26jNnZWTdvV+PIzpw540aa3W8zCgXsh7ndABBkBF0AXU2VWPXWNlZRFTA1U1d9sKqcqg+2sUVAX+t8/ZzCa+MM3s0ohDabiKCgW39bardB/bzaWOLnP/+5Gx1WTwvRmlWAa7cLALoZQRdAV9Nc2to82maBUVvz/upXv7KPP/74rukMqrJqhNf7779vf/d3f2dvvfWW3b59233vUen66yc8qP9W2/r++Z//uV29evWuCq2qvvpZzdPV9IVGBF0AIOgC6HIKlwq72jK32dxatR1o8de7775rf/u3f2v//b//d3f6i7/4C/vBD37ggq7CsGbXtiJY1toW1Iv79ttvu6CrtgXdjlqrghatKZxrq18FXfX1NmqsPgNANyLoAuh6al945pln3MQDhchGajPQzmnqkf3000/dQrCzZ8+6tgbNwlW/7GaL1hSkG+fcbkaXoTYFVY8//PBDF3a1w1l9L65Crebsvvrqq25HtvHxcXf7AQD3IugC6HoKotqJ7Mknn7QDBw7cs63u49BlP2wQVWvEuXPn7Gc/+5kL0bUFa6ryJhIJF2qffvppF3IVzHU7my2AEwXsZq0YANBNeBYEgKqXXnrJvvSlL7meV4XT2kKvzcKkztfP1E7Nfk4LzB426KontzYbt1Yh1mWqF/fgwYP2O7/zO/bVr37VhfEHUTBWSwYAdDOCLgDUUWX329/+tv2jf/SP7Mtf/rKdOHGi6Y5nCrZjY2P2+uuvu5NC8t69e6vf/S2FTW3TW28rIXRwcNC++MUv2ne/+13Xl6t/W08zeZvN0tXto6UBQLcLlVmxAAB3UU+sRoCpdUBBUj26jWFSlV7182q7XlHLwWeffeZ6eespnNb6aWv0s1rcdv369eo599Jlq7KsdgqF7802krhy5Yqbrat+3nojIyNuodo3vvGN6jkA0H2o6AJAg1qIHR0ddSHz9OnT9vzzz991UnA9efKkq+rqpNFfCsWNVLltrAirKrtZH7CuW5enkPrKK6+461ZobRZyRRtaNNsBTbe/2RQJAOgmBF0AeAx6U0wVX40Xawycah1Q68Hw8HD1nAqF0GbtEKJ/o3CrXuEnnnjivi0OqjxrW+BmQbenp8ddNwB0M4IuADwGLRpTC4Iqq9qkoZ56c1UVbgy1Ol9V2s0Wr20207eeAraqyJqxq/Fm9XS5aqnQdQBANyPoAsAjUkVVfbza1EGTEhppcVqzzRxUpVWVV2G2Mexq0wn1+q6srFTPaU4B+9KlS+56NwvYjYvgAKDbEHQB4BEokN65c8dtDzw5OekWr9UovCrMamKDZt82Ur+tQqgWqqmCW08BVjutaTe2Zi0JooVxus6PPvrIBd3GNcX79+93QVeTFwCgmxF0AeAhKEwqzGqqwo0bN9zuaL/5zW/cBAUtQqvfvUzhVSFWgVO9ss2omqsWBS1Mq6/q6nIUXrXzmiq7ak2opzaFq1evuq2HFYbrp0HUArauWwvaAKDbMV4MAKq03a4WljWjAKrvKeSqXUFb/87NzVW/+1va3EHV1K997WtuYsNmi8l0eWpP+Ju/+RsXWNVv20jVYC1M03SHGl2vKr7aOa2eQq4WsulntamEtjMGgG5H0AWAqj/90z+9Zx7tVqglQX252mhCAfVBGzaoTeHatWtuy9/bt2/f04KwFaoiq+/3e9/7ngvIbBYBALQuAEBLKFiqFeErX/mK+9jYe9uMemi1KcSLL77otvh9VLocbQusHd1UTX6Y6waAbkDQBYDHoFCp6u3v/M7vuJCr4NrYd7sZ/YxaHRSMtTmEdkFTYH6Yf1ujMWLaXEJzdxWWdXlb+fcAEGS0LgBA1YNaF9SaoPYAbfigQKr+W40PUy+uQuZm/bgPQ32/mqSgVgb1CqtnV7N5G2fkKljXrlfzedWmoHCtlgkFbADAbxF0AaDqhz/8oU1MTFS/updaBDTRQAFTYVM7j+3Zs6f63dZQ364WvCngqm9XobeeKrYK2wrXmqyg26DzAAD3IugCAAAgkOjRBQAAQCARdAEAABBIBF0AAAAEEj26ALCNMpmMW1CmhWWicWDaGnhkZMR9DQDYPlR0AWAbXb161f7zf/7Pbltenf7kT/7E7YQGANh+BF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEEkEXAAAAgUTQBQAAQCARdAEAABBIBF0AAAAEUqjsq34OAKijZ8eSV7ZS2at8/Pzkn+9/0/M/9/yPOs//P//ny1Z7QnUf/f934dxZ+/M/+z/s//s//7/d+V/48lfsn/8//p393h98z30dDoX8U/Wj/0mzzyPu6+rn/pnRSNii+iYA4L4IugC6kp74FFQrQbYSWmuf14JrqVS2vJ9q3alYsoL7vGyFomdF/wf0ddH/uuh/LLh/4wdd/99VnlUroffmpfP2s7/9b/Y3/8f/R2faUy9/0X7vH/8Le+0b3/Wfgc2FWIVWhddKiA1ZzP8Y8ZOtPnffq35fH+PRsCXcKeJ+XqdKAP5tQK4E498GZQDoVgRdAIFXzZ1OreaqoLqRL9latmir2YKt5YrutKqP/nnr/vcUaB/3CfL21Qv2zg/+3H70X/+L+/rUC6/bN//4n9uLX/s99/WjUoU3HYtYOh61noR/ivufVz/q67S+9r+XiFU61EJK1ZVPap8BQOARdAEEkp7ZVG1dyeZteUMhtuDCaybvh9hcybKqypY8V7n9vAXBP3me/7U++iddxuParqArroKrqm21qlur4FYqu5XPY5Gw9frBty8Vtf5kzD/5n/sf+/yPqgYDQJARdAF0PLUaZAslV5HN+CHWfawG2lxRJ89VZwt+ii2o9cAPuPo3O/Hst51B92Eo7Maj/ikS+bztwX2MhS0VUzVYld9qZdj/mPJPapMgAgMIAoIugI6hJyv1zSrUbvgnBVh9rlMt2GZUtfWD7rr/tb6/289wux10NxPyA3DShd3fBl19VNB1H6ttEfpa4ZjqL4BORNAF0Lb05KS2gsoiMC0I81yYXdoo2NJ6wVb8jyvZggu5alNoR+0adDejAKygO5SO2XBPwn0c8E8KvmqDiGmxnP9R7RJEXwDtrrJKAQDaiCKrXoKrh1YLw27Mr9uHN5bsx+dm7O/OTtnbl+fs7J1lm1hct2U/7LZryO1Eqn2oIn5rccM+vrVkP7s4a3/3yZT95PyMfTSxaDf9v8Wq/zfR30Z/I/7LA2hnBF0AbUN9swvrebs8s2bvXJ23vz87bf+/Tyft19cX7OpcxoVaVXixs9TbvJDR3yVj7/p/i7/z/yZ/9+mUveW/4Dh3Z8VmVnNW1Co+AGgzBF0Au0aTDRReb8xn7MzEkv3y8ry9e3XBPrm1bFdn12xyOWuL6wVX1VUfrkaCEXN3nquu+//t3YI//2+hv8nUStau+y8+Pptcsff88Ku/3Se3l10lWIsB9W8AYLcRdAHsKPXbqrf2th+ILk6t2jk/KH02Wfl4YXrVbvjhadoPUSt+oNLPoj2pXUSBdnY1ZxPz6+5vV/lbrriPl2ZW7c7Shvtb83cEsFsIugC2lQp7aknQDNvF9byr0l6eXbMzt5bsnWsLrpKryqCqhApEFAI7j/5mCr7za3m7MrNmH970/7ZX5+3jW8t25fPKfN71/rq/MX9kADuEoAtg21QCkOcmI1yaXrVfXJqzH52bdu0JWmCmnclouQ0evbDRPONr/guYd/y/9Q8/m7afXZi1c1OrrteXFzQAdgpBF0DLqZ9T7Qeq1mq1/g8+nbYzt5ZtZiXnRoShu2g03Nxa3s7eXrYf+/cHvdg5c3PRZlezbsoDAGwXgi6AltCqe709fWFq1X51Zd5+c33RfX5raeOut62p4HYfZVn97dW+ovnHd5azdmF6zX5zY9G1r6i9Qb28qgQDQCsRdAE8MgUYrcRX9VYjwT67U1mMpICrGbd6mzpXoIKLu6mqr/vGzfkNOz+5Wrnf+Cf19+q+pJYWCr0AWoGgC2DL1Jqg6txCJmc3F9bdW9Lv31h046WmlrMsOMJD0Xg5vVDSSLKPbi25Cu9ZP/DqPjXv37dq7wIAwKMi6ALYEr27vLJecFXbn1yYdSe9Db2ywexUPDrddzRTWfern/r3KfXynp1cscVMnpYGAI+MoAvggRRCckXPjQF769Ks/fTijKveqveWncrQam4jEf/FlHZd0xbEOmkDEd0HubcB2AqCLoBNKcNq8ZA2A9BcVM2+vT6fcSvo9bayZqcC2+G37TEFm1hYdzN53/Xvgxf9+6Luk7y+AvAwCLoA7qGK2tJ63oXac1OVna4UMO4sZd18VN5Kxk7RfVGBV73fF6fX3H3xvH+fvDaboa0BwAMRdAF8TlU0VWpnVnNuisL7Nxbs0+oCM6q32E2692lh2qT/YuuTW1r8uOBefM2sZG2V7aIBbIKgC+BzmmWqitmPPpv2g8SSza3mCbhoO3pBNp/J24cTS/YP/n31k9tLtqB+cTWTA0Adgi7Q5RQO5tZy9utrC/aLS7Nunmkmr615CQ1ob7qLbhQ819Lw1qU5t1HJ5PIG7QwAPkfQBbqUhvbXtunVLmZqVVDLgkIuQQGdQi/ItMHE/Frers1l7MObS27R5Kx/X6adAQBBF+gyJT8YKBRcmc246u25yVW7Mb/uZpjSpoBOpRdn6tWdWKjstqYWHI3D06JK3p0AuhdBF+gStcrX3GrOjQv7aGLJzk+tuoBLEEBQ6L6s+/Rnftj9aGLZLs2s+S/scrZRoB0H6EYEXaBLKORq6P6Pzs+4SQqqdAFBVfZDrXrP1cqg+/z12Yx7DADoLgRdIOCyxZLrv3378rx94B/017JFdjND19B9XdtTv39z0X8MzLmRZJrLC6A7EHSBgCp6nt1e2rCP/HCrCq4+X8sVXS8jMRfdQvf1Wv/u7aWsnb29Yh9NLLq+dC3IpJsBCDaCLhAwWmm+kMm7Km5lR7M1m1rJWrZAFQvdTY8BTRqp7bCmx8jiumZFM50BCCqCLhAQKkxpwY3GKl3yD+SVkWEZt9MZVSugwj1O8iW3vfX7Nxb9x8qqza3lLVcg7AJBRNAFAkJvz16ZXbNfXVUv7qJ7q1YLcgDcSw8NtfJodzVtlnJzYZ0XhEAAEXSBDqdWBW308POLs/bJrWXXtgDg4Sjc6vHz4cSivXV51j1+tMUwgGAg6AIdbGWj4PoMP7ixaBML6251OZs+AFujF4tL6wW7Pr9uv/EfSxrDp3dEAHQ+gi7QibyiFTKLNjm34DZ90AFaI5MYiA88GrX+aPSethHWzmq1LbGp7gKdjaALdJKyZ1bMmq3OWGH6gi3P3LSl1Qy9uECLaO6uRvF9emfZPvNPWtypaQ28iAQ6E0EX6CTFnNnSLbPLP7T01Ht2pHTDjqUy1W8CaBVVdzWG7CfnZ9xCNaYyAJ2JoAt0AlWT1qbNbr9vdv0XZrllM69kw8VZO+qH3eF4wcIhKk5AK6m6q8kM711bsDO3llx1F0BnIegCbc0Pr6WC2fxls8kz/sdLZtkl16Or78XKORsrL9iz0duWCJUsVPlHAFpALx3Vu7uSLdrV2Yx9dmfF7aim8wB0BoIu0K68kh9qV83mLppNnzVbuGq24YfceuWypcsZO2q37Wh82VJhVooD22F5Q1MZMnZ+SmE34zZnoW8XaH8EXaAdqWKbXTabv2J2812zpZtmhY3qN+8W8n82VVi2F2J3bDy6bjFaGIBtockm6td9/+ai3fI/qq2B6i7Q3gi6QDtSyJ0599t+3HKp+o3mwuWiDW1ct6PReRuOsWEEsF00p3p+LW+/uDTnRpAp7AJoXwRdoN2s3Da786EfdD/zA+5WVnqX7ah30w6Fpi0VYYU4sF3UsZAveXb29op9eHPJbi82f7cFwO4j6ALtQu0K6sOd+sRs8bp/JF3zz9za26Kp0podDc/Yidh89RwA28ENQskV3Y6EZ++s2MXpVcsXPXc+gPZB0AV2nX9kLKxX+nC16EwhN7da/d4WlUs2XF60Y+Ep2xffsAj9usC2cmF3cd3OTa64XdUy/teEXaB9EHSB3aQjohaZLd+qzMhdvLbporOHFSlu2Ghpzp5LTFtPuMh8XWCbqZI7tZyzD28uusVqlbDL4w5oBwRdYDepXUGTFSberYRdjRRrgWRpzQ7kLtuBeMaSYfp1ge2mUWOL6wX7wA+7WqSm8Atg9xF0gd1Qq+Te/sBs8uN75+M+trLFyzl7MXTJxkKrtDAAO0QjyDRr98OJJcvkaWMAdhtBF9hpbiMIP9gq5M5d8kPuQqWy22LhsmcDpXk7HZ+xfdFM9VwA26m2k5r6dc9MLNvyRp5Zu8AuIugCO0nb+a7PVWbkzvqnjfltCbkVZQuV8nbQpuxIdN4Go/51A9h2LuxuFO3yzKpdmFq1+UzeCiVaGYDdQNAFdopCbsYPubPnze58YJZb87Po9h/8EvklO2AzdjS+ZFFaGIAdoZ7d9VzJPr697Hp2FzIFK1LZBXYcQRfYKZlZs8mP/JB7phJ6tzgj93GMlPygW7phQzGmMAA7RY807aT2qR92z95ZtsUMuxYCO42gC2w39eRqRq4bH3bDP/q1ZrLClnieDduyfSF2xVKhooWqZwPYfmpluDm/7saP3VnaoGcX2EEEXWA7lfJmq1Nmk2cqW/sWd2ur0LLFvayNl6btmeS89UWoLAE7aaNQsjvLWfvk9rJNr2QZPwbsEIIusF0UctdmzWY+q1R0H3MjiMcVKpcsXlqzU6Fbti+6aqnwLlSWgS62kS/ZxMKGW6A2t5azPAvUgG1H0AW2g9oV1hfM5i9Vgq5CbxsI+2G3PzdpRyOzNhbbsDA9DMCO0vSFC9NrdmU2YwsZRo8B242gC2yH/GplusL0pzsyWWFrynbMu2mHbNqSVHWBHaftgc9PrtjFqVU3cxfA9iHoAq2kbZDya2a3P6ps7Vtqz4OY5useDc/Ys/Hp6jkAdpIquTfm1+3jiSVb3ii4cWQAWo+gC7SKKrcKuRoftnS98vkOjhDbEv+29nordsim7GRqlfm6wA7TI05bBN9a3HAL1FTZpY0BaD2CLtAKCrnZFbO5i/7pvP/5cuW8NhYu5WzAW7AnI7dtMJoj7AI7TEXctVzRrsxk3C5qquwSdoHWIugCj80/MOXXK5MV7nxolltt+5Bbk/A2bE/+ph2NLVpPuMB8XWCHqWVho1C0T24t282FjAu+dDEArUPQBR6XJiwsXKlu66uQ20FHKf+2xst5eyl0ycbCqxahqgvsOD1lZAuefTyxbFdm1ixXZJEo0CoEXeBxqHI7fdZs5nwl5HYi/3eIFFbt2fikHYmvVM8EsNM2/LB7eXbNPptcoYUBaBGCLvCoSoXKCLG5S2brc2Ze544JCnklGy3N2OHwrO2JZ6vnAthJamNQn66mMVyeWbNiibALPC6CLvAoin4YXJ6oVHMzM22zIcTjiBXXbF95xo5G5iwZ9ujXBXaBwq02ktDuadOrbBUMPC6CLrBVqtxqa9/JM2arU/6RKVf9RucbKC3aIe+27YtlLBLiAAvsBoVbhVyF3cV1dk8DHgdBF9iqzFxljNjSjY5uV2iqXLIRW7bX41csGSpS1QV2iSq7F6dX7fp8xlayheq5ALaKoAtshRacLVytTFkI6AygsJe3nvycfaFn2oajwalWA51GTzGXptfs6mzGMjm2CgYeBUEXeFiq3mpb30XterZePTOAyp7FvKwdKt60A9Fl64twgAV2i+bqqqp7dS5jhRLtRMBWEXSBh6FZuSu3K5Xc9Xn/jGD3zIX8sJsuLNix0JTtibBFMLBbVNXV4jRVdW8vbhB2gS0i6AIPUvZDbm7FbPJjs7WZ4PXlbqps+7xJOxyatsEILQzAblG/7txazj65vWxL6wXGjgFbQNAFHiS3VtkQQuPENFasi4RKOTsambVnE9PVcwDsBjeJYSVnH99acrN2ATwcgi5wP4X1SsCdOVvZIKILxQurttebshd6Fy3GyDFg1xQ9z24ubNiN+QxhF3hIBF1gM2pRWL5tNnuxMm1B2/12oVC5aL2lJTvhXbexWNbiYcIusBvUr5stlOzaXMbuLG2wmQTwEAi6wGa0KYRGia3eqZ7RvWJe3oaLM3YqOm194RzzdYFdNLeWt5sL6zazSu888CAEXaCRyiaFDf9ocqHSttClLQt3K1usXLAn7brtDy9ZKszIMWC3eP5z1NRy1q7MrNlGvhTUkd5ASxB0gUaeH2xnz1d2PtNCNFSUPQvn1+z5xJQdja9UzwSwG9b9gDu5vGGXZlZd7y6A5gi6QL1izmx10mz6M7OswhylkruVrSc37UaOHU4GeNMMoAOsZot2YXrVZldzlme+LtAUQReo0aYQ2gxi6hOzjcXKYjTcI+Llbbw8Y0dDk9YTLdGvC+ySole25fWCnZtccR/V0gDgbgRdoCa7VNned/EGIfcBekqrtt+btuOxBYuF/BcIAHaFwu6NhXW7tbhua1met4BGBF1AtOBMC8/mLvqf5/0zqIzcV9mzAVux58M3bCiatSjzdYFdoSJuruC5LYLvLG9YkRYG4C4EXUBWp8yW/KC7sVQ9Aw8S9l8Q9BTm7PX0lI1EGXME7KbZtZzdnF93/boAfougiy5XrlRw5y9XFqFRyd2SsFewsex1OxxdsKEYY9iA3aLK7uRy1i7PrlmuWOKZDKgi6KK7qRd3/kol5Gp2LrYk5B9O46WMHbM7ti+8YDF2TQN2zUahZFMrObdzWokWBsAh6KJ7acqCRojNXvA/Lru+UzyaYW/OjoRmbF80Uz0HwE5TVXd1o+A2kljJFq3kUdcFCLroXgU/lGnCgrb4LWarZ+JRhEoFOxCasydjU5YOFxk5BuySXNGz6ZWc2yJYm0oA3Y6gi+6k6m1mwezOR2zx2yKxwprtKU3Zi72LFqeFAdg1+VLZPr29bAvreWbrousRdNGd1mbMFq6Y+eGMloVWKVuqtGZH8ldsX2zdEoRdYFeU/XCrau6NuYzNrWpcItC9CLroPtrmd+WO2fLNSp8uWiZSLlpfacmeidy0ofC6hUNUk4DdoP7cW4sbNrWy4doZgG5F0EX3UTV35bbZxnL1DLRO2SJWsIPlO3Y0umCDEapJwG5Z2SjY5FLW5pitiy5G0EUXKVf6cRev+mF3uvI1Wq9ctnBh3Z6ITtmRGP26wG7RM9y0H3Kvz2esUPJ4xkNXIuiie6hNQZVctS3k1qpnYrv0ZKftsE3bkeR69RwAO209V7Sp5azdWcqax7gxdCGCLrqE/wSv3typTyszc6lt7ICyjXqzdtSbsP5Y0cLMHAN2nJ7pVrIFOze57DaUYAgDug1BF91Bu54t3ay0LCjwYkfEvaztsVl7NjZpMStWzwWwk7QYbXY1b3eWNizrh12gmxB0EXwaH7axVNkBrbBe+Ro7w/9v3etl7ETolh2Kr1oqzEEW2Gmq4irgXp3N2Gq2SFUXXYWgi+BTNVeV3OUbZh5VxZ0W8gqWzi/aS4kpG42uW4SRY8COq40bW8jkLc+4MXQRgi6CLzNjtqSQy5P7bgmXizaycdUORxZsKMZOdMBO08tLTV6YWFy3uQztW+geBF0Em/pxNTd3dap6BnZLqFyy4zZhh0IzjBwDdsmd5Q2bWcm50At0A4Iugk0hV6dCtnoGdlNPacWOhmfseGyxeg6AnbSRL9nsas6dgG5A0EVwaW7u8i2zzJz/BX2h7SDkFW20vGgnItM2FsuxRTCww7QQbW4t5/p1iyUefwg+gi6CSZMVcqtmq5P+x5XqmWgH0WLGRksz9mxy1tLhkjFeF9hZmqs7tZK15Y2CeYxgQMARdBFMmq4wd9EPucuV0Iu2kvLW7Ej+ku2LZSwZYeQYsJOUbVf8kHt5epWqLgKPoIvgUbDNb5gtXvM/Zqpnop2E/L9RwtuwlyJXbCS0RgsDsMPW8yW7sbjuAm+RrYERYARdBI/m5q7cqmwSUWJubrsKl0s2VJyzJ2Kztie6Xj0XwE7QXF1tHnFjYd0PvTxPIrgIuggWvSen3tz5y/4zeV5nVM5HGypbuJS1w6FpOxJdsL4IB1tgJ6lt4dpcxlY2ivTqIrAIuggWhduNBbPlicrUBbS9VH7eDpgfduMr7JoG7CCF27nVnC1kcm6LYCCICLoIlvX5SsgtafctQlOnGC3N2rHyTRuIlizMGAZgx+hZcnI567YGBoKIoIvgUAVXm0Ms366egU6hLYI1X/e1+HVLGFsEAztpejln82t517cLBA1BF8GhloWMH3Rza9Uz0DHKZUuUN2yfN2lPJhetL0LYBXbKRqHkKrpL61R1ETwEXQSDFlKokpuZ9T+n16wTade0RHHFnozcsj3RNUuEmX8M7AT16iroahMJIGgIuuh8CrlF/wla2/2uL1bPRCfSyLHB3G07EpmzkWiWXdOAHbK0UbDp5awVSmVWNyBQCLrofOWi/yx9wyy7ZObxlnfH81+4HPdu2qHQjMUjVHWBnZAven7YLdrMStY8enURIARddD4tQlu4zi5oARItbdix8Iw9E5+pngNgu63lim6uLjulIUgIuuhsCrnaIEKL0Eq56pnoeGXP+r0lO2xTdjSZsSjzdYFtlyuU3KixtWyBCQwIDIIuOpt6czVSTNVcNogIlEgpa0PevD0ZvWN9kTybSQDbTJXcVT/kTq9kLVfk+RTBQNBFZyusmy3dJOQGVNJbt/3563Y4umLpMFsEA9tNldzr8+u2luM5FcFA0EVny/tBVzuhaUEagqdctng5Z69EL9lIeNXCVHWBbaWge2dJ7QtF2hcQCARddK78WmXL38KGC0QIppDCbn7Jno1P2eH4avVcANtBz6TFkmfzmZyt5iggoPMRdNG5NpbM1qbdwiUEWdltJrGnNG2Hw3M2GmP3JmA7KezOruZsZYNxjeh8BF10JoXbjcXKtAV0hXhx1faXZ+xIdMHiYY/NJIBtpJ3SlteZvoDOR9BFZyrmKhVdndA1hrwFO+JN2HgsS78usI3Uo7u8UbBsgUVp6GwEXXSmzKxZdpG2hW7jFW3Eluz1+FVLGG+rAttFLyMVdGfXmE+OzkbQRWdSby7V3K4U8XI2kJ+xV3pmbSjKQRjYLksKuqs8xtDZCLroMOXKJhGZucqOaOg6obJncW/djno3bX90xXoivLUKbIf1fNEWM3nXvsBgG3Qqgi46i+dVRopll81KrL7vVgq7vYU5OxqatvHIGrumAdugWCrbWq5o82t580i66FAEXXSWcslscaKyIxq6m3/gPVS+Y4fD09YboV8X2A7r+ZLdWlpn+gI6FkEXncUrmi3fIOjCCRVzdiw8a88npqvnAGiljULJ7ZRG0EWnIuiic6hVITNf6c1V4AWsbIniiu31puyZnhWLhZjCAbSSAq5GjS2s5y1f4vGFzkPQRecoZM1WJyuBl34xVIW9gvWXluxk+YYNR3N+2OW+AbSKnmoVcDV9IVcg6KLzEHTROYoblaDrscoed4t7WRsrTtqJ2Kz1RnLsmga0kOeVbWY1a7kiz73oPARddIhydazYrP8pVQU0KlusnLdnQ9dtb3jZEmEOyECrqD13blVjxjy3kQTQSQi66Aylgll+3T+tEXTRnH+/iOSX7fnElB2Jr1TPBPC4NFpsJVtwc3WL9OmiwxB00RnymcpOaPTm4n78+0d/btoOh2bsQCJbPRPA49JT79J6wTI53i1BZyHoojMo6GYXq18Am4t6WdvjzdjR8JSlIh79ukCLLK7n3QYSQCch6KIz5NYqFV3gIfR5K3bAm7IjsSWLMnIMaAlVdNdybM6CzkLQRftz8238oKttf4GHUS7ZkC3bS9Eb1h/OskUw0ALq01XrAptHoJMQdNH+ChuV1oVirnoG8GDhUt568zP2hd4ZN18XwOMplsqudWGV9gV0EIIu2p96c/Or/idUEbAVZYt4eduXu2aHIos2EOXgDDwu7ZK2tJ6vfgW0P4Iu2t+Ggu5a9Qvg4YX8sJsortqx0B3bF1a/Li+WgMehiq56dYFOQdBF+9MitFym+gWwdWPenB0Jz9h4dL16DoBHoVm6y37Q1WxdoBMQdNHeyqXKIrQCAQWPLlTK2cHwrD0dn7ZEmJFjwKPS7miq6uaLHmPN0REIumhf2gFtoxpyPfor8XjihRXbU5q053uWLeaHXQCPRiF3eYOqLjoDQRftS0E3M8u0BbSGf1Du8VbtWPGyjUc3LE7YBR5JvuS5Pl1yLjoBQRftyysRdNFSEa9gA6UFeyZ62wbDG7QwAI+g4IJunoouOgJBF+1L/bkKuiWCLlqlbNFy3o6Wb9nhyKL1RxiTBGxVoVS2JVoX0CEIumhPegItFczWF/2PhBG0kH/fChfW7MnYlB2NM3IM2CpVdNWjyw5p6AQEXbQnhVuNFfP8sEvVANugNzdlB23aDiU3qucAeBgKuNl8ybJFtgNG+yPooj0p4GqsmBakAdsg5N+3xr1ZO1aesN5oiX5dYAtKfr7VPF1Vd4F2RtBFeyoVzXIrBF1sq6S3bvvKs/ZUfNpioVL1XAAPov5cTV5Qvy7Qzgi6aE9UdLET/PtXb3nNTocmbF9szRJhwi7wMFzQ3Si4UWNAOyPooj1pIVpWFV2qBdheYS9v6fyCvZycttFo1sIsTgMeSE/NGjFWKBJ00d4IumhPquiqdcF4EsX2i5SLNp69YociCzYYZRc+4EFU0dXkBXp00e4Iumg/2u63kDMrZqnoYoeULezf707YLTsYnrNYmPsdcD96as4Xy7ZRKBF20dYIumg/xbwfdNf9Z1KePLGTytZXWrKj4Rk7EluqngdgM6rqZgm6aHMEXbQfVXILmeoXwM4JeQUbL8/bqei0Dcfy9OsCD5AteK6yC7Qrgi7aTzFnll+vfgHsrFhxzcaK0/ZMasGSIY/5usB9qKLL5AW0M4Iu2k/JD7oFdqvC7kl7a3Ysf9H2xNYtEeYgDmxGPbp5Ji+gjRF00X60/S9BF7soVC5Z0svYS9FrNhxes5Dx1izQTKV1gaCL9kXQRftR60KRoIvdFfGKNlaatpOxORuLcX8EmqF1Ae2OoIv2Q0UXbaFsYf8F19HQtB2JLlpPhF3TgEZMXUC7I+iivWikmCq66tMF2kBPftYO2rQdiq9ZmJVpwF1yxUrrAs09aFcEXbSXQrZS0WWjCLSRsdKsHfduWG+kyJMmUKfklV3QZStgtCues9Fe1JuroAu0kUg5b2O2YK8mJyweYotgoJ5aF9TCALQjgi7ai3pztTMa0E7KZUuV1+2Qd8dOJpesJ0LYBWpU0dX0BaAdEXTRXtSf6xWqXwDtI+QVLVlYtqcit208krE483UBR1MXqOiiXXV90C2VSpbL5Wxtbc1WVlbuOq2vr5vnteZgVruebDZrq6ur91yXTroNGxsbVigUWnK9ugxdlq4zk8ncc326Hbo+3S7dvrbghwnzeMJEewqXizaam7DDkTkbiubYNQ3wFUuVPt12VS6XrVgsumOdjoXNjsE63uv7OmYiWEL+HaCrV/3MzMzY+fPn7eLFi7a0tFQ9t+Lw4cP2ne98x3p7ey0cfrzXBLdv37abN2+6B9nZs2ebPpgGBwdt//79dujQIdu3b58NDw8/1vXq95mennbXPTExYfPz83cF6Gg0ak888YQNDAzY0aNH7cCBA9Xv7KLps/7pU7OVO9UzgPZTiPXbGe+YnSkcsrx3/8fo7asX7J0f/Ln96L/+F/f1qRdet2/+8T+3F7/2e+5roNPt6U/aU/v6/FN/9Zz2ouPu7Oys3blzx27cuGFzc3Mu1NY7duyYjY2N2d69e91xEcHRlUFXYU+VTIVbnaamplw1tTF86o7//e9/3/r6+h4pcOoV5K1bt1ywnZycdNep8/RqslnFNhaLWSqVcqd0Ou3C7lNPPWV79uyxeDxe/an70+Xqlamu8/r16y7s6np1yufz7pVtjX4nhXgF3tr1PfPMM3bw4EF33q6YPFMJu2vT1TOANhSK2Hx0j12wI3ZmY6x6ZnMEXQTdWF/CTu/ts+cODFTP2X061umYrmP8lStXXFGrdixUyG08Bvf09LjjbDKZdEUmHQuPHDnizkdni/x7X/XzrrC8vGzXrl2zjz/+2D0AVO1UyG0WPIeGhuzJJ5+0RCJhodDW3qTUZV6+fNnOnDljly5dctXU2gNss9cWug21t1b0Vopuqz6PRCIukCoI34+CrAL1hx9+6KrU+t10GWpdaNaaoNuh69Ptql2fPtfvq+D7oOvbFqrkZmbMCuvVM4B2VHbTF6L+699MuM8yXtQ/p/lzxOrivN26cs6unf3QfT2y96Ade+oF23vkpPsa6HTJWMSG0nHbN5CsnrO7VFDS8eyjjz6yzz77zL2bWjsG63vNjsG1Nj8duxcXF92xt1Z8UvhF53q89+M7hO7UuoMrBJ47d87ee+89e/fdd93b+bpjt5quS5f9m9/8xi5cuOAeMFul0KsHqh6kCuUKrfejB68q0/pZ/X76XMF3K3Q7dXsVlFWJ1u+x4+jRRYeIljZsuDRrT8amrTdSsHCoq7vA0MU0S7fon9qBijp6J1Pvauo4r3c2t3oM1vH06tWrrlClarDehUXnCnTQVcDVHVav0NSX84tf/MLeeustV9HdTgqZn376qXuA6fprVBVWS4BeIaodor+/3530ud4eUSVV1dt6+ve6vbq8ZlXnGj0Q9cDWK1i9Mq1/xaoWBV22qsK169XnepumsVKtf6twrcvRC4Nmr3y3lYJumaCLzpDyMna4cNX2R9csGeZ+i+6koFtqk22A1bqnkKpjfeO7tTre6bin423tWKiPqtg2a0/UsVdhV5d3v+Mv2lugWxf0trwqk7/61a/s17/+tVuYpfMe1qO2LqhtQA+Oxp5fBVwtcPvyl79sX/3qV+2LX/yivfLKK/byyy/b8ePHXbtA7a2TenqFqn+rRWp6QDa7Laoe63ob/61osdmLL75ob775pn3pS1+yV1991U6ePOke2OpbatbWoFfAejIYHx9/6P7glli87j9Tzfm/NLN00Rki5tl4PGezpV5b9ZL3tDDQuoCgi0RCNpCO2ZGR3e9nVcvgBx984NoPGgs1akVQ7+3Xv/51+8pXvmKvvfaavfDCC+64Wmvda6Rjsi5Hx279+61kAbSHQFd09faFXonpjq8AqOpo4x1fd/BWBjldT60vtp6CqsLst771LRcy1eyuqmqtyqqFYC+99JJ70GnyQj3d5lrrRWMo1atMhVW1Suj3bfz9asFagVqhVdel69QCNwXe3/u933PnN9Ltr02K2FG0LqDDhMqepfML9nRixg7Gt96mBHQ617pQ2uF3/5pQuFVxS8fExmOhjrkKt6+//rpbcK0CkI6F+vjcc8/ZN7/5TXdsbqQWQE1sUFtf/Tu06ByBDrqqxOqkKm79nV6vyBRwT5w44cJlY7B8HAq5qoY2vs2hB5MqsrouPbjqWxR0e3Q79UBU4B0ZGal+57f0AFPYbXzwqmqsIK9G+8YKsi5PD9zTp0+7z9U2UXs1qlemo6OjrmJ96tQpV72up9uvB7cC9I4+uGldQMcpW8jL215vyg5pvm6MOZzoLu3So6uQq4JQ4zu3KvBohOazzz7rijz174zqnU2N9lQe0LFS48Xq6Zir1kAdZ2vVXXSWQAdd9d8oOCpk1vpvVFmtje3S2xZ6S193/FbRA6wxcIqqxrruB1EYbTbtQLe/8Xw94PRqs1axbqTRKBqRpt+/GT3Q1Z6gmYEK4I09SrpMhd3NxqFtCyq66FDaNW1/edqORBctFtpsBgMQPJ5/LFLY3c0MqGOUCjOakdtI71rqOKciUuNxrkbHZx0zFXgbf0bHdbU+6l3TZsd3tLdAB11VTRXyFPZUMdUdWW/lv/HGG/a9733PVTNbPSNPYbTZDFpVefW2SrN+2BoFVzXSN1vhqctVcK9/AOqydLl6m6bxFax+dz1oNQD7QfQzqug2LoTT5SvsanHd/W53S7mKLk3/6Eyj3oIdLU/YcCzLFAZ0DQVctyBtl5Kujp16x1PvbDYWfXRcUzFL76g+iPKCflbH21rFVxSiVc3VsbCxLRHtL9BBV9QmoLcjdCf/9re/7XY6285dT7SgTKG6kUKupjA067OtUchVX6zefqmn4Ky3XvSWSn0Y1QOu2eXpZ1S1VrtCs9vSSNenV6vNWhRUMW7cUW3bKODWTkAn8l+ojdqSfTFxw83ZBbqFqrqForcrVV0dA3UsbBZCdRxUMUfH5gdRNVgTmnTca2xR0DFQx8Ktju3E7gt80FXQU+P5N77xDdeLqqpos9aAVtHl64GlYFpPDxK9Gvzxj398z2xdPaD09fvvv+++11id1YNUVWlVpOtfZW4WQhV0FYobf76eQu3CwoK7PW+//bYL2I0PbNF16Oe2P+j61001Fx2vbNFS1oYLU/ZCet4GohwU0R10+Cj4x4mynst3WC2ENh47RWtRdFze7FhYO/5qMtPPfvYzt8FTs2OhrkPHQoJu5wl80NVb/Qp8zRaBbQeF6AMHDrjG90Z6takpBgq0GmStubfqKdJJI9D0tV5R1ofKWruFJjY06xtqFkL1c2pF2CzQ1xrrFXA/+eQTF3JVTW5G/UjaNa3ZA7+ldPGlAkEXHS9ULlm8lLHj3k3bF1m1VISecwSfnsJV1d0N9wuhOu7rONqMjsm1469mx6uaq+NdMzoG6nv06HaewAfd3aAeH7VLqBLbGE5VSdVOK3r1qLCreX861eb81toH9OpTD1A1xqsS3azXVg84Ncc3Bt3av20Muvo5LS7T1se6TgVutVTcb6qCvqcQ3Hgdrec/QXoKurvzRAm0UtgPuwOFaTsSnrGxyDpPtOgCu7cYTcenzRaKNWsnrP28xo/Wjr937txpWhGu0b/RsXDH1qugZUL+q5SuThZqXNeOaQqdjdQu8P3vf9+1ITQG1gfRKz+1Ifzyl790FVQ9OB72P7WuSw9OhVzNwN1sKoR2bfkf/+N/3DMVQQvs/viP/9i1bOgBruvVE4B+Tr+nbpfGoNUoGKvSrettfEVcqw7/y3/5L114rqcQ3LK7jyq56wtmV3/q/8e7/3bHQKcoR9P2d1cK9r/8Xx/Y//Vf/3d33snnX7Ovf///bi9+9dvuayAI9g0k7SunRm0wHbPwJm0Cj6J2bLoftR786Z/+qSsWNYbd7373u26TiNrxS8ctHfdrO4mq+FNP16d1MToW1h/fdJxU8egf/+N/3HTeLtoXQXebgq6Cp14d6q0Q7VqmBV8Pu1pT1VuNPqtNhdis3eJ+Qfef/JN/4vp09cDU76hXru+8887nb+/U/7x+Rr+rwrUe+I3U3/Rv/s2/uavvWE8WasPQSteWvMKtBd3bv/Gfte5+4gE6ln9w/PTOuv2PX16w//Ovf+jOOnz6OXvtzT+0J195w30NBMFYX8JePjxk/UnNa6+e+ZgUOLWwWseeZtOMau4XdP/wD//Qnn76ade+oOOWjsnvvfeea1nQ8av+WKjr0CgyBVllgsYKr8LuP/2n/3RbF7Sj9Qi62xR0Rf9pFW7VKvDhhx+6qQsPQw9I9fnWdnDZrL/ofkFXD0ZVgrUS9bPPPnM/q5BbX4VVgFYY1pOAPmpM2Q9+8AP3vXr6/f/tv/23dwVdve3zH/7Df3DbDtcvrHss2vY3u1z5CATEWq5k04trdmd63n2d6umzgdE91jtw9yYtQCeLR8M2kIpZNNy6aq6KLH/yJ39iX/jCF+7Z1Kje/YLuH/3RH7m5+Qq1H3/8sSv6qIqrY3N9/FGBSW2CWl+jQPsXf/EXTdeu/LN/9s8Iuh2GoLuNQVehUg8qndSX2/gWyWb0IFPLgebg6oGn29Fst7TNgq4qs7//+7/vHvAK1zrVtyqI3sbR5esBq4+q6qql4a/+6q+qP/FbzYKufhdVjVWt3qx5HwCAR6UJRv/pP/0nNxp0sxY+uV/Q1bb7CsnqwVXRSetSGqu4OgaqiqtF35qlq0XhurxmRRyCbuch6G5D0NV/Ur0S1ANLTe5qW9CryXoKmgqzelDeLyhqWsTzzz/vqq56dVtvs6CrXdjUk6RxZo1z/3SdeiBrrrD291bFWA903b5z587dE3QVuvUk8a/+1b+6q0dXTwT/+l//a9fIr+tvCd0VNWLMfvu7AJ0t5LZGzRdLVshXDsDRSMTi6gPcpCUJ6EQhHSN1n25V34JPx57/+B//o7355ptNF2TX3C/oKpTqvMY5uyru6JimVoUXXnjBhV29G6qf1eU0Bl0dC3WsVI+uClDoHATdbQi6ejCpgvvTn/70rjm3eqDochRE1X+rB64qrWqKVxhVBbg+sNaojUFbFb/88st39esq6CqY6jKa/bt6um49sGvBWVMh9KCuUdBVi8Nf//VfV8+p0L9RW4Oqt/U/r+vUE5BeIW82mmxr/LthyQ+56/NmRXaeQecr+4+5gv94X9zwD7KzSzZ9u/KOzqB/cD2kIfZ175AAnS6USFhkcNBC6qVtUdjVsfff/bt/Z6+88ooN+pe9GQXSP/uzP3PFncYF1c3ouKb5ujoO6riqwFs7xuvf63J0efVBV99XsUm7qioboHMQdLch6Cr8qdldYbc+gOrBpbdivvrVr37ee6v//LoNun61DjSr7irc6tWmXtUqdNbCrprp//7v/95Vjh+0IEzh+qWXXnIhVwFbt0Xht0Y9t5qp+6Mf/ah6TkUymXS3VVMc6neW0e+l27pZON86/26YW/PT+8+YuoCOV7aQbcTT9lm61967NmE//du37Kd/9lP3vZeffdL++ZffsO888bT7GgiC6Pi4pb/wBT/sDrQs6Oq4qxCq49f9jsEqtvzN3/yNa9N7mMKL3vHUsVD9uDoW1l+2/r0uR5dXf1k67qqF8A/+4A/c8Ridg6Db4qCrwKiQq7f069sV9CBRNfVLX/qSe5Ao5NYuU0FRlV9NMfj0009dpbaRArKqulqgVpsJqFedP//5z91OLo1v19ToCULhWA9qbTyhV8U6r5HCshbM6bbXUxVXvUvaOnmzRXEtobth3n/1fOkH/n/Em9Uzgc6Ti8ZtNjVgl8Mlm/WP9xcu3bRf/OVb9vf/29+77z/zypP2//r2d+3/9uwrFlprxbshwO6L7ttnPW+8YVEF3Yc8XraK3kX9yU9+4trvNmsFVNuBKrI6jirgquDT7JimY7iOw2+99dZdrQ769zqGquCkd1nROXb23tgF1AekU2NPrgKmgrOa3VUZrQ/O+lwPOr2NopOCaSO9slQQrq/c6oGnV7v1ldl6Csd65apwrFWnuo5mIVd0+c2eIPTzuu0PG/QfS1iV6tZUAoCd5oXCthhP29VUn52LhGwiVLbVcslKDbv9Ff3z53vLNjPkP6ai9OkiQHbp6VvHQB0LdUxsRsUqFWw0l15rU1R02qxwo9aFzXYc1bFQFWB0FoJui6nKqleEjdQPpEquWgE2C6Z6oNbCcKNmDz494O4XQvXqU/1HCruqzG52vbpMLShrdrtVPdZt3/agq5umoNuit7yAnaI2hUIkZvPxhF1Lpu18PGY3y1nL+yF3s33/F1JFuzVYsvX+hJVbOI4J2C166nYL0nZBLYRuVsipLTh79dVX3QK3zQKx3uBWFVdThRrbAXUdOhbW3lFF5yDotpgCY2M1VxRiVWF9EPUAaUB2I4VRtSfUd5ooNOtn9aBtFmL1qvVhrlMPbIVonerpMvWqV9dRvwhue+hZsnWLGICd4BacRaI2n+y1M+l++yxStoXig9sRCiHPFtOe3T6YtGKCF3gIAN2HdZzYhfuyjk86Tul41exYqONgs+NqIxWUVPDR1IX6opIuU4UlXYaOu+gsBN0OplevCsbqO2r2ClW9vqowP4jGn+nntLCsnqrAanfQk8S2V3RF1xHiLonOkYkl7eLAHns7FrLb5Zzl3Xi8h5MJF+16cs0y+4eslGpeiQI6hv/cHd6kUrrddHzScUqjM5tVXHV8a7b2pZHGZqpFsLGopGOtjoWq6G5WNUb7IlW0mF71Nat+ahyXdh57EFVVm4XTZm0KepWpB51aHepHf9XoAasHd7OWBNErVr1Fo8Z7LUZrXJeoEK2m+x0JuTUKuoRdtLliOGq30wP2cbrPzpc3XC9usext2qrQjH52I1yys4MZW+n3nzPi9P6hc4XCIQupf3UXKrqi45SOV83exdRx7vLly+5jfaW2no6Tmpikxd2Nx0IdX3Wc1fG2WcUY7Y1E0WJqem/W5K4HmObUaoSYJizUT0nQg0rz+hRMNVNXY8ka6TLVitAYohWANbxar2QbA6kuUw9uTYDQ/t71PUdqr1AI1oYWGqVSPy9QdH160tDGEjsqpLe+uFuiPalVYS3RY9dSabvgP/ZuhMu27BVM3biPwguVbS6eszvDIVvp8+/79OuiEyn8aY3FThZFmtDxSjuoNR4n1Z6ncZyarqQgWz82TMfF27dvu6lDOj437iKqcKseXx1nN+vtRXuL/Htf9fNA0h1ab80rXOpU60WtnfRWhR4A+thIvTjqrVXfbeO/00nfb3wbY7N+11wu56Ya6EGkn1HQ1Of6OV23bqNeTdZeddZTgNVbJhoRpo/1D2K9utQUB12OLk/XU0/j0/Q9XafoVau+1gNbwVvBurGnWNenhXPajW3Hg+7CVT+FL/qJ4v5zgYGdVvAP5MvxlE0k0nYpFrFpP97m/JD7ICsLKzZxYcKunKm8gB3dP2rHnz9u+47/tmcwHw9bvBy2vlzYInnu++gw/jEpMjxsiSYLqXeSjsk65usYVx9mRcdGvauqY6Gquiru6Od0vNVYMh0LlRHq6Vio4KypRZqI1FhMQmcI/BxdVS2bbZPbCs32vNaD51e/+pV75bjZbNutUJBVlVg7qWl+32ZvnSi4agau2hAae223Qg9kXd/v/u7vunEsO954f/mHZnOX2B0NbUNV3KJ/Woj32MW+YbtWWLHCFl6I3bp0y375V7/8fI7u6VdP25v/05v28psvu69r9hbSdnwhauPXV9RXVD0XaH+heMzix45Z79e/Xj1n96hwpOPg22+/7Y6FjxpxdJxVy8Jrr73mpjU0aw9EZ+DlSYupuqq3ODTSqxV0ec8++6ybhXu//iDN3tXPNQbvrVDI1cI2hVwN1N6VMSquR5e3b9E+srGkXe4dtl/7B7prhWUrbtO7DbPRDbvRl7PC+KCVIzw1o4OEIxZqsjZlN6hHV4Uh7QSq1r5HoeOs/q2Ouzqu1u8Kis7Ds2mL6QGitzo0v/YrX/mK+/xRHmzqBVLY1HbBmv+nHtzNQq6onUE9tXrlqVegevW5lbdZ1KKhkKyqsa5XD+z7Xd+2oUcXbUIbQMz0jtjHqZSdD3u26OWt4BacbY9SqGwLiaKdH81bMR33H9Q8DtAZ3PzcNgm6Ou4p7OoYrA0iNC2h2QLxzajAo23vdSxUy8KDjr1of4Hv0VVP6vnz5918vFZ3aWiHFU0maKSQqqCoKQmqkKoVQCc9gNQ+sVlrgR6c6sFVYFU/kF6VaqWnBlw/zANVgVrXqwemTvpcJ92exn4lXZ6+pwVu2lhCVWhdnzas0EK0XetFWpow21jwj/r56hnAzlKrwno0YbfTfXbFf+zc8kPuit27w9nDepge3RrPf9hlo2VLh+OW2PAsWgx0ZxkCIpRMWHRk1GL+sasd1I5vOu7qGKxCjo5rOulYWJ8FFGJ1bFZRSmtSTpw44Y6FOiZuNroTnSXwPboa1fXOO+/cc+duhW984xsulD7I4uKiC9xqdFczvBaNNesXVuhUqFVA1ucKro/zSlJbEavZXterBXf19ODVg18PbL3i1XXqSWDX3fil2ex5/2h/98pXYCdobNiq/9iYjCftarLH5oprfsB9vOeNh+3RrQlbyEZLKXtiwrOhhbxFco/ecw/shMjggMVPnrT0y83v07tNx0Ede7VW5+rVq3cVm3SMrRV91AKogpOOjQiOwAdddJhbvzabOWe2fvfUCmC7lcIRW0z02uVEwq6F/btgqTULIrcadGueXB+wg5MF653NaAZh9Vyg/biJC0+cstTzz1fPAdoHTWBoL9GU/6zJzjPYWUU/5F4b2GO/TsTskuVto3T3mL7dcDW1apODZSv3sdob7S0Ui1p4NxYvAw+BoIv2EksSdLFjVMWdT/TYR/0jdtYPuPNWtPwWdzjbLvmQZ5N9Jbs54t8WP0gYC2LQprQjWqhhpjzQLgi6aC9UdLFDNvwXVbeSPXY+kbCrkZDNewUXctvJSqxoUwOeLY2m3EI1oB2Fon7QpaKLNsVTJ9pLzA+6UZ4wsX00NmylusPZhXjCrkTMVosbbVHFbVQM+SE3UbJb42HL9ySYr4u25Cq6BF20KZ410V6o6GKblC1kJT/kZqIxu9A/Zh/GwjZRzlnBa++pBhvhot1MZmx5f58VU/5jgxYGtBmCLtoZQRftJeY/WSrocjBHixWicbudHrC3+4ftYnHV1r3H36J7pxTCnp3pX7algYhZgheCaC9uMRo9umhTBF20F+2M5gcSqrpopcXUgJ1L99rH0ZDNejnLlT3bvj3OWk+3dCNSsolRs/kB/2l7tzZ0ARpFwpWKLhsroE3xbIn2E0lUWhiAx6BWhUI46qq4F+Nxu+q/hpoNlSzvFf3vdU7IrdFtnk0VbHYobBsDyeq5wO4KxeLalpMXX2hb3DPRflTN1Zgx4BFpbFjGPwDfTqTsXKrXLodLtuAVzOvwjRc2QkWb7Svb3GjUykn/cUKLD3ZZOBF3FV2gXRF00X4UdKno4hFpwdma/0Lpeqrf3k332M3immXbfMHZVsxHs3azL2/ZsT6mMGDXaREaQRftjGdJtB+NF9OYMeARTPYO24fpXjsTLth6qT3Hhj2upXjRzoyuW6FXizcj1XOBnRdKJtksAm2NoIv2Q+sCtkizcdf9+8wn/WP2aTRkd8p5y2rBWYe3KmymGCq7sDuxL2YbaT/o0sKAXRJOp9n+F22NoIv2Q+sCtiAXjdtMssfOJVJ2ORq26XLRNsql6neDSVXqfNizif6CLQ/FK/N1gV2goMsMXbQzgi7aj8aL0bqABwpZJpawyUTaLvkh97N42BZLWSsGPOTWaDzaUjhrU8NhWx2M+Y8bxjthh4UIumh/BF20H1fRVesCb8eiOS8Uslw4Ytd7hu1MMmkXy1nLlwqB7Md9kBupNbsz4Fmh339xSAsDdlI4XGldoEcXbYygi/YT8u+WkVilT5cDNxoUw1FbSvbZrwZH7Wwob4vFjep3upOi/WRfya6OlvzHjP+44TGDneDfz1w1lxm6aHPcO9Gewgq6Pf4nHLTxW6vxtF3tGbT34hG7Uy5Yply0UhdWcRttRIo211u22f0p8yI8ZrD9Qqrm9vYyWgxtj6CL9qSKbnJAz6bVM9DNvFDEZpK9diWZtouaqhAq20YANoBoFYX9lXjRbg6VLDuYtnKMkWPYZqGQRfr62PoXbY8UgfakoJsaJOh2OY0Ny0bjNh1P2sVUjwu5017OD7he9SdQkwuVbCqetek9Mcv1xHk7GdtLFV0/6LIIEu2OZ0K0Jy1ISw8TdLuYFpwp5E6mBuyd3j67Us7bailX/S6aKYQ9O9u/ZosDEfO0RTCwXWoVXVoX0OZIEWhPCrqpEYJuF1tI9tunvcP2brhoy6WslbpkbNjjKvn/uz5WtpmhkP844vGD7aEe3Uh/P60LaHs8C6I9hf0nz3hPZZ5uiH7DblG2kBWicbvcO2SfJOJ2rZyzdfP8kKupsXgY+u+0GM3b3FDE1kbSlTOBVvJDbiiZsHBPD0EXbY+gi/akEUnq000M+B95Iu0GlbFhvXYhmbKLsajdDnm2Vu7O2biPKx8q2Wy6aFPDIfN6ma+L1lK7Qrivn3F26AgEXbQvtS2oT1dtDAi0rP+iZjaRsit+yP0kHrNpP+DmvEL1u3gUy5G83e7J28JYwrx4hECClgnF4xYdHnbtC0C7416K9vV50GV7yaAq++ErH47YZKrfPu4ZsDPlrK2X8kxVaBGNHPt0ZMOyvXErR3m6R2uE/BejkeEh18IAtDvupWhfehJV0I1S0Q0ihdxMvNfO9I3Yh7GwTRXXqt9Bq2i+biZasmuH4pZJq6pb/QbwGEKxuEWGhqjooiNwL0X7UkU3NeQHXW0FzF01SDQ2bKJ3xH6TiNn1UMlWykUrUsXdFsVQ2W4nNmxpLGmFvlT1XOAR+eE2nEy6iQu0w6ATkB7Qxvwn0WjCLNFb+YiOpw0gluIpu5bqtfPRsN0Ml21V2/gyOmzbaDHferhgtwZKtjAQsXKCd0jw6EKJ6rQFFqKhQxB00eb8J9LkYGXUGDqWGxsWidl8PGFXUz12Ph63CS9rBT/gMlVhZ0zHN+yOH3bXBvygGyag4NGE02kL9/dVvwLaH0EX7Y+g29EUcouRiM2n+u2jnn47Gy7bQnG9+l3sFL2cmO4t2fWRknkJqnF4NOFUyiIaLQZ0CIIu2l9KQbe3+gU6TSaWtPMDe+2X0bJNejkreMXqd7DTcqGSLfT4f4dDvVaKEHSxdaroRqjoooMQdNH+Ev6TqoKudktDx1Crwq20xob12sVy1pbLJSu4Hc5oVdgt+m+/Fi3a9b4NWx/vq1R2gYcVibj+3HAvhQd0DoIu2p82jFDrQpztTDuBxoatJXrsejJtF+Nxu+E/yyx5eWMT3/ZQCHm2GMvbjdGyrff6Lx6jbLGNhxPuVcjtcRtGAJ2CoIvOoMkL6tVFWyuEI7bovyC5nuyxz+Ixu2klWy/lqt9Fu9DIsWs96zY7GLZcmn5dPBzNzg330baAzkLQRWdQ64Jm6qItuQVnobALuZ8MjNn7obzNeXnGhrWxknk2MWou7Jap6uIhRP2gG6FtAR2GoIvOkBgwS/tHZY0bQ9vZiKfsYu+Q/Tqdshv5ZT/gsvlDJ1gOZ21uOGKre5hqggcIhy0yOGThHoIuOgtBF51B2wAn/bCr9gV2SWsbJf9vMd07Yp8kU3YhUrZ5r1CdjYtOoL/UdCJnNweKVhrqc2EGuIcLuQN+yE1biOo/OgzPaugMCrdakNa/1/+cJ9rdVvb/Hplowm6kB+xCLGrX/JC76MemIq0KHWcjXLSZVMFujYaslIj6RwXeNcHdQn7QjY6Ouq1/6edGpyHoonPEUmYDB/17LUF3NxXDUVuOJexmMm2fpdJ2tZyzjFe0cpk6bqdai5XsymDWlgfjVorx+EKDSMSi4+Nu+1+g0xB00TkUdPv2V8aNUVXYFWpVWE722rl0v30Qj9p0YZV+3ADQ6LdMxLPrB6KW6fGDLlVd1AnVgq4qukCHIeiic6h9IeY/0faO+2GXysJOK4SjdnVwr/06EbMrlrNcKV/9DoLAC3k2GV2zhT0pyw0wsxoVoVjMwgP9bkc0BV6g0xB00Vm0O5raF2IciHdKyf9vPp/stTN9Q3bOCjZXLlqOHc4CR39NbSZxvTdrM4P+12mqd/CDbiJRqeZG2ZkSnYmgi86i/tz+A9Vd0nh7dbutx1J2O5m2C/G4XY2E3WzcPAvOAm05mrfJfs/mh/zHmv83R3cLp5IW27fP9ekCnYhnMXQWTVxID5sl+vwnXvbp3y5eKGyrsaTd8kPu+UTCLvn/2VdLG1Rxu4D+wvOpok0MeZbtS1iZft2upVFi4d5ei46NuckLQCfinovOo/aFnlGzZH/1DLROyC04y/gvIs4N7LEPoyGb8HJW9IrV76Mb5EIlW0iXbepg2kox/zBB1u1KoXS6su1vKuV/wZ0AnYmgi87UM17ZQAItlYvG7VZ60N7uH7JLxVVb9wrV76DbZCIFu5Jas/V9g+Yl49Vz0U0i/QNufi7QyQi66EzpkeouafSNtcpCasDOp3vt06jZbDlvuXLJjZ1Cd9Lffj1StHNDWVvp8+8UMVqFuop2Qxsg6KLzEXTRmTRTVxXdBPuuP45yKGSFSNRup/vtUkILzkI2EypZXhtAEHK7XilUtplE1qaGQ7bW57+o5O3rrhHu6als+5tmwg06G0EXnUkzdVODZj1j1TOwVaVwxDLRuN2Jp+xsus8uhTxb8PLmscMZ6ijs3hnwbHYwbMUUVd1uERkZtvDAgKvsAp2MezA6l1oXtHkEtswLhWwtlrJr6QH7ZTpttwprlqMfF5tYCedsbihiK+M9VHW7gf83jo6OWaSfBb/ofARddK54b6VX1+2SxsH3YZX9/1a3e0fto3SPfRrKW7aUpU0BDzQd27Br/VkrjlLlCzQ/5Ia1ScTwsEV6/Bc2QIfj2QqdS5tHKOz27at8jvvSbNyM2hT6hu0z/z/X7XLBNsplWhXwUIohz+aTRbs4VrSCWhgIu4EUioQtumePhXv9kMsmEQgAnqnQ2eL+k/HwUf+ezPaU96OxYTPJXjuXSNqlWNSmrOiHXBacYWuyEc/u9OZtbixu+QQhKJCiMYsdOliZnQsEAEEXnU3TFwYOVgIvVd17qE1h3Q+5U4keu5hM2WfRsC2WslZkG188Ao0c24iU7Oa42Vp/1Dz/RRMCJBKxcE/abfkbTiarZwKdjaCLzqZKbqLfD7uHzKJUIOpVRodF7GrfiH2YTNglb8MKXoEqLh5Lyb//TEYyNj+etNygH4ZYnBYYCrcu5GqkGG0LCAiCLjqfwu7oKT/w9lXPQDEStYVkv/2qf8Q+s7wtlbLV7wCtcSW9ZncG/JdNvcxZDQpXzT1yxCxKpR7BQdBF59OiGM3T7RmttDJ0udV42q6mB+39eNhuW9Ey5ZKVyl71u0Br5MIlm+wv2e0R/wuCUccLJRIWGRx0O6GFWGiIAOHejAAI+QfahFnffrPUUPW87qMNILTg7EoybRejIbsdKtuGVzCPkIttoAaY5bgfdgc8Wx1OWjlCC0MnC/f3WXR83I0Wox0FQULQRXD076tUdrtsAoPGhmU1VSGWtIupXrsQDdu0lyPgYtsVQiVbSnp2e2/UCqm4lakEdib/76a5uRorBgQNz0oIDlVzFXQTvdUzgk8LzhRyJ9ND9qveXrtcztka/bjYQZlwwa6l1mx1b7+V2CK4I9U2iNAJCBqCLoJFQXfgcPWLYNPosLlkv33SN2TvhnO2UlIVl7Fh2HmFcNnODK3Ycr+moMSr56JTRPfutciQH3JpWUAAEXQRLKnByk5pUc2ADOaTtgJuPpqwKz2D9qkfKm6U85Ype27BGYPDsBt0z1uLFu3WaMgWByL+kYXA1ClCkYhrWYgM+c+dQAARdBEsWpSWHg7stsDFcNQWk712MZG0i/Go3Q55tuoVqt8Fdo/C7kxPweaGwpbrY7OBjhAOW2Rk2KIjIxZiJzQEFEEXAROq9OiOHDeLqF8wKJWlkGX932c2kbIrqR77xA+50+W85Qi5aCOZUMFm+szmR+NWjvuPP94Kb2uhWMziR45apL+PkWIILO7ZCJ5Yj9ngkcrHADx5q1Wh4P8ek+l+O9MzYB9767buxobRqID2MxvbsOt9OSuM9FmZFob25T+nqIobO3rUQj3+cyUQUARdBI+qSOrRVVU33tlP4OVQ2NaSffZR37B9FA3ZTHGt+h2gfS0nivbxeNYKPXGzCIeZdqRtfhNHDlsknaKai0Dj3o1gikTNhk9UtgXu0LdPNTZsonfEPkhE7XqoZMvlohWYjYsOkA+XbT5ZsMl9Ccsmg9cr3/H8YKt2hfixYxZiVzsEHEEXwRTyD649I5VxY7HO2otfG0AsxVN2LdlrF2IRuxEq2yrb+KKDlP3/5cKeTQwUbWUoYaUUI8faSbgnbdGxMYtobm6EFyIINoIugiscMxs4VAm7HVDVdb24kZgtxJN2Jdlj5xIJu1lat4IfchUcgE6iKQxzkQ2bHgnb2oAfdKMEqrbgPxdGh0cstn8/1Vx0BYIugk2L0jRqLNLeFSXF2FI4YvPpQfugp9/ORsq2WMxUvgl0sGvpjE0Oeub1Mr6qHWjSQnR8zKL7/OdFoAsQdBFs4ahZ/wE/8B6tntGe1uIpOzu4134ZKdmUl7WiV6x+B+hsquxO9nl2bdR/ORfzH48MYthVsQP7XduCNooAugFBF8GmloWeUbOhI2bx3rZrYShE4nYr1W8fp3rtcjlny1ZyC85oVUCQZKJFm/HD7sK+HvNY4b87/Oe+UDLhB90Dld7cDmjnAlqBZxwEXyxl1run0sagCm8bKPsHmdVEj11PpuxiPG43ImZLXo7ZuAikonm2HC/ZxLBn+YGUlenX3XGq4Mb27XPV3DC7oKGLEHTRHTRmbOzJalV3Nw+y2vwh4qYqXE/12tl4zG6EirZRylW/DwRTNly024kNmx1PWD4d848+HH52THVziPjJkxbu69yRi8Cj4JkG3SGaMOtTVfdwpcK7S4r+AWch0WNnBsbtA8vZvJc3j7Fh6BKFsGefDK7aUn+kskUwdkQoEbfonnGL79tv4WSyei7QHQi66B4R/8C651mz1JD/zL/zd/31eI9d7B209/wDzUR+mbm46DpqzCmESnZzPGRzQ/5jkKru9gv5T30DA5Z86qnKYkCgy/Asg+6hcKuQq6quPu6Qkn+90z0j9kkyYRe1Y5QVLO9m4wLdR/f7+XjeD7oR2xjurM1cOlGkr99ie/dZdGSErX7RlbjXo7uoqutm6+717/3bW90o+wE3E03YzXSfXYjH7FrEbMFKVvRK1Z8AulM2VLSZnpJNDYfM60nSM7pd/GAbGRu12KGDForH+e+MrkTQRffpHTPr32+WHKye0XpFP0Qvx/yQm0zbJ+leu1LOWsYrWpmpCoCzGM3ZRG/elkdS5sX8V4GEsJYL9/ZabO9eN2kB6FYEXXQftTD0+UF35Pi2HFw9/zKXk312rqff3o9HbDa/yoIzoImVeMk+HctagSkMrec/D8UPH7Lonj1s9YuuxjMLulNywGzgoFnPmH9AaN24sUI4apcH9tmv/YB7tZyzvFeofgdAo1LIs7Vo0W4cStp6D7N1W8Z/0RAe6K9sDjG4fe9cAZ2AoIvuFPYPqqlhs/GnKn27j6kYidpcstfO9A7a+VDR5qxkWe1wRqsCsCk9OvJhzybSG7Y0mrRiL6OvHlvI/794zJKnT7sd0KjmotsRdNG9YunKwrTe8cqc3Ue0HkvZ7UTaLsTjdiUWsTkv56YqAHgwbXe9Gs7bnYGSLQ34L0CZr/tYQvGExfbssdjhwxZOM9UCIOiie6mqm+g3Gz1V+bjF2bqe//OrsYTdSvXY+UTSLkXKtlbccAduAFtzJ5n1w65n6/1MB3hkmrIwOGCJU6cs0tfntv0Fuh1BF90tEjUbe6qya9oWqroKueuxuJ0d3Gsf+MeSW17WSowNAx6Z579AnOr37Pqo/1Ix7j8uCbtbFk6n3OKz+NGjtCwAVQRddDn/YOrC7tNmA4cqXz9ALpa0iZ5Be6t3wK4WV22DBWdAS2i+7nxv2WYP9VkpQtDdknDIovv3W+LkSVfZBVDBowFQuO0ZNRvSRhJ7quc1t5AasPOpHvs0YjZTLljWK7lKFIDHp8fSarRgV/uzlh3prVR28VCi43ssrikLAwPVcwAIQRcQtS30HzAbPm4WS931tmnZ/zwfidntVJ9dSiTsSiRk06GSFbQBBCEXaKl8yLO5WM4mxszWe2Jm9Jnen//8FEomLX74cGVmbozFfEA9gi5Qkxo0GzpaCbzV7YFL4YhlonGbjCft055+uxQq2qKXZ2wYsI1K4bJd6V23+cGw5VPq161+A/fQgrPo3r2Vmbn9/dVzAdQQdIHP+UdTzdY98IobPVYOhS0TT9vVniF7O5Wy24U1y3nF6s8C2C56GVkIeXZzLGRzQxH/SMWhqilVc/3nptRzz7ppCwDuxbMHUE8L09LDVt73vE2MnbAPUmk7a1k/4OZoUwB22FI464Lu2nhf9RzUUwU3+fRTFh0aYsoCsAmCLnCXkH/0iFto5KSt9o7ZUjRm62XPPFoVgB1XDHk2nczZxGDRvIFe/4hFD0NNuKfHogf2W/zYMQvFmT0MbIagCzTSxhHJQevv2299yWGLVvt1Aey8TKRoUz0FmxyNWIn5uk4oFv18Xq7ry6W1A9gUjw5gE/t79tuh/kM2mBi0EKthgF2zFvPs8lDOMgNx82Jdftjyg35kaMjiRw5bbN++6pkANkPQBTYRCUfsYN9BOzV0yiIhRhwBu0XTqlejRbtxKGmZni6ewqBqdjRqidOnLXbwIFv8Ag+BoAvcRzKStL09e+30sH9gCTOfEtgtpZBnE9EVWxpPWWEgXT23u2jBWfLppy22d6+FEw+/ZTnQzQi6wH2EQ2Hri/fZ8cHjNp4et3gkXv0OgJ2k5aD5UMmu9+VsZiBkluquoBfyg61aFRLHj1m4r89/cuLwDTwMHinAA6iSO5wcthODJ1y/Lm0MwO5ZiOVscsCzhcFo14Q9VXJdX+6pU+4jo8SAh0fQBR6CJi8cGzhmB/oOuApviJXfwK5QZXcuXbKJ4bLle+NWDvrIMf/3C/f3W/zQIYsfPULIBbaIoAs8JIXdJ4eetCP9RywepoUB2C3ZUNEWejybOdhrXiTYhzHNyFXATT55msVnwCMg6AJbkIwmXb/uk8NP0sIA7KK1cMEup1dtY8+AecmAvvD0g23yySctcfy469EFsHUEXWALtDitP95vh/sPu7FjsQiTGIDdUAqV3cixi6M5W+v1X3QG7C19bQqROHnSYkeOuNYFFp8Bj4ZHDrBFamEYSg7ZyaGTblMJVXkB7DyF3TvJnE0PR2y9V/N1g9Gvq+ptdO9eS5w6ZVEWnwGPhaALPAJNYhhNjboWBn1kxi6wO4ohz+4MeTY3FLZSovMDoUJtdGTYkqdPW3R8zPXoAnh0BF3gEalH1+2cNnjKhV0Au2MxnPWDbsTWxnur53SuyNCgxY8ds7j6cqnkAo+NoAs8JoXdE0Mn3IYSAHbHVHzDrvbnzBse6Nh+1vDAgB9wT7iQC6A1CLrAY9JuaQd6D3y+oYQWrAHYWfmQZ3Opol0e96yoFoZOCruhkIV7eixx6qTFDx+ycJK+f6BVOCIDLdAT66lUdv2w2xvrZfQYsAs2oiW71Ze3hdGEFeIdcnjzA3k4nbb4ieOWOHrUIgMDgVlUB7QDgi7QAiH/f9ox7fTwaRd407E0lV1gh3lWtkykZBN7wpbpj1k52uYvOKshN3bwgCWfecYig4OdVYkGOgCPKKBFFHY1auzl8ZdtX88+JjEAu6AU8mwitmoLYynLD6Sq57YnTVSIHdhv6S98wSK9vYRcYBvwqAJaSGFXPbtPjTxlRweOEnaBXXKlZ83uDHhW7mnPsKtZuYkTxy317LMW1q5ntCsA24KgC7RYyD9gaVHa8YHjLuxGwvTrAjttPVK0KT/oTg37h7lIGz0G/ecHVXITJ09Y/MQJC9OuAGwrHl3ANtDuaZqtq8Vph/sOWyKScNVeADuj7J+WEiWbHCxbZihp5XAbPP4UchNxix894kJudHTUQu0UwoEAIugC20QtDHvSe+y5sedsb89e17+rai+AnZELlWwh5YfdvXErpmL+EW8XH38KucmERffsseRzz1VCLhtCANuOoAtsI1fZTY7aF/d90fb37rd4mO08gZ20FinYpfSqre8ZMC+5e48/t7WvH3K18Cw6NETIBXYIQRfYZqriatzY82PP26mhU+5zADunEC7bx8NrttQXMYvv/AJRLTyLnzxh6RdesEh/v3/k5dAL7BQebcAO0EzdgcSA69l9YugJt6kEbQzAzvBCZVuK5W1yNGzL/X7Y3anHnn894VTKEk88YYlTpywyMkJPLrDDCLrADtFuacPJYTeN4eTQSeuP9zORAdghJSvbVG/R5gYjlu9NVM/dRn6gDff2VHY8O3nComNjtCsAu4CgC+wgVXYHk4P29MjTbvSYwq76eAFsv9Vw3mYHzBZHE1aO+Y+77SrsupDba7HDhy35/PMWpZIL7BqCLrDDNGYsFU25HdRODp50WwcD2BlT8Q272p81b3j7emXDPWmLHztqPa+/zo5nwC7j0QfsElV31cKg6u6enj3VcwFst+WkZ5+O56zgRo619jAYGRm25NNPuxNVXGD3EXSBXZSOpu1g30E7PXTaDvQecH28ALZXPuzZTKpg03uTlku16DHnh9ronnFLPvWUxY8csUhPz84tegOwKYIusMs0gUFhV9MY9vbudbuoAdg+npUtGynZzaGSrQ7GzUs+3sixUDJpsf37LHH6dCXkDgwQcoE2QdAF2oB6do/0H7Gnhp+y8fQ4WwYD20xTGGai6zYzErVMv//iMvIIh8Pq+LDYvr2WfOYZN0IsrEougLZB0AXahEaNKexqYwlVeNXDC2B7Xe5ZszuDnpXTqeo5Dy8Ui1r82DFLv/KqxQ8fpicXaEMcSYE2M5IasedGn7MXx1+03jgbSwDbSW0M0/2e3Rzzv3jYObeq5Pb1Weqlly35zNMW1m5nANoSQRdoM7FwzAYTg3Zs4Ji9OPai7evZR98usI1Wo0UXdpf39Jj3gBaGUDzuFp2lXnzB4kePupAbilLJBdoVQRdoQ2pj6E/0u7B7evi0Heo75ObtUt0FWq8Q8mwxUbKJUf/zvqSVNwmu4XS6sujsySctcfy4Rfr9xyTtCkBbI+gCbUqL0eKRuNsyWLN21b+rsMsIMqD1NsJFu5nM2MJ4sjJft/5FpVoVevyQe2C/C7nJJ56wUCJx988AaEsEXaADjKXH3CK1F8ZesHQszUI1YBsUwp6dGV6z5T7/8RWvjhzzw2zI/zzx1FOWeuklt+gMQOfgaAl0CPXpqoXhKwe+Yof7D1symqx+B0ArlP1TPlSyiT0Rmx+MuKptdO9e6/3a1yyp0WF9bNcNdBqCLtAhVMVVuNWc3WdGnnG7qY0kR5i3C7SQpjDMJfK2tN8Ptc88YekXX7DY/v0W7u2lHxfoQARdoIMo1EbDUdvbs9dODJ6wE0Mn3Oea1EDgBR5P7fHV1ztsvQePuA0gYgcP0o8LdDCCLtChhpJDdmrwlFuopiqvqr307gKPRo8d7VCox5IeU8fGTlvPwAgBF+hwHBWBDqZwq37dNw68YYf6D1kyQt8u8CgUco8NHrOvHfyaHe0/6r4G0PkIukCHUyWqJ9ZjL429ZK/sfcUtWFMrA4AHU6uCXiS+uvdVtyOhAi7vjADBwaMZCAAdmLVd8MHeg/b06NP2zOgz7i1YbTwB4F56zAwkBuzJ4Sft6eGn7UDvAfeCkZALBAuPaCBANGN3f89+OzV0yu2oprdgdTBX1QqAuQ1XemP+i8K+g/bE0BPutK93H60KQEARdIGAUUWqP95vJwdP2kvjL9nxweM2khpx/bxsIYxupYkKmkWtRZxHBo64zVf0zoe+ZrdBILgIukBA1d6aVdj9wt4v2LGBY66yyxgydCO18Wjh5mv7XrPX9r5Wae0h4AKBR9AFAk7Bdjg5bM+OPmtfP/h1V81iVzV0C93Xjw4cddMUVMUdS40RcIEuQtAFuoAbgh/vs309+9yuagq9+3v3WzwSr/4EECwKuOrD1SQF3ed1f1dLDxNJgO5C0AW6hCq7Cra1XdW0WE3tDKr2Mp0BQaD7uILsWHrMjg8cd/dx9arrPq/+XHrUge5D0AW6kFadK+Q+P/a8m9Awmhp1Ext4SxedSu9aaMTenp499tTIU/bC+Atu6oju1wC6F0EX6FKqfumtXG13+rUDX3PbCSsoAJ1GlVq9M6EpCt849A07OXDS0lECLgCCLtD1NJ2hJ97jqmDaSlgr0vVWL+0MaHe67w6nhu2V8VfcZBG1K8TDcVoUAHyOoAvAtSxoVyitSK+1NGgsmcYx6XxGkqGdaKGZXoxpUeWLYy/ascFjrv1Gmz4QcgHUI+gC+FxtOkNt1yi3mGfopPtabQ5sj4rdovueWms0PaG2mPL00Gk70n/E3Td5BwJAMxy1ANxDFVxVxw73HXazR18cr1TNtMOaKrxsKYydoPuh7mu6z40kR9ziMt0f9W6Dpin0J3jxBeD+eIYAcF8a16RdpF4ef9nePPyme7tYC38IGNhuuo/pxZVm4X7r8Ldc/7gquhoVBgAPgyMVgIei0KEqr942/tL+L9mXD3zZ7Til2bz08KJVdD/TSDCNvfvKwa+4+9rxwePuPF5cAdgqnjUAPLRa2FVFV20NGk32yp5XXPgdTAwSRPDI9IJJ7xw8OfykvbrnVffxYO9BG04Mu/sc9y0Aj4JnDgBbVgu82lJYi9YUSp4YfsJV3rQaXgva6OPFg+h+pEqt7jO677gFZv5JL5wUejVdgSkKAB4HQRfAY1Gg1W5U6t1VD6U+atGQtmHVaniFFXZcQ43Craq3boFZasQO9R1yPbiahasXTfR/A2glnk0AtIT6dLUblWbvvrbvNbd4SP2Vqs6pwkt4gZvmEUm5cPvK3lfs64e+7jYpOdR/yL0gAoBW48gDoKUUZvS/RDjh3n5WhVeBRidt0arB/rQ1dA9N7dDfXDvvaXHZm0fetJf3vOzCbm+s9/P7CwBsB4IugG2h3kq9Ra0wo7eoD/QecCvpNZNXQUe9mGpv0Kgogk5w1Pq31Xer3m39rfU3V1uCwu1oerTS0hKhpQXA9iPoAth2rsLrB1oN/Vdrg3a0UgjSSTuvKQCpN1Phh8VHnUeBVbuWqYKv/mwtTNTfVlXc2u5ln2/Ry4saADuIoAtgRynoqNKr4KMqn0ZJ1Sq82gxAgVcVP/X76ufo7W0/+huq/UTBVX8rVWkVZtWm8ureV93CMvVm628Zi8Sq/woAdl6o7Kt+DgC7pqz/+U9HeS9vCxsLNrcx9/kpU8iYV/aqP9lZbl26Zb/8q1/a3/9vf+++Pv3qaXvzf3rTXn7zZfd1p3EhNxJ1IXZveq97cTKWGrNIOOKq8VRsAbQTgi6AtqKnpKJXtIJX+Py0UdywpdySLWX9k/9xObds+VLeheN218lBV6FVFVlVbQcSA9af8D/GB1ybQjwcdxV3LTbTzxBwAbQjgi6Atqfgmy1mXeB1p9KGq/Ku5ddsrbBmmXzGMsWMlbxS9V+0j04JurVQq/m29Sdt6KDeaY3/qn1UwCXYAugEBF0AHUeVXAVfBd3V/KqtFlbd5wrBOj9XyrkWiEKpYMVy0VWJd0s7Bt1aqNUCwdpJAVY9tz3xHjcpo3ZKRJmKAaBzEXQBBIJ6eBV6F3OLrrVBwVdV3/XiuqsI6/ulcqny0at81P+2+ylwN4KugqkW8alnVh8bT9FQ1LUfqB1hMDHoPqolgVALIGgIugACxfXtuv+rPLUp3CrwKgSv5Fcqp9yKC8IKweoB3s6nwd0IuqrWuuqs2g+ilfaD+nYEVWprfbW1cW4EXABBRNAFEGgKvLUqrkKvPqqdoXaeWhxqLQ+1HmD3eWnDcsWcqwbr52tV4K1qddDVWC+1GijI1toNPv88UvmoHlpNQdB8W1Vwax9rn+vEvGIA3YCgC6CrKfy6KQ+l3055qE19qLU81E6ftz7UfawF6M/P96rnV8+7ev6q/ejPf2R/+V/+0l3fc68/Z9/7F9+zr3znK5+HT/c//2PTVgP/f7XzFVBrUw70UaHXfV091b4Oh/1/Q4UWAAi6APCwFFw/D7g61VWJa8H2rvP907mz5+wv/vQv7H/9z/+ru4zX33jd/sX/81/Yd7/33XsC7V1fNzlRjQWArWHLIQB4SAqbtdYB7dzWF+9zi7lGUiNu+9u9PXvtQO8Bt83xsYFjdnLwpNsSV5sr1Ki1YLxn3O0kpq2P9fP7evbZnp49NpYec5c1lBxyC8R0+eqpVWuCrlPXTcgFgIdH0AUAAEAgEXQBAAAQSARdAAAABBJBFwAAAIFE0AUAAEAgEXQBAAAQSARdAAAABBJBFwAAAIFE0AUAAEAgEXQBAAAQSARdAAAABBJBFwAAAIFE0AUAAEAgEXQBAAAQSARdAAAABBJBFwAAAIFE0AUAAEAgEXQBAAAQSARdANhGkUjEenp6bHh42J36+/stFotVvwsA2E4EXQDYRr29vXbixAn71re+5U4vvfSSjY+PV78LANhOobKv+jkAoMX0FFsqlaxYLLqvw+Gwq/LqBADYXgRdAAAABBKtCwAAAAgkKroAAimfz9vS0pIVCgVbXV11X9eLRqNukZh6aJPJpKXTaQuFQtXv3t+tW7dseXnZtSS0km6Tbs+BAwe21NqgtoiNjQ1bX1+3tbU1y2az99y2vr4+S6VS7jQwMFA9FwCCjaALIFByuZwLenNzc3bp0iXLZDJ2/fp1F3brKdju37/fDh48aCMjIy5cKmRqIsKDAu9f/dVf2blz51y4bCXdpuPHj9vv//7vu88fRE/fug2Li4s2PT1tU1NTLoTPz8+7/w71jhw5YqOjo24h3MmTJ93lJxIJ1zMMAEFF0AUQKB9//LF99NFHNjExYZ7nuTBYO9VTmK2dFG4VdF9//XU7fPiwq/DeTzsEXf0+CrPvv/++nT171mZmZtx5td+5kQJt7fdVVfeNN96wp556iuougEDjpTyAjqcKrqq2/+2//Tf7xS9+Ybdv33YtC3r7frPgVwuF+hkFRlVC3377bfvss89aHmBbTW0Yk5OT9td//dcu6M7Ozrr2Bf0uzX5Xqf2u+jlVud9991378MMPXSUYAIKKoAugoymU3rhxw375y1+6VgW1LDS+bf8gCof6N3fu3LHz58/btWvXqt/ZWaq6qk9XVdfNKMCrReGdd96xK1euuLYFnbcVCr36d6oEK9gTdgEEFa0LADqaqpMKp//wD//gwmrtKU1hUaFxaGjIndSPKqpqKuQ162MVLVA7ffq0vfnmm659oFno/OCDDz6vGm+VgrnCuG5DI93O559/3r785S9/fnsbqUVB7RmqyKo6W/8UrqBc+33VfqGvH/T77tmzx13nF77whQeGbADoNARdAB1PofPHP/6x68tV+FTAU9DTIrOnn376rl5UfV/9tQqrevu/WfhTv652MdMCLoW/VtJtVDVW1dR6CphaHPe1r33N7aTW7HoVbNV/rH+vsFxPP6/f8bnnnnO/r353nVf7ffXvVLFWm0c9TXc4evSoffvb33aL1djIAkCQRP69r/o5AHQkhVqFNAVeBTlNT3j22WftO9/5jgurWnxVq1QqyOlnBwcHP6+uNtLiNF2Ggmerg64CrlojVImup99BgfNLX/rSpmFTvbgKrc1aKzRN4Zvf/KYLugq8tcuo/b4K7/pvo7aHevUVcE2gaPXvCwC7iR5dAB1PwVRB76tf/aq98MIL9sUvftG9Fa82BAW3xrfjFf4U/BTs+vv7q+f+lgKh+lbVy9oqCpQKt1r0trCwUD33t9RCcOzYMVeN3owW3KkK3fhGnIKs2i3079Xy0Oz3HR4etieeeMKNFmuk26XwrDm8rfydAWC3EXQBdDwFOwU8VURfeuklF/rUp3q/0KifV+WzWdBVi4A2Xmhl6NNlXr161YXcxt5eBdGxsTEXvjejf6+Qq00wGinkq92hvnLdSIF/3759Lgw3hn/dHl2uqtuNG2sAQCcj6AIIBAU3LR5TWFTIfRjxeLzpzFxVTBUsW0WXp15gLZpbWVmpnvtbur179+7ddKatArd2YlMYbeyx1e1XNVhh90EUqHVqDMO6fQq7qmI3Xj4AdDKCLoCupYDX2AYgCoIKhK2i0KyQqtYDtQfU03Wpynq/fmBNTtgshGrRmU7NAnuNgrIq1Ddv3nS3QaG28ffWz6jaTEUXQJAQdAF0LQXIxjYCUeDUYrTGyuejUsi8fPnyPVViXb6qyrXteTejEKrxYM1CqEJuX19f9at76d9q++O33nrLfvjDH9rFixer37kbQRdAEBF0AXQttRE0Wxim8KnFW/fr8X1YCtMKqZq20Kw3V1sOawKEFtRt5n4hVAvuNpu5q0Vmut6//Mu/dB/1++qymqkF4la2bADAbiPoAuhKCp9afNXYSiBa1KVe31a0L6i3VmPPFFQbQ6bCrRbOqTf3ftVjtRkopDarPuu2NrYtKFxrusN7771nv/nNb1zLgkKszt+MrkOtEff7GQDoNARdAF1HYU4TEDTFoDF8qpqrxWGaUNCKoKvZtwqajQFSIVdtB2pb0CK6+1EI1WK2ZtVYhdxaNbhWldXWwB9++KHbJELbI9eqtArTui4tfGv2u6li3Ow6AKBTEXQBdBUFOVVZ1avauHmCKORqvq6qrI/buqAKrLbsVaBupL7aU6dOufFmjxOo1U+s26kwW/u9fvazn7mQWz+KTD+n69IItpdffvmeVgmF6WaL1ACgkxF0AXQVVS3fffddF0CbvU2vntlnnnmm+tXj0Xa/alvQDmyNVFnVdbWiaixqw9BiM50UrBt/N1Vxtb2wtvrdrKILAEFD0AXQNVTx/OCDD+zSpUtuEkIjbbpw/PhxN3GhFbTbmKrGjVVSVXM1TqwV7RHq/f31r39t//AP/+CuT3229e0HasV49dVX7Rvf+IbrB1ZPbysW2QFAJ+DZDkBX0Nv4elv/448/doG3vuKpsKng+eyzz7ZkEZqCpnpzFXKbBWqNElNvrvprH3eEmcaWffrpp64PWAvraqFagVbX8cYbb9iLL75ohw4dcgF+s5Cr26HbQwgGECQ8owEIPE0sqAVChc/6kKveVY0Se/755101t9mWwFulfllVVxcXF+8Z16Xr005m99vutxlVZpuFUP0+CtX1Exk0ruzkyZOuF/e1115z11UbQaYQ3mx6Q22hmm4fAAQFQRdAYKm6qbfy1apw5swZN4GgnoKjQuHTTz9tL7300qZb8G5F7To1+UBzbBspSI+NjbnrfVi6narG3i+EKqjWFpzp9/nSl75kL7zwgguv9VVjBe9m83Sp6AIIIp7RAASWKpfaKEHzZLUorJFCofpWv/rVr2666cJWaeGZZtjq+ppt2avtfrUYbCsUQtXXe7+gq++pJeIP/uAP7Mtf/vKm16ExZZoh3CzoPihMA0CnIegCCCRVUy9cuOA2TGgW7MbHx90iLZ1aGe5q2/1qukP9IjQFSe1ipqB7v+1+m1GVVf92s9upebz6Pf7oj/7ITXJQFXezyqxuV7PNK/TzGq2mFgkACAqCLoDAUVVVi7Pef//9e/pXa4FOPblPPfWU+7xVdD3qy71+/XrT3lwtCFMo3Wr1WLdZ7Q6b/Tv1/D755JNuQd39pioo3OoFQLPRalqAp8tp3GUNADoZQRdAoKhiqdYBLTxrDJwKc2oB0JxchVyFzlZS76tm2DZWTFXNVaVUG0Q8yugyBVdVoPVvm02E0HmNG0A0o5CrebsK4/XVZv17VYEVdFvVwgEA7YCgCyAwVKVUtVIjxNSbW09hsdY6oJFbrQ65CraagKBpC41UzdXiM123bsNW6bZroZyqz6rYNpqennZbGjdWkevpv41un8K/Ks/1QVfhVj29uvyHCcwA0CkIugACQUFTldS3337bzcttpIqlKqpvvvnmtrw9r3YJLUDTbmiNtOhNM3oVcjdrK3gYan1QC0MjVWk1WaLZjmg16lM+d+5c0/82qhTrvw0hF0DQEHQBdDxVMhXkfvzjH7veXLUv1FMVVNMVNEJMYVOtBK2mqmqzRV6i6zx69OhjL3o7ePCgay9ovJxaNVm7o2nChDbEqNF/m/Pnz9tPf/pTF3Ibg7BeAKi3V3N3H/f2AUC7CZXr378CgA6jt+Fr7Qo6aaRX49OaKpXabldvzz9s1VJhWG/pq59XG0rcj8Lkz3/+c9cXrLBbrzbX9pvf/Kbr032ckK2QqrCqSRKa09tIvbaq+Op3VYCVWjuHgrB2Tqunn9e2x6+88op7IQAAQUPQBdDRtABMb8n/7Gc/c+0DrXpKU4uBFq59//vfd721m1GQVOvAD37wA7chRWPFVJVS7U7WqiCp31dh99133206Nu1h6ffTjmmqciuIM20BQBDRugCgo2mSgAKfqpW78bpd1VwFz6WlpXtCriqmajVQb22rqEKs8KyAqgVuajfYSpW4NgFCVWrN3lUAJ+QCCCqCLgA8htrua6q0NtJkB7USNJuU8Dg0geHll1+2b33rW65NQYH6Yem2qEL9h3/4hy7k1locACCICLoA8IhUTdZYr9XV1XuquaJAqYpuqxe/1fqHjx8/bt/97nftO9/5zuftEY0LyvSzWgyn733961+33//933cBWf3KuoxW3zYAaCf06ALoaNpyV4utNFqr1RQE1SagFoFmcrmc68/VSLFmQVfb8aqiu92tAfpvoIqyepT136Kxb1e/h2bkqhKsUWK0KgDoFgRdAAAABBKtCwAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIJAIugAAAAgkgi4AAAACiaALAACAQCLoAgAAIIDM/v+h3EUd+HRqawAAAABJRU5ErkJggg==)

# In[56]:


#Start the first wedge at 90 degrees:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()


# ## Explode
# Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
# 
# The explode parameter, if specified, and not None, must be an array with one value for each wedge.
# 
# Each value represents how far from the center each wedge is displayed:

# In[57]:


#Pull the "Apples" wedge 0.2 from the center of the pie:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()


# ## Shadow
# Add a shadow to the pie chart by setting the shadows parameter to True:

# In[58]:


#Add a shadow:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()


# ## Colors
# You can set the color of each wedge with the colors parameter.
# 
# The colors parameter, if specified, must be an array with one value for each wedge:

# In[60]:


#Specify a new color for each wedge:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["r", "y", "b", "m"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()


# ## Legend
# To add a list of explanation for each wedge, use the legend() function:

# In[61]:


#Add a legend:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()


# ## Legend With Header
# To add a header to the legend, add the title parameter to the legend function.

# In[62]:


#Add a legend with a header:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()


# In[ ]:





# # DAY- 40

# # START SEABORN:

# In[ ]:





# # INTRODUCTION TO SEABORN :

# -> Data Visualization is the graphical representation of information and data.
# 
# -> In the world og Big Data, Data Visualization tools & Technology are essential to analyze massive amounts of information & make
#    Data-driven decision.

# # Line_Plot In Seaborn:

# In[63]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {"Days":[1,2,3,4,5],
       "NOP":[50,40,60,30,44]}

df = pd.DataFrame(data)
print(df)

sns.lineplot(data = data,x = "Days",y = "NOP")
plt.show()


# In[68]:


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")  #Here may be titanic,planets,iris,healthexp.csv,penguins.csv...
                                 #(if you want from where to come data then go to the chrome and write "seaborn github dataset")
print(data)


# In[64]:


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("titanic")  #Here may be titanic,planets,iris,healthexp.csv,penguins.csv...
                                 #(if you want from where to come data then go to the chrome and write "seaborn github dataset")
print(data)


# In[65]:


sns.barplot(data = data ,x = "sex",y = "age" )
plt.show()


# In[69]:


sns.barplot(data = data,x = "day",y = "tip")
plt.show()


# In[70]:


sns.barplot(data = data,x = "day",y = "tip",hue = "sex",palette = "viridis")
plt.show()


# In[71]:


sns.barplot(data = data,x = "day",y = "tip",hue = "sex",palette = "GnBu")
plt.show()


# In[72]:


sns.barplot(data = data,x = "day",y = "tip",hue = "sex",palette = "viridis",order = ["Sun","Sat","Fri","Thur"])
plt.show()


# # Histogram Plot:

# In[74]:


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)


# In[75]:


sns.histplot(data =data,x = "day")
plt.show()


# In[76]:


sns.histplot(data =data,x = "day",hue = "sex")
plt.show()


# In[77]:


sns.histplot(data =data,x = "day",hue = "sex",kde = True)
plt.show()


# In[78]:


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("titanic")
print(data)


# In[79]:


sns.histplot(data = data ,x = "age" )
plt.show()


# In[80]:


sns.histplot(data = data ,x = "age",hue = "sex")
plt.show()


# In[81]:


sns.histplot(data = data ,x = "age",hue = "who",kde = True)
plt.show()


# In[82]:


sns.histplot(data = data ,x = "age",hue = "who",kde = True,discrete = True)
plt.show()


# In[83]:


sns.histplot(data = data ,x = "age",hue = "who",kde = True,discrete = True, bins = 8)
plt.show()


# # Scatter Plot

# Number To Number Relation B/W 2 column

# In[85]:


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
print(data)


# In[86]:


sns.scatterplot(data = data, x = "total_bill",y = "tip")
plt.show()


# In[87]:


sns.scatterplot(data = data, x = "total_bill",y = "tip",hue = "smoker")
plt.show()


# In[88]:


sns.scatterplot(data = data, x = "total_bill",y = "tip",hue = "time")
plt.show()


# In[89]:


sns.scatterplot(data = data, x = "total_bill",y = "tip",hue = "day",size = "size")
plt.show()


# In[90]:


sns.scatterplot(data = data, x = "total_bill",y = "tip",hue = "day",size = "size",marker = "o",palette = "spring")
plt.legend(bbox_to_anchor = (0.2,0,1.2,1))  #(x-axis,y-axis,width,height)
plt.show()


# # Heatmap:

# It is also number to number relationship b/w 2 column

# In[91]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("tips")
print(data)

gp = data.groupby("day").agg({"tip":"mean"})
sns.heatmap(gp)
plt.show()


# In[92]:


gp = data.groupby("size").agg({"tip":"mean"})
sns.heatmap(gp)
plt.show()


# # Count Plot:

# In[93]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("tips")
print(data)


# In[94]:


sns.countplot(data = data,x = "sex")
plt.show()


# In[95]:


sns.countplot(data = data,x = "day")
plt.show()


# In[96]:


sns.countplot(data = data,x = "day",hue = "time")
plt.show()


# In[97]:


sns.countplot(data = data,x = "day",hue="sex",palette = "GnBu")
plt.show()


# # Violin Plot:

# -> For statistical data (mean median frequency temprature....etc)

# In[98]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("tips")
print(data)


# In[99]:


sns.violinplot(data = data,x = "total_bill")
plt.show()


# In[100]:


sns.violinplot(data = data,x = "tip",palette = "viridis")
plt.show()


# In[101]:


sns.violinplot(data = data,x = "total_bill",palette = "pink")
plt.show()


# # Pair Plot:

# In[102]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("tips")
print(data)


# In[103]:


sns.pairplot(data)
plt.show()


# In[104]:


sns.pairplot(data,hue = "day")
plt.show()


# In[105]:


sns.pairplot(data,hue = "day",palette = "viridis")
plt.show()


# # Strip Plot:

# In[106]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("tips")
print(data)


# In[107]:


sns.stripplot(data = data,x = "day",y = "total_bill")
plt.show()


# In[108]:


sns.stripplot(data = data,x = "day",y = "total_bill",hue = "sex")
plt.show()


# In[109]:


sns.stripplot(data = data,x = "day",y = "total_bill",hue = "sex",dodge = True)
plt.show()


# In[110]:


sns.stripplot(data = data,x = "day",y = "total_bill",hue = "sex",dodge = True,jitter = 0.8)
plt.show()


# In[111]:


sns.scatterplot(data = data,x = "day",y = "total_bill")
plt.show()


# # Box Plot:

# In[112]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = sns.load_dataset("tips")
print(data)


# In[113]:


sns.boxplot(data = data,x = "tip")
plt.show()


# In[114]:


sns.boxplot(data = data,x = "tip",y = "sex")
plt.show()


# In[115]:


sns.boxplot(data = data,x = "sex",y = "tip",orient = "vertical")
plt.show()


# In[116]:


sns.boxplot(data = data,x = "day",y = "tip",orient = "vertical",palette = "GnBu")
plt.show()


# In[117]:


sns.boxplot(data = data,x = "day",y = "tip",orient = "vertical",palette = "GnBu",dodge = True)
plt.show()


# # Multiple Plot:

# In[118]:


import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset("tips")
print(data)


# In[119]:


a = sns.FacetGrid(data,col = "day")
plt.show()


# # Style And Color In Plots:

# In[120]:


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("exercise")
print(data)


# In[121]:


#sns.set_style()
sns.barplot(data = data,x = "time",y = "pulse")
plt.show()


# In[ ]:




