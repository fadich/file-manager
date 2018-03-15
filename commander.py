import os
import re
import subprocess
import console_behaviour
from fs import Dir


HINT = """
There are the simple parameters that could be added after delimiter "|".

f - fully displaying (for directories)
e - execute, open
h - display the hint

For example:
\tpath | f
"""


def get_tree(dir, fully=False, dept=0):
    for item in dir.list_dir():
        print ('\t' * dept) + ('\033[4m' if isinstance(item, Dir) else '') + item.get_name() + '\033[0m'
        if fully and isinstance(item, Dir):
            get_tree(item, fully, dept + 1)


print HINT
print '-' * 32 + '\n'

while 1:
    try:
        input = raw_input('{}: '.format(os.getcwd())).split('|')
    except KeyboardInterrupt:
        exit('\nBye...')
    input = [i.strip() for i in input]
    path = input[0] or '.'
    input = [i.lower() for i in input]

    if input.count('h'):
        print HINT
        continue

    full = input.count('f')
    if Dir.is_dir(path):
        get_tree(Dir(path), bool(full))
        os.chdir(path)
    else:
        if input.count('e'):
            try:
                #subprocess.call([path])
                os.system(path)
            except OSError as err:
                print 'Command "%s" executed with error: %s' % (path, err)
            continue
        print '"%s" is not directory' % path

    print
