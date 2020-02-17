#!/usr/bin/env python3

import sys
import getopt
import pprint
import pyperclip


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
        lines = convert_file_to_markdown_list(inputfile)

        if len(lines) > 1:
            if outputfile != "":
                write_output_file(outputfile, lines)
                print("Markdown written to: " + outputfile)

            print("Markdown copied to system clipboard")
            copy_lines_to_clipboard(lines)


def print_help_and_exit():
    print('convert.py -i <inputfile> -o <outputfile>')
    print('\t-o <outputfile> is OPTIONAL')
    print('\tMarkdown is copied to system clipboard.')
    sys.exit(2)


def convert_file_to_markdown_list(input_file_name):
    output = []
    with open(input_file_name) as fp:
        line = fp.readline()

        # first line is the book title
        output.append("## " + line)

        line = fp.readline()

        cnt = 1
        while line:
            line = line.strip()

            output = output + convert_line_to_markdown(line)
            line = fp.readline()
            cnt += 1

    return output


def convert_line_to_markdown(line):
    markdown = []
    if len(line) > 1:

        if line[0] == "▪":
            note = ""
            note_start = -1
            if line[-1] == ")":
                # Notes are in parens at the end
                note_start = line.rfind("(")
                note = line[note_start + 1:-1]

            # Highlight
            markdown.append("    - " + line[2:note_start])

            if note != "":
                markdown.append("        - NOTE: `" + note + "`")

        elif line[0] == "◆":

            # Chapter
            markdown.append("- " + line[2:])

    return markdown


def write_output_file(output_filename, output_lines):
    with open(output_filename, mode="wt", encoding="utf-8") as fp:
        fp.write('\n'.join(output_lines))


def copy_lines_to_clipboard(output_lines):
    # Use pyperclip to copy to the system clipboard
    pyperclip.copy('\n'.join(output_lines))


if __name__ == "__main__":
    main(sys.argv[1:])
