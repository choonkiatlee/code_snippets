#!/bin/bash

if [ -z "$1" ]
then 
    echo Please enter a valid wrds data filepath to examine
    exit
else
    INPUT_DATABASE=$1
fi

# wc -l reads in a file and provides a count of the number of lines
LINECOUNT="$(wc -l "$INPUT_DATABASE" |awk '{ print $1 }')"

echo There are "${LINECOUNT}" lines in $INPUT_DATABASE

echo "These are a few sample lines... (possibly very big)"

head -3 $1

# grep -o provides a new line for every occurence of the chars its searching for,
# then count these lines with wc -l
COLUMNCOUNT="$(head -1 "$INPUT_DATABASE" | grep -o '|' | wc -l)"
echo "There are "$COLUMNCOUNT "columns in the data"
echo "You can choose a particular column index to view / save next or skip to skip"
read COL_IDX

if [ "$COL_IDX" = "skip" ]
then 
    echo skipping...
else
    echo Data for 1 feature:
    # Cut -d '|' splits by the delimiter '|', then -f1 prints the 1st column etc. 
    head -10 $INPUT_DATABASE | cut -d '|' -f$COL_IDX
    COLNAME="$(head -1 "$INPUT_DATABASE" | cut -d '|' -f"$COL_IDX" )"
    echo "Do you want to save this data? (yes/no)"

    read SAVE

    if [ "$SAVE" = "yes" ]
    then 
        awk -F\| '{ print $'${COL_IDX}' }' $INPUT_DATABASE > ${COLNAME}.txt
    fi
fi

echo "You can choose a particular gvkey to view / save next or skip to skip"

read GV_KEY

if [ "$GV_KEY" = "skip" ]
then
    echo "skipping..."
else
    echo "Collecting data for company with gvkey "$GV_KEY "..."
    Data=$(awk -v gv_key="$GV_KEY" -F\| '$1==gv_key || $1=="gvkey"' $INPUT_DATABASE   )
    #echo $Data | head -2

    echo "Collected Data for compay with gvkey "$GV_KEY

    echo "Do you want to save this data? (yes/no)"
    read SAVE

    if [ "$SAVE" = "yes" ]
    then 
        echo "$Data" > "${GV_KEY}.txt"
    fi
fi












