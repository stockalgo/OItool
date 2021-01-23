import time
import logging
from bandl.nse_data import NseData
from influxdb import InfluxDBClient

class FetchOI:
    def __init__(self,source=None,influxdb_client=None,database="oitool",log_path=None,logLevel='info'):
        """[summary]

        :param source: stock broker
        :type source: string, optional
        :param influxdb_client: influxdb client object, defaults to None
        :type influxdb_client: object, optional
        :param database: name of databse, defaults to "oitool"
        :type database: str, optional
        :param log_path: log file path, defaults to None
        :type log_path: str, optional
        :param logLevel: log level, defaults to 'info'
        :type logLevel: str, optional
        :raises Exception: database error/ bandl error
        """
        try:
            if not influxdb_client:
                self.client = InfluxDBClient(database=database)
            else:
                self.client = influxdb_client
            self.client.create_database(database)
            if not source:
                self.feeder = NseData()
            else:
                raise("Sources will be supported in future release")


            # setting logs
            if not log_path:
                log_path = "OItool_logs_"+ time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

            log_file = logging.FileHandler(log_path, 'a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            log_file.setFormatter(formatter)

            log = logging.getLogger()  # root logger
            log.addHandler(log_file)      # set the new handler
            numeric_log_level = getattr(logging, logLevel.upper(), 10)
            log.setLevel(numeric_log_level)

        except Exception as err:
            logging.error('%s raised an error', str(err))
            raise Exception("Error occurred in OItool initialization: ",str(err))

    def subscribe(self,symbol,level=10):
        """ To register ticker for data

        :param symbol: ticker to fetch option data
        :type symbol: string
        :param level: number of option strike from ATM
        :type symbols: interger
        """
        self.symbol = symbol
        self.level = level

    def create_influx_data(self,price,option_data,measurement):
        tags = {"price":price}
        fields = {}
        for keys in option_data:
            fields[str(keys)+" ce"] = option_data[keys]["CE"]["openInterest"]
            fields[str(keys)+" pe"] = option_data[keys]["PE"]["openInterest"]
        logging.info(fields)
        influx_json = [{"measurement": measurement,"tags":tags,"fields":fields}]
        return influx_json

    def get_option_data(symbol,strikes=None,expiry_date=None):
        return self.feeder.get_option_data(symbol=symbol,strikes=strikes,expiry_date=expiry_date)

    def start(self,interval=90,runtime=21600):
        """To start fetching data into influxdb

        :param interval: wait between data capture, defaults to 90 Seconds
        :type interval: int, optional
        :param runtime: runtime for script, defaults to 21600
        :type runtime: int, optional
        :raises Exception: InfluxDb error/ bandl error
        """
        if not self.symbol:
            raise Exception ("Symbol not subscribed.")
        starttime = time.time()
        strikes = self.feeder.get_oc_strike_prices(self.symbol,level=self.level)
        prev_dict = None
        while(True):
            try:
                price,oc_data = self.feeder.get_option_data(self.symbol,strikes=strikes)
                if prev_dict == oc_data:
                    time.sleep(15)
                    continue
                else:
                    prev_dict = oc_data
                formated_data = self.create_influx_data(price,option_data=oc_data,measurement=self.symbol)
                self.client.write_points(formated_data)
            except Exception as exc:
                logging.debug(str(exc))
                print("Error Occurred,Don't worry. We try again. Error: ",str(exc))
            timenow = time.time()
            if(timenow - starttime >= runtime):
                break
            time.sleep(interval)
