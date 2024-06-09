import os
import requests
import hashlib
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.firefox.options import Options

class Mlx:

    def __init__(self, email: str, password: str, token=None):
        self.email = email
        self.password = password
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def signin(self) -> str:
        url = "https://api.multilogin.com/user/signin"
        payload = {
            "email": self.email,
            "password": hashlib.md5(self.password.encode()).hexdigest()
        }
        r = requests.post(url=url, headers=self.headers, json=payload)
        if r.status_code != 200:
            print("Wrong credentials")
        else:
            json_response = r.json()
            self.token = json_response['data']['token']
            self.headers.update({"Authorization": f"Bearer {self.token}"})
            return self.token

    def start_quick_profile(self, browser_type="mimic"):
        
        if browser_type == "stealthfox":
            relative_path = './extensions/superagent.xpi'
            self.extension_path = os.path.abspath(relative_path)
        if browser_type == "mimic":
            relative_path = './extensions/superagent'
            self.extension_path = os.path.abspath(relative_path)

        payload = {
        "browser_type": browser_type,
        "os_type": "linux",
        "automation": "selenium",
        "parameters": {
            "fingerprint": {
                "cmd_params": {
                        "params": [
                            {
                                "flag": "load-extension",
                                "value": self.extension_path
                            }
                        ]
                }
            },
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
            response = requests.post(url="https://launcher.mlx.yt:45001/api/v2/profile/quick", headers=self.headers, json=payload)
            data = response.json()
            if data['status']['http_code'] != 200:
                message = data['status']['message']
                return None, None, False, message
            else:
                quick_profile_id = data['data']['id']
                quick_profile_port = data['data']['port']
                profile_started = True
                message = data['status']['message']
                return quick_profile_id, quick_profile_port, profile_started, message
        except Exception as e:
            return None, None, False, str(e)

    def start_normal_profile(self, profile_id: str, folder_id: str):
        url = f"https://launcher.mlx.yt:45001/api/v2/profile/f/{folder_id}/p/{profile_id}/start?automation_type=selenium&headless_mode=false"
        response = requests.get(url=url, headers=self.headers)
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

    def stop_profile(self, profile_id: str):
        url = f"https://launcher.mlx.yt:45001/api/v1/profile/stop/p/{profile_id}"
        r = requests.get(url=url, headers=self.headers)
        if r.status_code != 200:
            print("Can't stop profile")
        else:
            print("Profile stopped")

    def instantiate_driver(self, profile_port: str, browser_type="mimic") -> webdriver:
        if browser_type == 'mimic':
            options=ChromiumOptions()
            driver = webdriver.Remote(command_executor=f"http://127.0.0.1:{profile_port}", options=options)
        elif browser_type == 'stealthfox':
            options=Options()
            driver = webdriver.Remote(command_executor=f"http://127.0.0.1:{profile_port}", options=options)
        return driver
    
    def get_proxy_details(self, proxy_settings, token=None) -> dict:
        
        if token == None:
            self.token = self.signin()

        self.headers.update({
            "Authorization": f"Bearer {self.token}"
        })
        url = "https://profile-proxy.multilogin.com/v1/proxy/connection_url"
        payload = {
                "country": proxy_settings['country_code'],
                "region": proxy_settings['region'],
                "city": proxy_settings['city'],
                "protocol": "socks5",
                "sessionType": "sticky",
                "IPTTL": 0
        }
        response = requests.post(url=url,headers=self.headers,json=payload)
        if response.status_code != 201:
            print(f"Could not get proxy session: {response.status_code}")
        else:
            session = response.json()['data'].split(':')
            proxy_details = {
                "host": session[0],
                "port": session[1],
                "username": session[2],
                "password": session[3]
            }
            return proxy_details
    
    def create_profile(self, proxy_details, profile_details, FOLDER_ID):

        if self.token == None:
            self.token = self.signin()

        self.headers.update({
            "Authorization": f"Bearer {self.token}"
        })

        payload = {
        "name": f"{profile_details['first_name']} {profile_details['last_name']}",
        "folder_id": FOLDER_ID,
        "browser_type": "mimic",
        "os_type": "linux",
        "is_headless": False,
        "proxy": {
            "host": proxy_details['host'],
            "type": "socks5",
            "port": proxy_details['port'],
            "username": proxy_details['username'],
            "password": proxy_details['password']
        },
        "parameters": {
            "fingerprint": {
                "cmd_params": {
                    "params": [
                        {
                            "flag": "disable-notifications",
                            "value": "true"
                        }
                    ]
                }
            },
            "flags": {
                "audio_masking": "natural",
                "fonts_masking": "mask",
                "geolocation_masking": "mask",
                "geolocation_popup": "allow",
                "graphics_masking": "natural",
                "graphics_noise": "natural",
                "localization_masking": "mask",
                "media_devices_masking": "natural",
                "navigator_masking": "mask",
                "ports_masking": "natural",
                "proxy_masking": "custom",
                "screen_masking": "natural",
                "timezone_masking": "mask",
                "webrtc_masking": "mask"
            },
            "storage": {
                "is_local": False,
                "save_service_worker": False
            }
        }
        }
        url = "https://api.multilogin.com/profile/create"
        response = requests.post(url=url, headers=self.headers, json=payload)
        if response.status_code != 201:
            print(f"Could not create profile: Error {response.status_code}")
            return None, None, None
        else:
            profile_id = response.json()['data']['ids'][0]
            created = True
            return profile_id, FOLDER_ID, created