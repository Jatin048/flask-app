import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

start_time = time.time()

options = Options()

# 🔥 IMPORTANT: Snap Chromium path
options.binary_location = "/snap/bin/chromium"

# 🔥 Required for VM / headless
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--window-size=1920,1080")

# 🔥 Let Selenium auto-manage driver (Selenium 4.6+ feature)
driver = webdriver.Chrome(options=options)

# Open your Flask app
driver.get("http://localhost:5000")

print("Page Title:", driver.title)

driver.quit()

end_time = time.time()
print("Test Execution Time:", round(end_time - start_time, 2), "seconds")
