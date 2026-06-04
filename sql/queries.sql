-- 1 Top 5 funds by AUM
SELECT * FROM "03_aum_by_fund_house" LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) FROM "02_nav_history";

-- 3 Total SIP inflows
SELECT * FROM "04_monthly_sip_inflows" LIMIT 10;

-- 4 Transactions count
SELECT COUNT(*) FROM "08_investor_transactions";

-- 5 Scheme performance
SELECT * FROM "07_scheme_performance" LIMIT 10;

-- 6 Portfolio holdings
SELECT * FROM "09_portfolio_holdings" LIMIT 10;

-- 7 Benchmark indices
SELECT * FROM "10_benchmark_indices" LIMIT 10;

-- 8 Category inflows
SELECT * FROM "05_category_inflows" LIMIT 10;

-- 9 Industry folio count
SELECT * FROM "06_industry_folio_count" LIMIT 10;

-- 10 Fund master
SELECT * FROM "01_fund_master" LIMIT 10;