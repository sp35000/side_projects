#!/bin/sh
# -------------------------------------------------------------
# App       : Finn
# Program   : mfindPeople.sh
# Function  : find people in multiple files
# Site      : https://bitbucket.org/sp35000/
# Author    : Celso Kikuchi <sp35000@yahoo.com.br>
# -------------------------------------------------------------
# 20220628: initial version
# -------------------------------------------------------------
# initialize variables
FILES="/home/yzmu/Documents/europe-202205/*/*"
# -------------------------------------------------------------
# start
echo "\n----------------------------------------------------------"
echo "Script: $0 START"
date
# main
for FILE in $(ls $FILES); do
 python /home/yzmu/myCloud/to_cloud/lab/pythonStudy/findPeople/findPeople.py -i $FILE
done
date
echo "Script: $0 END"
echo "----------------------------------------------------------"
