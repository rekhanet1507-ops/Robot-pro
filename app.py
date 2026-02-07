import http.server
import socketserver
import urllib.parse
import os
from organize_downloads import organize_downloads

PORT = 8000

class OrganizerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Downloads Organizer</title>
            <style>
                body { font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }
                h1 { color: #333; }
                .container { background: #f9f9f9; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
                input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
                input[type="submit"] { background-color: #4CAF50; color: white; padding: 12px 20px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
                input[type="submit"]:hover { background-color: #45a049; }
                pre { background: #eee; padding: 15px; border-radius: 4px; overflow-x: auto; white-space: pre-wrap; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Downloads Organizer</h1>
                <p>Enter the full path to the folder you want to organize:</p>
                <form method="POST">
                    <input type="text" name="path" placeholder="e.g. C:\\Users\\Downloads" required>
                    <br><br>
                    <input type="submit" value="Organize Files">
                </form>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)
        
        path = params.get('path', [''])[0]
        
        result = ""
        if path:
            if os.path.exists(path) and os.path.isdir(path):
                try:
                    result = organize_downloads(path)
                except Exception as e:
                    result = f"Error during execution: {str(e)}"
            else:
                result = f"Error: The path '{path}' does not exist or is not a directory."
        else:
            result = "Error: No path provided."

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Downloads Organizer - Result</title>
            <style>
                body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
                h1 {{ color: #333; }}
                .container {{ background: #f9f9f9; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .back-link {{ display: inline-block; margin-top: 20px; text-decoration: none; color: #0066cc; }}
                pre {{ background: #eee; padding: 15px; border-radius: 4px; overflow-x: auto; white-space: pre-wrap; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Organization Result</h1>
                <p><strong>Target Path:</strong> {path}</p>
                <hr>
                <pre>{result}</pre>
                <a href="/" class="back-link">&larr; Back to Organizer</a>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode('utf-8'))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), OrganizerHandler) as httpd:
        print(f"Serving at port {PORT}")
        print(f"Open http://localhost:{PORT} in your browser")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
