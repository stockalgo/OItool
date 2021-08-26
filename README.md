# OItool Open Interest Analysis Tool




<p align="center"><a href="http://bandl.io/oitool.html" target="_blank"><img src="https://raw.githubusercontent.com/stockalgo/OItool/main/demo/bar.gif"></a> </p>
<p align="center"><a href="http://bandl.io/oitool.html" target="_blank"><img src="https://raw.githubusercontent.com/stockalgo/OItool/main/demo/chart.gif"></a> </p>

<br/><hr/>
# Installation

### 1) Install Oitool using python pip package manager
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bandl.

```bash
pip install oitool
```
### 2) Install [influxdb](https://github.com/influxdata/influxdb/releases) database and [Grafana](https://grafana.com/docs/grafana/latest/installation/) tool.

### 3) Connect grafana to influxdb [Check Here](https://www.influxdata.com/blog/how-grafana-dashboard-influxdb-flux-influxql/)


<br/><hr/>
# Usage

### 1) Start Influxdb database and Grafana.

### 2) To start fetching option open interest data and push it to influxDB
```python
from oitool.fetchoi import FetchOI
oi = FetchOI()
oi.subscribe(symbol="NIFTY") #to set stock ticker
oi.start()
```
### 3) Open Grafana, Add dashbord and charts [Refer this](https://www.influxdata.com/blog/how-to-use-grafana-with-influxdb-to-monitor-time-series-data/)

<br/><hr/>
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Kindly follow PEP 8 Coding Style guidelines. Refer: https://www.python.org/dev/peps/pep-0008/

Please make sure to update tests as appropriate.
<br/><hr/>
# License
[MIT](https://choosealicense.com/licenses/mit/)
