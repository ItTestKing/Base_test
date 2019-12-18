@echo off
del /f /s /q "%cd%\ping_tab.png"
del /f /s /q "%cd%\browser_tab.png" "%cd%\help_image.png" "%cd%\result.jpg"
del f/q "%cd%\archived_files\*.*" "%cd%\downloaded_files\*.*" "%cd%\latest_logs\*.*" "%cd%\archived_logs\*.*" 
rd /s /q "%cd%\archived_files" "%cd%\downloaded_files" "%cd%\latest_logs" "%cd%\archived_logs"
pause
