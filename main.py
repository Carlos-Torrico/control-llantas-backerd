from fastapi import FastAPI

app = FastAPI(title="Control Llantas Global - Backend")

@app.get("/")
def read_root():
    return {"status": "online", "message": "Backend de Control de Llantas funcionando al 100%"}
