# Example: Sort a list of files by extension
import os

os.path.splitext("Deltarune.zip")
os.path.splitext("Deltarune.tar.gz")
os.path.splitext("tmp/Deltarune.zip")
filename = "tmp/Deltarune.zip"
print(os.path.splitext(filename)[1])

# This lambda expression gets the file extension from a pathname:
lambda f: os.path.splitext(f)[1]

# .sort(key=lambda f: os.path.splitext(f)[-1]) # enables a list of files to be sorted in alphabetical order by extension

files = ['as_chapter5.pdf', 'Delarune.zip', 'install.sh', 'intro.odt']
files.sort(key=lambda f:os.path.splitext(f)[-1])
print(files)