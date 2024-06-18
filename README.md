# CookieRobot for Multilogin X

This is a tool for automatically visiting determined websites in order to collect cookies from them. You can either start a quick browser profile to do this, or start an existing browser profile.

## Considerations

In order to run this automation in an existing browser profile, you should add an extension that automatically consents with cookies, such as SugerAgent or Accept-All-Cookies.

On the other hand, if you want to run the Cookie Robot on quick browser profiles, the script will automatically install the SuperAgent extension and you won't have to worry about it.

## First time? Run in guided mode!

Simply run the script in guided mode, it will prompt you whatever it needs to start.

```bash
python cookie_robot.py --guided
```

## Instructions for non-guided mode

### Start your Multilogin X agent

#### Linux:
```bash
/opt/mlx/agent.bin
```
Or simply:
```bash
mlx
```

#### Windows:

```bash
Start-Process -FilePath "~/AppData/Local/Multilogin X/agent.exe"
```
### Edit the .env file

```env
MLX_EMAIL=yourmultiloginaccount@domain.com
MLX_PASSWORD=SuperSecretPassword
PROFILE_TYPE=quick
PROFILE_ID=
FOLDER_ID=
BROWSER_TYPE=mimic
```
### Edit the websites list

You need to tell the script where it needs to collect cookies from. Simply edit the "websites" array in the main.py file.

```python
# This is an example. Add as many as you want. If you want to, you can even remove this array here and add another
# method of reading the list of websites, such as by using a spreadsheet, for example.

websites = ["https://wikipedia.org/",
            "https://multilogin.com/"
            "https://dell.com/",
            "https://reddit.com/",
            "https://youtube.com/"]
```

### Run the script

On your terminal, run the script with python.
```bash
python cookie_robot.py
```
Or, if you're using the python3 interpreter:
```bash
python3 cookie_robot.py
```
