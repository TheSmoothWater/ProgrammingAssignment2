# CSCI-320 Mini-Project: TCP File Transfer


## Setup and Installation

This programmng assignment should be templated and cloned locally on your computer. 

## Introduction

This exercise aims to create a simple TCP file transfer system, where a client will send a file to a server, and the server will receive the file and save it to disk.  There are no limits on the size of the file.

You will implement a simple protocol for file transfer over TCP.  Because the socket is TCP, the transport layer is responsible for ensuring that the file is transferred without error.

Note: This programming assignment is intended to provide practice in TCP socket programming.  The assignment is similar to the previous one with the exception that no file hash needs to be generated since the application layer is using reliable transport.

The algorithms described below implements the following simple protocol.

<figure style="text-align:center;">
	<img src="TCPFileTransferProtocol.png" height="600"></div>
	<figcaption style="font-weight:bold; color:#0055ee;">Figure 1: Simple file transfer protocol.</figcaption>
</figure>

## 1. Implementing the Server

The server should:

1. Create a socket using the `socket` function and bind it to the (ip, port) pair. **(Implemented)**
2. Receive a message from the client using the `recv` function.
3. Decompose the message into an 8-byte integer representing file size. The rest of the bytes should be decoded into a string representing the file name. Use `get_file_info()`.
4. send `b'go ahead'` message to the client.
5. Using the filename provided, open the file for writing using the `with` python statement. **NOTE: since you will be transferring a file over localhost to the same directory, it is important that you modify the filename, say by adding a *.temp* extension, to avoid overwriting the original file.** (Implemented)
6. Inside the *with* statement, 
	<ol type="a">
	<li>Receive a chunk of data.</li>
	<li>Update the number of bytes received.</li>
	<li>Write the data to the file.</li>
	<li>Continue to perform steps 7a-c until all bytes have been received.</li>
	</ol>
	<div style="background-color:pink; border-radius: 5px; padding: 5px;">
	<strong>NOTE:</strong> Please exercise good coding practices!  Do not write loops with break statements!
	</div>
7. If an exception occurs, the file should be deleted. (Implemented)
8. Close the client socket. (Implemented)
9. Repeat steps 2 - 8. (Implemented)

## 2. Implementing the Client

The client should:

1.	Obtain the name of the file to transfer from the command line using sys.argv. **(Implemented)**
2. Obtain the size of the file in bytes by using the os.path module.(use `get_file_size()`)
3. Convert the file size to an 8-byte string using big endian.
4. Create a TCP socket using the `socket` function. **(Implemented)**
5. Connect to the server using the (ip, port) pair.
6. Send the 8-byte file size concatenated with the encoded filename to the server.
7. Wait for the server to send `b'go ahead'` message. If any other message is sent, `raise OSError('Bad server response - was not go ahead!')`
8. Open the file for reading in binary mode using the *with* python statement.
	<ol type="a">
	<li>Read a chunk of data from the file.</li>
	<li>If the length of the chunk > 0, then send the chunk to the server else go to step 9.  No more chunks to read and send.</li>
	<li>Repeat steps 8a - 8b</li>
	</ol>
	<div style="background-color:pink; border-radius: 5px; padding: 5px;">
	<strong>NOTE:</strong> Please exercise good coding practices!  Do not write loops with break statements!
	</div>

9. Close the client socket. **(Implemented)**

## 3. Testing Your Implementation

You can test your implementation by running client against the instructor's server.  Your instructor will provide the IP address of the server.

Once your client works against the instructor's server, you can test your server against your working client on the same machine.  Make sure to run the server first and then the client. **<span style="color:red">NOTE: as mentioned in section 1 above, it is important that you modify the filename, say by adding a *.temp* extension, to avoid overwriting the original file.</span>** This has already been done on the server's with statement. Such a filename change is only necessary when running both server and client on the same machine and using the same working directory. You do not have to modify the filename if you set the run configuration of the server to use a different working directory from that of the client.


## 4. Submitting This Work

You are required to submit your code on the CodeGrade link on Blackboard.  Further instructions will be provided about submission in Discord.

## Tips

- Make sure to handle errors in your code.
- Pay attention to the TODO tasks and how they are mapped to the algorithm steps above.  This will help guide you in implementing the code.
- Read the Python documentations for the sys, os, and os.path modules along with associated examples.  Avoid Googling the answer as this will get you into the habit of reading documentaton.

Good luck and happy coding!
