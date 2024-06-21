import requests
import json

def getDate():
    t_rates = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_long_term&field_tdr_date_value=2005"
    response = requests.get(t_rates)
    print(response.json())
getDate()