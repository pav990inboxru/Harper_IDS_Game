@echo off
chcp 65001 > nul
echo Запуск программы таблиц для Stay Out...
echo Создано Harper_IDS для игрового сообщества IgromanDS

python --version > nul 2>&1
if errorlevel 1 (
    echo Python не найден. Пожалуйста, убедитесь, что Python установлен и добавлен в PATH.
    echo Загрузите Python с официального сайта: https://www.python.org/downloads/
    pause
    exit /b 1
)

python main.py
if errorlevel 1 (
    echo Ошибка при запуске программы. Проверьте, установлены ли все зависимости.
    echo Запустите сначала файл setup.bat для установки зависимостей.
    pause
    exit /b 1
)
pause