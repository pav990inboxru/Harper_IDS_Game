@echo off
color 0C
title Uninstall Network Reset Utility - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                     UNINSTALL NETWORK RESET UTILITY                         *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo This will remove shortcuts and entries created by the installer.
echo.
echo Removing desktop shortcut...
del "%USERPROFILE%\Desktop\Network_Reset_Utility.bat" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Desktop shortcut removed successfully!
) else (
    echo Desktop shortcut not found or could not be removed.
)

echo.
echo Removing start menu entry...
rd /s /q "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Network Reset Utility" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Start menu entry removed successfully!
) else (
    echo Start menu entry not found or could not be removed.
)

echo.
echo Uninstallation completed!
echo The main utility files remain in this folder for backup purposes.
echo.
echo Press any key to exit.
pause >nul