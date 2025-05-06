import pandas as pd
rabia=[12,13,14,15]
rehman=pd.Series(rabia)
print(rehman)

#labeling
import pandas as pd
rabia2=[12,145,235,45]
rehman2=pd.Series(rabia2)
print(rehman2[2])

#selfindexing
import pandas as pd
rabia3=[12,56,78]
rehman3=pd.Series(rabia3,index=["x","y","z"])
print(rehman3["y"])

#dictionary
import pandas as pd
qudsia={
    "aqsa":23,
    "urooj":34,
    "qudsia":25
}
ashfaq=pd.Series(qudsia)
print(ashfaq)

#list in dict
import pandas as pd
qudsia={
    "aqsa":[12,45,25,16],
    "urooj":[45,67,89,23],
    "akbar":[12,78,45,23]
}
saqib=pd.Series(qudsia)
print(saqib.iloc[[0,1]])

#if_else conditions
# a=int(input("enter your age:"))
# print("your age is:" ,a)
# if(a>19):
#     print("yes you can drive")
# elif(a<19):
#     print("you cannot drive20")  
# else:
#     print("yes")   

#while
i=0
while(i<3):
    print(i)
    i=i+1

#list2
import pandas as pd
subject=["math","science","history","english"]
marks=[90,80,50]
subject2=pd.Series(subject)
marks2=pd.Series(marks)
print(subject2)
print(marks2)
var=subject2 + '-'+  marks2.astype(str)
print(var)
# var = pd.concat([subject2, marks2], ignore_index=True)
# print(var)

