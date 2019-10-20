#!/usr/bin/python3

import pandas as pd
from influxdb import DataFrameClient

DB_NAME = "rad_records_iss"

def main (host, port, csv):
	# Open the file and parse it

	pd.set_option('display.max_rows', 500)
	pd.set_option('display.max_columns', 500)
	pd.set_option('display.width', 1000)

	# Thanks to
	# https://stackoverflow.com/questions/29442370/how-to-correctly-read-csv-in-pandas-while-changing-the-names-of-the-columns
	print("Parsing csv...")
	headers = ['start_date', 'end_date', 'measurement_duration', 'detector_number', 'sensitivity', 'bubble_count', 'exposure', 'name']
	data_frame = pd.read_csv(csv, parse_dates=True, index_col=0, names=headers, header=0)

	# Format the date time values
	data_frame.index = pd.to_datetime(data_frame.index, utc=True)

	print(data_frame);

	# Create the database connection
	# Thanks to the influxdb pip docs 
	# https://influxdb-python.readthedocs.io/en/latest/examples.html#tutorials-basic

	print("Connecting to db...")
	client_connection = DataFrameClient(host=host, port=port, database=DB_NAME)
	print("Writing data...")
	client_connection.write_points(data_frame, DB_NAME, protocol="line")

	# Close the connection
	client_connection.close()

if __name__ == '__main__':
	# Host and port have been hardcoded for simplicity.
	main("127.0.0.1", 8086, "./records01.csv")
