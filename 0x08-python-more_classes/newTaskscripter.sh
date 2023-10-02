#!/bin/bash
echo "File name?"
read file
echo -e "#!/usr/bin/python3\n# -*- coding: UTF-8 -*-\n\"\"\"\n-rectangle.py: Defines a Rectangle\n\"\"\"\n\n\nclass Rectangle:\n    \"\"\"class Rectangle that\n\n    Attributes:\n        attr1 ():\n\n    \"\"\"" > $file
chmod u+x $file
vim $file
