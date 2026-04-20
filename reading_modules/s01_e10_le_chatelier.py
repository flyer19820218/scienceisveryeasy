# 檔案位置：reading_modules/s01_e10_le_chatelier.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render_reading_and_quiz():
    """渲染第十集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：總冠軍賽的巔峰對決——總裁的破壞平衡試煉")
    st.info("🎧 點擊播放，聽聽曉臻球評為您轉播這場決定總冠軍的終極戰役！")
    
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】十局下半，總冠軍賽進入白熱化！大聯盟總裁「<b>勒沙特列</b>」親自進場干預比賽！他的最高執法原則只有一個：<b>「你給我什麼，我就消耗什麼；你拿走什麼，我就補什麼！」</b> 整個化學系統會自動往「抵消變化」的方向移動！</p>

<p><b>⚾ 總裁第一招：濃度試煉</b><br>
如果總裁在左邊的休息室強行塞入 50 名新球員（增加反應物濃度），為了舒緩擁擠的壓力，球員自然會往寬敞的球場上跑，這時平衡就會「<b>向右移動</b>」。<br>
但記者要特別提醒！如果你加入的是「<b>純固體</b>」（例如大理石 CaCO<sub>3</sub>）或「純液體」，它們就像是球場的板凳或硬體設備，其「濃度」是固定不變的！<b>加入固體絕對不會改變球員的碰撞機率，也絕對無法破壞平衡！</b></p>

<p><b>⚾ 總裁第二招：溫度與極端氣候試煉</b><br>
當球場氣溫狂飆，正、逆反應的速率「<b>絕對會同時變快</b>」！但這是一場極度不公平的賽跑，關鍵就在於球場的牆有多高：<br>
🔸 <b>放熱反應（2公尺矮牆）</b>：因為牆很低，常溫下已經有高比例的球員能跨過。氣溫上升後，成長的「倍數」其實非常小。<br>
🔸 <b>吸熱反應（10公尺高牆）</b>：牆太高了，常溫下只有極少數的菁英能跨過。一旦氣溫飆升，全體體能拉高，過關比例會呈現驚人的「<b>暴倍數成長</b>」！<br>
因此，<b>溫度一旦上升，吸熱方向增加的「比例倍數」會遠遠輾壓放熱方向，平衡絕對會強力朝著「吸熱反應」移動！</b></p>
</div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：Plotly 動態圖表
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧪 戰術模擬中心：全體球員體能分佈曲線")
    st.markdown("<span style='color: #64748b; font-size: 16px;'>*(請拉動氣溫滑桿，親眼觀察右側「高牆區」的紅色面積是如何暴增的！)*</span>", unsafe_allow_html=True)
    
    temp_boost = st.slider("🌡️ 請調整「球場氣溫上升幅度」：", min_value=0, max_value=100, value=0, step=10, format="+%d°C")
    
    # 數學模型計算
    x = np.linspace(0.1, 15, 500)
    E_low = 3.0
    E_high = 10.0
    T_base = 1.0
    T_current = 1.0 + (temp_boost / 50.0)
    
    y_base = np.sqrt(x) * np.exp(-x / T_base)
    y_current = np.sqrt(x) * np.exp(-x / T_current)
    
    area_base_total = np.sum(y_base)
    area_current_total = np.sum(y_current)
    
    base_low_pct = np.sum(y_base[x >= E_low]) / area_base_total * 100
    base_high_pct = np.sum(y_base[x >= E_high]) / area_base_total * 100
    if base_high_pct < 0.01: base_high_pct = 0.01
        
    current_low_pct = np.sum(y_current[x >= E_low]) / area_current_total * 100
    current_high_pct = np.sum(y_current[x >= E_high]) / area_current_total * 100
    
    mult_low = current_low_pct / base_low_pct
    mult_high = current_high_pct / base_high_pct

    # 建立 Plotly 動態圖表
    fig = go.Figure()

    # 畫主曲線
    fig.add_trace(go.Scatter(x=x, y=y_current, mode='lines', name='全體球員體能分佈', line=dict(color='#334155', width=3)))

    # 填滿 2m 矮牆區域 (淺藍色)
    x_low = x[x >= E_low]
    y_low = y_current[x >= E_low]
    fig.add_trace(go.Scatter(x=x_low, y=y_low, fill='tozeroy', mode='none', fillcolor='rgba(147, 197, 253, 0.5)', name='跨過 2m 矮牆 (放熱)'))

    # 填滿 10m 高牆區域 (紅色)
    x_high = x[x >= E_high]
    y_high = y_current[x >= E_high]
    fig.add_trace(go.Scatter(x=x_high, y=y_high, fill='tozeroy', mode='none', fillcolor='rgba(225, 29, 72, 0.8)', name='跨過 10m 高牆 (吸熱)'))

    # 加上高矮牆垂直虛線
    fig.add_vline(x=E_low, line_dash="dash", line_color="#3b82f6", annotation_text="2m 矮牆", annotation_position="top right")
    fig.add_vline(x=E_high, line_dash="dash", line_color="#be123c", annotation_text="10m 高牆", annotation_position="top right")

    # 圖表設定
    fig.update_layout(
        title=f"球員體能分佈曲線 (氣溫 +{temp_boost}°C)",
        xaxis_title="分子動能 (體能)",
        yaxis_title="分子數量 (人數比例)",
        yaxis_range=[0, 0.45],
        margin=dict(l=20, r=20, t=50, b=20),
        plot_bgcolor='rgba(0,0,0,0)', # 透明背景
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    # 輸出圖表
    st.plotly_chart(fig, use_container_width=True)

    # 數據儀表板
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="⬇️ 放熱 (矮牆) 成功率", value=f"{current_low_pct:.1f}%", delta=f"{mult_low:.1f} 倍成長", delta_color="normal")
    with col2:
        st.metric(label="⬆️ 吸熱 (高牆) 成功率", value=f"{current_high_pct:.1f}%", delta=f"{mult_high:.1f} 倍成長", delta_color="normal")
    with col3:
        if temp_boost == 0:
            st.metric(label="⚖️ 總裁判定：平衡方向", value="維持平衡", delta="正逆倍數相同", delta_color="off")
        else:
            st.metric(label="⚖️ 總裁判定：平衡方向", value="強力向【吸熱】移動", delta="吸熱倍數完全輾壓！", delta_color="normal")

    if temp_boost > 0:
        st.info(f"💡 分析室快報：升溫 {temp_boost}°C 後，吸熱反應（高牆）的紅色面積雖然看起來還是一小塊，但比起一開始的狀態，可是翻了足足 **{mult_high:.1f} 倍**！成長倍數徹底輾壓了放熱反應，因此平衡被打破，朝吸熱方向移動！")

    st.markdown("""
<div style="background-color: #fff1f2; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e11d48; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); margin-top: 20px;">
<p>🚨 <b>大聯盟終極警告：催化劑的大魔王騙局！</b><br>
總裁祭出的最後一個神祕陷阱是引入「<b>催化劑（投球計時器）</b>」！許多新秀以為這能改變比賽勝負。<br>
但請永遠記住：催化劑會<b>同時、且等比例地</b>增加正逆反應的速率！它只能讓比賽「<b>提早打完（縮短達到平衡的時間）</b>」，但「<b>絕對不會</b>」破壞平衡狀態，也「<b>絕對無法</b>」增加最後生成的總產量！看穿這個騙局，你就能抱走化學大聯盟的總冠軍獎盃！</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導並觀察圖表面積變化後，請回答記者提問以領取總冠軍通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據大聯盟總裁的試煉規則，如果我們在一個已經達到平衡的化學反應中加入「催化劑」，會發生什麼事？",
        [
            "(A) 正反應速率會大於逆反應速率，成功破壞平衡讓反應向右移動。", 
            "(B) 催化劑能大幅增加反應的效率，所以最後生成的總產量會變多。", 
            "(C) 催化劑只能縮短達到平衡的時間，絕對不會破壞平衡，也無法增加總產量。", 
            "(D) 催化劑會像固體一樣，對反應速率與平衡狀態完全沒有任何影響。"
        ],
        index=None,
        key="reading_q10"
    )

    if q1 == "(C) 催化劑只能縮短達到平衡的時間，絕對不會破壞平衡，也無法增加總產量。":
        st.success("🏆 轟！再見滿貫全壘打！你成功識破了催化劑的偽裝，恭喜贏得化學大聯盟總冠軍！賽事大門為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者驚呼：你被總裁的陷阱騙到了！趕快回去看紅色警告框裡面的催化劑騙局！")
        return False
        
    return False
