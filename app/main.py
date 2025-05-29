from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.model import plot_from_image, label_from_image, probs_from_image
from PIL import Image,  UnidentifiedImageError, ImageFile
from io import BytesIO
import os

app = FastAPI()
ImageFile.LOAD_TRUNCATED_IMAGES = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("static", "index.html"))

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        image = Image.open(BytesIO(contents)).convert("RGB")
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Invalid or unreadable image.")

    max_size = (1024, 1024)
    image.thumbnail(max_size)

    label = label_from_image(image)
    probs = probs_from_image(image)
    plot = plot_from_image(image)

    return {
        "label":label,
        "probs":probs,
        "plot":plot
    }