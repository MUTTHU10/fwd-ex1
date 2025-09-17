from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocols</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <p>The TCP/IP model is a four-layer conceptual framework used to describe network communications. Each layer contains specific protocols that work together to enable data transmission.</p>

    <table>
        <thead>
            <tr>
                <th>Layer</th>
                <th>Protocol</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Application Layer</td>
                <td>HTTP</td>
                <td>Hypertext Transfer Protocol for web pages.</td>
            </tr>
            <tr>
                <td></td>
                <td>FTP</td>
                <td>File Transfer Protocol for transferring files.</td>
            </tr>
            <tr>
                <td></td>
                <td>SMTP</td>
                <td>Simple Mail Transfer Protocol for email.</td>
            </tr>
            <tr>
                <td></td>
                <td>DNS</td>
                <td>Domain Name System for translating domain names to IP addresses.</td>
            </tr>
            <tr>
                <td>Transport Layer</td>
                <td>TCP</td>
                <td>Transmission Control Protocol for reliable data delivery.</td>
            </tr>
            <tr>
                <td></td>
                <td>UDP</td>
                <td>User Datagram Protocol for fast, connectionless data transfer.</td>
            </tr>
            <tr>
                <td>Internet Layer</td>
                <td>IP</td>
                <td>Internet Protocol for logical addressing and routing.</td>
            </tr>
            <tr>
                <td></td>
                <td>ICMP</td>
                <td>Internet Control Message Protocol for network diagnostics.</td>
            </tr>
            <tr>
                <td>Network Access Layer</td>
                <td>Ethernet</td>
                <td>Physical and data link layer protocol for local area networks.</td>
            </tr>
            <tr>
                <td></td>
                <td>Wi-Fi (802.11)</td>
                <td>Wireless communication protocol.</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()