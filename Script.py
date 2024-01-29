from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

# Start the Tor Browser
tor_browser_path = '/path/to/tor-browser_en-US/Browser/start-tor-browser'
os.system(tor_browser_path)

# Set up Firefox profile with Tor proxy settings
profile_path = tor_browser_path + '/profile.default'
profile = FirefoxProfile(profile_path)
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)  # 9150 is the default port for Tor Browser
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()

# Set the path to your Firefox binary
firefox_binary_path = '/usr/bin/firefox'  # Default location on many systems

# Set the path to your geckodriver executable
geckodriver_path = '/path/to/geckodriver'

# Configure Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = firefox_binary_path

# Start the Firefox WebDriver with Tor proxy settings
driver = webdriver.Firefox(
    firefox_profile=profile, options=firefox_options, 
    executable_path=geckodriver_path
)

# Navigate to a website to check if Tor is working
driver.get("http://check.torproject.org")

# You can perform further actions with the WebDriver here

# Close the WebDriver
driver.quit()
