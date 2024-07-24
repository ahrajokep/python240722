import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 100):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    #<div class="fds-comps-right-image-text-container WDfJwV7NBYwCv9LJoBpg"><a nocr="1" href="https://in.naver.com/zzaru/contents/internal/701182182701856?areacode=itb_bas%2Af_other&amp;query=%EB%A7%A5%EB%B6%81%EC%97%90%EC%96%B4" class="IPXEr_it0BA1OpoWoFF7 fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000035491916.a0209rl4_nblog_post_223468912393'" data-cb-trigger="true"><span class="B8JXUcm_QYlAFsOH6qCs"><mark>맥북에어</mark> 15인치 M3 M2 고민 해결</span></a><a nocr="1" href="https://in.naver.com/zzaru/contents/internal/701182182701856?areacode=itb_bas%2Af_other&amp;query=%EB%A7%A5%EB%B6%81%EC%97%90%EC%96%B4" class="IPXEr_it0BA1OpoWoFF7 fds-comps-right-image-text-content" target="_blank" data-cb-target="'SYS-0000000035491916.a0209rl4_nblog_post_223468912393'" data-cb-trigger="true"><span class="B8JXUcm_QYlAFsOH6qCs">본 콘텐츠에서는 합리적인 가격에 쾌적한 디스플레이와 준수한 휴대성을 자랑하는 <mark>맥북에어</mark> 15인치 두 가지 모델을 비교하고 본문 말미에는 정가보다 훨씬 저렴하게 구매하는 방법까지 담겨있다. 아이폰, <mark>에어</mark>팟, 애플워치 등 애플 디바이스를 사용하고 있다면 이번 기회에 macOS에 입문해 보길 권한다. 1. M2 vs M3 가성비 모델 선택 팁의 결론부터... </span></a></div>
    posts = soup.find_all('div', {'class':'fds-comps-right-image-text-container WDfJwV7NBYwCv9LJoBpg'})
    for post in posts:
        try:
            #<a nocr="1" href="https://in.naver.com/zzaru/contents/internal/701182182701856?areacode=itb_bas%2Af_other&amp;query=%EB%A7%A5%EB%B6%81%EC%97%90%EC%96%B4" class="IPXEr_it0BA1OpoWoFF7 fds-comps-right-image-text-title" target="_blank" data-cb-target="'SYS-0000000035491916.a0209rl4_nblog_post_223468912393'" data-cb-trigger="true"><span class="B8JXUcm_QYlAFsOH6qCs"><mark>맥북에어</mark> 15인치 M3 M2 고민 해결</span></a>
            #<span class="B8JXUcm_QYlAFsOH6qCs"><mark>맥북에어</mark> 15인치 M3 M2 고민 해결</span>
            blog_address_elem = post.find("a", 
                attrs={"class":"IPXEr_it0BA1OpoWoFF7 fds-comps-right-image-text-title"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("span", attrs={"class":"B8JXUcm_QYlAFsOH6qCs"})
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        
        #<span class="fds-info-sub-inner-text B8JXUcm_QYlAFsOH6qCs">2024.06.04.</span>
        post_date_elem = post.find('span', {'class':'fds-info-sub-inner-text B8JXUcm_QYlAFsOH6qCs'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find("a", attrs={"class":"IPXEr_it0BA1OpoWoFF7 fds-comps-right-image-text-title"})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address_title, blog_address, post_title, post_date])

#path = 'c:\\work\\'
#file_path = f'{path}{search_keyword}_blog_data.xlsx'
file_path = f'{search_keyword}_blog_data.xlsx'
wb.save(file_path)