#!/usr/bin/env python3

import sys
import getopt
import pprint


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
    output = []
    with open(input_file_name) as fp:
        line = fp.readline()

        # first line is the book title
        output.append("## " + line)

        line = fp.readline()

        cnt = 1
        while line:
            if len(line) > 1:

                print("line[1] = {}".format(line[0]))
                if line[0] == "▪":
                    note = ""
                    note_start = -1
                    if line[-1] == ")":
                        # Notes are in parens at the end
                        note_start = line.rfind("(")
                        note = line[note_start + 1:line.rfind(")")]

                    # Highlight
                    output.append("    - " + line[2:note_start])

                    if note != "":
                        output.append("        - `" + note + "`")

                elif line[0] == "◆":

                    # Chapter
                    output.append("- " + line[2:])

            line = fp.readline()
            cnt += 1

        pprint.pprint(output)


if __name__ == "__main__":
    main(sys.argv[1:])
