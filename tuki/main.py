import sys
from . import start
from . import section
def print_help():
    print(r""" 
  _______    _    _
 |__   __|  | |  (_)
    | |_   _| | ___ 
    | | | | | |/ / |
    | | |_| |   <| |
    |_|\__,_|_|\_\_|
    """)

    print("TUKI is a simple static website generator")
    print("Available commands:")
    print(" init: initializes the site and its main article")
    print("     usage: tuki init path-to-markdown-file.md title")
    print(" section : modify a section or add a new one ")
    print("     usage: tuki section index path-to-markdown-file.md title\n")


def main():
   try:
        if sys.argv[1]=="help": print_help()
        if sys.argv[1]=="init":
                start.init(sys.argv[2],sys.argv[3])
        if sys.argv[1]== "section":
                section.add_article(sys.argv[2],sys.argv[3],sys.argv[4])
   except: print("use tuki help for help")

if __name__ == "__main__":
    main()
