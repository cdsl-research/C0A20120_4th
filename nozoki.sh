while true
start_time=$(date +%s)

duration=200

do
    kubectl top pod -n sock-shop >> usage.txt
    date >> usage.txt

    current_time=$(date +%s)
    if ((curren_time - start_time >= duration)); then
        break
    fi

    sleep 5s
done