@echo off
chcp 65001 > nul
echo Установка всех необходимых зависимостей для программы таблиц Stay Out...
echo Создано Harper_IDS для IgromanDS

REM Проверка наличия Python
python --version > nul 2>&1
if errorlevel 1 (
    echo Python не найден. Пожалуйста, установите Python с https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Используем python -m pip вместо прямого вызова pip
echo Проверка и обновление pip...
python -m pip --version > nul 2>&1
if errorlevel 1 (
    echo pip не найден как модуль Python. Пытаемся установить...
    python -m ensurepip --upgrade
    if errorlevel 1 (
        echo Не удалось установить pip. Пожалуйста, убедитесь, что Python установлен правильно.
        echo Попробуйте установить Python с https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

REM Обновление pip
echo Обновление pip...
python -m pip install --upgrade pip

REM Установка зависимостей из requirements.txt
echo Установка зависимостей из requirements.txt...
if exist requirements.txt (
    python -m pip install -r requirements.txt
) else (
    echo Файл requirements.txt не найден, устанавливаем стандартные зависимости...
    python -m pip install Pillow
)

REM Установка дополнительных полезных пакетов
echo Установка дополнительных пакетов...
python -m pip install --upgrade setuptools wheel

echo.
echo Установка всех зависимостей завершена!
echo Теперь вы можете запустить программу с помощью файла "Запустить_Программу.bat"
pause