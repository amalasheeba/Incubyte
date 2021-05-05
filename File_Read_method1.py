#import module
import pandas as pd

Country= input("Enter Country name:")

#read text file into pandas DataFrame
df = pd.read_csv("Customer_" + Country + ".txt", sep="|")

#display DataFrame
print(df)