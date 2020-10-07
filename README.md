# Mjollnir Grafana Test
This repository contains a potential dashboard for the rocket Mjollnir by AESIR at KTH.
It uses Grafana and InfluxDB

## prerequisites
Install python dependencies (and python)\
`python -m pip install -r requirements.txt`

#### linux only
Install InfluxDB and Grafana through your package manager.

## How to run
### Windows 
run `run.bat` and hope for the best.

### linux
run `influxd`\
run `./run_grafana.sh`\
run `python serial-reader/main.py`
in that order

## How to use

Go to `localhost:3000` in your browser and login as `admin` with the password `aesir`.
Under dashboards you can find `Mjollnir` and `Mjollnir (filtered)`. The end result is the same but they differ a little behind the scenes.
The performance starts to degrade after a few minutes as the database grows in size so use the version that you find works best

Grafana doesn't really have FPS in the traditional sense. You can configure an update frequency from the upper right drop down menu. If grafana fails to hit the targeted frequency it will stack all HTTP requests in a long queue and freeze...