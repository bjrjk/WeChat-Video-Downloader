import os
os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests, warnings
from bs4 import BeautifulSoup
from selenium import webdriver
warnings.filterwarnings("ignore")


def download(URL, fileName):
    with open(fileName, "wb") as f:
        r = requests.get(URL, verify=False)
        f.write(r.content)

def downloadVideo(videoName, videoFrameURL):
    driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
    driver.get(videoFrameURL)
    videoURL = driver.find_element_by_tag_name("video").get_attribute("origin_src")
    print("Video URL:", videoURL)
    download(videoURL, videoName + ".mp4")

def main():
    URL = input("Please input WeChat Offical Account Page URL (Like https://mp.weixin.qq.com/s/******): ")
    response = requests.get(URL, verify=False)
    HTMLContent = response.content
    bs = BeautifulSoup(HTMLContent, "html.parser")
    print("Video_Name", "Video_FrameURL")
    for video in bs.find_all("iframe", class_="video_iframe"):
        videoFrameURL = video.get("data-src")
        videoName = video.get("data-mpvid")
        print(videoName, videoFrameURL)
        downloadVideo(videoName, videoFrameURL)
    print("Download Finished!")


if __name__ == '__main__':
    main()
