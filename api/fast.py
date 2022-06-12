from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting":"medical_insurance"}

@app.get("/evaluation")
def predict(age,bmi,children,sex_category,smoker_category,region_northeast,region_northwest,region_southeast,region_southwest):

    predict_dict={"age":[int(age)],
                  "bmi":[int(bmi)],
                  "children":[int(children)],
                  "sex_category":[int(sex_category)],
                  "smoker_category":[int(smoker_category)],
                  "region_northeast":[int(region_northeast)],
                  "region_northwest":[int(region_northwest)],
                  "region_southeast":[int(region_southeast)],
                  "region_southwest":[int(region_southwest)]}

    X_pred=pd.DataFrame(predict_dict)

    model=load("model.joblib")

    prediction = model.predict(X_pred)
    print(round(prediction[0],2))
    prediction_round = round(prediction[0],2)
    return {"Annual Medical Expenditure":prediction_round}

# predict(60,29,5,1,0,0,0,0,1)
# ?age=60&bmi=29&children=5&sex_category=1&smoker_category=0&region_northeast=0&region_northwest=0&region_southeast=1&region_southwest=0
