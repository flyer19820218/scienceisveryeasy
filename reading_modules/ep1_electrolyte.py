import streamlit as st

def render_reading_and_quiz():
    """負責渲染第一集閱讀素養與測驗，並回傳是否通過測驗的狀態"""
    
    st.markdown("### 📖 課前戰術板：超級新秀「電解質」")
    st.info("🎧 點擊播放，聽曉臻助教教你怎麼畫重點！")
    # st.audio("audio/曉臻解說_電解質.mp3") 

    st.markdown("""
    在化學大聯盟裡，要被稱為**電解質**，必須滿足兩個嚴格的條件：
    1. <span style='color: #FF4B4B; font-weight: bold;'>必須能溶於水</span>
    2. <span style='color: #FF4B4B; font-weight: bold;'>其水溶液必須能夠導電</span>
    
    > 🔍 **曉臻提醒陷阱：** 銅線跟鐵絲雖然能導電，但他們不能溶於水，所以金屬絕對不是電解質！
    
    **強大陣容：** 在大聯盟裡，**「酸、鹼、鹽」**三大家族是頂尖電解質。而且，溶液中正、負離子的總電量絕對會相等，維持**「電中性」**。
    """, unsafe_allow_html=True)

    st.divider()

    st.subheader("🏆 戰術板隨堂測驗")
    st.write("👉 必須答對這題，才能解鎖下方的【賽事挑戰系統】喔！")
    
    q1 = st.radio(
        "Q1. 根據文章，下列哪一個家族 **不屬於** 電解質大軍？",
        ["(A) 酸類家族", "(B) 鹽類家族", "(C) 酒精與糖水家族", "(D) 鹼類家族"],
        index=None
    )

    # 判斷邏輯：答對了才回傳 True 給主程式
    if q1 == "(C) 酒精與糖水家族":
        st.success("✅ 答對了！糖水和酒精是頑固的非電解質。戰術板解鎖成功！")
        return True 
    elif q1 is not None:
        st.error("❌ 找錯人了喔，再看一下文章的陷阱區！")
        return False
        
    return False
