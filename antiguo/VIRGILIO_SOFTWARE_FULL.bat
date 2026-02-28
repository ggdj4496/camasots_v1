@echo off
title VIRGILIO OS - FULL SOFTWARE
cd /d "%~dp0\CORE"
echo ?? LANZANDO INSTALADOR DE DEPENDENCIAS...
python installer.py
echo ?? INICIANDO N?CLEO VIRGILIO...
python virgilio_main.py
pause
