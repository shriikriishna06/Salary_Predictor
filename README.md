# Salary Predictor

Small demo that estimates annual CTC for Indian tech roles using a tiny ML model.

Quick start
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run backend:
```bash
uvicorn app:app --reload
```
3. Open `index.html` in your browser and run a prediction.

API
- POST `/predict` — accepts `Experience`, `Role`, `Location`, `Education`, `Company_Type` and returns `salary`.

Files
- `app.py` — backend
- `index.html` — frontend
- `script.js` — frontend logic
- `india_job_market_2026.xlsx` — dataset (placed in project root)

