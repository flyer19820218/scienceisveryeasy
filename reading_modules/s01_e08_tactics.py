# 檔案位置：reading_modules/s01_e08_tactics.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第八集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：反應速率與「小球戰術」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第8集_反應速率與小球戰術.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>八局上半，面對擁有超高全壘打牆（<b>高活化能</b>）的球場，教練團決定改變進攻策略，利用三大戰術來加快得分的反應速率！</p>

<p><b>⚾ 戰術一：擴大接觸面積（機關槍打線）</b><br>
將巨大木頭劈成火媒棒、把胃藥錠咬碎吞下、或是把紙錢揉皺再燒，都是為了「<b>增加與另一半的接觸面積</b>」，這會讓反應速率瞬間暴增！</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>裁判紅牌警告：數學與化學的聯合陷阱！</b><br>
如果把一個正方體的每邊切成 9 等份，雖然會切出 729 塊小積木，但總表面積只會變成原來的「<b>9 倍</b>」，絕對不是 729 倍！千萬別被巨大的數字給騙了！
</div>

<p><b>⚾ 戰術二：提升濃度與壓力（塞滿壘包）</b><br>
當場上跑者的「<b>濃度</b>」極度密集（氣體則是看「<b>壓力</b>」），任何一個滾地球都能造成守備方極大的壓力，瞬間增加分子間的碰撞機會，反應速率絕對跟著飆升！</p>

<p><b>⚾ 戰術三：大聯盟超級教練（催化劑）</b><br>
面對難以跨越的活化能，超級教練親自下達觸擊與盜壘的「小球戰術」！這在化學上等於是<b>改變了反應途徑、直接降低活化能門檻</b>。教練有四大特性：<br>
1. <b>專一性</b>：只教特定的戰術（例如哈柏法製氨只能用鐵粉）。<br>
2. <b>全身而退</b>：指導結束後，教練的「<b>質量與化學性質完全不變</b>」，可重複使用！<br>
3. <b>極微量</b>：只需要一點點就能發揮神效。<br>
4. <b>雙向功能</b>：大聯盟也有專門減緩比賽節奏的「<b>負催化劑</b>」（例如在雙氧水中加入甘油，能減緩分解速度）。</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據球探機密報告，關於「改變反應速率」的戰術，下列哪一個說法是正確的？",
        [
            "(A) 把正方體木塊每邊切成 9 等份，接觸面積會暴增為原來的 729 倍。", 
            "(B) 催化劑（超級教練）在比賽結束後，他的質量與化學性質會發生改變。", 
            "(C) 濃度越高，代表場上跑者越密集，碰撞機會增加，反應速率也會跟著變快。", 
            "(D) 所有的催化劑都能加快反應速率，化學界絕對沒有用來減慢速度的催化劑。"
        ],
        index=None,
        key="reading_q8"
    )

    if q1 == "(C) 濃度越高，代表場上跑者越密集，碰撞機會增加，反應速率也會跟著變快。":
        st.success("✅ 戰術分析完美！濃度越高、碰撞越密集，得分速度就越快！賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 嗶嗶！你踩中陷阱啦！趕快回去複習機密報告裡面的紅色警告與教練特性！")
        return False
        
    return False
