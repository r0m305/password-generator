
    ░█▀█░█▀█░█▀▀░█▀▀░█▀▀░█▀▀░█▀█
    ░█▀▀░█▀█░▀▀█░▀▀█░█░█░█▀▀░█░█
    ░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀

[*] By Romeos
Usage: pass_generator.py [options]

Options:
  -h, --help         show this help message and exit
  --min-len=MIN      Minimum length of password combinations
  --max-len=MAX      Maximum length of password combinations
  --charset=CHARSET  Character set for generating password combinations e.g
                     abcde, ABCDE,abcd1234 etc

EXAMPLES:
- To generate password combinations from 'abcdefgh123' as the character set, with minimum length of 5 and a maximum length of 10:
	python3 pass_generator.py --min-len=5 --max-len=10 --charset=abcdefgh123
