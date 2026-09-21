set -e
mkdir -p relay_out
[ -s relay_out/img_001_body.png ] || python3 relay/compose.py
touch relay/urls.txt
while read -r name url; do
  [ -z "$name" ] && continue
  [ -s "relay_out/$name" ] && continue
  code=$(curl -sS -L -o "relay_out/$name" -w "%{http_code}" --max-time 180 "$url")
  echo "$name $code $(stat -c%s relay_out/$name)"
  [ "$code" = "200" ] || { rm -f "relay_out/$name"; echo "FAIL $name"; }
done < relay/urls.txt
