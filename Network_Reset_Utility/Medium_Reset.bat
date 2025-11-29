@echo off
color 0E
title MEDIUM RESET - Network Cache & Winsock Reset - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                    MEDIUM RESET - Network Cache & Winsock Reset             *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo WHAT THIS DOES: Clears multiple network caches and resets Windows socket layer
echo RISKS: Temporary network disconnection, may need to reconnect to WiFi
echo BENEFITS: Resolves most network cache-related issues, fixes socket problems
echo.
echo *******************************************************************************
echo * ПЕРЕВОД НА РУССКИЙ: СРЕДНИЙ СБРОС - Очистка кэша и сброс Winsock          *
echo * ЧТО ЭТО ДЕЛАЕТ: Очищает несколько сетевых кэшей и сбрасывает уровень       *
echo *                сокетов Windows                                             *
echo * РИСКИ: Временное отключение от сети, может потребоваться повторное         *
echo *        подключение к Wi-Fi                                                 *
echo * ПРЕИМУЩЕСТВА: Решает большинство проблем, связанных с кэшем сети,          *
echo *              исправляет проблемы с сокетами                                *
echo *******************************************************************************
echo.
echo Press any key to continue with medium reset...
pause >nul

ipconfig /flushdns
ipconfig /registerdns
nbtstat -R
netsh winsock reset

echo.
echo Medium reset completed!
echo.
echo You may need to reconnect to your network.
echo You can now close this window or press any key to exit.
pause >nul