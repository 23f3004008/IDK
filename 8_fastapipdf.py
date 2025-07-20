from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    target_product = "Gadget"  # <-- Replace with actual product name shown in the portal
    total_sum = 0

    contents = await file.read()
    with pdfplumber.open(io.BytesIO(contents)) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if not table:
                continue

            headers = table[0]
            rows = table[1:]

            try:
                product_idx = headers.index("Product")
                total_idx = headers.index("Total")
            except ValueError:
                continue

            for row in rows:
                if len(row) > max(product_idx, total_idx) and \
                   row[product_idx] == target_product:
                    try:
                        clean_value = re.sub(r"[^\d.]", "", str(row[total_idx]))
                        total_sum += float(clean_value)
                    except (ValueError, TypeError):
                        continue

    return {"sum": round(total_sum, 2)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)