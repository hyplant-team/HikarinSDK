@echo off
setlocal
cd /D "%~dp0"
for %%f in (workshop\*.py) do call :run_py %%f
cls
echo:ALL DONE
timeout /T 3 >NUL
exit /B 0

:run_py
set "SCRIPT=%1"
cls
echo:%cd%
echo:RUN %SCRIPT%
timeout /T 1 /NOBREAK >NUL
endlocal
python %SCRIPT%
set "e=%errorlevel%"
echo.
echo:exit_code: %e%
timeout /T 1 /NOBREAK >NUL
if "%e%" EQU "0" goto :eof
set /P"=press Enter to continue."
exit /B %e%
