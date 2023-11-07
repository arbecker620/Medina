## Get Started 
The process to get the app started is detailed in the process below. When specific packages are needed for the API, the adjusts can be made under the requirements.txt file.

Step 
Please run the following commands from project directory in terminal to build the container 

` docker build -t medina/analysis -f Analysis/Dockerfile . `
Result
The result of this command is a **Docker** image built called medina with the dev tag. To verify the image has been built run the following command in the terminal and you should see the image in the list outputted from **Docker**.
