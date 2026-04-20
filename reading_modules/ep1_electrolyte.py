# 檔案位置：reading_modules/ep1_electrolyte.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第一集閱讀素養，過關回傳 True"""
    
    st.markdown("### 📖 課前戰術板：超級新秀「電解質」")
    st.info("🎧 點擊播放，聽曉臻助教教你怎麼畫重點！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/曉臻解說_電解質.mp3") 

    # ✨ 升級版：加上高質感的卡片背景、大字體與明顯的行距
    st.markdown("""
    <div style="background-color: #f8fafc; padding: 30px; border-radius: 12px; border: 1px solid #e2e8f0; font-size: 22px; line-height: 1.8; color: #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
        在化學大聯盟裡，要被稱為<b>電解質</b>，必須滿足兩個嚴格的條件：<br><br>
        1. <span style='color: #E65100; font-weight: bold; font-size: 24px;'>必須能溶於水</span><br>
        2. <span style='color: #E65100; font-weight: bold; font-size: 24px;'>其水溶液必須能夠導電</span><br><br>
        <div style="background-color: #fffbeb; padding: 15px 20px; border-left: 6px solid #f59e0b; margin: 20px 0; border-radius: 4px; font-size: 20px;">
            🔍 <b>曉臻提醒陷阱：</b><br>銅線跟鐵絲雖然能導電，但他們不能溶於水，所以金屬絕對不是電解質！
        </div>
        <b>強大陣容：</b> 在大聯盟裡，<b>「酸、鹼、鹽」</b>三大家族是頂尖電解質。而且，溶液中正、負離子的總電量絕對會相等，維持<b>「電中性」</b>。
    </div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 戰術板隨堂測驗")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 必須答對這題，才能解鎖下方的【賽事挑戰系統】喔！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據文章，下列哪一個家族 **不屬於** 電解質大軍？",
        ["(A) 酸類家族", "(B) 鹽類家族", "(C) 酒精與糖水家族", "(D) 鹼類家族"],
        index=None,
        key="reading_q1"
    )

    if q1 == "(C) 酒精與糖水家族":
        st.success("✅ 答對了！糖水和酒精是頑固的非電解質。戰術板解鎖成功！")
        return True 
    elif q1 is not None:
        st.error("❌ 找錯人了喔，再看一下文章的陷阱區！")
        return False
        
    return False
