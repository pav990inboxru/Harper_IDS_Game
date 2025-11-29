@echo off
color 0A
title Network Reset Utility Menu - Harper_IDS for IgromanDS

REM ******************************************************************************
REM *                   СЕТЕВАЯ УТИЛИТА СБРОСА - МЕНЮ (ПЕРЕВОД НА РУССКИЙ)       *
REM *                   Network Reset Utility Menu (Russian Translation)           *
REM *                   Разработчик: Harper_IDS                                    *
REM *                   Для игрового сообщества IgromanDS                          *
REM ******************************************************************************/

:menu
cls
echo.
echo ********************************************************************************
echo *                       NETWORK RESET UTILITY MENU                             *
echo *                     Developed by Harper_IDS for IgromanDS                    *
echo ********************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ================================================================================
echo.
echo SELECT A RESET OPTION:
echo.
echo [1] LIGHT RESET - DNS Cache Clear (No restart required)
echo      ^| WHAT: Clears DNS cache only
echo      ^| RISKS: Minimal - No network disruption
echo      ^| BENEFITS: Fixes temporary DNS problems
echo.
echo [2] MEDIUM RESET - Network Cache & Winsock Reset (No restart required)
echo      ^| WHAT: Clears multiple network caches and resets Windows socket layer  
echo      ^| RISKS: Temporary network disconnection
echo      ^| BENEFITS: Resolves most network cache-related issues
echo.
echo [3] HEAVY RESET - TCP/IP Stack & Adapter Reset (No restart required)
echo      ^| WHAT: Resets TCP/IP stack to default configuration
echo      ^| RISKS: Complete network disconnection, requires reconnection
echo      ^| BENEFITS: Fixes deep TCP/IP stack issues
echo.
echo [4] COMPLETE RESET - Full Network Stack Reset (Restart recommended)
echo      ^| WHAT: Complete network stack reset, removes all network profiles
echo      ^| RISKS: Complete network configuration loss
echo      ^| BENEFITS: Fixes all network-related issues, like starting fresh
echo.
echo [5] EXTREME RESET - All-in-One Network Reset (Restart required)
echo      ^| WHAT: Runs ALL network reset commands in sequence
echo      ^| RISKS: Maximum - Complete network configuration loss
echo      ^| BENEFITS: Fixes ALL network-related issues completely
echo.
echo [6] VIEW CURRENT NETWORK SETTINGS
echo [7] RESTART COMPUTER
echo [8] CANCEL PENDING RESTART
echo [0] EXIT
echo.
set /p choice="Enter your choice (0-8): "

if "%choice%"=="1" goto light
if "%choice%"=="2" goto medium
if "%choice%"=="3" goto heavy
if "%choice%"=="4" goto complete
if "%choice%"=="5" goto extreme
if "%choice%"=="6" goto view
if "%choice%"=="7" goto restart
if "%choice%"=="8" goto cancel
if "%choice%"=="0" goto exit

echo.
echo Invalid choice! Please select 0-8.
timeout /t 2 >nul
goto menu

:light
start "" "Light_Reset.bat"
goto menu

:medium
start "" "Medium_Reset.bat"
goto menu

:heavy
start "" "Heavy_Reset.bat"
goto menu

:complete
start "" "Complete_Reset.bat"
goto menu

:extreme
start "" "Extreme_Reset.bat"
goto menu

:view
start "" "View_Network_Settings.bat"
goto menu

:restart
start "" "Restart_Computer.bat"
goto menu

:cancel
start "" "Cancel_Restart.bat"
goto menu

:exit
echo.
echo Thank you for using Network Reset Utility by Harper_IDS for IgromanDS!
echo All rights reserved for IgromanDS community.
pause
exit