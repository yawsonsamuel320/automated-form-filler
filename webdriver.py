from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to your WebDriver executable. You should download the appropriate WebDriver for your browser (e.g., Chrome, Firefox).
driver = webdriver.Chrome()

# Open the Google Form URL
form_url = 'https://forms.gle/vWVmojtWdfFvEj8V6'
driver.get(form_url)

# Fill out the form fields
name = driver.find_elements("class", "ndJi5d snByac")  # Replace "entry.123456789" with the actual field name or ID for Name
name.send_keys("Your Name")

email = driver.find_element_by_name("entry.987654321")  # Replace "entry.987654321" with the actual field name or ID for Email
email.send_keys("your@email.com")

address = driver.find_element_by_name("entry.567890123")  # Replace "entry.567890123" with the actual field name or ID for Address
address.send_keys("Your Address")

phone = driver.find_element_by_name("entry.456789012")  # Replace "entry.456789012" with the actual field name or ID for Phone
phone.send_keys("123-456-7890")

comments = driver.find_element_by_name("entry.345678901")  # Replace "entry.345678901" with the actual field name or ID for Comments
comments.send_keys("Your comments here")

# Submit the form
submit_button = driver.find_element_by_xpath("//span[text()='Submit']")  # Replace with the text on the submit button
submit_button.click()

# Close the browser
driver.quit()
