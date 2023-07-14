# Python sample codes for Cognite Data Fusion

## Prerequisites

- Python 3.8-3.11
- [Cognite Python SDK](https://cognite-sdk-python.readthedocs-hosted.com/)

install dependent Python packages

```
pip3 install -r requirements.txt
```

- set environment variables(Azure AD tenant / CDF Project credentials) in .env

```
cp dotenv-sample .env
vi .env
```



## upload CSV data into Timeseries/Datapoints

### [create Timeseries](https://cognite-sdk-python.readthedocs-hosted.com/en/latest/core_data_model.html#create-time-series) w/o datapoints based on column information CSV

```
python3 16_create_timeseries.py
```

### upload CSV data to Datapoints using [time_series.data.insert_multiple](https://cognite-sdk-python.readthedocs-hosted.com/en/latest/core_data_model.html#insert-data-points-into-multiple-time-series)

```
python3 19_insert_multiple_ts.py
```
