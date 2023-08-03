
<div align=center>
  
![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300§ion=header&text=오늘의%20밥상%20메뉴%20알림봇🍚&desc=오늘의밥상%20인스타그램%20크롤링을%20통해%20메뉴%20알림%20슬랙%20봇%20제작&fontSize=40&descSize=25&fontColor=000000&fontAlignY=30)

<br/>
<h2> 🌱 tech used in the project 🌱 </h2>
<h6> <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/> 
<img src="https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=red"/> 
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> </h6>
<br/><br/>


---------------------------------------
<br/>

<h2>1. 프로젝트 개요  </h2><br/>
<img width="304" alt="오늘의밥상_개요" src="https://github.com/sesac-2023/sub_project_kimsj/assets/55127185/a49d614d-4532-43dc-82c7-c3f5de5247d0"><br/><br/>
1. mysql과 python이랑 연동하여, 최신 날짜를 가져왔고, datetime.today()를 이용해 오늘 날짜를 가져왔다.<br/><br/>
2.-1 오늘날짜 =! db날짜 이면, 크롤링이 필요하다고 생각하고 계속 크롤링<br/><br/>
2-2. 오늘날짜 == db날짜 이면, 크롤링이 이미 끝나 데이터 수집이 완료되었다고 봄.<br/><br/>
3-1. 크롤링 날짜 != 오늘 날짜 이면, 게시물이 아직 올라오지 않았다고 판단하여 계속 크롤링<br/><br/>
3-2. 크롤링 날짜 == 오늘 날짜 이면, 크롤링이 완료되었다고 보고 mysql db에 업데이트를 해줌<br/><br/>
4. 슬랙봇에게 정보를 줘서 슬랙에 알림이 가게 만듦
<br/><br/><br/>

---------------------------------------

<h3>2. 프로젝트 정보</h3><br/>
- 오늘의_밥상_알리미.py : 최종적인 오늘의밥상 슬랙 봇 코드가 있는 python 파일<br/><br/>
- 데이터베이스.ipynb : python과 데이터베이스 연결 jupyter notebook 파일<br/><br/>
- 슬랙봇만들기.ipynb : python과 슬랙 연결 jupyter notebook 파일<br/><br/>
- 오밥크롤링_인스타.ipynb : 오늘의 밥상 인스타그램 크롤링 하는 코드가 있는 jupyter notebook 파일
<br/><br/><br/>

---------------------------------------

<h3>3. 프로젝트 결과물 </h3>
<img width="986" alt="오늘의밥상_결과물_db" src="https://github.com/sesac-2023/sub_project_kimsj/assets/55127185/8076a2cb-8584-4d19-85db-220a61a4645b"><br/>
mysql 저장된 데이터 <br/><br/><br/>
<img width="910" alt="오늘의밥상_결과물" src="https://github.com/sesac-2023/sub_project_kimsj/assets/55127185/759d2168-ff9a-435c-b184-469c00927f42"><br/>
슬랙에 보내진 메시지

</div>
