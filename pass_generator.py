#!/usr/bin/python3
'''
Author: Romeos CyberGypsy
Name: pass_generator.py
License: romeos (c)
'''
#########################
##website: romeoscybergypsy.pb.online
##GitHub: https://github.com/r0m305
##Facebook: Romeos CyberGypsy
##email: Romeoscommunity@protonmail.com
#########################

import itertools
from termcolor import colored
from colorama import Fore
import sys
import optparse

class Generator:
    def __init__(self):
        #code comes here
        self.parser = optparse.OptionParser()
        self.parser.add_option("--min-len", dest = "min", help = "Minimum length of password combinations")
        self.parser.add_option("--max-len", dest = "max", help = "Maximum length of password combinations")
        self.parser.add_option("--charset", dest = "charset", help = "Character set for generating password combinations e.g abcde, ABCDE,abcd1234 etc")
        (self.values, self.keys) = self.parser.parse_args()

        if len(sys.argv) < 4:
            print(colored("Usage:","yellow"))
            print("python3 pass_generator.py --min-len=<min_len> --max-len=max_len> --charset=<charset>")
            sys.exit()

        try:
            self.generate(int(self.values.min), int(self.values.max), self.values.charset)

        except KeyboardInterrupt:
            print(colored("Exiting safely!!","red"))
            sys.exit()

        except Exception as e:
            print(colored(e,"red"))
            sys.exit()


    def generate(self, min_len, max_len, charset):
        while min_len <= max_len:
            combs = itertools.permutations(charset, min_len)
            for combination in combs:
                print(''.join(combination))

            min_len+=1

if __name__ == '__main__':
    banner = '''
    ░█▀█░█▀█░█▀▀░█▀▀░█▀▀░█▀▀░█▀█
    ░█▀▀░█▀█░▀▀█░▀▀█░█░█░█▀▀░█░█
    ░▀░░░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀
'''
    print(colored(banner,"green"))
    print(f"{Fore.RED}[{Fore.YELLOW}*{Fore.RED}]{Fore.GREEN} By {Fore.BLUE}Romeos{Fore.RESET}")
    obj = Generator()
