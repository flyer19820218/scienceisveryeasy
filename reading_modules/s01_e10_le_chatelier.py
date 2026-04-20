# 檔案位置：reading_modules/s01_e10_le_chatelier.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第十集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：總冠軍賽的巔峰對決——總裁的破壞平衡試煉")
    st.info("🎧 點擊播放，聽聽曉臻球評為您轉播這場決定總冠軍的終極戰役！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第10集_破壞平衡的大魔王_完美版.mp3") 

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】十局下半，總冠軍賽進入白熱化！大聯盟總裁「<b>勒沙特列</b>」親自進場干預比賽！他的最高執法原則只有一個：<b>「你給我什麼，我就消耗什麼；你拿走什麼，我就補什麼！」</b> 整個化學系統會自動往「抵消變化」的方向移動！</p>

<p><b>⚾ 總裁第一招：濃度試煉</b><br>
如果總裁在左邊的休息室強行塞入 50 名新球員（增加反應物濃度），為了舒緩擁擠的壓力，球員自然會往寬敞的球場上跑，這時平衡就會「<b>向右移動</b>」。<br>
但記者要特別提醒！如果你加入的是「<b>純固體</b>」（例如大理石 CaCO<sub>3</sub>）或「純液體」，它們就像是球場的板凳或硬體設備，其「濃度」是固定不變的！<b>加入固體絕對不會改變球員的碰撞機率，也絕對無法破壞平衡！</b></p>

<p><b>⚾ 總裁第二招：溫度與極端氣候試煉</b><br>
當球場氣溫狂飆，正、逆反應的速率「<b>絕對會同時變快</b>」！但這是一場極度不公平的賽跑，關鍵就在於球場的牆有多高：<br>
🔸 <b>放熱反應（2公尺矮牆）</b>：本來就有一大票球員能輕鬆跨過，加溫補血後，能過關的人數只會「微幅增加」。<br>
🔸 <b>吸熱反應（10公尺高牆）</b>：本來只有極少數的菁英能過，一旦氣溫飆升、全體體能拉高，能跨過高牆的人數會呈現「<b>暴倍數成長</b>」！<br>
因此，<b>溫度一旦上升，平衡絕對會朝著成長倍數最驚人的「吸熱反應」方向強力移動！</b></p>
</div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：Streamlit 原生滑桿與高矮牆數據面板
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧪 戰術模擬中心：溫度試煉與高矮牆效應")
    st.markdown("<span style='color: #64748b; font-size: 16px;'>*(請拉動氣溫滑桿，觀察 2m 矮牆與 10m 高牆的「通關人數倍數」差異！)*</span>", unsafe_allow_html=True)
    
    # 氣溫滑桿
    temp_boost = st.slider("🌡️ 請調整「球場氣溫上升幅度」：", min_value=0, max_value=100, value=0, step=10, format="+%d°C")
    
    # 完美重現劇本的數學邏輯：
    # 常溫下：放熱(矮牆)有 80 人過，吸熱(高牆)只有 1 人過。
    # 升溫 100 度時：放熱變成 88 人(+10%)，吸熱變成 100 人(+10000%)
    exo_base = 80
    endo_base = 1
    
    exo_current = int(exo_base + (8 * temp_boost / 100))
    endo_current = int(endo_base + (99 * temp_boost / 100))
    
    exo_multiplier = exo_current / exo_base
    endo_multiplier = endo_current / endo_base

    # 數據儀表板
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="⬇️ 放熱反應 (2m 矮牆) 通關人數", value=f"{exo_current} 人", delta=f"{exo_multiplier:.1f} 倍成長", delta_color="normal")
    with col2:
        st.metric(label="⬆️ 吸熱反應 (10m 高牆) 通關人數", value=f"{endo_current} 人", delta=f"{endo_multiplier:.1f} 倍成長", delta_color="normal")
    with col3:
        if temp_boost == 0:
            st.metric(label="⚖️ 總裁判定：平衡移動方向", value="維持平衡", delta="正逆速率相同", delta_color="off")
        else:
            st.metric(label="⚖️ 總裁判定：平衡移動方向", value="強力向【吸熱】移動", delta="吸熱通關倍數輾壓！", delta_color="normal")

    if temp_boost > 0:
        st.info(f"💡 分析室快報：升溫 {temp_boost}°C 後，雖然放熱與吸熱的通關人數都變多了，但吸熱方向（高牆）的成長幅度遠大於放熱方向（矮牆），因此平衡被打破，朝吸熱方向移動！")

    st.markdown("""
<div style="background-color: #fff1f2; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e11d48; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); margin-top: 20px;">
<p>🚨 <b>大聯盟終極警告：催化劑的大魔王騙局！</b><br>
總裁祭出的最後一個神祕陷阱是引入「<b>催化劑（投球計時器）</b>」！許多新秀以為這能改變比賽勝負。<br>
但請永遠記住：催化劑會<b>同時、且等比例地</b>增加正逆反應的速率！它只能讓比賽「<b>提早打完（縮短達到平衡的時間）</b>」，但「<b>絕對不會</b>」破壞平衡狀態，也「<b>絕對無法</b>」增加最後生成的總產量！看穿這個騙局，你就能抱走化學大聯盟的總冠軍獎盃！</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導並完成模擬演練後，請回答記者提問以領取總冠軍通行證：</span>", unsafe_allow_html=True)
    
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
