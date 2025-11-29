@echo off
color 0C
title Restart Computer - Harper_IDS for IgromanDS

echo.
echo *******************************************************************************
echo *                          RESTART COMPUTER                                   *
echo *                     Developed by Harper_IDS for IgromanDS                   *
echo *******************************************************************************
echo.
echo AUTHORSHIP: Harper_IDS - All rights reserved for IgromanDS community
echo ===============================================================================
echo.
echo This will restart your computer in 30 seconds.
echo Save all your work before proceeding!
echo.
echo Press any key to proceed with restart in 30 seconds...
echo To cancel, press Ctrl+C within 5 seconds.
timeout /t 5
shutdown /r /t 30
echo.
echo Computer will restart in 30 seconds...
echo.
echo To cancel the restart, run: shutdown /a
echo.
pause