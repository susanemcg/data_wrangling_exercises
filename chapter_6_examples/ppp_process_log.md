# About

This is the process log for my work on the Paycheck Protection Program (PPP) loan data. In order to capture the process as completely as possible, this file may contain typos or other errors, though hopefully none that are substantive!

# Locating the data

Started out by trying several sets of search terms, beginning with the (autocompleted) "ppp loan database." This led to the following page on the treasury website, where I had previously downloaded a version of the data for an earlier project:

https://home.treasury.gov/policy-issues/cares-act/assistance-for-small-businesses/sba-paycheck-protection-program-loan-level-data

Wanting to make sure I hadn't missed anything, I went to the PPP Wikipedia page (https://en.wikipedia.org/wiki/Paycheck_Protection_Program) and skimmed through the entry, which indicated that the program had been renewed in early 2021. Recalling news coverage of problems with the reporting about who was receiving PPP funds, I read a few of the articles linked from the "Criticism of recipients" section (https://en.wikipedia.org/wiki/Paycheck_Protection_Program#Criticism_of_recipients), including an NBC news article that indicating that new data had been released in December, 2020 (https://www.nbcnews.com/business/business-news/release-ppp-loan-recipients-data-reveals-troubling-patterns-n1249629). Although that article contained a link directly to the data (https://sba.app.box.com/s/5myd1nxutoq8wxecx2562baruz774si6), to confirm its provenance I went back to my search results and found a link to the Small Business Administration website (https://www.sba.gov/funding-programs/loans/coronavirus-relief-options/paycheck-protection-program/ppp-data) "below the fold" on the search results page. There I found a link back to the same SBA Box folder.

# Timeliness

The process of finding the data in the first place included some of the timeliness work. Given that the "last updated" date on the SBA page (https://www.sba.gov/funding-programs/loans/coronavirus-relief-options/paycheck-protection-program/ppp-data#section-header-4) was only a few days earlier, I felt comfortable that this was, in fact, the most recent data available.

# Completeness

Given that this program happened in phases, I can think of a few ways to confirm the data I was looking at contained *all* the loan info:

1. Did it include loans dated prior to August 8, 2020?
2. Wash it larger/did it have more rows than the data released in August 2020?
3. Could I find the records from August 2020 in the most recent file?

Having downloaded the `public_150k_plus.csv` data from https://sba.app.box.com/s/5myd1nxutoq8wxecx2562baruz774si6/folder/127201759675, I opened it in a text editor. First row of data contained a `DateApproved` value of `05/01/2020`. First test passed.

Needing to compare the August release to the most recent release, I renamed the file I had downloaded to `public_150k_plus_recent.csv` and downloaded the August file linked from https://home.treasury.gov/policy-issues/cares-act/assistance-for-small-businesses/sba-paycheck-protection-program-loan-level-data, naming it `public_150k_plus_august2020.csv`.
