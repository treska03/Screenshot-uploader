# Screenshot-uploader
Allows taking screenshots with automatic upload\
Currently supports only windows OS.

# How to get started
- Clone the project
&ensp;  <pre>
        git clone https://github.com/treska03/Screenshot-uploader Screenshoter
        cd Screenshoter
        </pre>
- Create and activate virtual environment
- Install required modules
&ensp;  <pre>
        pip install -r requirements.txt
        </pre> 
- Register your application [https://api.imgur.com/oauth2/addclient](https://api.imgur.com/oauth2/addclient) and paste clientID into config.json file
- Run app 
&ensp;  <pre>
        python app.py
        </pre>
# How to use
- Whenever you want to take a screenshot, press combination of all shortcut keys that are in config.json file.
- Click and drag the mouse over the area you want to capture. Then release.
- The screenshot is uploaded to imgur.com website and link has been compied into your clipboard.
- Now you can do it all over again!