@echo off
color 04
title EXTREME RESET - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                          EXTREME RESET                                      *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo WHAT THIS DOES: Runs ALL network reset commands in sequence
echo RISKS: Complete network configuration loss, requires restart, need to reconfigure everything
echo BENEFITS: Fixes ALL network-related issues, complete fresh start
echo.
echo Press any key to continue with EXTREME reset...
echo WARNING: This will require a system restart to complete!
echo WARNING: You will lose ALL network profiles and configurations!
pause >nul

echo.
echo Step 1: Clearing DNS cache...
ipconfig /flushdns

echo.
echo Step 2: Clearing ARP and NetBIOS cache...
nbtstat -R
ipconfig /registerdns

echo.
echo Step 3: Resetting Winsock...
netsh winsock reset catalog

echo.
echo Step 4: Resetting TCP/IP stack...
netsh int ip reset
netsh int ipv4 reset
netsh int ipv6 reset

echo.
echo Step 5: Resetting firewall...
netsh advfirewall reset

echo.
echo Step 6: Releasing and renewing IP...
ipconfig /release
ipconfig /renew
ipconfig /flushdns

echo.
echo Step 7: Resetting network interfaces...
netsh int reset all

echo.
echo Extreme reset completed!
echo.
echo Please restart your computer now to complete the process.
echo You will need to reconfigure all your network connections after restart.
echo.
echo Press any key to exit.
pause >nul