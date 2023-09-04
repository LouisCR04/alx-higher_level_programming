#!/bin/bash
echo "File name?"
read file
echo "#!/usr/bin/python3" > $file
chmod u+x $file
vim $file
