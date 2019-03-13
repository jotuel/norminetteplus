#!/usr/bin/python
import os
import sys
import urllib

VERSIONFILE = "https://raw.githubusercontent.com/thijsdejong/codam-norminette-plus/master/version"
__version__ = '19.3.2'

def update():
    try:
        v = urllib.urlopen(VERSIONFILE)
    except Exception as e:
        print("\nUpdate: can't fetch version file: " + e)
    else:
        if (v.getcode() == 200):
            version = v.read().rstrip()
            if (version != __version__):
                print("\nUpdate: you do not have the latest version! The latest version is " + version + ", you have " + __version__ + "!")
        else:
            print("\nUpdate: can't fetch version file")

def get_files(folder):
    for f in os.listdir(folder):
        if (not f.startswith('.')):
            if os.path.isdir(folder + f):
                get_files(folder + f + "/")
    files = [folder + f for f in os.listdir(folder) if os.path.isfile(folder + f)]
    files.sort()
    for file in files:
        check_file(file)


def double_operation(line):
	operations = 0

	if (" = " in line):
		operations += 1
	if ("++" in line):
		operations += 1
	if ("--" in line):
		operations += 1
	if ("+=" in line):
		operations += 1
	if ("-=" in line):
		operations += 1
	if ("*=" in line):
		operations += 1
	if ("/=" in line):
		operations += 1
	if ("&=" in line):
		operations += 1
	if ("|=" in line):
		operations += 1
	if ("^=" in line):
		operations += 1
	if ("<<=" in line):
		operations += 1
	if (">>=" in line):
		operations += 1
	if ("if (" in line):
		operations += 1
	if ("while (" in line):
		operations += 1
	if ("return (" in line):
		operations += 1
	if ("?" in line):
		operations += 1

	if (operations > 1):
		return (1)
	return (0)

def check_file(filename):
	print("Norme: " + filename)
	if (filename.endswith(".c")):
		file = open(filename, "r")
		ln = 1
		for line in file:
			if (double_operation(line)):
				print("line " + str(ln) + ": multiple operations")
			ln += 1

def main():
    argv = sys.argv
    arguments = len(argv)
    if (arguments == 1):
        get_files("./")
    else:
        for f in argv[1:]:
            if os.path.isdir(f):
            	get_files(f + "/")
            elif os.path.isfile(f):
            	check_file(f)
            elif "./" in f:
            	print("Norme: " + f + "\nWarning: Not a valid file")
            elif f[0] != "/":
            	print("Norme: ./" + f + "\nWarning: Not a valid file")
            else:
            	print("Norme: " + f + "\nWarning: Not a valid file")
    update()

if (__name__ == "__main__"):
	main()
