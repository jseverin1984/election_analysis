# Election Results Analysis

## Overview of Election Audit

For this election audit, I was tasked with analyzing all of the votes for a specific precinct in the state of Colorado.
While analyzing the data, I needed to collect the overall total votes, total votes for each candidate, percentage of votes for each candidate,
and the overall winner of the election by popular vote.  Also, I collected data based off of votes cast in each county.  I was asked
to write a script in Python in order to automate the vote counting process. This way, Colorado could use the Python script 
to automate all election data for any congressional or local election. 
	

## Election Audit Results

- How many votes were cast in this congressional election?

A total of 369,711 votes were cast in the congressional election.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

- Which county had the largest number of votes?
Denver county had the largest number of votes with 306,055. Below was the code used to find that data.
```
for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes_each_county = county_votes[county_name]
        # 6c: Calculate the percent of total votes for the county.
        votes_each_county_percentage = float(votes_each_county) / float(total_votes) * 100

        # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {votes_each_county_percentage:.1f}%({votes_each_county:,})\n")

        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (votes_each_county > largest_county_votes_count):

            largest_county_votes_count = votes_each_county
            largest_county = county_name
```


- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

![alt text](https://github.com/jseverin1984/election_analysis/blob/master/Resources/candidates.png "candidate results")

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

![alt text](https://github.com/jseverin1984/election_analysis/blob/master/Resources/overall_winner.png "overall winner results")


## Election Audit Summary

With this general election results Python script, the state of Colorado would be able to automate election results, with slight modification,
at all level of government.  This script can be used as a template to fit the desired needs for each election.  For example, if in a senate election,
votes came in by mail, by paper ballot and by electronic and all three data sets were counted and stored separately in their own csv files. I
could modify the script in order to merge all forms of voting in order to streamline the tallying of votes and automate the winner. Also,
if the results needed to be broken down into how many votes each candidate received from each county, modifying some of the script would produce
that data.