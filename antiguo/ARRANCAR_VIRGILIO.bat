@echo off
title NUCLEO VIRGILIO - TERMINAL SOBERANA
echo [!] Iniciando Motores de Virgilio...
start /min python C:\VIRGILIO_CORE\MONITOR.py
start /min C:\VIRGILIO_CORE\bin\virgilio_engine.exe
echo [OK] El Agente esta escuchando. 
echo [!] Suelte archivos en EL CAJON o hablele por Telegram.
pause
