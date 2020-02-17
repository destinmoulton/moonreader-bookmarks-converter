#!/usr/bin/env python3

import sys
import getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print_help_and_exit()
    for opt, arg in opts:
        if opt == '-h':
            print_help_and_exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile == "":
        print_help_and_exit()
    else:

        print('Input file is "', inputfile)
        print('Output file is "', outputfile)
        read_file_lines(inputfile)


def print_help_and_exit():
    print('convert.py -i <inputfile> -o <outputfile>')
    sys.exit(2)


def read_file_lines(input_file_name):
    with open(input_file_name) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1


if __name__ == "__main__":
    main(sys.argv[1:])
