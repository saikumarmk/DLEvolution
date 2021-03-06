# DLEvolution

### Breakdown

This is a repository consisting of notebooks that scrape Github repository data.

## Progress

So far, I've got a basic class for sending requests to the Github REST API (see here: https://docs.github.com/en/rest). You will need to create a token for more requests. 

- You can scrape repositories by topic and thing such as when they were released
- Scrape commits and releases from a repository
- Scrape diffs from each file in each commit along with the message

## Files

The `tools.py` file contains a class that handles request sending. You will need to do `.json()` on any function you call within the class as it returns the raw request. The other files are named by their purpose. The speechbrain and yolov5 files contain experiments on extracting diff information.

# DotEnv

You will need to place a `.env` file with your username and token in order to use it. Or, you can just put your username and token directly in.

## Future work

In the future, I recommend developing the regex expression in CommitScraping, so that we can capture more information from each changed line. Additionally, grouping repositories then running the analysis on those sets will yield more information on types of mutations one can perform.

- When performing regular expression matching, group the types of matches by things like hyperparameters or layers, or perhaps for different libraries.
- Automate the scraping process for topics by having the scraper cool down after it hits the 2000 request per hour limit.
- Begin to scrape details such as how many layers are being used, settings for each layer and so on.
- Classify commit diffs.