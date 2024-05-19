import os
import dotenv
import requests
import hashlib
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options

dotenv.load_dotenv()
mlx_email_address = os.getenv("MLX_EMAIL")
mlx_password = os.getenv("MLX_PASSWORD")

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def signin() -> str:
    url = "https://api.multilogin.com/user/signin"
    payload = {
        "email": f"{mlx_email_address}",
        "password": hashlib.md5(mlx_password.encode()).hexdigest()
    }
    r = requests.post(url=url, headers=HEADERS, json=payload)
    if r.status_code != 200:
        print("Wrong credentials")
    else:
        json_response = r.json()
        token = json_response['data']['token']
        return token

def start_quick_profile(token, browser_type="mimic"):
    HEADERS.update({
        "Authorization": f"Bearer {token}"
    })
    payload = {
    "browser_type": f"{browser_type}",
    "os_type": "windows",
    "automation": "selenium",
    "is_headless": False,
    "parameters": {
        "fingerprint": {},
        "flags": {
            "audio_masking": "mask",
            "fonts_masking": "mask",
            "geolocation_masking": "mask",
            "geolocation_popup": "prompt",
            "graphics_masking": "mask",
            "graphics_noise": "mask",
            "localization_masking": "mask",
            "media_devices_masking": "mask",
            "navigator_masking": "mask",
            "ports_masking": "mask",
            "proxy_masking": "disabled",
            "screen_masking": "mask",
            "timezone_masking": "mask",
            "webrtc_masking": "mask"
        }
    }
    }
    try:
        response = requests.post(url="https://launcher.mlx.yt:45001/api/v2/profile/quick", headers=HEADERS, json=payload)

        if(response.json()['status']['http_code'] != 200):
            quick_profile_id = False
            quick_profile_port = False
            profile_started = False
            message = response.json()['status']['message']
            return quick_profile_id, quick_profile_port, profile_started, message
        else:
            quick_profile_id = response.json()['data']['id']
            quick_profile_port = response.json()['data']['port']
            profile_started = True
            message = response.json()['status']['message']
            return quick_profile_id, quick_profile_port, profile_started, message
    except Exception as e:
        quick_profile_id = False
        quick_profile_port = False
        profile_started = False
        message = e
        return quick_profile_id, quick_profile_port, profile_started, message

def start_normal_profile(token: str, profile_id: str, folder_id: str) -> str:
    HEADERS.update({
        "Authorization": f"Bearer {token}"
    })

    url = f"https://launcher.mlx.yt:45001/api/v2/profile/f/{folder_id}/p/{profile_id}/start?automation_type=selenium&headless_mode=false"
    response = requests.get(url=url, headers=HEADERS)
    if response.status_code != 200:
        message = response.json()['status']['message']
        profile_port = False
        profile_started = False
        print(f"Error at starting profile: {message}")
        return profile_id, profile_port, profile_started, message
    else:
        profile_port = response.json()['data']['port']
        message = response.json()['status']['message']
        profile_started = True
        return profile_id, profile_port, profile_started, message

def stop_profile(profile_id: str, token: str) -> str:
    HEADERS.update({
        "Authorization": f"Bearer {token}"
    })
    url = f"https://launcher.mlx.yt:45001/api/v1/profile/stop/p/{profile_id}"
    r = requests.get(url=url, headers=HEADERS)
    if r.status_code != 200:
        print("Can't stop profile")
    else:
        print("Profile stopped")

def instantiate_driver(profile_port: str, browser_type="mimic") -> webdriver:
    if browser_type == 'mimic':
        driver = webdriver.Remote(command_executor=f"http://127.0.0.1:{profile_port}", options=ChromiumOptions())
    elif browser_type == 'stealthfox':
        driver = webdriver.Remote(command_executor=f"http://127.0.01:{profile_port}", options=Options())
    return driver