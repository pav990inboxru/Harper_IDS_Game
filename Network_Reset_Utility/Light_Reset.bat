@echo off
color 0A
title LIGHT RESET - DNS Cache Clear - Harper_IDS for IgromanDS

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
pause >nul

ipconfig /flushdns

echo.
echo DNS cache cleared successfully!
echo.
echo You can now close this window or press any key to exit.
pause >nul