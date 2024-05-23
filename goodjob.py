import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

def get_followed_by_span(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    followed_by_span = soup.find('div', class_='src-components-ExperienceDetail-Article-__Article-module___date').text.strip()

    # 找到公司名稱
    company = soup.find('div', class_='src-components-ExperienceDetail-Article-__InfoBlock-module___content').text.strip()

    # 找到面試地區
    interview_location = soup.find_all('div', class_='src-components-ExperienceDetail-Article-__InfoBlock-module___content')[1].text.strip()

    # 找到應徵職稱
    job_title = soup.find_all('div', class_='src-components-ExperienceDetail-Article-__InfoBlock-module___content')[2].text.strip()

    # 找到相關職務工作經驗
    experience = soup.find_all('div', class_='src-components-ExperienceDetail-Article-__InfoBlock-module___content')[3].text.strip()

    # 找到面試時間
    interview_time = soup.find_all('div', class_='src-components-ExperienceDetail-Article-__InfoBlock-module___content')[4].text.strip()

    # 找到面試結果
    interview_result = soup.find_all('div', class_='src-components-ExperienceDetail-Article-__InfoBlock-module___content')[5].text.strip()

    # 找到待遇
    salary = soup.find_all('div', class_='src-components-ExperienceDetail-Article-__InfoBlock-module___content')[6].text.strip()

    # 找到整體面試滿意度
    satisfaction = soup.find('div', class_='src-components-ExperienceDetail-Article-__RateButtons-module___ratingText').text.strip()

    # 找到面試者過程
    interview_process = soup.find('div', class_='src-components-common-base-__P-module___l src-components-ExperienceDetail-Article-__SectionBlock-module___content').text.strip()

    # 給其他面試者的中肯建議
    encourage = soup.find('div', class_='src-components-common-base-__P-module___l src-components-ExperienceDetail-Article-__SectionBlock-module___content').text.strip()

    # 輸出結果
    return {
        "刊登日期": followed_by_span,
        "公司": company,
        "面試地區": interview_location,
        "應徵職稱": job_title,
        "相關職務工作經驗": experience,
        "面試時間": interview_time,
        "面試結果": interview_result,
        "待遇": salary,
        "整體面試滿意度": satisfaction,
        "面試者過程": interview_process,
        "中肯建議": encourage
    }


url = input("請輸入要爬取的面試網址：")
a = get_followed_by_span(url)
for i in a:
    print(i, ":", a[i])

