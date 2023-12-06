import pandas as pd

time_encoding = pd.read_csv("step2/missing_values_deleted.csv", sep=",", low_memory=False)

hrmn=pd.cut(time_encoding['hrmn'],24,labels=[str(i) for i in range(0,24)])
time_encoding['hrmn']=hrmn.values
time_encoding.to_csv("step3/time_encoding.csv", index=False)