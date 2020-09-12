read str
printf "%.3f\n" `echo $str | bc -l`
