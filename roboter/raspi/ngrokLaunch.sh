#!/bin/sh
# launcher.sh

cd /
cd /usr/local/bin
./ngrok config add-authtoken "ngrok_token_kommt_hier"
sleep 3s
./ngrok http "--domain=up-peaceful-martin.ngrok-free.app" "statische_ip_kommt_hier"  &

