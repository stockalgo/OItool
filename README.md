# OItool Open Interest Analysis Tool




<p align="center"><a href="http://bandl.io/oitool" target="_blank"><img src="https://raw.githubusercontent.com/stockalgo/OItool/main/demo/bar.gif"></a> </p>
<p align="center"><a href="http://bandl.io/oitool" target="_blank"><img src="https://raw.githubusercontent.com/stockalgo/OItool/main/demo/chart.gif"></a> </p>


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install bandl.

```bash
pip install oitool
```


## Usage

### To start fetching option open interest data and push it to influxDB
```python
from oitool.fetchoi import FetchOI
testObj = FetchOI()
t.subscribe(symbol="NIFTY") #to set stock ticker
t.start()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Kindly follow PEP 8 Coding Style guidelines. Refer: https://www.python.org/dev/peps/pep-0008/

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
