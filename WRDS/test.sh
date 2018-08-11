INPUT_DATABASE=$1
COL_IDX=$2
awk -v var="$COL_IDX" '$1 == var{print NR;exit} ' RS="|" $INPUT_DATABASE
awk -v var="$COL_IDX" -F'|' 'NR==1{ for (i=1; i<=NF; ++i) { if ($i == var) print i} }' $INPUT_DATABASE
