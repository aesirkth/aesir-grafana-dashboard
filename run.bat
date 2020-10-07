ECHO OFF
START /MIN bin\influxd.exe
START /MIN bin\grafana-server.exe --homepath grafana\
timeout /t 5 /nobreak
python serial-reader\main.py
PAUSE