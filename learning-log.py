# Exercise 1
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'date':   ['2024-01-01','2024-01-01','2024-01-02','2024-01-02','2024-01-03'],
    'ticker': ['AAPL','MSFT','AAPL','MSFT','AAPL'],
    'price':  [185.2, 374.0, 186.5, 376.1, None],
    'volume': [72_000_000, 21_000_000, 68_000_000, 19_500_000, 75_000_000],
    'sector': ['Tech','Tech','Tech','Tech','Tech']
})
result_df = (
    df
    .groupby('ticker')
    .agg(
        avg_price   = ('price',  'mean'),
        total_volume = ('volume', 'sum'),
        price_range  = ('price',  lambda x: round(x.max() - x.min(), 2))
    )
    .assign(avg_price = lambda x: x['avg_price'].round(2))
    .sort_values('ticker')
    .reset_index()
)
print(result_df)

# Exercise 2
prices = pd.DataFrame({
    'date':   ['2024-01-01','2024-01-01','2024-01-02','2024-01-02'],
    'ticker': ['AAPL','MSFT','AAPL','MSFT'],
    'price':  [185.2, 374.0, 186.5, 376.1]
})

fundamentals = pd.DataFrame({
    'ticker':    ['AAPL','AAPL','MSFT'],
    'metric':    ['PE_ratio','market_cap','PE_ratio'],
    'value':     [28.5, 2900000, 35.2]
})
# You wrote this (two assignments)
pe_ratios = fundamentals[fundamentals['metric'] == 'PE_ratio'][['ticker','value']]
merged_df = pd.merge(prices, pe_ratios, on='ticker', how='left')
merged_df = merged_df.rename(...)

# Tighter — one chain
merged_df = (
    prices
    .merge(
        fundamentals[fundamentals['metric'] == 'PE_ratio'][['ticker','value']],
        on='ticker',
        how='left'
    )
    .rename(columns={'value': 'PE_ratio'})
)

#ALternatve approach using pivot
fund_wide = fundamentals.pivot_table(
    index='ticker', columns='metric', values='value'
).reset_index()[['ticker', 'PE_ratio']]
merged_df = prices.merge(fund_wide, on='ticker', how='left')

# Exercise 3

df = pd.DataFrame({
    'date':   ['2024-01-01','2024-01-01','2024-01-02','2024-01-02','2024-01-03'],
    'ticker': ['AAPL','MSFT','AAPL','MSFT','AAPL'],
    'price':  [185.2, 374.0, 186.5, 376.1, 188.0],
    'volume': [72_000_000, 21_000_000, 68_000_000, 19_500_000, 75_000_000],
})

grouped = df.groupby('ticker')

avg_price_transformed = grouped['price'].transform('mean')
pct_volume_transformed = grouped['volume'].transform(lambda x: round(x / x.sum() * 100, 2))

result_df = (
    df
    .assign(
        avg_price_by_ticker = avg_price_transformed.round(2),
        pct_of_ticker_volume = pct_volume_transformed
    )
)
# Another way to do it without intermediate variables
result_df = (
    df
    .assign(
        avg_price_by_ticker  = lambda x: x.groupby('ticker')['price']
                                          .transform('mean')
                                          .round(2),
        pct_of_ticker_volume = lambda x: x.groupby('ticker')['volume']
                                          .transform(lambda v: (v / v.sum() * 100).round(2))
    )
)

# Exercise 4
df = pd.DataFrame({
    'ticker': ['AAPL','MSFT','GOOGL','AMZN','META'],
    'price':  [185.2, 374.0, 140.5, 178.3, 485.0],
    'volume': [72_000_000, 21_000_000, 18_000_000, 35_000_000, 15_000_000],
    'market_cap_B': [2900, 2800, 1750, 1850, 1250]
})

# Junior code — 4 separate apply calls
df['price_category'] = df['price'].apply(
    lambda x: 'high' if x > 300 else 'low'
)

df['volume_M'] = df['volume'].apply(lambda x: round(x / 1_000_000, 2))

df['price_to_cap'] = df.apply(
    lambda row: round(row['price'] / row['market_cap_B'], 4), axis=1
)

df['flag'] = df.apply(
    lambda row: 'whale' if row['volume'] > 30_000_000
                and row['market_cap_B'] > 1800 else 'normal',
    axis=1
)
# Another way : vectorization (apply is not needed)
df = (
    df
    .assign(
        price_category = lambda x: np.where(x['price'] > 300, 'high', 'low'),
        volume_M       = lambda x: (x['volume'] / 1_000_000).round(2),
        price_to_cap   = lambda x: (x['price'] / x['market_cap_B']).round(4),
        flag           = lambda x: np.where(
                             (x['volume'] > 30_000_000) & (x['market_cap_B'] > 1800),
                             'whale', 'normal'
                         )
    )
)

#%% Exercise 5
import matplotlib.pyplot as plt
import seaborn as sns

# filter to clean data only
clean_df = df[df['data_quality'] == 'ok'].copy()
# %%
