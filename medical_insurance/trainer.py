from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import RobustScaler, StandardScaler
from medical_insurance.data import get_expenses
from termcolor import colored
import joblib

class expenses_trainer(object):

    def __init__(self):
        """
        X:pandas DataFrame
        y:pandas Series
        """
        self.pipeline=None
        self.data=get_expenses()
        self.X=self.data.drop(columns='charges')
        self.y=self.data['charges']
        self.model=None

    def run_model(self):
        X=self.X
        y=self.y

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
        lin_model=LinearRegression().fit(X_train,y_train)

        self.model=lin_model

    def save_model_locally(self):
        """
        Save model into joblib format
        """
        joblib.dump(self.model,"model.joblib")
        print(colored("Model joblib saved locally","green"))

if __name__ == '__main__':
    print("its workingg :D")

    trainer=expenses_trainer()
    X_train,X_test,y_train,y_test=train_test_split(trainer.X,trainer.y,test_size=0.3)
    trainer.run_model()

    accuracy= trainer.model.score(X_test,y_test)
    print ("accuracy = ", accuracy)

    trainer.save_model_locally()
