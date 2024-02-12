<div align="center">
  <a href="https://github.com/5ukui/waybackmachine-cli">
    <img src="build/main/wayback.png" alt="Logo" width="380" height="140">
  </a>
  
  <h3 align="center">waybackmachine-cli</h3>
</div>

## About The Project
A CLI application that allows you to interact with the Archive.org's Wayback Machine to download webpages and search for text within the pages using scraping.

## Installation
• Create a new folder for the application.

• Open the folder using command prompt.

• Clone the repository
```
git clone https://github.com/5ukui/waybackmachine-cli
```

## Options
• Help page:
```
wayback.exe --help
```
• Options:
```
Usage: wayback.exe [OPTIONS]

  CLI program to interact with the wayback machine.

Options:
  --url example.com  Specify the URL to search for.
  --term "example"   Specify the search term.
  --date YYYYMMDD    Specify a specific date.
  --time HHMMSS      Include the time in the search.
  --find "Example"   Find text on the webpage. (Case sensitive, include capitalization)
  --download         Download webpage html.
  --help             Show this message and exit.
```

## Usage Examples
#### • Searching for captures info about a website:
```
wayback.exe --url justice.gov
```
#### • Output:
```
Searching for the URL: justice.gov
Saved 31,741 times between September 26, 2001 and February 11, 2024.
```
____________________________________________________________________________________________________________________
#### • Searching for a term instead of an URL (Searching for websites without the URL)
with space:
```
wayback.exe --term "privacy tools"
```
without space:
```
wayback.exe --term privacytools
```
#### • Output:
```
+---------------------------------------+-----------------------------------------------+-----------+--------+-------+---------+
|                  Link                 |                      Desc                     | Web Pages | Images | Audio | VID/GIF |
+---------------------------------------+-----------------------------------------------+-----------+--------+-------+---------+
|        http://privacytools.io/        |                 privacy tools                 |     11    |  207   |   0   |    0    |
|       http://privacytools.info/       |             www.privacytools.info             |     12    |   3    |   0   |    0    |
|        http://privacytool.org/        |                privacytool.org                |     12    |   3    |   0   |    0    |
|         http://privacytool.tk/        |                 privacytool.tk                |     1     |   1    |   0   |    0    |
|  http://privacytools.freeservers.com/ |             internet privacy tools            |     18    |   24   |   0   |    0    |
|     http://privacy.policytool.net/    | a privacy policy generator called privacytool |     18    |   22   |   0   |    0    |
|   http://privacytools.xeudoxus.com/   |        http://privacytools.xeudoxus.com       |     2     |   1    |   0   |    0    |
| http://privacytools.seas.harvard.edu/ |     http://privacytools.seas.harvard.edu/     |    517    |  155   |   0   |    0    |
|         http://privacytool.cf/        |             http://privacytool.cf             |     0     |   9    |   0   |    0    |
|       http://e-privacytools.com/      |                 e-privacytools                |     1     |   0    |   0   |    0    |
|       http://iprivacytools.com/       |               iprivacytools.com               |     95    |  165   |   0   |    0    |
|      http://perfectlyprivate.com/     |             perfectlyprivate, inc.            |    353    |  284   |   0   |    0    |
|        http://killhistory.net/        |          http://www.killhistory.net/          |     62    |   61   |   0   |    0    |
+---------------------------------------+-----------------------------------------------+-----------+--------+-------+---------+
```
___________________________________________________________________________________________________________________
#### • Searching for URL (justice.gov) with date (2022-02-19) and no time and searching for a string within the snapshot:
```
wayback.exe --url justice.gov --date 20220219 --find U.S
```
#### • Output:
```
Searching for the URL: justice.gov
Saved 31,741 times between September 26, 2001 and February 11, 2024.

Matches for "U.S":
• U.S. Department of Justice
• FBI U.S. Capitol Violence Most Wanted
• U.S. Department of Justice
```
___________________________________________________________________________________________________________________
#### • Searching for URL (justice.gov) with date (2022-02-19) and time (21:44:31) and searching for a string:
```
wayback.exe --url justice.gov --date 20220219 --time 214431 --find U.S
```
#### • Output:
```
Searching for the URL: justice.gov
Saved 31,741 times between September 26, 2001 and February 11, 2024.

Matches for "U.S":
• U.S. Department of Justice
• FBI U.S. Capitol Violence Most Wanted
• U.S. Department of Justice
```
___________________________________________________________________________________________________________________
#### • Searching for URL (justice.gov) with date (2022-02-19) and time (21:44:31) and searching for multiple words on the webpage, then downloading the snapshot:
```
wayback.exe --url justice.gov  --date 20220219 --time 214431 --find Man,man,"Conspiracy to",WHY --download
```
#### • Output:
```
Searching for the URL: justice.gov
Saved 29,552 times between September 26, 2001 and February 11, 2024.

Matches for "Man":
• Justice Manual
• Tennessee Man Sentenced to Seven Years for Series of Church Arsons
• California Man Sentenced to Life in Prison for Creating Child Sexual Abuse Material of A Number of Young Children and Engaging in a Child Exploitation Enterprise
• Pakistani Man Sentenced for Health Care Fraud and Money Laundering Conspiracy
• Wisconsin Man Convicted of Sex Trafficking Adult and Minor Victims
• Pennsylvania Man Charged with Torture

Matches for "man":
• Budget &amp; Performance
• Oregon State Employee Indicted for Sexual Misconduct and Kidnapping Woman with Developmental Disabilities
• Budget &amp; Performance

Matches for "Conspiracy to":
• Former Massachusetts Resident Pleaded Guilty to Conspiracy to Commit Sex Trafficking and Related Charges

No matches found for "WHY".

The snapshot for that time doesn't exist. Downloading snapshot: 2022-02-19 21:40:58 instead.
Downloading Snapshot (2022-02-19 21:40:58): 1.27MB [01:14, 17.0kB/s]
```


