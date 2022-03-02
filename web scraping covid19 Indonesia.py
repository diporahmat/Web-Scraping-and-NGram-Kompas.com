import requests
import json
import matplotlib.pyplot as plt
import pandas as pd

response = requests.get("https://api.covid19api.com/total/country/indonesia/status/confirmed?from=2021-12-15T00:00:00Z&to=2022-01-15T00:00:00Z")
print(response.status_code)
print(response.text)

text = json.dumps(response.json(), sort_keys=True, indent=4)
print(text)

df_indo_confirm = pd.DataFrame(response.json())
print(df_indo_confirm)

df_indo_confirm.plot(x='Date', y='Cases', figsize=(20,10), grid=True)