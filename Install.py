import os
import platform
import sys
# Linux
geckoLinux = 'https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz'
geckoArchiveLinux = 'geckodriver-v0.34.0-linux64.tar.gz'
torLinux = 'https://www.torproject.org/dist/torbrowser/13.0.9/tor-browser-linux-x86_64-13.0.9.tar.xz'
torArchiveLinux = ''
# macOS
geckomacOS = 'https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-macos.tar.gz'
geckoArchivemacOS = 'geckodriver-v0.34.0-macos.tar.gz'
tormacOS = 'https://www.torproject.org/dist/torbrowser/13.0.9/tor-browser-macos-13.0.9.dmg'
# Windows
geckoWindows = 'https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-win32.zip'
geckoArchiveWindows = 'geckodriver-v0.34.0-win32.zip'
torWindows = 'https://www.torproject.org/dist/torbrowser/13.0.9/tor-browser-windows-x86_64-portable-13.0.9.exe'

if os.name == 'nt':  
    print("Running on Windows")
    print("Windows is not tested so it might not work.")
    print("Downloading geckodriver")
    os.system("wget " + geckoWindows)

elif platform.system() == 'Linux':
    print("Running on Linux")
    print("Downloading geckodriver")
    os.system("wget " + geckoLinux)
    print("Done downloading")
    print("Extracting")
    os.system("tar -xzf " + geckoArchiveLinux)
    print("Done extracting")
    print("Removing archive")
    os.system("rm geckodriver-v0.34.0-linux64.tar.gz")
    print("Done removing")
    print("Downloading Tor")
    os.system("wget " + torLinux)
    print("Done downloading Tor")
    print("Extracting Tor")
    os.system("tar -xzf ")
    
    
elif platform.system() == 'Darwin':
    print("Running on macOS")
    print("Downloading geckodriver")
    os.system("wget " + geckomacOS)

else:
    print("Unsupported operating system")
    sys.exit(1)
