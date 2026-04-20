# 檔案位置：reading_modules/ep2_acid_team.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第二集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：火力全開的腐蝕性打線——酸球隊深度剖析")
    st.info("🎧 點擊播放，聽聽曉臻球評為您帶來的賽前分析！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/曉臻解說_酸球隊.mp3") 

    # ✨ 記者專欄版：HTML 標籤全部靠最左邊，文字具備起承轉合
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】隨著比賽進入二局上半，全聯盟防守方的噩夢——「<b>酸球隊</b>」正式踏上打擊區。這支球隊不以細膩技巧著稱，他們靠的是足以溶解金屬的霸道火力與火爆脾氣。記者在休息區觀察發現，這群球員大多具有強烈的腐蝕性，球團也多次警告：在化學球場上，絕對禁止用舌頭去嚐這些職業球員，否則下場會非常慘烈。</p>

<p><b>⚾ 致命的氫離子直球</b><br>
酸球隊的核心戰術非常明確，只要球員一溶於水，就會立刻釋放他們的招牌武器「<b>氫離子 (H<sup>+</sup>)</b>」。當這顆直球高速撞上活性金屬組成的防守陣容時，會引發極度劇烈的反應——金屬會被逐漸侵蝕溶解，並伴隨著大量噴發的「<b>氫氣 (H<sub>2</sub>)</b>」全壘打，這往往能瞬間瓦解對方的防線。</p>

<div style="background-color: #fff7ed; padding: 15px; border-left: 5px solid #f97316; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🔍 <b>場邊筆記：防守方的心理陷阱</b><br>
資深球評曉臻特別提醒，這場比賽存在一個關鍵陷阱：當酸球隊遇到由「<b>碳酸鈣</b>」構成的防守球員（如大理石或是貝殼）時，他們產生的氣體與金屬完全不同，而是「<b>二氧化碳 (CO<sub>2</sub>)</b>」。若防守方搞錯氣體種類，將會面臨嚴重的防守失誤。
</div>

<p><b>⚾ 三大強酸先發投手陣容</b><br>
本季酸球隊排出了極具威脅性的先發名單：<br>
1. <b>硫酸 (H<sub>2</sub>SO<sub>4</sub>)</b>：人稱「工業之母」，擅長脫水戰術，曾將整盤白糖瞬間化為焦黑碳柱。稀釋時必須嚴格執行「<b>酸加進水</b>」的動作，若操作錯誤會導致強酸沸騰濺射。<br>
2. <b>鹽酸 (HCl)</b>：這是一位脾氣直接的球員，本體是氯化氫氣體溶於水。雖然常用於清潔，但教練團嚴禁將其與「漂白水」共同訓練，否則會釋放出劇毒的「<b>氯氣</b>」。<br>
3. <b>硝酸 (HNO<sub>3</sub>)</b>：見不得光的刺客，必須待在<b>深褐色瓶子</b>中避光，否則會分解出有毒的二氧化氮。當他與鹽酸以 1:3 的黃金比例組成「王水」時，連黃金都能被他吞噬。</p>

<p><b>⚾ 板凳上的弱酸老將</b><br>
相比強酸投手的霸道，板凳席上的<b>醋酸 (CH<sub>3</sub>COOH)</b> 則溫和許多。雖然高純度的「冰醋酸」在寒冷的 17°C 就會結冰，但他在日常生活中通常以稀釋過的「食用醋」身份現身。儘管如此，他依然是酸球隊中不可或缺的救援戰力。</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據報導內容，當酸球隊的球員遇到含有「碳酸鈣」成分的防守員時，會轟出哪一種氣體的全壘打？",
        ["(A) 劇毒的氯氣", "(B) 助燃的氧氣", "(C) 可怕的氫氣", "(D) 二氧化碳"],
        index=None,
        key="reading_q2"
    )

    if q1 == "(D) 二氧化碳":
        st.success("✅ 採訪成功！你已經掌握了酸球隊的關鍵數據，正式解鎖賽事挑戰！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者搖頭：這個數據記錯了喔，快回去看『場邊筆記』！")
        return False
        
    return False
