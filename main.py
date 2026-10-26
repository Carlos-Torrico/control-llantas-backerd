from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI(title="Control Llantas Global - Backend")

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Control de Llantas Global</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-100 font-sans p-4">
        <div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl p-6 mt-6">
            <h2 class="text-2xl font-bold text-slate-800 mb-4 text-center">Control de Llantas Global</h2>
            <p class="text-sm text-slate-500 mb-6 text-center">Registro de inspección y profundidad de cocada</p>
            
            <form action="/guardar-llanta" method="POST" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium text-slate-700">Placa del Vehículo / Unidad:</label>
                    <input type="text" name="unidad" required class="mt-1 block w-full rounded-md border border-slate-300 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                </div>
                
                <div>
                    <label class="block text-sm font-medium text-slate-700">Número de Marcado a Fuego:</label>
                    <input type="text" name="marcado_fuego" required class="mt-1 block w-full rounded-md border border-slate-300 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                </div>

                <div>
                    <label class="block text-sm font-medium text-slate-700">Posición del Eje (Ej: 1 al 10):</label>
                    <input type="number" name="posicion" required class="mt-1 block w-full rounded-md border border-slate-300 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                </div>

                <div>
                    <label class="block text-sm font-medium text-slate-700">Profundidad de Cocada Actual (mm):</label>
                    <input type="number" step="0.1" name="profundidad" required class="mt-1 block w-full rounded-md border border-slate-300 p-2 shadow-sm focus:border-indigo-500 focus:ring-indigo-500">
                </div>

                <button type="submit" class="w-full bg-indigo-600 text-white font-bold p-3 rounded-md hover:bg-indigo-700 transition">
                    Guardar Registro
                </button>
            </form>
        </div>
    </body>
    </html>
    """
    return html_content

@app.post("/guardar-llanta")
def guardar_llanta(unidad: str = Form(...), marcado_fuego: str = Form(...), posicion: int = Form(...), profundidad: float = Form(...)):
    # Aquí conectaremos con Supabase en el siguiente paso
    return {
        "status": "success",
        "mensaje": f"Llanta {marcado_fuego} de la unidad {unidad} registrada correctamente.",
        "datos": {
            "unidad": unidad,
            "marcado_fuego": marcado_fuego,
            "posicion": posicion,
            "profundidad_mm": profundidad
        }
    }
import os
import uvicorn

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
