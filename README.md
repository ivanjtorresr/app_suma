# Proyecto: App de Suma con Tkinter + Tests + EXE + CI/CD

Este proyecto demuestra:
- Crear entorno virtual y requirements.
- Crear GUI básica con Tkinter.
- Tests unitarios con unittest.
- Generar `.exe` con PyInstaller.
- CI con GitHub Actions para pruebas.
- Pipeline para generar `.exe` automáticamente al hacer push en `main`.

## 1. Entorno virtual

```bash
python -m venv .venv
# Activación en Windows
.\.venv\Scripts\activate
# Activación en Linux/Mac
source .venv/bin/activate
```

Instalar dependencias y generar requirements:

```bash
pip install -r requirements.txt
pip freeze > requirements.txt
```

## 2. Ejecutar la app

```bash
python app.py
```

## 3. Ejecutar tests

```bash
python -m unittest discover -v
```

## 4. Generar EXE local

```bash
pyinstaller --onefile --windowed app.py
```
El ejecutable se guarda en `dist/app.exe`.

## 5. CI en GitHub

En `.github/workflows/ci.yml` se ejecutan los tests automáticamente.

## 6. Build automático del EXE en main

`.github/workflows/build-exe.yml` genera el `.exe` en Windows y lo sube como artefacto.
