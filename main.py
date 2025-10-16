import pandas as pd
from sklearn.linear_model import LinearRegression
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


# MOCK_DATA = {
#     "men's age": [20, 25, 30, 35, 40, 45, 50, 22, 28, 32, 38],
#     "mohor": [10000, 20000, 50000, 100000, 300000, 500000, 1000000, 15000, 75000, 150000, 400000],
#     "dowry": [50000, 100000, 250000, 500000, 1000000, 1500000, 2000000, 75000, 300000, 750000, 1200000]
# }
# MOCK_DATA=pd.read_excel(r"C:\Users\Shrikrishna R Prabhu\OneDrive\Desktop\Project\data0.xlsx")
import os
import pandas as pd

file_path = os.path.join(os.path.dirname(__file__), "data0.xlsx")
MOCK_DATA = pd.read_excel(file_path)

class DowryRequest(BaseModel):
    age: str
    salary: str


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
@app.get("/")
def serve_index():
    return FileResponse(os.path.join("static", "index.html"))


@app.post("/predict")
async def predict_dowry(request: DowryRequest):
    """
    Predicts the dowry value based on age and salary.
    """
    try:
   
        df = pd.DataFrame(MOCK_DATA)
        df['dowry'] = pd.to_numeric(df['dowry'], errors='coerce')
        df.fillna(int(df["dowry"].mean()),inplace=True)


        X = df[["men's age", "mohor"]]
        Y = df[["dowry"]]
        
        model = LinearRegression()
        model.fit(X, Y)

        if '-'in request.age:
            lower,upper=map(int,request.age.split('-'))
            age=(lower+upper)//2
        else:
            age=int(request.age)

        if 'k' in request.salary:
            salary=(int(request.salary.split('k')[0]))*1000
        else:
            salary=int(request.salary)

        
        

        predicted_value = model.predict([[age,salary]])

        return {"dowry_value": int(predicted_value[0])}
        
    except Exception as e:
       
        return {"error": str(e)}

