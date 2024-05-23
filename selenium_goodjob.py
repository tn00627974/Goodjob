"""
登入帳號密碼開發中
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 設置Chrome瀏覽器選項
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 在後台運行Chrome瀏覽器，不顯示界面

# 初始化Chrome服務
chrome_service = Service("path_to_chromedriver")  # 替換為您的Chrome驅動程式的路徑
chrome_service.start()

# 初始化Chrome瀏覽器
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 載入目標網頁
driver.get("https://www.goodjob.life/experiences/6527d5f74d98a0a9fb7b6f45")  # 替換為您要抓取的網頁URL

# 等待動態內容加載
time.sleep(5)  # 這裡可以調整等待時間，視網頁加載速度而定

# 獲取網頁內容
html_content = driver.page_source

# 關閉瀏覽器
driver.quit()

# 使用Beautiful Soup解析HTML
soup = BeautifulSoup(html_content, "html.parser")
