# Chatbot-using-Raspberry-pi-For-Building-Navigation
Chatbot using Raspberry-pi to navigate inside the building or apartment 
In the master branch there was a problem with multithreading that is multipe user can connect but each will recieve the same message eventhough a single user request for a Navigation details.Once any one of the user asks for the navigation details all will be delivered with the same message. So in this new branch i have added a code to securely send message to a particular user and automatically that user get disconnected.
