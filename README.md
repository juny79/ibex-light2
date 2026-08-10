# IBEX Light2 - 생산 교육 및 재고 관리 시스템

> (주)아이벡스메디칼시스템즈 IBEX Light2 고압산소챔버 공장 신입직원 교육 및 재고 관리 웹 애플리케이션

## 📋 개요

IBEX Light2는 1인용 고압산소챔버(Monoplace Hyperbaric Oxygen Chamber)입니다.  
이 웹 애플리케이션은 공장에서 해당 제품을 생산하는 과정을 신입직원에게 교육하고,  
5가지 핵심 구성 요소의 재고를 관리하기 위한 목적으로 만들어졌습니다.

## 🏗️ 5가지 구성 요소

| # | 구성 요소 | 설명 |
|---|---------|------|
| 1 | **하단 프레임** (Bottom Frame) | 제품의 기초 골격, 내구성과 안정성 확보 |
| 2 | **앞기판** (Front Panel) | 환자 진입부, 시야 확보용 투명창, 기밀 씰링 |
| 3 | **뒷기판** (Back Panel) | 배관 연결부, 산소 공급 밸브, 압력 릴리프 밸브 |
| 4 | **챔버** (Chamber) | 투명 아크릴 실린더 본체, 2ATA 내압 설계 |
| 5 | **컨트롤도어** (Control Door) | 반투명 슬라이딩 도어, 디지털 컨트롤 패널 |

## ✨ 주요 기능

### 📚 생산 교육
- 5가지 구성 요소 시각화 및 상세 설명
- 분해도(Exploded View) 인터랙티브 다이어그램
- 7단계 생산 공정 타임라인 (애니메이션)
- 이해도 퀴즈 (5문항)

### 📦 재고 관리
- 실시간 재고 현황 대시보드
- 부품별 재고 카드 (상태 표시: 🟢정상/🟡주의/🔴부족)
- 입고/출고 처리 폼
- 트랜잭션 로그 테이블
- CSV 내보내기
- LocalStorage 기반 데이터 영속 저장

## 🎨 디자인 특징
- 다크 네이비 프리미엄 테마
- 글라스모피즘 카드 효과
- 스크롤 애니메이션 (Intersection Observer)
- 완전 반응형 설계 (모바일/태블릿/데스크탑)
- Google Fonts (Inter + Noto Sans KR)

## 🚀 실행 방법

별도 빌드 없이 `index.html`을 브라우저에서 열면 바로 사용 가능합니다.

```
# 로컬 서버로 실행 (선택사항)
npx serve .
```

## 📁 프로젝트 구조

```
ibex-light2-training/
├── index.html          # 메인 애플리케이션 (HTML + JS)
├── styles.css          # 프리미엄 CSS 스타일시트
├── README.md           # 프로젝트 설명서
└── images/
    ├── hero_banner.jpg     # 히어로 배너 이미지
    ├── exploded_view.jpg   # 제품 분해도
    ├── bottom_frame.jpg    # 하단 프레임
    ├── front_panel.jpg     # 앞기판
    ├── back_panel.jpg      # 뒷기판
    ├── chamber_body.jpg    # 챔버
    └── control_door.jpg    # 컨트롤도어
```

## 🔗 참조

- [IBEX Light2 제품 페이지](https://ibex.co.kr/kr/product/mono/ibex-light/)
- [아이벡스메디칼시스템즈 공식 사이트](https://ibex.co.kr)

## 📄 라이선스

© 2026 (주)아이벡스메디칼시스템즈. All rights reserved.
