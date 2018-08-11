#!/bin/sh

source_includes(){
    DIR="${BASH_SOURCE%/*}"
    if [[ ! -d "$DIR" ]]; then DIR="$PWD"; fi
    source "$DIR/$1"   
}

source_includes utils.sh

# search for a line
# 001000|19711231| 22806
# 001000|19721231| 24005
# 001000|19721231| 26059
# 001000|19731231| 27248

get_file_offset(){
    
}


get_from_index 