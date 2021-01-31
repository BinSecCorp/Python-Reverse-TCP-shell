# Python-Reverse-TCP-shell #
## Overview ##
This is a simple tool for remote command execution. The client connects to the host server, the server can send commands to execute to the client.

## usage ##
Simply execute the client script and it will automatically start connecting to the server. The client script will attempt a connection every 3 seconds.
Execute the server script on a remote host machine and it will start listening for connections from the client.
The order of execution does not matter

After successfully connecting, the server will prompt the user to enter a command. After sending the command to the client, the client will first respons with the size of the result,
then it will send the result.

**working commands include**
1. ipconfig/ifconfig
2. shutdown/sleep
3. execution of applications
4. netsh
5. etc

**Current unworking commands**
1. cd
2. actions that require more than one command in a single cmd/terminal session

*for unix systems, if the command requires a sudo, type in:*

            echo <thepassword> | sudo -s <command>
 
this will read the password from the echo instead of prompting the password
