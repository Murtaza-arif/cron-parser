# Cron Parser

How to run the code
```run the code
python main.py "*/15 0 1,15 * 1-5 /usr/bin/find"
```
output would be in terminal would be
```commandline
minute: 0 15 30 45
hour: 0
day of month: 1 15
month: 1 2 3 4 5 6 7 8 9 10 11 12
day of week: 1 2 3 4 5
command: /usr/bin/find
```

How to run the unit test cases
```run the tests
python  -m coverage run -m unittest parser_test.py
```

Generate the coverage report
```generate report
python -m coverage report
```
output would be
```commandline
Name             Stmts   Miss  Cover
------------------------------------
cron_parser.py      34      6    82%
parser_test.py      15      0   100%
------------------------------------
TOTAL               49      6    88%
```