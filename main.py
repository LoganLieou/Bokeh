import os
import markdown

paths = []

# takes all the files in current directory
# collect all markdown files
files = os.listdir(".")
for file in files:
    if ".md" in file:
        paths.append(file)

# convert each markdown file to a html file
# the html file is named the same as the markdown one
for path in paths:
    with open(path, "r") as f:
        contents = f.read()
        f.close()

    newfile = "{}.html".format(path[:-3])

    with open(newfile, "w") as f:
        f.write(markdown.markdown(contents))
        f.close()
