#!/bin/bash

#calculate the period for blocking
time=$(($2*60))

#create IP Set
ipset create temp_host hash:ip timeout $time

#create the rule for IP Set
iptables -A INPUT -m set ! --match-set temp_host src -j DROP

#extract the ip addresses from file and add to IP Set
while IFS= read -r ip || [ -n "$ip" ]; do

  echo "$ip is being blocked for $2 minutes which is $time seconds"
  ipset add temp_host $ip timeout $time

done <$1