@echo off
chcp 65001 > nul
echo Запуск программы таблиц для Stay Out...
echo Создано Harper_IDS для игрового сообщества IgromanDS

python main.py
if errorlevel 1 (
    echo Ошибка при запуске программы. Проверьте, установлены ли все зависимости.
    echo Запустите сначала файл setup.bat для установки зависимостей.
    pause
    exit /b 1
)
pause