#in series we write a program:
import pandas as pd
qudsia=[1,2,3,4]
qudsiaashfaq=pd.Series(qudsia)
print(qudsiaashfaq)

#accessing the data 

import pandas as pd
qudsia=[34,67,45,12]
ali=pd.Series(qudsia)
print(ali[1])

#self indexing

import pandas as pd
ahmad=[23,34,56,78]
ali2=pd.Series(ahmad,index=["x","y","z","e"])
print(ali2)                            

#accessing by self indexing

import pandas as pd
ahmad=[23,34,56,78]
ali2=pd.Series(ahmad,index=["x","y","z","e"])
print(ali2["y"]) 

#series from dictinoary

import pandas as pd
cal={
    "day1":123,
    "day2":1234,
    "day3":12345,
    "day4":12
}
qudsia=pd.Series(cal)
print(qudsia)

#indexing 

import pandas as pd
cal={
    "day1":123,
    "day2":1234,
    "day3":12345,
    "day4":12
}
qudsia=pd.Series(cal,index=["x","y","z","a"])
print(qudsia)

#data frame accessing
import pandas as pd
qudsia2={
 "cal":[12,13,14,15],
 "cal2":[16,17,18,19]
}
ashfaq=pd.DataFrame(qudsia2)
print(ashfaq["cal"])

