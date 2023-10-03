#!/bin/bash
echo "Enter Answer:"
read ans
echo "File no:"
read file
echo $ans > $file-answer.txt
