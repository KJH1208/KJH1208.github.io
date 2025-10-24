---
title: 자바 멀티플레이 카드게임 ‘결!합!’
summary: Java Swing + Socket으로 구현한 실시간 멀티플레이 카드게임. 채팅, 정답판정, 서버/클라이언트 프레임 포함.
type: project
tags:
  - WEB        
date: 2024-12-20
draft: false
featured: false
share: false

image:
  filename: projects/java-set-cover.jpg   # static/media/projects/java-set-cover.jpg
  preview_only: false

links:
  - icon: file-archive
    icon_pack: fas
    name: 전체 소스 ZIP
    url: /files/projects/java-set/java-set-source.zip

  - icon: java
    icon_pack: fab
    name: clientFrame.java
    url: /files/projects/java-set/clientFrame.java

  - icon: java
    icon_pack: fab
    name: Server.java
    url: /files/projects/java-set/Server.java

  - icon: java
    icon_pack: fab
    name: StartFrame.java
    url: /files/projects/java-set/StartFrame.java

  - icon: java
    icon_pack: fab
    name: Round2.java
    url: /files/projects/java-set/Round2.java

  - icon: file-word
    icon_pack: fas
    name: 프로젝트 보고서(DOCX)
    url: /files/projects/java-set/project-report.pdf
---

## 프로젝트 개요
**Java Swing UI**와 **TCP 소켓 통신**으로 멀티플레이 카드게임 *‘결!합!’*을 구현했습니다.  
실시간 채팅, 서버의 정답 판정, 클라이언트 UI/이벤트 처리, 라운드 관리 등을 포함합니다.

### 주요 기능
- 서버/클라이언트 구조 (다중 접속, 실시간 브로드캐스팅)
- 채팅 및 게임 이벤트 메시지 프로토콜
- Java Swing 기반 게임 보드/컨트롤 UI
- 서버 측 정답 판정 로직 및 라운드 관리

### 역할 분담(요약)
- 강주현: 전체 프레임/클라이언트(UI) 설계, 이미지 리소스 제작
- 팀원: StartFrame, 멀티플레이/서버 구현, 피드백 및 안정화