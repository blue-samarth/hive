Web Application using Flask
This web application is built using Flask, a micro web framework for Python. It provides functionalities to fetch user transactions from the Hive blockchain, search for specific transactions, and summarize comments from the blockchain discussions.

Features:
1. Home Page:
The home page displays a list of recent transactions along with the current block number.
Transactions are fetched using the tetsttt module which provides the transactions and current_block_num variables.
2. Search Functionality:
Users can search for specific transactions by entering a username.
The get_user_transactions(username) function retrieves the transactions for the specified user from the Hive blockchain.
3. Summarization:
Users can summarize comments from discussions on the blockchain by entering a tag.
The application uses the facebook/bart-large-cnn model through the Hugging Face Transformers library to perform summarization of comments.
Comments are fetched from the blockchain using the beem library and then cleaned before summarization.
Setup Instructions:
Install dependencies using pip install -r requirements.txt.
Run the Flask application using python app.py.
Access the application in your web browser at http://localhost:5000.
Dependencies:
Flask: pip install Flask
Transformers: pip install transformers
Beem: pip install beem
Usage:
Navigate to the home page to view recent transactions.
Use the search functionality to find transactions by username.
Use the summarization functionality to summarize comments by entering a tag.
