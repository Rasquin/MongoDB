# Download and install MongoDB client 3.4 for mLab
wget -q https://git.io/vFb1J -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh

# Download and install MongoDB client 4.0.6 for Atlas
wget -q https://git.io/fh7vV -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh

# Create And Read Back Data
https://github.com/Code-Institute-Solutions/GoHumongousWithMongoDB/blob/master/02-ManipulateDataUsingMongoShell/01-create_and_read_back_data/commands.sh

# Mongo Commands
create and read data
https://github.com/Code-Institute-Solutions/GoHumongousWithMongoDB/blob/master/02-ManipulateDataUsingMongoShell/01-create_and_read_back_data/mongoCommands.js
Update and delete data
https://github.com/Code-Institute-Solutions/GoHumongousWithMongoDB/blob/master/02-ManipulateDataUsingMongoShell/02-update_and_delete_data/mongoCommands.js

# Mongo from Python
Install mongo libraries related to python
sudo pip3 install dnspython
sudo pip3 install pymongo
cd ..  to get to the home directory
nano .bashrc to edit the .bashrc since the nano editor
export MONGO_URI="mongodb+srv://User:<password>@myfirstcluster-pjgpn.mongodb.net/myTestDB?retryWrites=true"
close and reopend the terminal and type: echo $ MONGO_URI
