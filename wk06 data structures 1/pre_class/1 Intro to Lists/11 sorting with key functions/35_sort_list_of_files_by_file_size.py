# Example: Sort a list of files by file size
import os
files = ['as_chapter5.pdf', 'Deltarune.zip', 'install.sh', 'intro.odt']
files.sort(key=os.path.getsize)
print(files)