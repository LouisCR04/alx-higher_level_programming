#!/bin/bash
echo "File name?"
read file
echo -e "#!/usr/bin/node\n//$file" > $file
chmod u+x $file
vim $file
