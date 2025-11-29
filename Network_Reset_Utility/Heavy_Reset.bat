@echo off
color 0C
title HEAVY RESET - TCP/IP Stack & Adapter Reset - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                   HEAVY RESET - TCP/IP Stack & Adapter Reset                *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo WHAT THIS DOES: Resets TCP/IP stack to default configuration, resets network adapters
echo RISKS: Complete network disconnection, requires network reconnection
echo BENEFITS: Fixes deep TCP/IP stack issues, resolves adapter problems
echo.
echo Press any key to continue with heavy reset...
echo WARNING: This will disconnect your network connection!
pause >nul

netsh int ip reset
netsh int ipv4 reset
netsh int ipv6 reset
ipconfig /release
ipconfig /renew
ipconfig /flushdns

echo.
echo Heavy reset completed!
echo.
echo You need to reconnect to your network.
echo You can now close this window or press any key to exit.
pause >nul