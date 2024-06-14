from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import uvicorn
import numpy as np
import cv2
from tensorflow.keras.models import load_model

app = FastAPI()

# Carregar o modelo treinado
model = load_model('model/modelo.h5')

# Configurar templates e arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    # Verificar se o arquivo é uma imagem
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem.")

    # Ler a imagem
    image = await file.read()
    image = np.frombuffer(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (28, 28))  # Ajustar o tamanho para o modelo
    image = image.reshape(1, 28, 28, 1).astype('float32') / 255  # Normalizar a imagem

    # Fazer a predição
    prediction = model.predict(image)
    digit = np.argmax(prediction)

    return {"digit": int(digit)}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
