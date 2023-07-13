# from cdf_auth import get_client
from cdf_auth_interactive import get_client
# from cognite.client.data_classes import TimeSeries
from cognite.client.data_classes import TimeSeriesUpdate

client = get_client()

asset = client.assets.retrieve(external_id='千葉/千葉4/焼結/焼結/A1234')
my_update = TimeSeriesUpdate(external_id='A1234 速度').asset_id.set(asset.id)
res = client.time_series.update(my_update)
print(res)