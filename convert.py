#!/usr/bin/env python3

import sys
import pprint
import pyperclip
import argparse


def main(argv):

    parser = argparse.ArgumentParser()
    #parser.add_argument("-h", dest="help", action="store_true")
    parser.add_argument("-i", "--inputfile")
    parser.add_argument("-o", "--outputfile")
    parser.add_argument("-m", "--markdowntype")
    args = parser.parse_args()

    if args.inputfile == "":
        print_help_and_exit()
    else:

        print('Input file is "', args.inputfile)
        if args.markdowntype == "tiddlywiki":
            lines = convert_file_to_tiddlywiki_markdown(args.inputfile)
        else:
            lines = convert_file_to_standard_markdown(args.inputfile)
        

        if len(lines) > 1:
            if args.outputfile != "":
                write_output_file(args.outputfile, lines)
                print("Markdown written to: " + args.outputfile)

            print("Markdown copied to system clipboard")
            copy_lines_to_clipboard(lines)


def print_help_and_exit():
    print('convert.py -i <inputfile> -o <outputfile> -m <markdowntype>')
    print('\t-o <outputfile> is OPTIONAL')
    print('\tMarkdown is copied to system clipboard.')
    print('\ti.e. `convert.py -i bookmarks.txt -m tiddlywiki`')
    sys.exit(2)

# Convert a file to a standard markdown format
def convert_file_to_standard_markdown(input_file_name):
    output = []
    with open(input_file_name) as fp:
        line = fp.readline()

        # first line is the book title
        output.append("## " + line)

        line = fp.readline()

        cnt = 1
        while line:
            line = line.strip()

            output = output + convert_line_to_standard_markdown(line)
            line = fp.readline()
            cnt += 1

    return output

# Convert a line from the bookmarks to a standard markdown format
def convert_line_to_standard_markdown(line):
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

# Convert a file to a tiddlywiki markdown format
def convert_file_to_tiddlywiki_markdown(input_file_name):
    output = []
    with open(input_file_name) as fp:
        line = fp.readline()

        # first line is the book title
        output.append("! " + line)

        line = fp.readline()

        cnt = 1
        while line:
            line = line.strip()

            output = output + convert_line_to_tiddlywiki_markdown(line)
            line = fp.readline()
            cnt += 1

    return output

# Convert a line from the bookmarks to a tiddlywiki markdown format
def convert_line_to_tiddlywiki_markdown(line):
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
            markdown.append("* " + line[2:note_start])

            if note != "":
                markdown.append("* NOTE: `" + note + "`")

        elif line[0] == "◆":

            # Chapter
            markdown.append("!! " + line[2:])
    
    # Append an extra line for tiddlywiki
    markdown.append("")
    return markdown

def write_output_file(output_filename, output_lines):
    with open(output_filename, mode="wt", encoding="utf-8") as fp:
        fp.write('\n'.join(output_lines))


def copy_lines_to_clipboard(output_lines):
    # Use pyperclip to copy to the system clipboard
    pyperclip.copy('\n'.join(output_lines))


if __name__ == "__main__":
    main(sys.argv[1:])
