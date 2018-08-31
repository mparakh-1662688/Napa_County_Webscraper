# Napa_County_Webscraper
    1) For each inspection for each facility on a single page of results from the Napa county health
       department website (url given below), the following information will be scraped:
       - Street info
       - City
       - State
       - Zipcode
       - Inspection date
       - Inspection grade
       - For each out-of-compliance violation type, scrape the violation type number and corresponding description.
         For example, an inspection might contain violation type numbers 6 and 7, and descriptions
         "Adequate handwashing facilities supplied & accessible" and "Proper hot and cold holding temperatures"
    2) This information will be placed in a SQL database. Which can constantly be update if the link gets modified to
       Scrape an other page with on the Napa county health department website.
    3) The current database only holds a sample of data from the first 3 page on their website. 
       (But the same could be done for all the pages if required) 


SQLite recommended settings
.width 30 10 15 10 15 6
.mode column
.header on 
