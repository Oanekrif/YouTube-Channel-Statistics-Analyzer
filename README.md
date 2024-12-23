# 📊 YouTube Channel Statistics Analyzer </br></br></br>
• A Python project that uses the YouTube Data API to analyze channel statistics such as subscriber count, total views, and the number of videos. </br>
• Visualize the results with Seaborn and Matplotlib for better insights! 🚀</br>

## 📋 Features</br>
• Fetches detailed statistics for multiple YouTube channels. 🎥</br>
• Outputs the data in a tabular format using Pandas. 🗂️</br>
• Generates a bar chart to visualize the total number of videos for each channel. 📊</br>
• Simple and efficient design for beginners and enthusiasts alike.</br>

## 🛠️ Installation</br>
Clone this repository to your local machine:
    
    git clone https://github.com/yourusername/YouTube-Channel-Statistics-Analyzer.git
Navigate to the project directory:
   
    cd YouTube-Channel-Statistics-Analyzer
Install the required libraries:

    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    pip install pandas seaborn matplotlib pyyaml
</br>

## 🚀 Usage</br>
1. Prepare API Credentials:</br>
• Create a youtube_api_token.yaml file in the project directory.</br>
• Add your YouTube Data API key in the following format:

       parameters_dictionary:
           TOKEN: YOUR_API_KEY_HERE
2. Add Channel IDs:</br>
• Update the channel_ids list in the script with the IDs of the YouTube channels you want to analyze:

       channel_ids = ['CHANNEL_ID_1', 'CHANNEL_ID_2', ...]
3. Run the Script: Execute the script to fetch channel statistics and display the results:

       python youtube_channel_analyzer.py
</br>

## 🧮 How It Works</br>
1. Load API Token:</br>
• Reads the API key from youtube_api_token.yaml using the PyYAML library.</br>

2. Fetch Channel Statistics:</br>
• Uses the YouTube Data API to fetch details like subscribers, views, and video counts.</br>

3. Visualize Data:</br>
• Converts the statistics into a DataFrame using Pandas.</br>
• Visualizes the total videos per channel with Seaborn bar plots.</br>

## 📊 Example Output</br>
### Terminal Output:
       
    | Channel Name        | Subscribers | Views   | Total Videos |
    |---------------------|-------------|---------|--------------|
    | Example Channel 1   | 1,000,000   | 500,000 | 50           |
    | Example Channel 2   | 750,000     | 300,000 | 40           |
    
### Bar Chart:</br>
Displays a bar plot showing the number of videos for each channel.

## ✨ Future Enhancements</br>
• 📈 Add more visualization options (e.g., line charts for views over time).</br>
• 🌍 Support for internationalization with multilingual outputs.</br>
• 🔍 Fetch video-level details for deeper insights.</br>

## 📜 License</br>
• This project is licensed under the MIT License.
• Feel free to use and modify it! 📝</br>

## 🙌 Contributions</br>
Contributions are welcome! Open an issue or submit a pull request to make this project even better. 💡</br>

## ❤️ Thank You for Exploring This Project! ❤️
Enjoy analyzing YouTube channel statistics and gaining valuable insights! 🚀🎥
