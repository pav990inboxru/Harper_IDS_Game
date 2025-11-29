@echo off
color 0A
title LIGHT RESET - DNS Cache Clear - Harper_IDS for IgromanDS

REM Проверка прав администратора
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo *******************************************************************************
    echo *                    ТРЕБУЮТСЯ ПРАВА АДМИНИСТРАТОРА                          *
    echo *            Эта программа требует права администратора                      *
    echo *       Пожалуйста, запустите этот файл от имени администратора              *
    echo *******************************************************************************
    echo.
    pause
    exit /b
)

echo.
echo *******************************************************************************
echo *                        LIGHT RESET - DNS CACHE CLEAR                        *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo WHAT THIS DOES: Clears DNS cache to resolve minor DNS resolution issues
echo RISKS: Minimal - No network disruption
echo BENEFITS: Fixes temporary DNS problems, clears old DNS entries
echo.
echo *******************************************************************************
echo * ПЕРЕВОД НА РУССКИЙ: ЛЕГКИЙ СБРОС - Очистка кэша DNS                        *
echo * ЧТО ЭТО ДЕЛАЕТ: Очищает кэш DNS для решения незначительных проблем         *
echo * РИСКИ: Минимальны - Без прерывания сети                                     *
echo * ПРЕИМУЩЕСТВА: Исправляет временные проблемы с DNS, очищает старые записи    *
echo *******************************************************************************
echo.
echo Press any key to continue with DNS cache clear...
echo ВНИМАНИЕ: Убедитесь, что вы хотите выполнить эту операцию!
pause >nul

ipconfig /flushdns

echo.
echo DNS cache cleared successfully!
echo.
echo You can now close this window or press any key to exit.
pause >nul