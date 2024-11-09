import pandas as pd
student_dic={"RRR":100,"ABC":78,"DEF":98,"XYZ":87}
series_a=pd.Series(student_dic)
print(series_a.iloc[2])
print(series_a.loc["RRR"])