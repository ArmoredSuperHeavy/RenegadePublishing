#!/bin/bash
clear



FILE_NAME=$1
PAGE_COUNT=$2
EMPTY_PAGE=$3
PAPER_SIZE=$4
echo "Looking at page $EMPTY_PAGE for a blank filler"
echo "... looking at the following file:"
ls -la $FILE_NAME
echo

echo "........ with the expected paper size $PAPER_SIZE"

SIG_SIZE=20
SIGS=$(($PAGE_COUNT / $SIG_SIZE))
REMAINDER=$(($PAGE_COUNT % $SIG_SIZE))
BLANKS=$(($SIG_SIZE-$REMAINDER))

echo "Checking..."
if [ "$REMAINDER" -gt 0 ]
  then
    echo "You will have $BLANKS blank page(s) at the end"
    SIGS=$(($SIGS + 1))
fi

echo "There will be $SIGS signatures"


DIR_NAME="output_20"


if [ -d '$DIR_NAME' ]
  then
    rm -rf $DIR_NAME
    echo "Dumping all old content from the directory '$DIR_NAME'"
fi


mkdir $DIR_NAME


for sig in `seq 1 $SIGS`;
do
  echo "Signature : $sig of $SIGS"
  i=$(($(($sig - 1)) * $SIG_SIZE))
  sig_file_name="$DIR_NAME/temp_sig_$i.pdf"


  [ $((i + 1)) -le $PAGE_COUNT ] && p1="$((i + 1))" || p1=$EMPTY_PAGE
  [ $((i + 2)) -le $PAGE_COUNT ] && p2="$((i + 2))" || p2=$EMPTY_PAGE
  [ $((i + 3)) -le $PAGE_COUNT ] && p3="$((i + 3))" || p3=$EMPTY_PAGE
  [ $((i + 4)) -le $PAGE_COUNT ] && p4="$((i + 4))" || p4=$EMPTY_PAGE
  [ $((i + 5)) -le $PAGE_COUNT ] && p5="$((i + 5))" || p5=$EMPTY_PAGE
  [ $((i + 6)) -le $PAGE_COUNT ] && p6="$((i + 6))" || p6=$EMPTY_PAGE
  [ $((i + 7)) -le $PAGE_COUNT ] && p7="$((i + 7))" || p7=$EMPTY_PAGE
  [ $((i + 8)) -le $PAGE_COUNT ] && p8="$((i + 8))" || p8=$EMPTY_PAGE


  [ $((i + 9)) -le $PAGE_COUNT ] && p9="$((i + 9))" || p9=$EMPTY_PAGE
  [ $((i + 10)) -le $PAGE_COUNT ] && p10="$((i + 10))" || p10=$EMPTY_PAGE
  [ $((i + 11)) -le $PAGE_COUNT ] && p11="$((i + 11))" || p11=$EMPTY_PAGE
  [ $((i + 12)) -le $PAGE_COUNT ] && p12="$((i + 12))" || p12=$EMPTY_PAGE
  [ $((i + 13)) -le $PAGE_COUNT ] && p13="$((i + 13))" || p13=$EMPTY_PAGE
  [ $((i + 14)) -le $PAGE_COUNT ] && p14="$((i + 14))" || p14=$EMPTY_PAGE
  [ $((i + 15)) -le $PAGE_COUNT ] && p15="$((i + 15))" || p15=$EMPTY_PAGE
  [ $((i + 16)) -le $PAGE_COUNT ] && p16="$((i + 16))" || p16=$EMPTY_PAGE
  [ $((i + 17)) -le $PAGE_COUNT ] && p17="$((i + 17))" || p17=$EMPTY_PAGE
  [ $((i + 18)) -le $PAGE_COUNT ] && p18="$((i + 18))" || p18=$EMPTY_PAGE
  [ $((i + 19)) -le $PAGE_COUNT ] && p19="$((i + 19))" || p19=$EMPTY_PAGE
  [ $((i + 20)) -le $PAGE_COUNT ] && p20="$((i + 20))" || p20=$EMPTY_PAGE

  # the 5 folio sig
  #temp_cmd="pdfjam --nup 10x1 $FILE_NAME '$p20,$p1,$p4,$p17,$p16,$p5,$p8,$p13,$p12,$p9' $FILE_NAME '$p10,$p11,$p14,$p7,$p6,$p15,$p18,$p3,$p2,$p19'   --outfile $sig_file_name  --papersize '$PAPER_SIZE'"
  # the 2/3 folio sigs
  temp_cmd="pdfjam --nup 10x1 $FILE_NAME '$p6,$p3,$p2,$p7,$p10,$p19,$p18,$p11,$p14,$p15' $FILE_NAME '$p16,$p13,$p12,$p17,$p20,$p9,$p8,$p1,$p4,$p5'   --outfile $sig_file_name  --papersize '$PAPER_SIZE'"
  echo $temp_cmd
  eval $temp_cmd
done 

exit 0
TEMP_CMD="ls"
echo
echo "what? '$TEMP_CMD'"
eval $TEMP_CMD
echo "done"





