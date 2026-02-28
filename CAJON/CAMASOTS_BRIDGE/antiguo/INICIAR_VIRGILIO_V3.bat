@echo off
title VIRGILIO ULTIMATE OS
color 0b
cd /d "%~dp0"
echo [!] VERIFICANDO DEPENDENCIAS...
pip install telethon flask --quiet
echo [!] LANZANDO N?CLEO SOBERANO...
python CORE\virgilio_engine.py
pause
