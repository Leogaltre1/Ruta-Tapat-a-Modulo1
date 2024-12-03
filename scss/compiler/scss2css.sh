#!/bin/bash
#Generator of scss files to css files

echo " "
echo "======================================"
echo "    Executing commands_sass.py"
echo "======================================"
python commands_sass.py
sleep 4
echo "======================================"
echo "    Executing compiler_scss2css.sh"
echo "======================================"
echo "        ==== scss to css ====         "
./compiler_scss2css.sh
sleep 4
echo " "
echo "   ====    DONE Successfully ===="
echo "Do not forget you are La mera V"