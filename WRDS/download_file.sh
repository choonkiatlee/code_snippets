#!/bin/bash


if [ $# -eq 2 ]
	then 
		scp manufact@wrds.wharton.upenn.edu:$1 $2
	else 
		echo "Please input 2 arguments of the form <remote_file_to_copy> <local_file_to_copy_to>"
fi
