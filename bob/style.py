import autopep8
import os.path
from termcolor import colored


def output(newfilename):
    pr = open(newfilename)
    print()
    for lines in pr.readlines():
        print(colored(lines.rstrip(), 'yellow'))


def load_file(file, newfilename):

    outfile = open(newfilename, 'w+')
    autopep8.fix_file(file, None, outfile)
    outfile.close()
    print("Code formatted successfully and saved to", newfilename)
    if input("Press 'y' if you want to print the output to console: ") == 'y':
        output(newfilename)

        
def styleme():
    filename = input("Enter file name: ")
    while not os.path.exists(filename):
        print(colored("File not found. Try again", "red"))
        filename = input("Enter file name: ")
    else:
        newfilename = filename.rstrip('.py') + "-styled.py"
        load_file(filename, newfilename)


