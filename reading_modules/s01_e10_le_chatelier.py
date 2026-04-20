# 檔案位置：reading_modules/s01_e10_le_chatelier.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第十集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：破壞平衡的「終極大魔王」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第10集_破壞平衡的大魔王_完美版.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>十局下半，總冠軍賽的巔峰對決！大聯盟總裁「<b>勒沙特列</b>」親自進場干預比賽！他的最高原則只有一個：<b>「你給我什麼，我就消耗什麼；你拿走什麼，我就補什麼！」</b> 系統會自動往抵消變化的方向移動！</p>

<p><b>⚾ 第一招：濃度試煉</b><br>
如果在左邊休息室強行塞入新球員（增加反應物濃度），為舒緩擁擠壓力，球員自然會往球場上跑，平衡就會「<b>向右移動</b>」。<br>
但要注意！如果你加入的是「<b>純固體</b>」（例如大理石 CaCO<sub>3</sub>）或「<b>純液體</b>」，它們就像是球場的硬體設備，濃度是固定不變的！<b>加入固體絕對不會改變碰撞機率，也絕對不會破壞平衡！</b></p>

<p><b>⚾ 第二招：溫度與極端氣候試煉</b><br>
當球場氣溫狂飆，正、逆反應的速率「<b>絕對會同時變快</b>」！但這是一場不公平的賽跑：<br>
🔸 <b>放熱反應</b>：就像 2 公尺的矮牆，本來就很多人能跨過，加溫後成長空間小。<br>
🔸 <b>吸熱反應</b>：就像 10 公尺的高牆，本來極少數人能過，一旦加溫補血，過關人數的「<b>成長倍數</b>」會遠遠大於放熱方向！<br>
因此，<b>溫度上升，平衡絕對會朝著「吸熱反應」的方向強力移動！</b></p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>裁判紅牌警告：催化劑的大魔王騙局！</b><br>
引入催化劑（投球計時器）會同時、等比例地增加正逆反應速率！它只能讓比賽「<b>提早打完（縮短達到平衡的時間）</b>」，但「<b>絕對不會</b>」破壞平衡狀態，也「<b>絕對無法</b>」增加最後的總產量！千萬別被騙了！
</div>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 總冠軍資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能贏得總冠軍並解鎖挑戰系統！</span>", unsafe_allow_html=True)
    
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
        st.error("❌ 嗶嗶！你被總裁的陷阱騙到了！趕快回去看紅色警告框裡面的催化劑騙局！")
        return False
        
    return False
