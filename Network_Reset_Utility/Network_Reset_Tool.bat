@echo off
color 0A
title Network Reset Utility - Developed by Harper_IDS for IgromanDS

REM ******************************************************************************
REM *                   СЕТЕВАЯ УТИЛИТА СБРОСА (ПЕРЕВОД НА РУССКИЙ ЯЗЫК)         *
REM *                   Network Reset Utility (Russian Translation)              *
REM *                   Разработчик: Harper_IDS                                  *
REM *                   Для игрового сообщества IgromanDS                        *
REM ******************************************************************************
REM *
REM * ОПИСАНИЕ:
REM * Эта утилита предназначена для устранения сетевых проблем, вызванных VPN,
REM * изменениями DNS и различными сетевыми инструментами (zapret-discord-youtube,
REM * nekobox, nekoray, adguard и др.), которые нарушают сетевые настройки Windows 11.
REM *
REM * ОСНОВНЫЕ ВОЗМОЖНОСТИ:
REM * - Легкий сброс: Очистка только кэша DNS (перезагрузка не требуется)
REM * - Средний сброс: Очистка DNS, ARP, кэша NetBIOS и сброс Winsock (перезагрузка не требуется)
REM * - Тяжелый сброс: Сброс стека TCP/IP и сетевых адаптеров (перезагрузка не требуется)
REM * - Полный сброс: Полный сброс сети (рекомендуется перезагрузка)
REM * - Все операции включают подробные объяснения того, что они делают, риски и преимущества
REM ******************************************************************************

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

:menu
cls
echo.
echo ********************************************************************************
echo *                       NETWORK RESET UTILITY                                  *
echo *                     Developed by Harper_IDS                                  *
echo *                 For IgromanDS Gaming Community                               *
echo ********************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ================================================================================
echo.
echo Select reset mode:
echo.
echo [1] LIGHT - Clear DNS cache only (Recommended for minor issues)
echo [2] MEDIUM - Clear DNS, ARP, NetBIOS cache and reset Winsock
echo [3] HEAVY - Reset TCP/IP stack and network adapters
echo [4] COMPLETE - Full network reset (Requires restart)
echo [5] VIEW_CURRENT_SETTINGS - Show current network configuration
echo [6] HELP - Detailed information about each option
echo [0] EXIT - Close the utility
echo.
set /p choice="Enter your choice (0-6): "

if "%choice%"=="1" goto light_reset
if "%choice%"=="2" goto medium_reset
if "%choice%"=="3" goto heavy_reset
if "%choice%"=="4" goto complete_reset
if "%choice%"=="5" goto view_settings
if "%choice%"=="6" goto help
if "%choice%"=="0" goto exit

echo.
echo Invalid choice! Please select 0-6.
timeout /t 2 >nul
goto menu

:light_reset
echo.
echo LIGHT RESET: Clearing DNS cache only...
echo.
echo WHAT THIS DOES: Clears DNS cache to resolve minor DNS resolution issues
echo RISKS: Minimal - No network disruption
echo BENEFITS: Fixes temporary DNS problems, clears old DNS entries
echo.
echo ***************************************************************************
echo * ПЕРЕВОД НА РУССКИЙ: ЛЕГКИЙ СБРОС - Очистка только кэша DNS              *
echo * ЧТО ЭТО ДЕЛАЕТ: Очищает кэш DNS для решения незначительных проблем       *
echo * РИСКИ: Минимальны - Без прерывания сети                                  *
echo * ПРЕИМУЩЕСТВА: Исправляет временные проблемы с DNS, очищает старые записи *
echo ***************************************************************************
echo.
pause
ipconfig /flushdns
echo.
echo DNS cache cleared successfully!
pause
goto menu

:medium_reset
echo.
echo MEDIUM RESET: Clearing DNS, ARP, NetBIOS cache and resetting Winsock...
echo.
echo WHAT THIS DOES: Clears multiple network caches and resets Windows socket layer
echo RISKS: Temporary network disconnection, may need to reconnect to WiFi
echo BENEFITS: Resolves most network cache-related issues, fixes socket problems
echo.
echo ***************************************************************************
echo * ПЕРЕВОД НА РУССКИЙ: СРЕДНИЙ СБРОС - Очистка кэша и сброс Winsock        *
echo * ЧТО ЭТО ДЕЛАЕТ: Очищает несколько сетевых кэшей и сбрасывает уровень    *
echo *                сокетов Windows                                          *
echo * РИСКИ: Временное отключение от сети, может потребоваться повторное      *
echo *        подключение к Wi-Fi                                              *
echo * ПРЕИМУЩЕСТВА: Решает большинство проблем, связанных с кэшем сети,       *
echo *              исправляет проблемы с сокетами                             *
echo ***************************************************************************
echo.
pause
ipconfig /flushdns
ipconfig /registerdns
nbtstat -R
netsh winsock reset
echo.
echo Medium reset completed!
pause
goto menu

:heavy_reset
echo.
echo HEAVY RESET: Resetting TCP/IP stack and network adapters...
echo.
echo WHAT THIS DOES: Resets TCP/IP stack to default configuration, resets network adapters
echo RISKS: Complete network disconnection, requires network reconnection
echo BENEFITS: Fixes deep TCP/IP stack issues, resolves adapter problems
echo.
echo ***************************************************************************
echo * ПЕРЕВОД НА РУССКИЙ: ТЯЖЕЛЫЙ СБРОС - Сброс стека TCP/IP и адаптеров      *
echo * ЧТО ЭТО ДЕЛАЕТ: Сбрасывает стек TCP/IP к конфигурации по умолчанию,     *
echo *                сбрасывает сетевые адаптеры                              *
echo * РИСКИ: Полное отключение от сети, требуется повторное подключение       *
echo * ПРЕИМУЩЕСТВА: Исправляет глубокие проблемы со стеком TCP/IP,            *
echo *              решает проблемы с адаптерами                               *
echo ***************************************************************************
echo.
pause
netsh int ip reset
netsh int ipv4 reset
netsh int ipv6 reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
echo.
echo Heavy reset completed! You may need to reconnect to your network.
pause
goto menu

:complete_reset
echo.
echo COMPLETE RESET: Full network reset (Requires restart)...
echo.
echo WHAT THIS DOES: Complete network stack reset, removes all network profiles
echo RISKS: Complete network configuration loss, requires restart, need to reconfigure WiFi
echo BENEFITS: Fixes all network-related issues, like starting fresh
echo.
echo WARNING: This will require a system restart to complete!
echo ***************************************************************************
echo * ПЕРЕВОД НА РУССКИЙ: ПОЛНЫЙ СБРОС - Полный сброс сети                   *
echo * ЧТО ЭТО ДЕЛАЕТ: Полный сброс сетевого стека, удаляет все сетевые        *
echo *                профили                                                  *
echo * РИСКИ: Полная потеря сетевой конфигурации, требуется перезагрузка,      *
echo *        нужно заново настроить Wi-Fi                                     *
echo * ПРЕИМУЩЕСТВА: Исправляет все проблемы, связанные с сетью, как начать    *
echo *              с нуля                                                      *
echo ***************************************************************************
pause
netsh winsock reset catalog
netsh int ip reset
netsh int ipv4 reset
netsh int ipv6 reset
netsh advfirewall reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns
echo.
echo Complete reset completed! Please restart your computer now.
pause
goto menu

:view_settings
echo.
echo CURRENT NETWORK CONFIGURATION:
echo.
ipconfig /all
echo.
pause
goto menu

:help
echo.
echo DETAILED INFORMATION ABOUT EACH OPTION:
echo.
echo [1] LIGHT - Clear DNS cache only (Recommended for minor issues)
echo     - Use this for temporary DNS resolution problems
echo     - No network interruption
echo     - Quick and safe
echo.
echo [2] MEDIUM - Clear DNS, ARP, NetBIOS cache and reset Winsock (Recommended for moderate issues)
echo     - Fixes most cache-related network problems
echo     - Resets Windows socket layer
echo     - May require reconnecting to WiFi
echo.
echo [3] HEAVY - Reset TCP/IP stack and network adapters (For persistent issues)
echo     - Resets TCP/IP to default state
echo     - Fixes deep network stack problems
echo     - Requires network reconnection
echo.
echo [4] COMPLETE - Full network reset (For severe issues, requires restart)
echo     - Total network stack reset
echo     - Removes all network profiles and configurations
echo     - Like starting fresh, but requires reconfiguration
echo.
echo [5] VIEW_CURRENT_SETTINGS - Show current network configuration
echo     - Displays all network adapters and their settings
echo     - Useful for troubleshooting
echo.
echo [6] HELP - This help screen
echo.
pause
goto menu

:exit
echo.
echo Thank you for using Network Reset Utility by Harper_IDS for IgromanDS!
echo.
pause
exit