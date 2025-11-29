@echo off
color 0A
title Install Network Reset Utility - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                      INSTALL NETWORK RESET UTILITY                          *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo This will create shortcuts and configure the Network Reset Utility.
echo.
echo Creating desktop shortcut...
copy "Network_Reset_Menu.bat" "%USERPROFILE%\Desktop\Network_Reset_Utility.bat" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Desktop shortcut created successfully!
) else (
    echo Failed to create desktop shortcut. Creating in current directory instead.
    copy "Network_Reset_Menu.bat" "Network_Reset_Utility_Desktop.bat" >nul 2>&1
)

echo.
echo Creating start menu entry...
md "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Network Reset Utility" >nul 2>&1
copy "Network_Reset_Menu.bat" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Network Reset Utility\Network Reset Utility.bat" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Start menu entry created successfully!
) else (
    echo Failed to create start menu entry.
)

echo.
echo Installation completed!
echo.
echo To run the utility, you can:
echo 1. Double-click the desktop shortcut
echo 2. Run Network_Reset_Menu.bat from this folder
echo 3. Use the start menu entry (if created)
echo.
echo IMPORTANT: Always run as Administrator for best results!
echo.
echo Press any key to exit.
pause >nul