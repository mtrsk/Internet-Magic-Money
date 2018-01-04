# Internet-Magic-Money
An analysis of the Weighted Price of some criptocurrencies using Pandas and Quandl's Bitcoin API.

--------

# Tutorial

## Setting your API Key

Set your Quandl API Key in the `scripts/settings/__init__.py` file, or better, just overwrite it when calling the settings package.

```
from scripts import settings as st
st.API_KEY = "YOUR QUANDL API_KEY"
```

## Folder Structure (As of now)
    .
    ├── DATA                    # Pickled files from Quandl API
    ├── scripts                 # Scripts package
    |   ├── utils
    |   |   ├── data.py         # Useful methods for using the data
    |   |   └── __init__.py
    |   ├── settings
    |   |   └── __init__.py     # You can place your Quandl API Key here
    |   └── __init__.py
    ├── bitcoin.ipynb           # Jupyter Notebook
    ├── environment.yml         # Conda environment
    ├── LICENSE
    └── README.md
