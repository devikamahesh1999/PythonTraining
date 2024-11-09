import re
#pattern='[0-9]+'
#string='My phn no is 8547307776 and age is 25'
#result=re.findall(pattern,string)
#print(result)

pattern=r'\bs\w+'
string='She will bring the sea food'
result=re.findall(pattern,string,re.IGNORECASE)
print(result)