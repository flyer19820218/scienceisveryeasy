# 檔案位置：reading_modules/s01_e08_tactics.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第八集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：突破僵局的機關槍打線與小球戰術")
    st.info("🎧 點擊播放，聽聽曉臻球評為您解析這場高智商的戰術對決！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第8集_反應速率與小球戰術.mp3") 

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】八局上半，主場球隊祭出了極端防守，將全壘打牆（<b>活化能</b>）修築得無比高聳。面對打線全面熄火的僵局，進攻方的教練團果斷改變策略，連續發動三大戰術來催出得分的「<b>反應速率</b>」！</p>

<p><b>⚾ 戰術一：機關槍打線（擴大接觸面積）</b><br>
教練團放棄了單靠第四棒揮大棒的策略，改為棒棒都能上壘的機關槍打線。在化學上，這就像是把一根巨大的木頭劈成無數根細小的火媒棒，或是將胃藥錠咬碎吞下、把紙錢揉皺再丟入金爐。這些動作都是為了「<b>大幅增加與另一半的接觸面積</b>」，讓反應速率瞬間暴增！</p>

<div style="background-color: #fff1f2; padding: 15px; border-left: 5px solid #e11d48; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>數據中心警告：數學與化學的聯合陷阱！</b><br>
許多球探在計算接觸面積時常犯下致命錯誤：如果把一個正方體的每邊切成 9 等份，雖然會切出驚人的 729 塊小積木，但它的「總表面積」只會變成原來的「<b> 9 倍</b>」，絕對不是 729 倍！千萬別被龐大的切塊數量給騙了！
</div>
</div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：Streamlit 原生滑桿與數據儀表板
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧪 戰術模擬中心：立體切割與表面積計算")
    st.markdown("<span style='color: #64748b; font-size: 16px;'>*(請操作下方的切割滑桿，親眼破解「邊長切 n 等份，表面積變 n 倍」的數學魔咒！)*</span>", unsafe_allow_html=True)
    
    # 使用 Streamlit 原生滑桿
    n_cuts = st.slider("🔪 請選擇「每邊切成幾等份」(n)：", min_value=1, max_value=10, value=1, step=1)
    
    # 即時計算化學數據
    total_blocks = n_cuts ** 3
    surface_multiplier = n_cuts
    
    # 建立三個精美的數據面板
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="總方塊數量 (n³)", value=f"{total_blocks} 塊")
    with col2:
        st.metric(label="單一小塊表面積", value=f"1/{n_cuts**2}")
    with col3:
        st.metric(label="🔥 總表面積變為", value=f"{surface_multiplier} 倍", delta="反應速率大飆升！")
        
    # 防呆提示區塊
    if n_cuts == 9:
        st.error("🚨 陷阱警告！注意看上方數據：切成 9 等份時，方塊有高達 729 塊，但總表面積只有 9 倍！千萬別選錯了！")
    elif n_cuts > 1:
        st.info(f"💡 戰術總結：邊長切成 {n_cuts} 等份，總表面積就是 {n_cuts} 倍。切塊數呈「立方」增加，但總表面積僅呈「線性」增加！")
    else:
        st.info("💡 目前是一整塊完整的正方體，請拉動滑桿開始切割！")

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); margin-top: 20px;">
<p><b>⚾ 戰術二：塞滿壘包（提升濃度與壓力）</b><br>
第二招是讓場上跑者的「<b>濃度</b>」變得極度密集（若是氣體球員則看「<b>壓力</b>」）。當壘包被徹底塞滿，任何一個滾地球都能造成守備方極大的壓力，瞬間增加分子間的碰撞機會，得分速率絕對跟著飆升！</p>

<p><b>⚾ 戰術三：超級教練的「小球戰術」（催化劑）</b><br>
面對高聳的活化能巨牆，球隊請出了大聯盟的終極武器：超級教練（<b>催化劑</b>）！他不要求球員硬扛全壘打，而是下達觸擊與盜壘的「小球戰術」。這在化學上等於是<b>改變了反應途徑、直接降低活化能門檻</b>。這位教練具備四大特性：<br>
1. <b>專一性</b>：只指導特定的戰術（如哈柏法製氨只認鐵粉教練）。<br>
2. <b>全身而退</b>：比賽結束後，教練的「<b>質量與化學性質完全不變</b>」，隨時能支援下一場！<br>
3. <b>極微量</b>：只需一點點指導就能發揮神效。<br>
4. <b>雙向功能</b>：大聯盟也有專門減緩比賽節奏的「<b>負催化劑</b>」（例如雙氧水加入甘油，能減緩分解速度）。</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導並完成切割模擬後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據記者的專欄報導與您的模擬操作，關於「改變反應速率」的戰術，下列哪一個說法是正確的？",
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
        st.error("❌ 記者搖頭：嗶嗶！你踩中陷阱啦！趕快回去複習模擬器上面的紅色警告與教練特性！")
        return False
        
    return False
