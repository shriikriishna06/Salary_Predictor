# 💰 PayLensAI

Small demo that estimates annual CTC for Indian tech roles using a tiny ML(Linear Reg.) model.<br>
Live on : https://paylensai.netlify.app<br>
⚠️IMP NOTE: Backend deployed on Render (free tier), may sleep causing cold starts...

# 📜 About
PayLensAI is a lightweight demo that estimates annual CTC (salary in LPA) for Indian tech roles using a small, transparent machine learning model trained on a curated 2026 dataset.

🎯Key points:
- Inputs: Experience, Role, Location, Education, Companytype — output: estimated salary.
- Model: simple, interpretable regression with straightforward preprocessing so results are easy to inspect and reproduce.

❗Limitations:
- Trained on a limited dataset; may reflect sampling bias and market changes.
- Predictions are approximate.


# 🚀 Quick start
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run backend:
```bash
python -m uvicorn app:app --reload
```
3. Open `index.html` in your browser and run a prediction.

# 🔌API
- POST `/predict` — accepts `Experience`, `Role`, `Location`, `Education`, `Company_Type` and returns `salary`.

# 📁 Files
- `app.py` — backend
- `index.html` — frontend
- `script.js` — frontend logic
- `india_job_market_2026.xlsx` — dataset (placed in project root)

