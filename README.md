# 🍽️ My Food Diary

> 광고나 리뷰 이벤트로 부풀려진 맛집 정보에 지쳤다면? 🤦
> **My Food Diary**는 사용자가 직접 기록한 음식과 맛집 데이터를 기반으로 관리하고 추천받을 수 있는 서비스입니다.

## 📌 Overview

My Food Diary는 개인의 음식 취향과 맛집 기록을 관리하기 위한 Python 기반 프로젝트입니다.

사용자가 직접 추가한 음식과 식당 정보를 바탕으로 음식 일정을 관리하고, Food WorldCup 기능을 통해 개인 맞춤형 맛집 및 메뉴 추천을 제공합니다.

### 주요 기능

1. **먹부림 캘린더**

   * 먹고 싶은 음식과 가고 싶은 식당을 캘린더 형태로 관리
   * 개인 식단 및 맛집 방문 계획 기록

2. **Food WorldCup**

   * 선호하는 음식을 토너먼트 방식으로 선택
   * 사용자의 취향을 반영한 메뉴 추천

3. **맛집 데이터 관리**

   * 사용자가 직접 등록한 식당 및 메뉴 정보 저장
   * Notion Database와 연동하여 데이터 관리

---

## ✨ Features

* 📅 캘린더 기반 음식 일정 관리
* 🏆 Food WorldCup을 통한 음식 취향 분석
* ⭐ 맛집 정보 및 별점 관리
* 🔐 로그인 기능
* 📝 Notion API 연동
* 🎨 Tkinter 기반 GUI 제공

---

## 🛠 Tech Stack

| Category    | Technology |
| ----------- | ---------- |
| Language    | Python     |
| GUI         | Tkinter    |
| API         | Notion API |
| Library     | requests   |
| Data Format | JSON       |

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/ch0rca/MyFoodDiary.git
cd MyFoodDiary
```

### 2. Install Required Packages

```bash
pip install tk
pip install requests
```

### 3. Run Project

```bash
python main.py
```

---

## 🔑 Notion API Setup

<img width="500" alt="Notion API" src="https://user-images.githubusercontent.com/50176033/203196346-1e129121-4c9d-45c5-a2c5-c00d3d76d10c.png"> 

### 1. Create Integration

https://www.notion.so/my-integrations

Notion Integration을 생성한 후 API Token을 발급받습니다.

### 2. Connect Database

사용할 Notion Database에 생성한 Integration을 연결하여 접근 권한을 부여합니다.

### 3. Configure Token

발급받은 Token을 프로젝트 설정 파일에 입력합니다.

---

## 👥 Contributors

| 이름  | 개발 파트           | 담당 업무                                      |
| --- | --------------- | ------------------------------------------ |
| 문성재 | Notion API      | Notion DB 내 사용자 정보 조회 및 Calendar 연동        |
| 조성원 | Food WorldCup   | Food WorldCup 기능 구현 및 맛집/별점 데이터 전달         |
| 황준영 | GUI Development | Login Screen, Main Screen, Calendar GUI 구현 |

---

## 🎯 Purpose

본 프로젝트는 Python GUI 프로그래밍과 API 연동을 학습하고, 팀 프로젝트를 통해 협업 경험을 쌓기 위해 개발되었습니다.

또한 사용자가 직접 기록한 데이터를 기반으로 더욱 신뢰도 높은 맛집 관리 서비스를 제공하는 것을 목표로 합니다.
