import sys
from init import init
from section import add_article
def print_help():
    print("TUKI is a simple static website generator")
    print("Available commands:")
    print(" init: initializes the site and its main article")
    print("     usage: tuki init path-to-markdown-file.md title")
    print(" add : adds a section ")
    print("     usage: tuki add index path-to-markdown-file.md title")
def main():
    try:
        if sys.argv[1]=="help": print_help()
        if sys.argv[1]=="init":
                init(sys.argv[2],sys.argv[3])
        if sys.argv[1]== "add":
                add_article(sys.argv[2],sys.argv[3],sys.argv[4])
    except: print("use help for help")

if __name__ == "__main__":
    main()
