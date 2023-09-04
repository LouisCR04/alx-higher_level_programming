#!/bin/bash
echo "File name?"
read file
echo "#!/bin/bash" > $file
chmod u+x $file
vim $file
