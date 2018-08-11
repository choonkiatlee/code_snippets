
getopts_build_index(){

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

}

