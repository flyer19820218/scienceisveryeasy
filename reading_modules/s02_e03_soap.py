import streamlit as st

def render_reading_and_quiz():
    st.markdown("### 📜 黎明韓流 S02E03 機密任務：肥皂的暴力美學")
    st.info("💡 **總製作人黎明**：『在皂化反應的過程中，每一個加入的試劑都有其戰略意義。搞錯酒精的用途，你的肥皂就只是一灘廢水。』")
    
    st.write("請破解皂化反應的配方密碼，解鎖本單元的挑戰：")
    
    st.markdown("#### 🔍 賽前資格測驗")
    q1 = st.radio(
        "在製造肥皂的『皂化反應』（油脂 + 氫氧化鈉）中，我們通常會加入『酒精』。請問酒精在這裡扮演的真實角色是什麼？",
        [
            "A. 作為催化劑，加快反應速率",
            "B. 作為助溶劑，讓不互溶的油脂與鹼水均勻混合",
            "C. 作為反應物，直接參與肥皂的化學鍵結",
            "D. 作為香料，讓做出來的肥皂有酒香味"
        ],
        index=None
    )
    
    if st.button("🛡️ 提交配方解析", use_container_width=True):
        if q1 is None:
            st.warning("請先選擇一個答案！")
        elif q1.startswith("B"):
            st.success("✅ 破解成功！酒精是絕佳的助溶劑，能將油與水拉攏在一起反應，絕對不是催化劑！準備進入正式挑戰！")
            return True
        else:
            st.error("❌ 配方調製失敗！請記住，這是一個段考最愛考的超級陷阱，酒精在這裡『不是』催化劑喔！")
            
    return False
