@echo off
color 0A
title Create Portable ZIP - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                     CREATE PORTABLE ZIP ARCHIVE                             *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo Creating portable ZIP archive of Network Reset Utility...
echo.

REM Use PowerShell to create the ZIP file if available
powershell -Command "Compress-Archive -Path '.\*' -DestinationPath 'Network_Reset_Utility_Portable.zip' -Force" >nul 2>&1

if %ERRORLEVEL% EQU 0 (
    echo ZIP archive created successfully: Network_Reset_Utility_Portable.zip
    echo This file can be copied to a USB drive for portable use.
) else (
    echo PowerShell compression failed. Trying alternative method...
    
    REM Alternative method using 7z if available
    7z a -tzip "Network_Reset_Utility_Portable.zip" "*" >nul 2>&1
    
    if %ERRORLEVEL% EQU 0 (
        echo ZIP archive created successfully using 7-Zip: Network_Reset_Utility_Portable.zip
    ) else (
        echo Could not create ZIP automatically. Please manually compress these files:
        echo.
        dir /b
        echo.
        echo Create a ZIP file containing all these files for portable use.
    )
)

echo.
echo The portable version can be used on any Windows system without installation.
echo Remember to run as Administrator for best results!
echo.
echo Press any key to exit.
pause >nul