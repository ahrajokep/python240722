# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
# 웹브라우저 인 것 처럼 취하는거. 비어있지만 않으면 됨.

# <span class="subject_fixed" data-role="list-title-text" title="gs25 뮤비페 일산 모바일티켓 판매합니다. 2매.">
# 	gs25 뮤비페 일산 모바일티켓 판매합니다. 2매.
# 	</span>


for n in range(1,11): ### 수정
        #오늘의 유머 주소 
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n) ### 수정
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        # 한글이 깨지는 경우 디코딩
        page = data.decode('utf-8', 'ignore')
        # 스프 객체
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td',attrs={'class':'subject'})
    

        for item in list:
                # 에러 처리 구문
                try:
                        title = item.find("a").text.strip()
                        print(title)
                        # if (re.search('한국', title)):
                        #         print(title.strip())
                except:
                        pass
        
