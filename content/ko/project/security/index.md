---
title: 네트워크 보안 실습 프로젝트
summary: Wireshark, Nmap, 방화벽 등 네트워크 보안 핵심 실습을 수행한 보고서 모음.
type: project
tags:
  - SEC
date: 2024-12-31
draft: false
featured: true
share: false

image:
  filename: security-cover.jpg
  preview_only: false

links:
  - icon: file-archive
    icon_pack: fas
    name: 전체 ZIP 다운로드
    url: /files/projects/security_reports.zip
---

## 프로젝트 개요
네트워크 보안 관련 수업/개인실습에서 수행한 보고서를 모은 페이지입니다.  
Wireshark 기반 패킷 분석, Nmap 스캐닝, 배너 그래빙, SNMP 시도, 방화벽/DoS 등 주제를 다룹니다.

---

### 📘 주요 실습 목록
- 패킷 스니핑/분석 (Wireshark)
- 다양한 포트 스캔 및 우회 기법 (Nmap SYN/FIN/Fragmentation 등)
- 배너 그래빙(FTP/SMTP/SSH/HTTP)
- SNMP 정보 수집 시도
- 방화벽/네트워크 토폴로지 구성 실습
- 간단한 패킷 트레이서 구성/경로 확인

---

### 📄 세부 실습 설명(간단설명)
### 🔎 세부 실습 설명 (간단 요약)

- **패킷 분석 (Packet Analysis)**  
  네트워크에 오가는 패킷을 캡처하고(예: Wireshark) 헤더와 페이로드를 해석하여 프로토콜 동작, 통신 흐름, 비정상 트래픽을 식별합니다.  
  *학습 포인트:* 패킷 구조(TCP/UDP/IPv4/IPv6), 패킷 필터링, 트래픽 재구성.

- **Whois & DNS 조사**  
  도메인/호스트에 대한 등록 정보와 DNS 레코드를 조회하여 소유자, 네임서버, A/AAAA/MX/TXT 레코드 등 네트워크 식별 정보를 수집합니다.  
  *학습 포인트:* DNS 동작 원리, 레코드 종류, 역추적 기법.

- **IP 주소 추적 (IP Geolocation / Tracing)**  
  IP 주소의 라우팅 경로(traceroute)와 공개 데이터(WHOIS, BGP 등)를 조합해 트래픽 경로와 소스/대상 위치를 추정합니다.  
  *학습 포인트:* 라우팅/AS 개념, TTL 기반 추적, 한계와 프라이버시 고려사항.

- **목록화 (Asset/Service Enumeration)**  
  네트워크에 존재하는 호스트와 서비스(포트)를 식별하여 실제 공격 표면을 이해하고, 중요 자산을 목록화합니다.  
  *학습 포인트:* 포트 스캐닝(Nmap 옵션), 서비스 배너 확인, 자산 우선순위화.

- **스니핑·스푸핑 (Sniffing & Spoofing)**  
  스니핑은 네트워크 트래픽을 수집하는 행위, 스푸핑은 발신자 정보를 위조하는 기법으로서, 둘을 통해 인증우회나 세션 가로채기 가능성을 실습합니다.  
  *학습 포인트:* ARP 스푸핑, MAC/IP 위조, HTTPS/TLS의 방어 역할.

- **터널링 및 TCP 세션 하이재킹 (Tunneling & TCP Session Hijack)**  
  합법적/비합법적 터널(예: SSH 터널)을 통한 우회 접속과, 기존 TCP 세션을 가로채 세션을 탈취하는 원리를 실험합니다.  
  *학습 포인트:* TCP 3-way handshake, 세션 식별자, 시퀀스 번호 조작의 위험성.

- **SSL 스니핑·MITM 공격 (SSL Sniffing / MITM)**  
  중간자 공격을 통해 암호화 통신을 가로채는 방법과 이를 방지하는 인증서 검증, HSTS, 공개키 기반 방어를 비교 실습합니다.  
  *학습 포인트:* TLS 핸드셰이크, 인증서 신뢰 체계, Mitigation(예: certificate pinning).

- **서비스 거부 공격 (DoS/DDoS) 시뮬레이션**  
  트래픽 과부하나 자원 고갈을 유발하는 간단한 DoS 실험(비파괴적)/시뮬레이션을 통해 방어책(레이트리밋, 방화벽 룰)을 테스트합니다.  
  *학습 포인트:* 공격 벡터 종류, 트래픽 분산 방지 전략, 모니터링 필요성.

- **방화벽 실습 (Firewall Configuration & Rules)**  
  패킷 필터링과 상태 기반 방화벽 규칙을 설계·적용하여 불필요한 접근을 차단하고, 정책별 예외 처리와 로깅을 실습합니다.  
  *학습 포인트:* ACL 작성법, 상태 트래킹, NAT/포트포워딩 고려사항.
---
