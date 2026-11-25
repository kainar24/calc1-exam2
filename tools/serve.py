"""Static server for the site that tells browsers not to cache (so updates show up at once)."""
import http.server, os, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()
    def log_message(self, *a):
        pass
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8028
http.server.ThreadingHTTPServer(("0.0.0.0", port), H).serve_forever()
