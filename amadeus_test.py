import os
import pandas as pd

from amadeus import Client, ResponseError
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SEC = os.getenv('API_SEC')

amad = Client(client_id = API_KEY, client_secret = API_SEC)

def single():
    try:
        res = amad.reference_data.location('ABOM').get()
        pprint(res.data)

    except ResponseError as res_er:
        print(res_er)
    except Exception as e:
        print(e)

def multi():
    airports = pd.Series(['BOM', 'JFK', 'BLR'])

    airports = airports.apply(lambda x: 'A' + x)

    for i in airports:
        try:
            res = amad.reference_data.location(i).get()
            pprint(res.data)
            print('-' * 20)

        except ResponseError as res_er:
            print(res_er)
        except Exception as e:
            print(e)

multi()