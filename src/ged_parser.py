"""
    SSW555
    Matheus Silva
    September 18, 2015
"""

import sys

gedcom_tags_path = "resources/gedcom5.5.1_tags.ged"
gedcom_tags = []


def __init__():
    if len(sys.argv) != 2:
        print("Oops.")
        print("Usage: python ged_parser.py gedcomfile.ged")
        exit(1)
    source_file = sys.argv[1]
    load_valid_tags()
    parse_file(source_file)
    print("Done.")


def parse_file(filename):
    for l in open(filename, "r"):
        line = l[:-2] # Removing 2 last chars, they are line breaks

        elements = line.split(" ", 2) # Spliting string by the 2 first spaces
        level = elements[0]
        tag = elements[1]
        is_tag_valid = tag in gedcom_tags # Check if tag is valid

        print("Line: " + line)
        print(" level: " + level)
        print(" tag  : " + tag)
        print(" Is tag valid? " + ("yes." if is_tag_valid else "no!"))
        print("")


def load_valid_tags():
    # Read Tags file and load tags to gedcom_tags list
    global gedcom_tags
    gedcom_tags = [l[:-1] for l in open(gedcom_tags_path, "r").readlines()]


__init__()

