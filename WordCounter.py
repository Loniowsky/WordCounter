#!/usr/bin/env python3

import argparse as ap
import sys
import mmap

def word_counter(do_count_chars, do_count_words, do_count_lines, stream):
	if stream == False:
		stream = sys.stdin
	else:
		stream = open(stream.name,"r")

	number_of_lines = number_of_words = number_of_chars = 0
	for line in stream:
	    if do_count_lines:
	        number_of_lines += 1
	    if do_count_words:
	        for _ in line.split():
	            number_of_words += 1
	    if do_count_chars:
	        for char in line:
	        	if (not ( char == "\n" or char == " ")):
	        		number_of_chars+=1

	if do_count_lines:
	    print('Number of lines: ', number_of_lines)
	if do_count_words:
	    print('Number of words: ', number_of_words)
	if do_count_chars:
	    print('Number of characters: ', number_of_chars)

parser = ap.ArgumentParser(description='Program for counting lines/words/letters in a given file')


parser.add_argument('--file', '-f', default = False, type = ap.FileType('r'), action = 'store', help = "read input from specified file (with extension)\n" "standard input is default")

parser.add_argument('--lines', '-l', action = 'store_true', dest = 'do_count_lines', default = False, help = "print number of lines")
parser.add_argument('--words', '-w', action = 'store_true', dest = 'do_count_words', default = False, help = "print number of words")
parser.add_argument('--chars', '-c', action = 'store_true', dest = 'do_count_chars', default = False, help = "print number of characters (without whitespace)")

try:
	args = parser.parse_args()
except :
	print("Argument or file error. Check -h and/or file name. Exiting")
	exit(-1)

if args.do_count_lines or args.do_count_chars or args.do_count_words:
    word_counter(args.do_count_lines, args.do_count_chars, args.do_count_words, args.file)
else:
    print('No options chosen, use -h option to see the other options.')
