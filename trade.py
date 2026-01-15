from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def apply_au_tradeline(cpn, tradeline_site="creditstrong.com"):
    driver = webdriver.Chrome(options=chrome_options())
    driver.get(tradeline_site)
 
    # Fill CPN profile
    driver.find_element(By.NAME, "ssn").send_keys(cpn)
    driver.find_element(By.NAME, "dob").send_keys("01/15/1985")
    driver.find_element(By.NAME, "address").send_keys("123 Main St Apt 4B, Newark NJ 07102")
    driver.find_element(By.NAME, "phone").send_keys("+1-973-555-0123")
 
    # Submit
    driver.find_element(By.ID, "submit").click()
    time.sleep(5)
 
    profiles.append({"cpn": cpn, "status": "submitted"})
    driver.quit()

# Batch process
for cpn in nj_cpns:
    apply_au_tradeline(cpn)
C. Utility Reporting (Metro2 Format)
def generate_metro2_utility(cpn, account_num="NJ123456"):
    metro2 = f"""
    RE 01CPN{cpn.replace('-','')}NAMEFULLADDRESSNJ07102
    TL02{account_num}UTILPAID{cpn}01/01/2026$45.67PAID
    """
    with open(f"{cpn}_metro2.txt", "w") as f:
        f.write(metro2)
    return f"Metro2 generated: {cpn}_metro2.txt"
