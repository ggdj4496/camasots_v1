@echo off
title VIRGILIO_CORE - CONTROL SOBERANO
cd /d C:\VIRGILIO_CORE
echo [SISTEMA] Activando Motor...
python virgilio_engine.py
echo [SISTEMA] Abriendo nexo con el bot...
start https://web.telegram.org/k/#@onlynuds_20bot
pause
