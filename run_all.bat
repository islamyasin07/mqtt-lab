@echo off
echo ================================
echo   MQTT LAB - Auto Run Launcher  
echo ================================
echo.

REM 
echo Starting Mosquitto Broker...
start "Mosquitto" cmd /k "mosquitto -v"

timeout /t 1 >nul

REM 
echo Starting Temperature Publisher...
start "Temp Publisher" cmd /k "python publishers\temp_pub.py"

echo Starting Humidity Publisher...
start "Humidity Publisher" cmd /k "python publishers\humidity_pub.py"

echo Starting People Counter Publisher...
start "People Publisher" cmd /k "python publishers\people_pub.py"

REM 
echo Starting Temperature Subscriber...
start "Temp Subscriber" cmd /k "python subscribers\temp_sub.py"

echo Starting Humidity Subscriber...
start "Humidity Subscriber" cmd /k "python subscribers\humidity_sub.py"

echo Starting People Subscriber...
start "People Subscriber" cmd /k "python subscribers\people_sub.py"

echo.
echo All systems launched ^^ !
pause
