@echo off
setlocal
cd /D "%~dp0"
for %%f in (workshop\*.py) do call :run_py %%f
cls
echo:ALL DONE, Exporting...
python export.py
set "e=%errorlevel%"
echo.
echo:exit_code: %e%
if "%e%" NEQ "0" goto :error
echo:build succeeded
timeout /T 3 >NUL
exit /B 0

:error
echo:export filed
set /P"=press Enter to exit."
exit /B %e%


:run_py
set "SCRIPT=%~nx1"
if "%SCRIPT:~0,1%" EQU "_" exit /B 0
cls
echo:RUN %SCRIPT%
timeout /T 1 /NOBREAK >NUL
endlocal
python %1
set "e=%errorlevel%"
echo.
echo:exit_code: %e%
timeout /T 1 /NOBREAK >NUL
if "%e%" EQU "0" goto :eof
set /P"=press Enter to continue."
exit /B %e%
