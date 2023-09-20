# medina-didactic-sniffle

## Introduction
    This solution is the first step into a data ingestion platform. Medina is a reference to the JA Corey's Expanse series. Medina is space station which is situated by the Ring gates to other worls and star light years away. It serves as a place where traffic and travelers can go through to go  to other galaxies and through many other places.

    This app is cloud agnotisc and focuses on intaking unstructured data and moving it into a serachable semi setructured manner. 



## Requirements

The following is list of software or applications which need to be installed as apart of the project. Python is not installed directly onto the machine you are developing on but utilized in Docker containers. This is primarily because I use a M1 Macbook Air with 256gb, I want to avoid having as much software installed on the system as much as possible. So I push the install of python into Docker so I can use multiple versions without dependency issues.

Ide of your choosing
Docker
Git


## Get Started 
The process to get the app started is detailed in the process below. When specific packages are needed for the API, the adjusts can be made under the requirements.txt file.

Step 
Please run the following commands from project directory in terminal to build the container 

 ` docker build -t medina/dev . `
Result
The result of this command is a **Docker** image built called medina with the dev tag. To verify the image has been built run the following command in the terminal and you should see the image in the list outputted from **Docker**. 



run the following command to start the container in interactive mode

` docker container run -it medina/dev `


the container will run into interactive mode.


