"""
    SSW555
    Team 4
"""

import sys

gedcom_tags_path = "resources/gedcom5.5.1_tags.ged"
gedcom_tags = []

individuals = {}
families = {}


def __init__():
    if len(sys.argv) != 2:
        print("Oops.")
        print("Usage: python ged_parser.py gedcomfile.ged")
        exit(1)
    source_file = sys.argv[1]
    load_valid_tags()
    parse_file(source_file)

    print("\nIndividuals:")
    for i in individuals:
        print("id: " + i + " name: " + individuals[i].name)
    print("\nFamilies:")
    for f in families:
        print("id: " + f +
                " huband: " + individuals[families[f].husband].name +
                " wife: " + individuals[families[f].wife].name)
    print("\nDone.")


def load_valid_tags():
    # Read Tags file and load tags to gedcom_tags list
    global gedcom_tags
    gedcom_tags = [l[:-1] for l in open(gedcom_tags_path, "r").readlines()]


def parse_file(filename):
    index = 0  # line index
    lines = open(filename, "r").readlines()

    while index < len(lines)-1:
        line = GedLine(lines[index])

        if line.level() == 0 and line.content() == "INDI":
            # Create Individual
            ind = Individual(line.tag())  # Tag is the ID
            ind.name = GedLine(lines[index+1]).content()
            individuals[ind.id] = ind

        if line.level() == 0 and line.content() == "FAM":
            # Create Family
            fam = Family(line.tag())  # Tag is the ID
            fam.husband = GedLine(lines[index+1]).content()
            fam.wife = GedLine(lines[index+2]).content()
            families[fam.id] = fam

        index += 1


class GedLine:
    def __init__(self, line):
        self.line = line.strip()  # Removing 2 loose chars and line breaks
        self.elements = line.split(" ", 2)  # Spliting by the 2 first spaces

    def level(self):
        return int(self.elements[0].strip())

    def tag(self):
        return self.elements[1].strip()

    def content(self):
        return self.elements[2].strip() if len(self.elements) == 3 else ""

    def is_tag_valid():
        return self.tag() in gedcom_tags  # Check if tag is valid


class Individual:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.givenname = ""
        self.surname = ""
        self.birthday = ""
        self.deathday = ""


class Family:
    def __init__(self, id):
        self.id = id
        self.husband = ""
        self.wife = ""
        self.children = []


__init__()
