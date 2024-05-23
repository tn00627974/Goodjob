# goodjob
這是一個簡易版的 爬取goodjob求職網 面試內容

使用說明
安裝所需的 Python 庫：


```
pip install requests
pip install beautifulsoup4
```
將上述程式碼保存到一個 Python 文件中，例如 goodjob.py。

執行程式：

```
python goodjob.py
```
根據提示輸入要爬取的面試經驗網址，程式將會自動提取相關信息並輸出。

注意事項
請確保輸入的網址對應的是一個有效的面試經驗頁面。
如果頁面結構發生變化，可能需要相應更新程式碼中的 CSS 選擇器。
程式碼中的 headers 用於模擬正常的瀏覽器請求，避免被目標網站屏蔽。

