Write-Host 'iniciando trinidad: dante, aria y virgilio activos...' -ForegroundColor Cyan
cd C:\VIGILIA_SISTEMA\ZBRAIN
git pull origin main
Start-Process powershell -ArgumentList '-NoExit', '-Command', 'Write-Host Aria Online -ForegroundColor Magent'
