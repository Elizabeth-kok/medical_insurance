import pandas as pd

def encode_sex(x):
   return 0 if x=="female" else 1

def encode_smoker(x):
   return 0 if x=="no" else 1

def cleandata(data):
    data['sex_category']=data['sex'].map(encode_sex)
    data['smoker_category']=data['smoker'].map(encode_smoker)
    data=pd.get_dummies(data, columns=['region'])
    data=data.drop(columns=['sex','smoker'])
    return data
