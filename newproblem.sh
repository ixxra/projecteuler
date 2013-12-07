#!/bin/bash
id=$1
new_folder=$( printf "problem%03d" $id )

test -e $new_folder && echo "Error: $new_folder already exists!" && exit 1

mkdir $new_folder
touch $new_folder/statement.md
echo -e "#!/usr/bin/env python2\n" > $new_folder/problem"$id".py
echo "Problem ready...  go get it!"
