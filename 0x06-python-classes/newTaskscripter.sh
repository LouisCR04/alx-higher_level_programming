#!/bin/bash
echo "File name?"
read file
echo -e "#!/usr/bin/python3\n# -*- coding: UTF-8 -*-\n\"\"\"\n0-square.py: Empty class Square that defines a square\n\"\"\"\n\n\nclass Square:\n    \"\"\"class Square that\n\n    Attributes:\n        attr1 ():\n\n    \"\"\"" > $file
chmod u+x $file
vim $file
