# 檔案位置：reading_modules/s01_e04_molarity_ph.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第四集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：數據勝於一切——揭開『火力密度』與『戰況計分板』的祕密")
    st.info("🎧 點擊播放，聽聽曉臻球評為您分析進階數據的奪冠關鍵！")
    
    # 為了防止複製貼上時漏掉引號產生 Bug，這裡改用最安全的單行字串連接法
    html_content_1 = (
        "<div style='background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);'>"
        "<p>【特約記者 彥君／分析室報導】在現代棒球中，勝負往往不再只靠熱血，精準的數據分析才是王道。今天本報獲准進入化學大聯盟最神祕的「進階數據分析室」，為各位球迷拆解兩個決定奪冠機率的魔王級指標：<b>體積莫耳濃度 (M)</b> 與 <b>pH 值</b>。</p>"
        "<p><b>⚾ 數據一：火力密度 (Molarity)</b><br>"
        "如何衡量一支打線的「破壞密集度」？分析師們使用體積莫耳濃度（代號大寫 M）來運算。公式很簡單：將球員的總數量（莫耳數）除以球場的大小（體積）。<br>"
        "這就像是<b>「珍珠奶茶」的黃金比例</b>：如果將 50 顆珍珠裝在 1 公升的巨型杯裡，口感可能剛好；但如果把同樣數量的珍珠硬塞進僅有 100 毫升的小杯子中，整杯就會變成「珍珠森林」，密度瞬間飆升。這就是為什麼球員數不變，球場縮小，火力（濃度）卻會變強的原因。</p>"
        "<div style='background-color: #fff1f2; padding: 15px; border-left: 5px solid #e11d48; margin: 15px 0; border-radius: 4px; font-size: 18px;'>"
        "🚨 <b>數據中心警告：致命的單位紅牌</b><br>"
        "分析師強調，計算 M 濃度時，球場大小（體積）<b>絕對、必須、只能使用「公升 (L)」</b>作為單位。如果球探報告給的是「毫升 (mL)」，必須立刻除以 1000 進行校正，否則數據出錯，球隊將面臨慘烈的三振。"
        "</div>"
        "<p><b>⚾ 數據二：終極計分板 (pH Scale)</b><br>"
        "當比賽進行時，觀眾席最關心的就是 <b>pH 計分板</b>。這是一套衡量「酸球隊」與「鹼性部隊」誰佔優勢的系統：<br>"
        "🔸 <b>平手僵局 (pH = 7)</b>：雙方人數平手，呈現中性（如純水）。<br>"
        "🔸 <b>酸性領先 (pH &lt; 7)</b>：這是一個具有「反向衝擊」的計分系統——<b>戰力越強（越酸），計分板上的數字反而越小</b>！例如兇猛的胃酸新秀，pH 值僅有 1 到 2。<br>"
        "🔸 <b>鹼性壓制 (pH &gt; 7)</b>：數字越大代表鹼性越強，就像漂白水能打出 pH 超過 11 的驚人數據。</p>"
        "</div>"
    )
    st.markdown(html_content_1, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：原生 Streamlit 珍珠奶茶模擬器
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧋 戰術模擬中心：珍珠奶茶火力密度 (M)")
    st.markdown("<span style='color: #64748b; font-size: 16px;'>*(請調整下方滑桿，看看珍珠數量與杯子大小如何影響最終的濃度！)*</span>", unsafe_allow_html=True)
    
    # === 新增：漂亮的 LaTeX 公式 ===
    st.latex(r"[\text{珍珠}] = \frac{\text{珍珠莫耳數 } (n)}{\text{公升 } (L)}")
    st.write("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        moles = st.slider("🧋 珍珠數量 / 莫耳數 (n)：", min_value=1.0, max_value=50.0, value=10.0, step=1.0)
    with col2:
        vol = st.slider("🥤 杯子大小 / 公升 (L)：", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
        
    molarity = moles / vol
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("莫耳數 (n)", f"{moles} 莫耳")
    with m2:
        st.metric("體積 (V)", f"{vol:.1f} 公升")
    with m3:
        if molarity > 100:
            st.metric("🔥 火力密度 (M)", f"{molarity:.1f} M", delta="火力徹底爆表！", delta_color="normal")
        elif molarity < 10:
            st.metric("💧 火力密度 (M)", f"{molarity:.1f} M", delta="水水的很淡~", delta_color="inverse")
        else:
            st.metric("⚡ 火力密度 (M)", f"{molarity:.1f} M", delta="完美比例！", delta_color="off")
            
    if vol == 0.1:
        st.error("🚨 警告！你把珍珠全擠在 100 毫升 (0.1 公升) 的小杯子裡了，整杯都是料吸不起來啦！這就是體積變小、濃度飆高的原理！")

    html_content_2 = (
        "<div style='background-color: #f0fdf4; padding: 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 19px; line-height: 1.8; margin-top: 20px;'>"
        "🛡️ <b>防守大戰：稀釋的物理極限</b><br>"
        "專欄最後，記者也採訪了防守教練。對於「能否透過加水稀釋讓酸球隊變成鹼性部隊」的疑問，教練給出了斬釘截鐵的回答：<b>絕對不可能！</b>即便瘋狂稀釋檸檬汁，其 pH 值只會不斷變大並趨近於中性的 7，但永遠無法跨越那道紅線變成大於 7 的鹼性。這就是化學大聯盟最頑強的物理邊界。"
        "</div>"
    )
    st.markdown(html_content_2, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據記者的專欄報導，曉臻球探把一杯 pH = 3 的檸檬汁「瘋狂加水」不斷稀釋後，其戰況計分板（pH值）的最終變化為何？",
        [
            "(A) 一路飆升，最後變成 pH = 9 的鹼性部隊", 
            "(B) 數字會隨稀釋變大，但最終僅會無限靠近 7 而無法超越", 
            "(C) 戰力會越來越集中，數字一路掉到谷底的 1", 
            "(D) 稀釋不影響數據，pH 值會永遠維持 3 不變"
        ],
        index=None,
        key="reading_q4"
    )

    if q1 == "(B) 數字會隨稀釋變大，但最終僅會無限靠近 7 而無法超越":
        st.success("✅ 採訪成功！你已經掌握了進階數據的物理極限，正式解鎖賽事挑戰！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者搖頭：數據分析出錯囉！趕快回去複習最後一段『防守大戰』！")
        return False
        
    return False
