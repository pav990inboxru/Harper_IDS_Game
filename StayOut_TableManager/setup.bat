@echo off
chcp 65001 > nul
echo Установка зависимостей для программы таблиц Stay Out...
echo Создано Harper_IDS для IgromanDS

python -m pip install --upgrade pip
if errorlevel 1 (
    echo Установка pip не найдена. Пожалуйста, убедитесь, что Python установлен правильно.
    echo Попробуйте установить Python с https://www.python.org/downloads/
    pause
    exit /b 1
)

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo Ошибка при установке зависимостей. Попробуем установить вручную...
    python -m pip install Pillow
    if errorlevel 1 (
        echo Не удалось установить зависимости. Проверьте, правильно ли установлен Python и pip.
        pause
        exit /b 1
    )
)

echo.
echo Установка завершена!
echo Для запуска программы используйте файл "Запустить_Программу.bat"
pause