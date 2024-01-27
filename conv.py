from selenium import webdriver

# Specify the URL you want to open
url = "https://www.ilovepdf.com/pdf_to_word"

# Set the path to the ChromeDriver executable
# Make sure to replace 'path/to/chromedriver' with the actual path to the chromedriver executable on your system
chromedriver_path = 'path/to/chromedriver'

# Create a Chrome webdriver instance
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Open the specified URL
driver.get(url)

# Optionally, you can perform additional actions here, such as interacting with elements on the page

# Close the browser window
driver.quit()
