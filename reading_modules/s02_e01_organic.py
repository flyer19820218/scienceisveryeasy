import streamlit as st

def render_reading_and_quiz():
    st.markdown("### 📜 黎明韓流 S02E01 機密任務：碳基生命的審判")
    st.info("💡 **總製作人黎明**：『不是所有含有碳元素的物質都能被稱為有機物。在這場生存戰中，認錯叛徒的代價就是淘汰。』")
    
    st.write("在正式上台前，請回答總製作人的提問，以獲取挑戰資格：")
    
    st.markdown("#### 🔍 賽前資格測驗")
    q1 = st.radio(
        "請問下列哪一個物質雖然含有碳元素（C），但因為性質偏向無機物，被我們稱為『四大叛徒』之一（屬於無機化合物）？",
        [
            "A. 甲烷 (CH₄) - 天然氣成分",
            "B. 乙醇 (C₂H₅OH) - 消毒酒精",
            "C. 碳酸鈣 (CaCO₃) - 大理石成分",
            "D. 乙酸 (CH₃COOH) - 食用醋"
        ],
        index=None
    )
    
    if st.button("🛡️ 提交審判結果", use_container_width=True):
        if q1 is None:
            st.warning("請先選擇一個答案！")
        elif q1.startswith("C"):
            st.success("✅ 審判通過！碳酸鹽類（如碳酸鈣）、二氧化碳、一氧化碳與氰化物，就是有機物宇宙中的四大叛徒！準備進入正式挑戰！")
            return True
        else:
            st.error("❌ 審判失敗！請回想一下講義中提到的『四大叛徒』包含哪些物質。")
            
    return False
