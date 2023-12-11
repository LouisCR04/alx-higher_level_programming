#!/bin/bash
echo "File name?"
read file
echo -e "#!/usr/bin/node" > $file
chmod u+x $file
vim $file
