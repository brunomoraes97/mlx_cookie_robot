# CookieRobot for Multilogin X

This is a tool for automatically visiting determined websites in order to collect cookies from them. You can either start a quick browser profile to do this, or start an existing browser profile.

## Instructions

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
MLX_EMAIL=add your multilogin x email address here
MLX_PASSWORD=add your multilogin x password here
PROFILE_TYPE=normal OR quick
PROFILE_ID=paste the profile ID here
FOLDER_ID=paste the folder ID of the group that profile belongs to
```
### Edit the websites list

You need to tell the script where he needs to collect cookies from. Simply edit the "websites" array in the main.py file.

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
python main.py
```
Or, if you're using the python3 interpreter:
```bash
python3 main.py
```