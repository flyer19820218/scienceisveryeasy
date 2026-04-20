# 檔案位置：reading_modules/s01_e04_molarity_ph.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第四集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：進階數據「濃度與 pH 計分板」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第4集_胃酸全壘打_究極完全體.mp3") 

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>歡迎來到大聯盟最機密的「進階數據分析室」！今天我們要公開兩個決定勝負的終極指標，這可是讓許多球員吃盡苦頭的大魔王！</p>

<p><b>⚾ 火力密集度：體積莫耳濃度 (M)</b><br>
要計算球隊的火力密集度，就是把「球員總數量（溶質莫耳數）」除以「球場大小（溶液體積）」。<br>
想像一下<b>阿嬤養的珍珠奶茶</b>：50 顆珍珠裝在 1 公升的胖胖杯裡剛剛好；但如果硬擠在 100 毫升的小杯子裡，整口都是珍珠！數量沒變，但空間變小，濃度就會瞬間飆高！</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>裁判紅牌警告：體積單位的陷阱！</b><br>
計算大寫 M 濃度時，體積的單位<b>絕對、必須、只能使用「公升 (L)」</b>！如果題目給的是「毫升 (mL)」，第一步就是立刻除以 1000 換算成公升，否則會直接被三振出局！
</div>

<p><b>⚾ 春訓報到守則：精準泡製藥水</b><br>
要泡製特定濃度的水溶液，<b>絕對不能先加滿水再倒粉</b>！因為溶質加進去也會佔據空間（就像人跳進裝滿水的浴缸會溢出來）。正確流程是：<b>先加少量的水，讓粉末完全攪拌溶解，最後再慢慢加水，直到剛好對齊指定的刻度線</b>！</p>

<p><b>⚾ 終極計分板：pH 值</b><br>
當球場上同時有酸球隊（H<sup>+</sup>）和鹼性部隊（OH<sup>-</sup>）時，誰的人數多，那裡就是誰的主場！而顯示戰況的計分板就叫 <b>pH 值</b>：<br>
🔸 <b>平手（中性）</b>：計分板顯示幸運數字 <b>7</b>（例如純水）。<br>
🔸 <b>酸性主場</b>：數字<b>小於 7</b>。注意強烈反差！<b>酸性越強，數字反而越小</b>（例如胃酸 pH 值低到只有 1~2）。<br>
🔸 <b>鹼性主場</b>：數字<b>大於 7</b>。數字越大，鹼性越強（例如漂白水超過 11）。</p>

<div style="background-color: #f0fdf4; padding: 12px 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🛡️ <b>防守秘訣：稀釋的極限</b><br>
如果把檸檬汁（pH=3）瘋狂加水稀釋，它的酸性會變弱，pH 數值會變大並慢慢靠近 7，但<b>絕對不可能跨越 7 變成鹼性</b>！加水的極限，就是無限接近中性平手！
</div>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 曉臻球探把一杯 pH = 3 的檸檬汁「瘋狂加水」不斷稀釋，請問這杯檸檬汁最後的 pH 值變化會是如何？",
        [
            "(A) 一路飆升，最後變成 pH = 9 的鹼性", 
            "(B) 數字會無限靠近 7，但絕對不會超過 7", 
            "(C) 數字會越來越小，最後變成 1", 
            "(D) 只要加水，pH 值就會永遠維持 3 不變"
        ],
        index=None,
        key="reading_q4"
    )

    if q1 == "(B) 數字會無限靠近 7，但絕對不會超過 7":
        st.success("✅ 判斷精準！酸球隊就算被加水稀釋到極限，也只能回到中性平手（7），絕對不會變成鹼性。賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 揮棒落空！趕快回去看最後一個綠色框框的「防守秘訣」！")
        return False
        
    return False
