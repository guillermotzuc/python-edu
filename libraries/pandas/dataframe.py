import pandas as pd
import numpy as np

# define the data as a list; made up data for an imaginary vet service
data = [
     ("Dexter","Johnsons","dog","shiba inu","red sesame",1.5,35,"m",False,"both",True),
     ("Alfred","Johnsons","cat","mix","tuxedo",4,12,"m",True,"indoor",True),
     ("Petra","Smith","cat","ragdoll","calico",None,10,"f",False,"both",True),
     ("Ava","Smith","dog","mix","blk/wht",12,32,"f",True,"both",False),
     ("Schroder","Brown","cat","mix","orange",13,15,"m",False,"indoor",True),
     ("Blackbeard","Brown","bird","parrot","multi",5,3,"f",False,"indoor",),
 ]

# define the labels
labels = ["name","owner","type","breed","color","age","weight","gender","health issues","indoor/outboor","vaccinated"]

vet_records = pd.DataFrame.from_records(data, columns=labels)
print(vet_records)

vet_records.head()
vet_records.dtypes
vet_records.type.count()
vet_records.type.value_counts()


# Create a pandas series from the DataFrame
weight = vet_records['weight']
print(weight)

### Boolean Filter
# Collect the dog weights only using a boolean filter
dog_weight = vet_records.weight[vet_records.type=='dog']
print(dog_weight)

# We can get all the data for dogs:
dogs = vet_records[vet_records.type=='dog']
print(dogs)

# loc and iloc
# loc allows you to use column names to slice data
# iloc requires the use of index numbers. (Example: .iloc[row, column]) Remember: Python indexes starting at 0.
# We can use loc to get the name and owner of each pet.
vet_records.loc[:,["name", "owner"]]

# We can also get just the third and fourth record.
vet_records.loc[2:3,["name", "owner"]]

# Using iloc means we use indexes to filter our data. 
# Let's get the color and age of the third and fourth pet. The third pet (Petra) will be a row index of 2, 
# and the fourth pet (Ava) has a row index of 3. If we examine the vet_records DataFrame, we will see that the color index is 4, and the age index is 5.
pets = vet_records.iloc[[2,3],[4,5]]
print(f"3,4 {pets}")


# .isin can be used to gather data about a list of items. For example, let's get the data for "Dexter" and "Blackbeard".
vet_records[vet_records.name.isin(['Dexter','Blackbeard'])]

# The tilde symbol (~) can be used as the logical NOT operator.
# This means we ask for all pets excluding Dexter or Blackbeard:

vet_records[~vet_records.name.isin(['Dexter','Blackbeard'])]


table = pd.pivot_table(vet_records, values=['weight', 'age'], index=['type', 'breed'], aggfunc='sum')
print(table)

# You can import NumPy and use its functions as the aggfunc, such as aggfunc=np.mean.
table = pd.pivot_table(vet_records, values=['weight', 'age'], index=['type', 'breed'], aggfunc='mean')
print(table)


# Another way to examine the data in a DataFrame is to look at stats such as mean, quartiles, and standard deviation.
vet_records.describe()
# Notice that age is only using 5 values. Since one is NaN, those are left out of the calculation. Therefore, if you have a policy for how to deal with missing data other than leaving them out, it is advisable to adjust the missing data before any calculations.

# The isna Function
# In large datasets, the function isna can be used to find missing data.
missing_data = vet_records.isna()
missing_data

# The fillna Function
# .fillna() can be used in two different ways. First, let's look at adding a constant to every column with Noneor NaN.
vet_records_value = vet_records.fillna(0)
vet_records_value

# We can also use a dictionary with the .fillna function to fill in values according to their column's format.

values = {"age": 12, "vaccinated": False}
vet_records_dict = vet_records.fillna(value=values)
vet_records_dict