#import modules selenium to translate from baidu
from selenium import webdriver
#import By
from selenium.webdriver.common.by import By
from time import sleep
import clipboard
import os

def save_the_text(i):
    copy_button = driver.find_element(By.CLASS_NAME, "icon-copy")
    #click the copy button
    copy_button.click()
    sleep(1)
    #save to file
    with open(f"E:/LT/Trans/output/result_{i}.txt", 'a', encoding='utf-8') as f:
        f.write(clipboard.paste() + ' ')
    sleep(2)
    input_box.clear()
def error_paragraph(paragraph, i):
    with open(f'E:/LT/Trans/output/error_paragraph_{i}.txt', 'a', encoding='utf-8') as f:
        f.write(paragraph)

#mở file test.txt
with open('test.txt', 'r', encoding="utf-8") as f:
    paragraph = f.read()
    # chia thành từng đoạn 1000 ký tự
    paragraphs = [paragraph[i:i+1000] for i in range(0, len(paragraph), 1000)]

#open the browser
#head-less mode
driver = webdriver.Chrome()
driver.get("https://fanyi.baidu.com/#zh/vie/")
sleep(1)

for paragraph, i in zip(paragraphs, range(1, len(paragraphs) + 1 )):
    input_box = driver.find_element(By.TAG_NAME, "textarea")
    input_box.send_keys(paragraph)
    try:
        sleep(2)
        #find the copy button
        try:
                save_the_text(i)
        except:
            try:
                sleep(5)
                save_the_text(i)
            except:
                error_paragraph(paragraph, i)
                input_box.clear()
    except:
        try:
            driver.refresh()
            sleep(5)
            input_box = driver.find_element(By.TAG_NAME, "textarea")
            input_box.send_keys(paragraph)
            sleep(5)
            save_the_text(i)
        except:
            error_paragraph(paragraph, i)
            input_box.clear()

#tìm các txt lỗi 
error_files = [file for file in os.listdir() if file.startswith('error_paragraph_')]

#đọc file lỗi
for file in error_files:
    #lấy giá trị số trong tron tên file
    i = int(file.split('_')[2].split('.')[0])
    with open(file, 'r', encoding='utf-8') as f:
        paragraph = f.read()
        input_box = driver.find_element(By.TAG_NAME, "textarea")
        input_box.send_keys(paragraph)
        sleep(5)
        save_the_text(i)
        sleep(3)
        input_box.clear()

result_files = [file for file in os.listdir('E:/LT/Trans/output') if file.startswith('result')]

with open('E:/LT/Trans/result.txt', 'a', encoding='utf-8') as f:
    for file in result_files:
        with open(f'E:/LT/Trans/output/{file}', 'r', encoding='utf-8') as f1:
            f.write(f1.read())
            f.flush()

driver.close()