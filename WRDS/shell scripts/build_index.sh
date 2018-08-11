#!/bin/sh

# ------------------------------------------------------------------
# [thevillageidiot] Build Index 
#          build index for a flat file
# ------------------------------------------------------------------

VERSION=0.1.0
SUBJECT=00001
USAGE="
Description: builds an index for a flat file, with the 1st column being
             the index and the 2nd column being the file offset
Usage: arguments -i => input filename  (database) |
                 -o => output filename (index file) |
                 -d => delimiter |
                 -h => help |
                 -v => version |
                 "

# --- Source includes from other files -----------------------------

function source_includes(){
    DIR="${BASH_SOURCE%/*}"
    if [[ ! -d "$DIR" ]]; then DIR="$PWD"; fi
    source "$DIR/$1"   
}

source_includes utils.sh

# --- Options processing -------------------------------------------
if [ $# = 0 ] ; then
    echo '$USAGE'
    exit 1;
fi

while getopts ":i:o:vh" optname
  do
    case "$optname" in
    "v")
        echo "Version $VERSION";
        exit 0;
        ;;
    "i")
      #echo "-i argument: $OPTARG";
      input_filename=$OPTARG;
        ;;
    "o")
      #echo "-o argument: $OPTARG";
      output_filename=$OPTARG;
        ;;
    "d")
      #echo "-d argument: $OPTARG";
      delimiter=$OPTARG;
        ;;
    "h")
        echo "$USAGE";
        exit 0;
        ;;
    "?")
        echo "Unknown option $OPTARG"
        exit 0;
        ;;
    ":")
        echo "No argument value for option $OPTARG"
        exit 0;
        ;;
    *)
        echo "Unknown error while processing options"
        exit 0;
        ;;
    esac
  done

shift "$(($OPTIND -1))"

# depends on utils.sh
check_variable_present "$input_filename" "input fileame not present!"
check_variable_present "$output_filename" "output filename not present!"

##############################################################################
# ------------------ Start Program Logic Here! ----------------------

# prints the byte offset 
grep --byte-offset --only-matching "^.\{6\}|.\{8\}|" "$input_filename" > "$output_filename"

# awk -F: '{print $2 "\t" $1}' > 
