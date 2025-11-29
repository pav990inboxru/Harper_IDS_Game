@echo off
color 0B
title View Current Network Settings - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                    CURRENT NETWORK CONFIGURATION                          *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo Displaying current network configuration...
echo.
ipconfig /all
echo.
echo.
echo Displaying current network routes...
echo.
route print
echo.
echo.
echo Displaying ARP table...
echo.
arp -a
echo.
echo.
echo Press any key to exit.
pause >nul