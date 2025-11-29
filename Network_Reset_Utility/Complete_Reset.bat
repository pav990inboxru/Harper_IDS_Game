@echo off
color 04
title COMPLETE RESET - Full Network Stack Reset - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                    COMPLETE RESET - Full Network Stack Reset                *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo WHAT THIS DOES: Complete network stack reset, removes all network profiles
echo RISKS: Complete network configuration loss, requires restart, need to reconfigure WiFi
echo BENEFITS: Fixes all network-related issues, like starting fresh
echo.
echo *******************************************************************************
echo * ПЕРЕВОД НА РУССКИЙ: ПОЛНЫЙ СБРОС - Полный сброс сетевого стека            *
echo * ЧТО ЭТО ДЕЛАЕТ: Полный сброс сетевого стека, удаляет все сетевые профили  *
echo * РИСКИ: Полная потеря сетевой конфигурации, требуется перезагрузка,        *
echo *        нужно заново настроить Wi-Fi                                       *
echo * ПРЕИМУЩЕСТВА: Исправляет все проблемы, связанные с сетью, как начать      *
echo *              с нуля                                                        *
echo *******************************************************************************
echo.
echo Press any key to continue with complete reset...
echo WARNING: This will require a system restart to complete!
echo WARNING: You will lose all network profiles and configurations!
pause >nul

netsh winsock reset catalog
netsh int ip reset
netsh int ipv4 reset
netsh int ipv6 reset
netsh advfirewall reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns

echo.
echo Complete reset completed!
echo.
echo Please restart your computer now to complete the process.
echo You will need to reconfigure your network connections after restart.
echo You can now close this window or press any key to exit.
pause >nul