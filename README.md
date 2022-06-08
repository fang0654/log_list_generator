# log_list_generator
Simple tool to generate a wordlist of potential log file names for use in web application brute forcing.

# Usage

You know that feeling. You've just gotten that 403 on `https://<appname>/logs`. You _know_ there is something juicy in there. 

This tool generates a list of potential log file names. It'll substitute in dates and times to make a large brute forcible list to throw at an endpoint.

```
usage: create_log.py [-h] [-t TEMPLATE] [-o OUTPUT] [-d DAYS] [-p PID]

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        Template file to use (default log_names.tmpl)
  -o OUTPUT, --output OUTPUT
                        Output file for generated wordlist. (default lognames.txt)
  -d DAYS, --days DAYS  Number of days back to generate (default 14)
  -p PID, --pid PID     Max PID (default 10000)

```

The idea is to have a list of 'templates' in the "templates" folder with .tmpl extensions. If there are date ({m} {y} {d}) fields, the script will auto generate candidates from DAYS. If there is a {pid} the system will generate all candidates from 0 to PID.

Any contributions on additional log naming formats would be most welcome!
