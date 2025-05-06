import pandas as pd
csv_2=pd.read_csv("C:\\Users\\PC\\Downloads\\Untitled spreadsheet - Sheet1.csv")
print(csv_2)
csv=csv_2.dropna()         #dropna function is use to del the null value columns
print(csv)

#parameters of dropna functions
import pandas as pd
csv_2=pd.read_csv("C:\\Users\\PC\\Downloads\\Untitled spreadsheet - Sheet1.csv")
print(csv_2)
csv=csv_2.dropna(axis=1)         #axis =1 is used to dropna value in columna and axis=0 is use to drop value in rows
print(csv)

#subset parameters
import pandas as pd
csv_2=pd.read_csv("C:\\Users\\PC\\Downloads\\Untitled spreadsheet - Sheet1.csv")
print(csv_2)
csv=csv_2.dropna(subset=["name"])         
print(csv)

#fillna function to fill the values
import pandas as pd
csv_2=pd.read_csv("C:\\Users\\PC\\Downloads\\Untitled spreadsheet - Sheet1.csv")
print(csv_2)
csv=csv_2.fillna("qudsia")        #the blank place enter the thing which we enter
print(csv)


#replace and interpolate function
import pandas as pd
csv=pd.read_excel("C:\\Users\\PC\\Documents\\myfile.csv.xlsx")
print(csv)
csv_2=csv.replace(to_replace=1,value=100)
print(csv_2)
csv_3=csv.replace([7,12,1,3,14],1000)
print(csv_3)

