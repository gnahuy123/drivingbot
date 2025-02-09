from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import cv2
import time

# Function to capture screenshot
def take_screenshot(url, save_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run browser in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.save_screenshot(save_path)
    time.sleep(10)
    driver.quit()

# Function to compare screenshots
def compare_screenshots(ref_image_path, new_image_path):
    ref_img = cv2.imread(ref_image_path, cv2.IMREAD_GRAYSCALE)
    new_img = cv2.imread(new_image_path, cv2.IMREAD_GRAYSCALE)
    diff_img = cv2.absdiff(ref_img, new_img)
    return diff_img

# Example usage
reference_image_path = "reference.png"
new_screenshot_path = "new_screenshot.png"
website_url = "https://www.youtube.com/watch?v=j7VZsCCnptM&ab_channel=freeCodeCamp.org"

# Take a new screenshot
take_screenshot(website_url, new_screenshot_path)

# Compare screenshots
diff_img = compare_screenshots(reference_image_path, new_screenshot_path)

# Calculate the percentage difference
difference_percentage = (diff_img.sum() / (diff_img.shape[0] * diff_img.shape[1])) * 100

if difference_percentage > 5:
    print("Visual change detected!")
    # Implement logic to trigger a notification or take other action
else:
    print("No significant visual change detected.")