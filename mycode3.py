#read CSV file


import pandas as pd
dis={
    "a":[1,2,3,4,1,5],
    "b":[12,13,141,15,16,21],
    "c":[21,22,23,24,25,26]
}
dis2=pd.DataFrame(dis)
dis2.to_csv("test_new2.xlsx",index=False,header=[5,6,7])
print(dis2)

#excel file to pandas csv

# import pandas as pd

# csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv")
# print(csv_1)
# csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv",nrows=2)
# print(csv_1)
# csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv",usecols=["time"])
# print(csv_1)

# #for multiple columns we get
# import pandas as pd
# csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv",usecols=["time","duration"])
# print(csv_1)

# #we get columns bt indexing
import pandas as pd
csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv",usecols=[0,3])
print(csv_1)


#how we skip rows
import pandas as pd
csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv",skiprows=[1,2])
print(csv_1)

#by self indexing
import pandas as pd
csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv",index_col="duration")
print(csv_1)

#heading by self
import pandas as pd
csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv",header=2)
print(csv_1)

#name

import pandas as pd
csv_1=pd.read_excel("C:\\Users\\PC\\Downloads\\data.csv","names"==["name1","name2","name3","name4"])
print(csv_1)

#pandas function

import pandas as pd
csv_2=pd.read_excel("C:\\Users\\PC\\Documents\\test_csv.xlsx")
print(csv_2)
csv_3=csv_2.index                  #for getting index
print(csv_3)
csv_4=csv_2.columns                 #for getting columns
print(csv_4)
csv_5=csv_2.describe()              #for describing values
print(csv_5)
csv_6=csv_2.head(2)                 #if we use head funtion we get first five values but if we pass a number in funtion then we get its number values
print(csv_6)
csv_7=csv_2.tail(2)                  #it work same as header function but its gets ;ast values 
print(csv_7)
csv_8=csv_2[0:3]                      #for getting rows bt slicing
print(csv_8)
csv_9=csv_2.index.array               #index in array
print(csv_9)
csv_10=csv_2.to_numpy()                #data in numpy array
print(csv_10)
csv_11=csv_2.sort_index(axis=0,ascending=False)             #data in decending order in rows order
print(csv_11)
csv_12=csv_2.sort_index(axis=1)                         #data arrange in columns
print(csv_12)
csv_13=csv_2.loc[[1,2],["name","city"]]                 #by using we get only this data of rows and columns
print(csv_13)
csv_14=csv_2.loc[:,["name","city"]]                        #to get all data of name and city as coulms
print(csv_14)
csv_15=csv_2.loc[[2,3],:]                                 #to get rows 
print(csv_15)


   




