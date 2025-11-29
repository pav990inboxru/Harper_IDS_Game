@echo off
color 0A
title ALL-IN-ONE Network Reset Utility - Harper_IDS for IgromanDS

:menu
cls
echo.
echo ********************************************************************************
echo *                     ALL-IN-ONE NETWORK RESET UTILITY                         *
echo *                     Developed by Harper_IDS for IgromanDS                    *
echo ********************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ================================================================================
echo.
echo QUICK ACCESS MENU:
echo.
echo [1] Run System Check
echo [2] View Current Network Settings
echo [3] Light Reset (DNS only)
echo [4] Medium Reset (Caches + Winsock)
echo [5] Heavy Reset (TCP/IP + Adapters)
echo [6] Complete Reset (Full network stack)
echo [7] Extreme Reset (All commands)
echo [8] Restart Computer
echo [9] Cancel Pending Restart
echo [10] Install Utility Shortcuts
echo [11] Uninstall Utility Shortcuts
echo.
echo [0] Main Menu (Full Network Reset Tool)
echo [X] Exit
echo.
set /p choice="Enter your choice (0-X): "

if /i "%choice%"=="1" goto syscheck
if /i "%choice%"=="2" goto view
if /i "%choice%"=="3" goto light
if /i "%choice%"=="4" goto medium
if /i "%choice%"=="5" goto heavy
if /i "%choice%"=="6" goto complete
if /i "%choice%"=="7" goto extreme
if /i "%choice%"=="8" goto restart
if /i "%choice%"=="9" goto cancel
if /i "%choice%"=="10" goto install
if /i "%choice%"=="11" goto uninstall
if /i "%choice%"=="0" goto main
if /i "%choice%"=="X" goto exit

echo.
echo Invalid choice! Please select 0-X.
timeout /t 2 >nul
goto menu

:syscheck
start "" "System_Check.bat"
goto menu

:view
start "" "View_Network_Settings.bat"
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

:restart
start "" "Restart_Computer.bat"
goto menu

:cancel
start "" "Cancel_Restart.bat"
goto menu

:install
start "" "INSTALL.bat"
goto menu

:uninstall
start "" "UNINSTALL.bat"
goto menu

:main
start "" "Network_Reset_Tool.bat"
goto menu

:exit
echo.
echo Thank you for using Network Reset Utility by Harper_IDS for IgromanDS!
echo All rights reserved for IgromanDS community.
pause
exit