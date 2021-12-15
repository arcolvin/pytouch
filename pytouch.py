#!/usr/bin/env python3

import os, sys

if len(sys.argv) < 2:
    # Check for at least 1 argument
    print('Argument required. Type "{} --help" for more info'.format(sys.argv[0]))
    sys.exit()

if '--help' in sys.argv:
    # help string
    # presented when --help flag is used
    hlp = '''
    This is a script designed to automate making a python script.
    It condenses creating and setting basic executable permissions
    for your scripts. It will also set up your shebang at the top 
    of your script.

    basic usage is:

    {} <desired_file_name> <OPTIONAL_python_version_number>

    Default python version is python3
    
    To change version enter just the version number. 
    ex. "3.6" or "2.7"



    Thank you for using pytouch!
    ~Adam
    '''.format(sys.argv[0])

    print(hlp)
    sys.exit()

if len(sys.argv) > 2:
    # setting the desired python value if user does not want to use default
    version = sys.argv[2]

else:
    # default python version
    version = '3'

if os.path.isfile('./{}'.format(sys.argv[1])):
    # check to see if file already exists
    # prevent clobber if file already present
    print('File exists already!')
    sys.exit()

else:
    # main script
    # create desired empty python script
    # give executible permissions to only the file owner
    # populate the shebang line for desired python version
    # open new python script in vi

    os.system("touch {} && \
            chmod 700 {} && \
            echo '#!/usr/bin/env python{}' > {} && \
            vi {}".format(sys.argv[1], sys.argv[1], version, sys.argv[1], sys.argv[1]))

