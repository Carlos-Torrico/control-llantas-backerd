from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
import uvicorn

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
    <body class="bg-slate-100 min-h-screen flex items-center justify-center p-4">
        <div class="bg-white rounded-xl shadow-lg p-6 w-full max-w-lg">
            <h1 class="text-2xl font-bold text-slate-800 mb-6 text-center">Control de Llantas - Global</h1>
            <form action="/guardar-llanta" method="POST" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-1">Empresa / Cliente</label>
                    <input type="text" name="empresa" required placeholder="Ej. Transportes del Sur" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none">
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-1">Unidad / Placa</label>
                    <input type="text" name="unidad" required placeholder="Ej. ABC-123" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none">
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-1">Marcado a Fuego</label>
                    <input type="text" name="marcado_fuego" required placeholder="Ej. F-01" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none">
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-1">Posición de Eje</label>
                    <input type="number" name="posicion" required placeholder="Ej. 2" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none">
                </div>
                <div>
                    <label class="block text-sm font-medium text-slate-700 mb-1">Profundidad de Cocada (mm)</label>
                    <input type="step" step="0.1" name="profundidad" required placeholder="Ej. 14.5" class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none">
                </div>
                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg transition duration-200">
                    Guardar Registro
                </button>
            </form>
        </div>
    </body>
    </html>
    """
    return html_content

@app.post("/guardar-llanta")
def guardar_llanta(
    empresa: str = Form(...),
    unidad: str = Form(...), 
    marcado_fuego: str = Form(...), 
    posicion: int = Form(...), 
    profundidad: float = Form(...)
):
    return {
        "status": "success",
        "mensaje": f"Llanta {marcado_fuego} de la empresa {empresa} (Unidad {unidad}) registrada correctamente.",
        "datos": {
            "empresa": empresa,
            "unidad": unidad,
            "marcado_fuego": marcado_fuego,
            "posicion": posicion,
            "profundidad_mm": profundidad
        }
    }

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
