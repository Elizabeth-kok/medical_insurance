import os
import pandas as pd
from medical_insurance.utils import cleandata
def get_expenses():
    """
    This function takes in the expenses data and returns the cleaned expenses data
    """
    current_dir=os.path.dirname(__file__)
    raw_data_dir=os.path.join(current_dir,"..","raw_data")
    expenses_data=os.path.join(raw_data_dir,'expenses.csv')
    data=pd.read_csv(expenses_data)
    data=cleandata(data)
    return data

# data=get_expenses()
# print(data.head())
