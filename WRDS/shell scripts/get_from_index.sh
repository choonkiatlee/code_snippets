#!/bin/sh

# ------------------------------------------------------------------
# [thevillageidiot] Build Index 
#          build index for a flat file
# ------------------------------------------------------------------

VERSION=0.1.0
SUBJECT=00001
USAGE="
Description: Gets rows from an index and outputs to a file
Usage: arguments -i => input filename  (database) |
                 -o => output filename (index file) |
                 -d => delimiter |
                 -h => help |
                 -v => version |
                 "

# --- Source includes from other files -----------------------------

source_includes(){
    DIR="${BASH_SOURCE%/*}"
    if [[ ! -d "$DIR" ]]; then DIR="$PWD"; fi
    source "$DIR/$1"   
}

source_includes utils.sh

get_from_index(){

    USAGE="Input indexes to search for as input arguments"

    local input_filename=$1
    local start_index=$2
    local next_index=$3

    check_variable_present "$1" "input filename not present!"
    check_variable_present "$2" "start index not present!"
    check_variable_present "$3" "next index not present!"

    local end_index=$(($next_index-$start_index))

    dd if=$input_filename ibs=1 skip=start_index count=1197 status=none

}

dd if=test.txt ibs=1 skip=5240 count=1197 status=none