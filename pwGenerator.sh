#!/bin/bash

mnml Password Generator

echo "      Mnml Password Generator     "
read -p "Enter the length of password you would like: " PLEN

for p in $(seq 1 2); do
        openssl rand -hex 12 | cut -c1-$PLEN

done


# #!/usr/bin/env sh
# echo 'Generating 12-character passwords'
# for ((n=0;n<12;n++))
# do dd if=/dev/urandom count=1 2> /dev/null | uuencode -m - | sed -ne 2p | cut -c-12
# done