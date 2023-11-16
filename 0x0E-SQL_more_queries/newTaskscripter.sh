#!/bin/bash
echo "File name?"
read file
echo "" > $file
chmod u+x $file
vim $file
