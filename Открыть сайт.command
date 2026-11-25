#!/bin/bash
# Double-click: starts the local site and opens it in the browser.
# The phone link (same Wi-Fi) is printed below. Close this window to stop the server.
cd "$(dirname "$0")"
PORT=8028
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null)
echo "Calc 1 Exam 2 site"
echo "  On this Mac:   http://localhost:$PORT"
[ -n "$IP" ] && echo "  On the phone:  http://$IP:$PORT   (same Wi-Fi)"
echo "Close this window to stop."
( sleep 1; open "http://localhost:$PORT" ) &
exec /usr/bin/python3 tools/serve.py $PORT
