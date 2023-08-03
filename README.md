
<div align=center>
  
![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300§ion=header&text=오늘의%20밥상%20메뉴%20알림봇🍚&desc=This%20is%20Sumin%20playground.%20&fontSize=40&descSize=30&fontColor=000000&fontAlignY=20)
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 
<h2 > 🛠 my Tech Stack 🛠 </h2>
<h6> <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 
<img src="https://img.shields.io/badge/PowerBI-F2C811?style=flat-square&logo=PowerBI&logoColor=yellow"/> 
<img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=red"/> 
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> </h6>

<h2> 🌱 tech used in the project 🌱 </h2>
<h6> <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 
<img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=red"/> 
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> </h6>

---------------------------------------

<h2> <span style="color:red">주제 </h2></span>
<h3> 오늘의 밥상 인스타그램 크롤링을 통해 메뉴 알림 슬랙 봇 제작 </h3>

<h4 align="center">
우리가 매일 가는 문래 오늘의 밥상! 매번 홈페이지 들어가기 귀찮은데, 알려주는 봇이 있으면 좋겠다!! --> 오밥봇을 만들자! </h4>




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
