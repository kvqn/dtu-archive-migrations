# DTU Archive Scraping and Migration Tool

Command line utility for scraping (and migrating) results published by Delhi Technological Univesity.

This is a utility I made for internal use to create the database for [DTU Archive](https://github.com/kvqn/dtu-archive) but decided to make it and the migrations public for transparency and convinience.

## Creating excel file from a result PDF

If you've come here, you most likely want to create an EXCEL file from a result PDF.

If I'm right, clone the repo and run the command below :

```
python manage.py scrape create-excel <pdf>
```

This should create an .xlsx file in the same directory.

If something goes wrong and you get an error see creating an issue section.

Further reading about the CLI.

## Creating an issue

### There's an issue with the results

If you encounter some inconsistency with the results shown on the website, then create and issue. \
 Be sure to highlight which record has the problem and provide the link to the result which contains the correct and most up to date result.

([ List of all results published by DTU ](http://exam.dtu.ac.in/result.htm))

### There's an error with the scraping tool.

Make sure you have the dependencies installed and are executing the command in the correct directory.

If you have an error saying `Expected student line or table header, but got something else.`, then create an issue. Provide the link to the result you tried to scrape. This error means that the scraping utility encountered a new pattern of strings and was unable to understand how to declutter or understand how to parse the text.


