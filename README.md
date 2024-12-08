# us-department-treasury

## Project Overview

This project automates the process of fetching, processing, and storing daily Treasury Par Yield Curve Rates data from
the US Department of the Treasury. It provides a reliable and up-to-date source of Treasury yield curve data for
financial analysis and research purposes.

### What it does

1. Data Retrieval: The project downloads the latest Daily Treasury Par Yield Curve Rates data from the US Department of
   the Treasury website.
2. Data Storage: The processed data is committed to a GitHub repository, creating a historical record of Treasury yield
   curve rates.
3. Automated Execution: The entire process is automated to run daily, ensuring the dataset is always current.

### How it works

1. Scheduled Execution: The project is set up to run automatically using Google Cloud Run's scheduled tasks.
2. Data Download: The script uses the provided URL to download the latest CSV file containing Treasury Par Yield Curve

### us-department-treasury - yield curves and such

### Daily Treasury Par Yield Curve Rates - Website

https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2024

### Download Link for 2024 Data

https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2024/all?type=daily_treasury_yield_curve&field_tdr_date_value=2024&page&_format=csv

## Nightly, download the Daily Treasury Par Yield Curve Rates into CSV

commit to GitHub/data

## Trap for calendar year - change the params of the URL

Throw an error if NOT EXIST

## GCP Cloud Run - scheduled 1AM NYC

##############

## Reference dataset: QC

https://www.quantconnect.com/data/us-treasury-yield-curve
https://github.com/QuantConnect/Lean.DataSource.USTreasury/blob/master/USTreasuryYieldCurveDataAlgorithm.cs
https://github.com/QuantConnect/Lean.DataSource.USTreasury/
https://github.com/QuantConnect/Lean.DataSource.USTreasury/blob/master/USTreasuryYieldCurveRate.cs

## Treasury Yield Curve Methodology

![Methdology](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics/treasury-yield-curve-methodology)

Treasury Par Yield Curve Rates: These rates are commonly referred to as "Constant Maturity Treasury" rates, or CMTs.
Yields are interpolated by the Treasury from the daily par yield curve. This curve, which relates the yield on a
security to its time to maturity, is based on the closing market bid prices on the most recently auctioned Treasury
securities in the over-the-counter market. These par yields are derived from indicative, bid-side market price
quotations (not actual transactions) obtained by the Federal Reserve Bank of New York at or near 3:30 PM each trading
day. The CMT yield values are read from the par yield curve at fixed maturities, currently 1, 2, 3, 4 and 6 months and
1, 2, 3, 5, 7, 10, 20, and 30 years. This method provides a par yield for a 10-year maturity, for example, even if no
outstanding security has exactly 10 years remaining to maturity.

# Docker cli

docker build -t gcr.io/dfg-analytics-insights-prod/us-department-treasury .
docker push gcr.io/dfg-analytics-insights-prod/us-department-treasury

#################################

## Sample Data

Date,"1 Mo","2 Mo","3 Mo","4 Mo","6 Mo","1 Yr","2 Yr","3 Yr","5 Yr","7 Yr","10 Yr","20 Yr","30 Yr"
10/07/2024,5.00,4.87,4.77,4.67,4.45,4.24,3.99,3.89,3.86,3.92,4.03,4.37,4.30
10/04/2024,5.01,4.88,4.73,4.68,4.45,4.20,3.93,3.84,3.81,3.88,3.98,4.33,4.26
10/03/2024,4.99,4.85,4.68,4.61,4.37,4.02,3.70,3.62,3.62,3.71,3.85,4.24,4.18
10/02/2024,4.92,4.83,4.69,4.61,4.36,3.97,3.63,3.54,3.55,3.65,3.79,4.19,4.14
10/01/2024,4.96,4.87,4.71,4.63,4.36,3.96,3.61,3.52,3.51,3.60,3.74,4.14,4.08
09/30/2024,4.93,4.87,4.73,4.65,4.38,3.98,3.66,3.58,3.58,3.67,3.81,4.19,4.14
09/27/2024,4.90,4.87,4.68,4.64,4.35,3.90,3.55,3.49,3.50,3.60,3.75,4.15,4.10
09/26/2024,4.90,4.87,4.68,4.65,4.38,3.96,3.60,3.54,3.55,3.65,3.79,4.17,4.12
09/25/2024,4.79,4.78,4.69,4.64,4.36,3.89,3.53,3.49,3.52,3.65,3.79,4.18,4.14
09/24/2024,4.78,4.78,4.69,4.63,4.36,3.88,3.49,3.44,3.47,3.60,3.74,4.13,4.09
09/23/2024,4.85,4.84,4.72,4.65,4.40,3.91,3.57,3.47,3.51,3.62,3.75,4.12,4.09
09/20/2024,4.87,4.88,4.75,4.70,4.43,3.92,3.55,3.46,3.48,3.59,3.73,4.10,4.07
09/19/2024,4.89,4.91,4.80,4.73,4.46,3.93,3.59,3.47,3.49,3.60,3.73,4.11,4.06
09/18/2024,4.91,4.91,4.84,4.76,4.50,3.95,3.61,3.49,3.47,3.58,3.70,4.08,4.03
09/17/2024,5.05,5.05,4.95,4.87,4.55,3.99,3.59,3.45,3.44,3.53,3.65,4.02,3.96
09/16/2024,5.11,5.10,4.96,4.88,4.55,3.96,3.56,3.42,3.41,3.51,3.63,4.01,3.94

## Screenshot

For: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2024

![US Treasury-Daily Treasury Par Yield Curve Rates](https://github.com/deerfieldgreen/us-department-treasury/blob/main/images/Screenshot%202024-10-08%20at%2014.41.25.png)