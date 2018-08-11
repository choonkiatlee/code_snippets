check_variable_present () {
    
    # Params:
    # -------
    # $1 -- variable to check
    # $2 -- error message to print out if variable is missing

    # Returns:
    # --------
    # void if variable is not missing
    # exits program if variable is missing

    if [ -z "$1" ]
    then 
        echo "$2"
        exit
    fi
}