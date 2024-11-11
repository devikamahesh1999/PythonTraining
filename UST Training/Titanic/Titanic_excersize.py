import pandas as pd 
df=pd.read_csv(r"C:\Users\Administrator\Desktop\PythonTraining\UST Training\Titanic\Titanic\titanic.csv")

#calculate the average age of passengers who survived
avg_age_survived=df[df['Survived']]==1['Age'].mean()

#Calculate the average age of passengers who didn't survive
avg_age_notsurvived=df[df['Survived']]==0['Age'].mean()

print("Average age of survivors: ",avg_age_survived)
print("Average age of non-survivors: ",avg_age_notsurvived)