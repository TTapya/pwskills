from selenium import webdriver
from bs4 import BeautifulSoup as bs
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/@PW-Foundation/videos")
soup = bs(driver.page_source, "html.parser")

video_urls = []
for a in soup.find_all("a", {"class":"yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media"})[:5]:
    video_urls.append("https://www.youtube.com" + a['href'])
    # print(f"Video {index + 1} URL: https://www.youtube.com{a['href']}")

thumbnail_urls = []
for img_url in soup.find_all('img',{'class':"yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded"}):
    thumbnail_urls.append(img_url['src'])
    # print(f"Video {index + 1} Thumbnail URL: {img_url['src']}")
for i in range(5 - len(thumbnail_urls)):
    thumbnail_urls.append("N/A")
    
titles = []
for title in soup.find_all('a',{'class':'yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media'})[:5]:
    titles.append(title.text)
    # print(f"Video {index + 1} Title: {title.text}")

views = []
for item in soup.find_all("ytd-rich-item-renderer", {"class":"style-scope ytd-rich-grid-row"})[:5]:
    views.append(item.find('span',{'class':'inline-metadata-item style-scope ytd-video-meta-block'}).text)
    # print(f"Video {index + 1} Views: {views}")

upload_dates = []
for item in soup.find_all("ytd-rich-item-renderer", {"class":"style-scope ytd-rich-grid-row"})[:5]:
    upload_dates.append(item.find_all('span',{'class':'inline-metadata-item style-scope ytd-video-meta-block'})[1].text)
    # print(f"Video {index + 1} Views: {views}")

# print(video_urls)
# print(thumbnail_urls)
# print(titles)
# print(views)
# print(upload_dates)

fields = ["Video_URL", "Thumbnail_URL", "Title", "Views", "Upload Date"]
filename = "image_scapper.csv"

with open(filename, 'w', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    for i in range(5):
        csvwriter.writerow([video_urls[i], thumbnail_urls[i], titles[i], views[i], upload_dates[i]])