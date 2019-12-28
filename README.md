### pwGenerator🔐

mnml password generator 🗝



#### Main Loop 
```Script
for p in $(seq 1 2); do
        openssl rand -base64 48 | cut -c1-$PLEN

done
```
