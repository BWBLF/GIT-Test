from bs4 import BeautifulSoup
import requests



html_text = requests.get ('https://careerbuilder.vn/viec-lam/Backend-k-vi.html').text
#print(html_text)
soup = BeautifulSoup(html_text, "lxml")
print(soup)
jobs = soup.find_all("div", class_= "job-item")
print(jobs)
