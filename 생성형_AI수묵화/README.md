# 🎨 AI 수묵화 웹 애플리케이션
> **Stable Diffusion 기반 수묵화 생성 + Flask 웹 구현 프로젝트**  
> 텍스트 입력을 기반으로 AI가 전통 수묵화를 생성하고, 회원 관리 및 커뮤니티 기능까지 지원하는 웹서비스입니다.  
> (벤처스타트업 아카데미 K프로젝트, 2023)

---

## 📌 프로젝트 개요
- **목표**: 전통 예술(수묵화)에 AI를 접목하여 새로운 디지털 창작 경험 제공
- **기간**: 2023.07 ~ 2023.08
- **성과**: 회원 관리 / 이미지 생성 / 커뮤니티 게시판 기능까지 포함된 웹 애플리케이션 구현
- **역할 분담**: 4인 팀 프로젝트, 저는 데이터 처리 및 Flask 기반 웹 구현에 주도적으로 참여

---

## 🛠️ 기술 스택
- **AI 모델**: Stable Diffusion (`diffusers` 라이브러리 활용)
- **Backend**: Flask, Flask-SQLAlchemy
- **DB**: PostgreSQL
- **Frontend**: HTML, CSS, Jinja2

---

## 🧩 주요 기능
| 기능 | 설명 | 기술 |
|------|------|------|
| 회원 관리 | 회원가입, 로그인, 비밀번호 찾기 | Flask, PostgreSQL, bcrypt |
| 수묵화 생성 | 프롬프트 기반 Stable Diffusion 그림 생성 | HuggingFace diffusers |
| 커뮤니티 | 생성된 그림 공유, 댓글/피드백 기능 | Flask-SQLAlchemy, Jinja2 |
| UI | 직관적이고 간단한 인터페이스 제공 | HTML, CSS, Jinja2 |

---

## 📂 프로젝트 구조
```
생성형_AI수묵화/
├─ static/ # 정적 파일 (CSS, JS)
├─ templates/ # HTML 템플릿
├─ image/ # 생성 이미지 저장
├─ 수묵화_코드.ipynb # Stable Diffusion 모델 테스트 및 코드 정리
├─ 발표.pdf # 프로젝트 발표 자료
├─ 시연영상.mp4 # 웹 서비스 시연 영상
├─ 포스터.pdf # 포스터 (요약본)
└─ README.md # 프로젝트 설명 (현재 문서)
```
