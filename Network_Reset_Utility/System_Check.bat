@echo off
color 0B
title System Check - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                           SYSTEM CHECK                                      *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo Running system diagnostics...
echo.
echo Checking Windows version:
ver
echo.
echo Checking network adapters:
wmic path win32_networkadapter get name,netconnectionstatus | findstr /v "0$"
echo.
echo Checking IP configuration:
ipconfig
echo.
echo Checking DNS resolution:
nslookup google.com
echo.
echo Checking network connectivity:
ping -n 1 google.com >nul && echo Internet connectivity: OK || echo Internet connectivity: ISSUE DETECTED
echo.
echo Checking for common network issues...
netsh winsock show catalog | findstr /C:"Error" >nul && echo Winsock catalog: ISSUES FOUND || echo Winsock catalog: OK
echo.
echo System check completed!
echo.
echo RECOMMENDATIONS:
echo - If you have connectivity issues, try LIGHT reset first
echo - If DNS issues persist, try MEDIUM reset
echo - If network is completely broken, try HEAVY or COMPLETE reset
echo - For VPN/DNS tool related issues, COMPLETE reset is recommended
echo.
echo Press any key to exit.
pause >nul