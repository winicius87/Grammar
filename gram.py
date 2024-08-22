#!/usr/bin/python3

import socketserver
import os
import subprocess
import re

class MyTCPHandler(socketserver.StreamRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        
        # self.request is the TCP socket connected to the client
        self.data = self.rfile.readline().strip()
        aa = self.data.split(b" ")
        aaa = aa[1].split(b"/")
        mimetype=b''
        header=b''
        response=''
        path = aa[1]
        path=path.strip(b'/')
        if re.search(b"_public", path) != None:
            if path == b'/g/_public':
                path=b'_public/index.html'
            
            #path=re.sub(b'/', path)
            print(b"path:" + path)
            try:
                file = open(path, 'rb')
                response = file.read()
                #print(response)
                file.close()
                header = b'HTTP/1.1 200 OK\n'
                if(path.endswith(b".jpg")):
                    mimetype = b'image/jpg'
                elif(path.endswith(b".png")):
                    mimetype = b'text/png'
                elif(path.endswith(b".css")):
                    mimetype = b'text/css'
                else:
                    mimetype = b'text/html'
                header += b'Content-Type: '+mimetype+b'\n\n'
            except Exception as e:
                print(e)
                header = b'HTTP/1.1 404 Not Found\n\n'
                response = b'<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'
        
        if re.search(b"_public", path) != None:
            pout = header + response
            self.request.sendall(pout)
            return
        
        #aaa[1] = b"\"" + aaa[1] + b"\""
        aaa[1] = aaa[1].replace(b'%20', b' ')
        
        print(aaa[1])
        
        #if re.fullmatch(b"[a-zA-Z0-9\"\\s\\.,:;\'\\?!-]+", aaa[1]) == None and aaa[1] != b'""':
        if re.fullmatch(b"[a-zA-Z0-9\"\\s\\.,:;\'\\?!-]+", aaa[1]) == None and aaa[1] != b'':
        #if re.match(b"[a-zA-Z0-9\" \\s\\., ]+", aaa[1]) == None and aaa[1] != b'""':
                print("No match.");
                return
        
        p = subprocess.run(b"echo '"+aaa[1]+b"' | link-parser ", stdout=subprocess.PIPE, shell=True)
        #print(p.stdout)
        #p.stdout = re.sub(b'(.*\n)*LEFT-WALL ', b'', p.stdout)
        #p.stdout = re.sub(b'\n\nBye.*\n', b'', p.stdout)
        
        try:
                if aaa[1] != b'':
                        #p.stdout = p.stdout.replace(b'\n', b'<br>\n')
                        p.stdout = re.sub(b'(.*\n)*LEFT-WALL ', b'', p.stdout)
                        p.stdout = re.sub(b'\nBye.*\n', b'', p.stdout)
                        print(p.stdout)
                        pout = b"<span>"+p.stdout+b"</span>"
                        #pout = p.stdout
                        if re.search(b"No definitions found", pout) != None:
                                print("No definitions found, try these words.")
                                """
                                """
                                return
                        """
                        """
                        self.request.sendall(pout)
                        return
        except:
                print("Empty string.")
                #p.stdout = p.stdout.replace(b'\n', b'<br>\n')
                #pout = p.stdout
                pout = b"<pre>"+p.stdout+b"</pre>"
                self.request.sendall(pout)
                return
                
        
        pout = (b'HTTP/1.0 200 OK\n'
        + b"Content-Type: text/html\n"
        + b"\n"
        + b'<!DOCTYPE html><html lang="en"><head>'
        + b"<TITLE>/g/rammar</TITLE>"
        + b"""<link rel="apple-touch-icon" sizes="180x180" href="/g/_public/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/g/_public/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/g/_public/favicon-16x16.png">
<link rel="manifest" href="/g/_public/site.webmanifest">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<!--meta charset="utf-8"-->
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="/g/_public/Strategy_files/bootstrap.css">
<link rel="stylesheet" href="/g/_public/Strategy_files/aos.css">
<link rel="stylesheet" href="/g/_public/Strategy_files/hamburgers.css">
<link rel="stylesheet" href="/g/_public/Strategy_files/owl.css">
<link rel="stylesheet" href="/g/_public/Strategy_files/style_002.css">
<link rel="stylesheet" href="/g/_public/Strategy_files/animsition.css">
<link rel="stylesheet" href="/g/_public/Strategy_files/font-awesome.css">
<link rel="stylesheet" href="/g/_public/Strategy_files/style.css">
<style>.scrollax-performance, .scrollax-performance *, .scrollax-performance *:before, .scrollax-performance *:after { pointer-events: none !important; -webkit-animation-play-state: paused !important; animation-play-state: paused !important; }</style>
<style>
.templateux-footer {
  padding: 0em;
  border-top: none;
}

.aos-animate{ padding-bottom: 0em;}

.project .project-hover, .project .post-hover, .post .project-hover, .post .post-hover{

background: rgba(8, 87, 13, 0.9);

}


html, body {

	background-color: #123;

}


.code {
	font-family: monospace;
	color: #ffd0d0;
	font-size: 14px;
	line-height: 1.0;
	background: #373719;
}

.newsletter {
	padding: 80px 0;
	background: #19beda;
}

.newsletter .content {
	max-width: 650px;
	margin: 0 auto;
	text-align: center;
	position: relative;
	z-index: 2; }
	.newsletter .content h2 {
		color: #243c4f;
		margin-bottom: 40px; }
.newsletter .content .form-control {
	height: 50px;
	border-color: #ffffff;
	border-radius:0;
}
.newsletter .content.form-control:focus {
	box-shadow: none;
	border: 2px solid #243c4f;
}
.newsletter .content .btn {
	min-height: 50px; 
	border-radius:0;
	background: #243c4f;
	color: #fff;
	font-weight:600;
}
h2 a, li a:visited {
	color: #1b7d18;
}

pre, #dictionary{
    color: #eff;
}

.form-control{
	background-color: #a5ff9e;

    width: 100%;
    min-height: 10em;
    resize: both;
}

.link{
color: #eff;
margin-left: 1em;
text-decoration: underline;

}

</style>


<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1819312738814111"
     crossorigin="anonymous"></script>"""
        
        
        
        
        + b"</head>"
        + b'<body style="padding: 3em;">'
        + b'<h1 style="color: #00ff58;">/g/rammar</h1>' 
        #+ b'<p style="padding: .5em;">'
        + b'<form style="padding: .5em 0 .5em 0;" class="upload-form" action="/g/">'
        #+ b'<textarea value="A woman is pretty." id="search" class="form-control" type="text"><!-- name="search" value="" pattern="[a-zA-Z0-9\x22\\s\\.,:;\'\\?!-]+" required --></textarea>'
        + b'<textarea value="A woman is pretty." id="search" class="form-control" type="text"></textarea>'
        + b'<br><button class="btn btn-success" type="submit">Search (Press Once)</button>'
        + b'<a class="link" target="_blank" href="/MediaLight/XEhA2/ZasumAki45.jpg">Part of Speech Convention</a>'
        + b'<br><span class="direction">After searching for grammar errors, an error is surrounded by square brackets, [].</span>'
        #+ b'<button id="send" class="btn btn-primary" type="submit" name="submit" value="Search (Press Once)" onClick="javascript: window.open(\'/\' + document.getElementById(\'search\').value);" ></button>'
        + b'</form>'
        #+ b'</p>'
        + b"""
<script>
// Declare global variables for easy access 
const uploadForm = document.querySelector('.upload-form');
let search = document.getElementById('search').value;
// Attach submit event handler to form
uploadForm.onsubmit = event => {
    event.preventDefault();
    // Search for nonempty string
    search = document.getElementById('search').value;
    if (search != ''){
        // Create the form object
        let uploadFormDate = new FormData(uploadForm);
        // Initiate the AJAX request
        let request = new XMLHttpRequest();
        // Ensure the request method is POST
        console.log(uploadForm.action + '/' + search);
        request.open('GET', uploadForm.action + search);
        // Attach the progress event handler to the AJAX request
        request.upload.addEventListener('progress', event => {
            // Disable the submit button
            uploadForm.querySelector('button').disabled = true;
        });
        // The following code will execute when the request is complete
        request.onreadystatechange = () => {
            if (request.readyState == 4 && request.status == 200) {
                // Output the response message
		document.getElementById('dictionary').innerHTML = request.responseText;
            }
        };
/*
.then(data => {
			if(data.includes("Error")){
					
					document.getElementById('response2').innerHTML = "The domain is already in use. Try a new domain or contact support.<br><br>";
				} else{
					document.getElementById('response1').innerHTML = data;
					
					var x = document.getElementById("intro");
					var y = document.getElementById("register");
					if (x.style.display === "none") {
					x.style.display = "block";
					y.style.display = "none";
					}
				}
			
			})
			.catch(error => {
			console.error('Error:', error);
			});



*/




        // Execute request
        request.send(uploadFormDate);
    }
};
</script>
        """
        + b'<p id="dictionary" style="padding-top: 3em;">'
        #+ p.stdout
        + b"</p></body>"
        + b"</html>")
        #print(pout)

        self.request.sendall(pout)

if __name__ == "__main__":
    HOST, PORT = "localhost", 8001

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

"""
    print("Content-Type: text/html")
    print()
    print('<!DOCTYPE html><html lang="en"><head>')
    print("<TITLE>CGI script output</TITLE>")
    print("<body>")
    print("<H1>This is my first CGI script</H1>")
    print("Hello, world!")
    print("</body>")
    print("</html>")
"""
