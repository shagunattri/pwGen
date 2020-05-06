#!/bin/bash

mnml Password Generator

echo "      Mnml Password Generator     "
read -p "Enter the length of password you would like: " PLEN

for p in $(seq 1 2); do
        openssl rand -hex 12 | cut -c1-$PLEN

done
