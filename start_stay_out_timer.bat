@echo off
REM Ярлык для запуска Stay Out Timer на Windows 11
REM Этот файл запускает приложение с иконкой в стиле STALKER
cd /d "%~dp0"
if exist "dist\StayOutTimer.exe" (
    start "" "dist\StayOutTimer.exe"
) else (
    echo Файл StayOutTimer.exe не найден в папке dist
    pause
)