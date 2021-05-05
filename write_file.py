file1 = open('Customer_Australia.txt', 'w')
L = ["Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active \n", "Jacob|1256|20101012|20121013|MVD|Paul|VIC|AU|06031987|A \n"]

  
# Writing multiple strings
# at a time
file1.writelines(L)
  
# Closing file
file1.close()
  
# Checking if the data is
# written to file or not
file1 = open('Customer_Australia.txt', 'r')
print(file1.read())
file1.close()
