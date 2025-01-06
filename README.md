# Candlestick Chart Plotter with Support and Resistance Identification

This repository contains a Python script to plot candlestick charts and identify key support and resistance levels using the Nifty 50 index data.

## Overview

Technical analysis often involves identifying **support** and **resistance** levels to understand market trends. This project automates this process by:

- **Loading Nifty 50 index data** for a specified time range.
- **Plotting candlestick charts** using the `mplfinance` library.
- **Identifying support and resistance levels** with the help of the `argrelextrema` function from `scipy`.
- **Overlaying the levels** on the candlestick chart for visualization.

## Features

- **Dynamic Support and Resistance Levels:** Adjust the sensitivity using the `order` parameter.
- **Custom Chart Styling:** Utilize custom themes for professional-looking charts.
- **Visualization with Volume:** Charts include volume bars for deeper market insights.

## Prerequisites

Ensure you have the following Python packages installed:

- `pandas`
- `mplfinance`
- `matplotlib`
- `scipy`
- `numpy`

Install the required packages using pip:

```bash
pip install pandas mplfinance matplotlib scipy numpy
```

## Data Format

The input data should be in CSV format with the following columns:

| Date        | Open      | High      | Low       | Close     | Shares Traded | Turnover (₹ Cr) |
|-------------|-----------|-----------|-----------|-----------|----------------|-----------------|
| 08-JAN-2024 | 21747.6   | 21763.95  | 21492.9   | 21513     | 231452935      | 21140.94        |
| 09-JAN-2024 | 21653.6   | 21724.45  | 21517.85  | 21544.85  | 228568589      | 24055.74        |

Rename the column `Shares Traded` to `Volume` during preprocessing.

## How to Use

1. Clone this repository:

```bash
git clone https://github.com/asircar/candlestick-support-resistance.git
```

2. Navigate to the repository:

```bash
cd candlestick-support-resistance
```

3. Replace `NIFTY 50-06-01-2024-to-06-01-2025.csv` with your own dataset in the same format.

4. Run the script:

```bash
python script.py
```

## Output

The script generates a candlestick chart with:

- **Red dashed lines** for resistance levels.
- **Green dashed lines** for support levels.
- Volume bars for additional context.

## Example Chart

*<img width="1270" alt="image" src="https://github.com/user-attachments/assets/7cc58f74-c5e0-40d4-acfa-df4c071d9cde" />
*

## Notes

This code is provided as-is, with no warranties or guarantees. It is free for anyone to view, use, or modify for their own purposes. Credit is appreciated but not required.

## References

- **Data Source:** [NSE India Historical Index Data](https://www.nseindia.com/reports-indices-historical-index-data)
- **Development Tools:** This project was developed using **GitHub Copilot** and **ChatGPT**.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

---

Feel free to reach out with questions or suggestions. Happy coding!
