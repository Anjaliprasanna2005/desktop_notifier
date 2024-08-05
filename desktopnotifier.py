import platform
import subprocess
import ctypes

def send_notification(title, message):
    """Send a desktop notification."""
    system = platform.system()

    if system == "Windows":
        
        ctypes.windll.user32.MessageBoxW(0, message, title, 1)
    elif system == "Darwin":
        
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(["osascript", "-e", script])
    elif system == "Linux":
       
        subprocess.run(["notify-send", title, message])
    else:
        print("Unsupported OS")

def main():
    """Main function to demonstrate desktop notifications."""
    print("Desktop Notifier App")
    
    while True:
        title = input("Enter the notification title: ")
        message = input("Enter the notification message: ")
        
        send_notification(title, message)
        
        print("Notification sent!")
        
        
        time.sleep(10)

if __name__ == "__main__":
    import time
    main()

import ctypes

def send_notification(title, message):
    """Send a desktop notification."""
    system = platform.system()

    if system == "Windows":
       
        ctypes.windll.user32.MessageBoxW(0, message, title, 1)
    elif system == "Darwin":
       
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(["osascript", "-e", script])
    elif system == "Linux":
        
        subprocess.run(["notify-send", title, message])
    else:
        print("Unsupported OS")

def main():
    """Main function to demonstrate desktop notifications."""
    print("Desktop Notifier App")
    
    while True:
        title = input("Enter the notification title: ")
        message = input("Enter the notification message: ")
        
        send_notification(title, message)
        
        print("Notification sent!")
        
        
        time.sleep(10)

if __name__ == "__main__":
    import time
    main()
