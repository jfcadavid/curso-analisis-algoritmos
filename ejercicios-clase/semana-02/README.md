# Laboratorio 02 - Configuración del entorno

Para crear el entorno virtual utilicé `python -m venv venv`.
Lo activé en PowerShell con `.\venv\Scripts\Activate.ps1`.
Verifiqué que apareciera `(venv)` antes de instalar dependencias.
Instalé matplotlib utilizando `pip install matplotlib`.
Generé `requirements.txt` con `pip freeze > requirements.txt`.
Para reproducir el entorno se crea y activa un nuevo entorno virtual.
Luego se ejecuta `pip install -r requirements.txt`.
Finalmente, se comprueban las dependencias utilizando `pip list`.