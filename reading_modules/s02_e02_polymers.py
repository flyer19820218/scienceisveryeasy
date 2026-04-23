import streamlit as st

def render_reading_and_quiz():
    st.markdown("### 📜 黎明韓流 S02E02 機密任務：戰袍的殘酷洗禮")
    st.info("💡 **舞台導師韓流**：『一件頂級的純羊毛戰袍如果洗錯了，上台就會變成縮水的童裝！連洗衣服都不懂，怎麼當偶像？』")
    
    st.write("請回答導師的隨堂抽考，證明你具備保護戰袍的知識：")
    
    st.markdown("#### 🔍 賽前資格測驗")
    q1 = st.radio(
        "如果練習生拿到了一件昂貴的『純羊毛』與『蠶絲』訂製戰袍（動物纖維），請問在清洗時，絕對**不能**使用下列哪一種洗劑？",
        [
            "A. 弱酸性的洗潔劑",
            "B. 中性的洗潔劑",
            "C. 清水直接沖洗",
            "D. 強效的鹼性肥皂"
        ],
        index=None
    )
    
    if st.button("🛡️ 提交洗衣策略", use_container_width=True):
        if q1 is None:
            st.warning("請先選擇一個答案！")
        elif q1.startswith("D"):
            st.success("✅ 策略正確！動物纖維的成分是『蛋白質』，蛋白質最怕強鹼，用強鹼肥皂洗會直接報銷！準備進入正式挑戰！")
            return True
        else:
            st.error("❌ 戰袍毀損！動物纖維是由蛋白質組成，請思考蛋白質最怕什麼酸鹼性？")
            
    return False
