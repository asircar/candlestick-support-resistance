import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import numpy as np

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')
        df.set_index('Date', inplace=True)
        df.rename(columns={'Shares Traded': 'Volume'}, inplace=True)
        df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def find_support_resistance_levels(df, order=20):
    resistance_indices = argrelextrema(df['High'].values, np.greater, order=order)[0]
    support_indices = argrelextrema(df['Low'].values, np.less, order=order)[0]
    resistance_levels = df['High'].iloc[resistance_indices].values
    support_levels = df['Low'].iloc[support_indices].values
    return resistance_levels, support_levels

def create_custom_style():
    return mpf.make_mpf_style(
        base_mpf_style="nightclouds",
        marketcolors={
            'candle': {'up': '#26a69a', 'down': '#ef5350'},
            'edge': {'up': '#26a69a', 'down': '#ef5350'},
            'wick': {'up': '#26a69a', 'down': '#ef5350'},
            'ohlc': {'up': '#26a69a', 'down': '#ef5350'},
            'volume': {'up': '#26a69a', 'down': '#ef5350'},
            'vcedge': {'up': '#26a69a', 'down': '#ef5350'},
            'alpha': 0.9,
            'vcdopcod': False
        },
        facecolor='#131722',
        gridcolor='#292929',
        gridstyle='--',
        figcolor='#131722'
    )

def plot_candlestick_chart(df, resistance_levels, support_levels, style):
    add_lines = []
    for level in resistance_levels:
        add_lines.append(mpf.make_addplot([level] * len(df), color='red', linestyle='--'))
    for level in support_levels:
        add_lines.append(mpf.make_addplot([level] * len(df), color='green', linestyle='--'))
    
    fig, ax = mpf.plot(
        df,
        type='candle',
        title='Candlestick Chart with Support and Resistance',
        style=style,
        volume=True,
        addplot=add_lines,
        returnfig=True
    )
    plt.show()

def main():
    file_path = "NIFTY 50-06-01-2024-to-06-01-2025.csv"  # Replace with your file path
    df = load_data(file_path)
    if df is not None:
        resistance_levels, support_levels = find_support_resistance_levels(df, order=20)
        print("Resistance Levels:", resistance_levels)
        print("Support Levels:", support_levels)
        style = create_custom_style()
        plot_candlestick_chart(df, resistance_levels, support_levels, style)

if __name__ == "__main__":
    main()
