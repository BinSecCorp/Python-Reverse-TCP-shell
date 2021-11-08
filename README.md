# Dynamic-Buffer Python-Reverse-TCP-shell #
## Overview ##
This is a simple tool for remote command execution. The client connects to the host server, the server can send commands to execute to the client.

## usage ##
The IP of the host must be changed in the server AND the client file prior to installation, note that the ports on both the client and server must be matching.
Simply execute the client script and it will automatically start search mode; in which the client script will attempt a connection every 3 seconds.
Execute the server script on a remote host machine and it will start listening for connections from the client.
The order of execution does not matter.

After successfully connecting, the server will prompt the user to enter a command. After sending the command to the client, the client will first respons with the size of the result,
then it will send the result.

Unless using a public IP, the reverse shell can only be connected to if the server and client are under the same localhost.

**working commands include**
1. Pretty much anything that doesn't need password authentication

*for unix systems, if the command requires a sudo, type in:*

            echo <thepassword> | sudo -s <command>
 
this will read the password from the echo instead of prompting the password

In order to disconnect from the client properly, the server shell must send a disconnect message. To trigger this message, type

            close connection

in the shell. This will reactivate the search mode in the client shell and automatically quit the server program.
The client program will not quit unless the host machine has been shutoff or it was manually killed.
