
│
├── Home.py                          ← 첫 화면
├── pages/
│   ├── 2_개인정보_유출_예방_교육.py       ← 2페이지
│   ├── 3_보안_상식_퀴즈.py               ← 3페이지
│   ├── 4_비밀번호_강도_테스트.py         ← 4페이지
│   └── 5_개인정보_위험도_자가진단.py     ← 5페이지
import streamlit as st

st.set_page_config(page_title="정보보안 체험 앱", layout="centered")

st.title("🔐 정보보안 체험 통합 앱")
st.markdown("""
이 앱은 다음과 같은 체험으로 구성되어 있어요:

1. 개인정보 유출 예방 교육  
2. 보안 상식 퀴즈  
3. 비밀번호 강도 테스트  
4. 개인정보 위험도 자가진단  

👉 왼쪽 상단 메뉴에서 원하는 체험을 선택하세요!
""")
import streamlit as st

st.title("📢 개인정보 유출 예방 교육")

st.markdown("""
### 💡 개인정보란?
이름, 생년월일, 주민등록번호, 주소, 전화번호 등 개인을 식별할 수 있는 정보예요.

---

### 🔒 유출 사례
- 피싱 사이트를 통한 계정 탈취
- SNS에 올린 정보로 인한 사칭

---

### ✅ 예방법
1. 의심스러운 링크 클릭하지 않기  
2. 비밀번호 주기적으로 변경하기  
3. 2단계 인증 설정하기  
""")
import streamlit as st

st.title("🧠 보안 상식 퀴즈")

questions = [
    {
        "question": "비밀번호는 생일과 같은 정보를 포함해도 된다.",
        "options": ["O", "X"],
        "answer": "X"
    },
    {
        "question": "공공 와이파이에서는 금융 거래를 해도 안전하다.",
        "options": ["O", "X"],
        "answer": "X"
    },
    {
        "question": "2단계 인증은 계정 보안에 도움이 된다.",
        "options": ["O", "X"],
        "answer": "O"
    }
]

score = 0

for i, q in enumerate(questions):
    user_answer = st.radio(q["question"], q["options"], key=i)
    if user_answer == q["answer"]:
        score += 1

st.subheader(f"당신의 점수: {score} / {len(questions)}")
import streamlit as st
import re

st.title("🛡️ 비밀번호 강도 테스트")

password = st.text_input("비밀번호를 입력하세요", type="password")

def evaluate_password(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"[0-9]", pw):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
        score += 1
    return score

if password:
    score = evaluate_password(password)
    st.subheader(f"비밀번호 강도 점수: {score} / 5")
    if score <= 2:
        st.error("⚠️ 보안에 매우 취약한 비밀번호입니다.")
    elif score == 3:
        st.warning("🔒 보통 수준의 비밀번호입니다.")
    else:
        st.success("✅ 강력한 비밀번호입니다.")
import streamlit as st

st.title("📋 개인정보 위험도 자가진단")

questions = {
    "SNS에 생년월일을 공개하고 있다": False,
    "같은 비밀번호를 여러 사이트에 사용한다": False,
    "공공 와이파이를 자주 사용한다": False,
    "이메일에 도착한 링크를 바로 누른 적이 있다": False,
    "2단계 인증을 사용하지 않는다": False,
}

risk_score = 0

for q in questions:
    answer = st.checkbox(q)
    if answer:
        risk_score += 1

st.subheader(f"위험 항목 선택 개수: {risk_score}개")

if risk_score == 0:
    st.success("🎉 아주 잘 관리되고 있어요!")
elif risk_score <= 2:
    st.warning("⚠️ 약간의 개선이 필요해요.")
else:
    st.error("🚨 개인정보 보호에 주의가 필요해요!")
