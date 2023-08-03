
<div align=center>
  
![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300§ion=header&text=오늘의%20밥상%20메뉴%20알림봇🍚&desc=오늘의밥상%20인스타그램%20크롤링을%20통해%20메뉴%20알림%20슬랙%20봇%20제작&fontSize=40&descSize=25&fontColor=000000&fontAlignY=30)

<br/><br/>
<h2> 🌱 tech used in the project 🌱 </h2>
<h6> <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 
<img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=red"/> 
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> </h6>
<br/><br/>


---------------------------------------
<br/>

<h3>1. 프로젝트 개요  </h3>



<h3>2. 프로젝트 정보</h3>

<h3>3. 프로젝트 결과물 </h3>


오늘의 밥은 뭘까?

오늘의 밥상에서 이미지를 긁어와 OCR을 이용해 메뉴를 업로드한다.

url : https://blog.naver.com/skfoodcompany

## 구체화

1. 오늘의 밥상에서 일자 크롤링
2. 오늘의 밥상에서 제일 첫번째 이미지 크롤링
3. 크롤링 한 내용을 .. OCR처리 tool에 가져오기
4. OCR에서 내용 처리하기
(PORORO OCR : https://yunwoong.tistory.com/210)
5. 처리한 내용 데이터 베이스에 저장?하기
6. 텔레그램 봇 통해서 나한테 알림 보내기

</div>

#### 새로 올라온 데이터라는걸 어떻게 확인할 수 있을까??
목록열기 - 게시물 누르면 url이 바뀌는데 이 url을 저장해놓고
어제의 url과 현재 url이 같으면 업로드 x
어제의 url과 현재 url이 다르면 업로드 o
로 판단해서 크롤링 하면 되지 않을까?? 
