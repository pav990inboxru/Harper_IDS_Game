@echo off
color 0A
title Network Reset Utility - Developed by Harper_IDS for IgromanDS

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