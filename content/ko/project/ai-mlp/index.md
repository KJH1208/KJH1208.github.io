---
title: 인공신경망 (MLP) 실습 프로젝트
summary: Python을 활용한 선형회귀, 로지스틱회귀, 다층퍼셉트론 실습 프로젝트
tags: 
  -AI
date: 2025-10-25
featured: true

# 미리보기 이미지
image:
  filename: ai_project.jpg
  preview_only: false

# 링크 (깃허브나 파일 다운로드)
links:
  - icon: python
    icon_pack: fab
    name: MLP 코드
    url: /files/projects/MLP.py
  - icon: file-archive
    icon_pack: fas
    name: 전체 ZIP 다운로드
    url: /files/projects/ai_project_files.zip
  - icon: file
    icon_pack: fas
    name: 프로젝트 보고서
    url: /files/projects/202212080_강주현_AI_project2_.hwpx
---
## 프로젝트 개요
이 프로젝트는 **기초 머신러닝 알고리즘**을 Python으로 직접 구현하고,  
데이터셋을 생성하여 회귀·분류·다층퍼셉트론(MLP) 모델을 실습한 내용입니다.

---

### 📘 포함된 주요 코드
- `gen_random_dataset.py` : 난수 기반 데이터 생성  
- `linear_regression.py` : 단순 회귀 분석  
- `logistic_regression.py` : 로지스틱 회귀  
- `MLP.py`, `MLP_minist.py` : 신경망 모델 구현  

---

### 🧠 학습 포인트
- Gradient Descent를 이용한 모델 학습
- Sigmoid, ReLU 등 활성함수 구현
- MNIST 손글씨 데이터 분류 성능 비교