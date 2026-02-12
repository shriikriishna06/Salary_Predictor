import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
#reads the dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "india_job_market_2026.xlsx")

data = pd.read_excel(file_path)

df=pd.DataFrame(data)
#encodes the categorical values
encoded_data=pd.get_dummies(df,columns=["Role","Location","Education","Company_Type"],dtype=int)

model=LinearRegression()

X=encoded_data.drop(columns=["Salary_LPA"])
y=encoded_data["Salary_LPA"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#model is trained on the dataset
model.fit(X_train,y_train)

#pydantic model for validation
class SalaryInput(BaseModel):
    Experience:float
    Role:str
    Location:str
    Education:str
    Company_Type:str

#API
@app.post("/predict")
async def predict(request:SalaryInput):
    try:
        user_input = pd.DataFrame([{
        "Experience": request.Experience,
        "Role": request.Role,
        "Location": request.Location,
        "Education": request.Education,
        "Company_Type": request.Company_Type
        }])

        user_encoded = pd.get_dummies(user_input, dtype=int)
        user_encoded = user_encoded.reindex(
        columns=X.columns,
        fill_value=0
        )
        #prediction on user input
        sal=model.predict(user_encoded)
        
        return {"salary": int(sal[0])}
    except Exception as e:
        return {"error":str(e)}

