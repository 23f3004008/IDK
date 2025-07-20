from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import easyocr
import io
import re

app = FastAPI()


YOUR_EMAIL = "yourmail"  # Replace with your actual email

reader = easyocr.Reader(['en'], gpu=False)

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image_bytes = io.BytesIO(contents)
        image = Image.open(image_bytes).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Ungültige Bilddatei")

    try:
        result = reader.readtext(np.array(image), detail=0)
        full_text = " ".join(result)
    except Exception:
        raise HTTPException(status_code=500, detail="OCR fehlgeschlagen")

    numbers = re.findall(r'\d{8}', full_text)
    if len(numbers) < 2:
        raise HTTPException(status_code=400, detail="Nicht genügend 8-stellige Zahlen gefunden")

    try:
        num1, num2 = int(numbers[0]), int(numbers[1])
        product = num1 * num2
    except Exception:
        raise HTTPException(status_code=400, detail="Fehler beim Rechnen")

    return JSONResponse(content={"answer": product, "email": YOUR_EMAIL})


if __name__ == "__main__":
    import uvicorn
    import numpy as np
    uvicorn.run("2_captcha:app", host="0.0.0.0", port=8002, reload=True)
