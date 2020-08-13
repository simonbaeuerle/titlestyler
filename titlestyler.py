"""
Adjusts Capitalization inside *.bib file

Words that need to be uppercase can be defined within a list
They are searched within the *.bib file and eclosed into curly braces
This will lead to proper definition within the *.bbl file
*.bbl file will lead to proper output in the *.pdf file

13.08.2020 Simon Bäuerle
"""

import os
import fileinput
import copy


# Define root directory location
if (os.name == "nt"):
    osPath = "C:\\Users\\Simon\\Git\\titlestyler"
else:
    osPath = "home/simon/git/titlestyler"

# Define bibliography file name
bibFile = "Literature.bib"

# Define search strings and how they should be replaced
# First entry: this string is search for
# Second entry: This is what we replace the first entry with
searchAndReplace = [ \
    ["3d", "3D"], \
    ["6d", "6D"], \
    ["rgb", "RGB"], \
    ["posecnn", "PoseCNN"], \
    ["ssd-6d", "SSD-6D"], \
    ["test99", "test88"], \
    ["test1", "test99"]]


# Open bib file and read content  
with open(os.path.join(osPath, "Latex", bibFile), 'r') as file :
  allLines = file.readlines()


newContent = ""
for line in allLines:
    # Cache line content before modification
    newLine = copy.deepcopy(line)

    # Only modify title
    if line.startswith("\ttitle ="):
        # Replace strings as defined above
        # Also: introduce curly braces around replaced string
        # the curly braces will tell bibtex to keep the capitalization "as is"
        for entry in searchAndReplace:
            newLine = newLine.replace(entry[0], "{" + entry[1] + "}")
    
    # Append (possibly modified) line
    newContent += newLine

# Overwrite bib file with modified version
with open(os.path.join(osPath, "Latex", bibFile), 'w') as file:
  file.write(newContent)

print("")