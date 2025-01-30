from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes. Para mayor seguridad, especifica el dominio de tu app Flutter.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permite todos los headers
)

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Emanuel"}

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}
#uvicorn main:app --host 0.0.0.0 --port 8000 --reload
