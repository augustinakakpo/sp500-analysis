# S&P 500 Financial Analysis

End-to-end analysis of S&P 500 constituents including data cleaning,
exploratory data analysis, and SQL window functions.

## Dataset
- 503 companies · 14 original columns · 2017 snapshot
- Source: S&P 500 Companies & Financials (GitHub datasets)
- Link: https://github.com/datasets/s-and-p-500-companies-financials

## What I did

### 1. Data Cleaning
- Identified 15 companies with systematic missingness across all financial metrics — flagged as `incomplete`, not dropped
- Filled 102 missing Dividend Yield values with 0 — companies that don't pay dividends have a true yield of zero
- Flagged 18 Price/Earnings outliers above 100 — economic outliers, not data errors
- Dropped SEC Filings column — contained URLs with no analytical value
- Validated every cleaning step with assertions

### 2. Exploratory Analysis
- Analyzed sub-industry concentration across 125 sub-industries
- Compared median P/E ratios across sectors excluding outliers

## Key Findings
- S&P 500 representation is highly concentrated — Health Care Equipment 
  leads with 18 companies while most of the 125 sub-industries have only 
  one company large enough to qualify by market cap
- Health Care REITs trade at a median P/E of 77 vs Cable & Satellite at 4.3 
  — the market prices in strong earnings growth for Real Estate while 
  Cable & Satellite faces structural decline from streaming substitution

### 3. SQL Analysis
- 10 window function queries on sp500.db
- Covers ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, running totals
- *(coming next session)*

## Tools
Python · pandas · NumPy · matplotlib · seaborn · SQL · SQLite

## Files
- `sp500_analysis.ipynb` — full analysis notebook
- `sp500.db` — cleaned SQLite database

## Status
🟡 In progress — SQL section coming next session
