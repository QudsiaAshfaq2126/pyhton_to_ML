#dataframe
import pandas as pd

data={
    "cal":[12,13,14,15],
    "cal2":[16,17,18,19],
    "cal3":[12,56,23,24]
}
data2=pd.DataFrame(data)
print(data2)

# #accessing

import pandas as pd

data={
    "cal":[12,13,14,15],
    "cal2":[16,17,18,19],
    "cal3":[12,56,23,24]
}
data2=pd.DataFrame(data)
print(data2["cal"])

# #locate row

import pandas as pd

data={
    "cal":[12,13,14,15],
    "cal2":[16,17,18,19],
    "cal3":[12,56,23,24]
}
data2=pd.DataFrame(data)
print(data2)
print(data2.loc[1,"cal2"])
print(data2.iloc[[1,2]])
print(data2.iloc[0])

#self indexing

import pandas as pd

data={
     "cal":[12,13,14,15],
     "cal2":[16,17,18,19],
     "cal3":[12,56,23,24]
 }
data2=pd.DataFrame(data,index=["day1","day2","day3","day4"])
print(data2)

# #locate the name indexing

import pandas as pd

data={
    "cal":[12,13,14,15],
    "cal2":[16,17,18,19],
    "cal3":[12,56,23,24]
}
data2=pd.DataFrame(data,index=["day1","day2","day3","day4"])
print(data2.loc[["day1","day2"]])
print(data2.loc["day1"])

#insert data in pandas

import pandas as pd
var={
    "a":[12,13,14,15],
    "b":[16,17,18,19]
}
var2=pd.DataFrame(var)
print(var2)
var2.insert(1,"python",var["a"])
print(var2)
var2.insert(1,"python_1",[12,13,14,15])
print(var2)

#if we want to access first elements

import pandas as pd
var={
    "a":[12,13,14,15],
    "b":[16,17,18,19]
}
var2=pd.DataFrame(var)
print(var2)
var2.insert(1,"python_1",[12,13,14,15])
var2["python2"]=var2["b"][:3]
print(var2)

#how we delete values bt using pop amd del function

import pandas as pd
var={
    "a":[12,13,14,15],
    "b":[16,17,18,19]
}
var2=pd.DataFrame(var)
print(var2)
var2.insert(1,"python_1",[12,13,14,15])
var2["python2"]=var2["b"][:3]
var2.pop("python_1")
var2.pop("b")
del var2["a"]
print(var2)













