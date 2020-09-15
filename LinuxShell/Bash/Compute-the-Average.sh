read n
sum=0
for ((i; i < $n; i++)); do
    read tmp
    sum=$((sum+tmp))
done

printf "%.3f\n" `echo "$sum / $n" | bc -l`
