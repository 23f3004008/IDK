from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import csv
import io
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"]
)

EMAIL = "yourmail"  # Replace with your email
EXAM_ID = "tds-2025-05-roe"

def clean_text(text: str) -> str:
    return text.strip().lower()

def clean_amount(raw: str) -> float:
    raw = raw.strip().replace(" ", "")
    raw = raw.replace(",", ".") 
    return float(re.sub(r"[^\d.]", "", raw)) 

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    decoded = content.decode("utf-8", errors="ignore")
    reader = csv.reader(io.StringIO(decoded))

    headers = next(reader, [])
    food_total = 0.0

    for row in reader:
        if len(row) < 4:
            continue  
        name, date_str, amount_str, category = row[:4]

        if clean_text(category) == "food":
            try:
                amount = clean_amount(amount_str)
                food_total += amount
            except ValueError:
                continue 

    return {
        "answer": round(food_total, 2),
        "email": EMAIL,
        "exam": EXAM_ID
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("2_csv_fastapi:app", host="0.0.0.0", port=8004, reload=True)
