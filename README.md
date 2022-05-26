# IBC_BIFR-Analysis

The Insolvency and Bankruptcy Code, and the Board for Industrial and Financial Reconstruction are 2 institutions set up by the Indian Government to help companies
that are bankrupt or entering bankruptcy to revive their businesses.

The BIFR was abolished for the IBC with a new set of rules and financial reconstruction.

In this project, we perform some financial stability tests, and run regressions on company performances pre and post BIFR and pre and post IBC respectively, 
to deduce if the newly formed instituion was any better.

I first start with scraping all the companies in IBC, Debt Recovery Tribunal (DRT) and the BIFR (had to scrape a decomissioned webssite), and match them with their 
respective CINs from a different website which has a company directory using fuzzy match
I then used Prowess data for the respective historical financials, and performed the relevant financial stability tests (ROE, Debt and Liquidity ratios, Escrow accounts
Offshore payments, Loans taken) on a yearly basis, and the regression was performed on Stata.

We find that the IBC was in fact, doing much better.

This was a project I did during my internship at the Indian School of Business, and the report was passed to the Government of India
