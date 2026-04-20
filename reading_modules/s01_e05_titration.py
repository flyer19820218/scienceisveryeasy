# 檔案位置：reading_modules/s01_e05_titration.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第五集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：五局下半的「極限拆彈任務」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第5集_極限拆彈_無語助詞強化版.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>五局下半，世紀大決戰正式爆發！酸球隊的王牌「<b>氫離子 (H<sup>+</sup>)</b>」與鹼性部隊的防守大將「<b>氫氧根離子 (OH<sup>-</sup>)</b>」在球場中央正面衝撞！這兩個極度危險的球員互撞後，戰力瞬間歸零，結合成全宇宙最和平的物質——「<b>水 (H<sub>2</sub>O)</b>」，這個過程就稱為<b>中和</b>。</p>

<p><b>⚾ 裝備碎片與熱血沸騰</b><br>
雙方互撞後，除了產生水，球員斷裂的裝備碎片會掉落在球場上，這些碎片在化學上統稱為「<b>鹽類</b>」。同時，如果你摸一下燒杯，會發現它變得非常燙！這代表酸鹼中和是一個絕對的「<b>放熱反應</b>」！</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>裁判紅牌警告：鹽類的致命陷阱！</b><br>
千萬別以為化學上的「鹽類」就是炸薯條撒的食鹽（氯化鈉）！鹽類只是酸鹼中和產物的「統稱」，有些鹽類有劇毒，有些甚至能做成炸藥，<b>絕對不可以隨便拿來吃！</b>
</div>

<p><b>⚾ 極限拆彈：滴定戰術</b><br>
為了解析敵方未知濃度的戰力，教練團會啟動滴定戰術！<br>
🔸 <b>防守方（未知濃度）</b>：潛伏在下方的「<b>錐形瓶</b>」裡。<br>
🔸 <b>進攻方（已知濃度）</b>：躲在上方帶有刻度的「<b>滴定管</b>」裡。<br>
🔸 <b>標準姿勢</b>：左手控制活塞滴入溶液，右手輕輕搖晃錐形瓶，視線平齊液面凹下最底端。</p>

<div style="background-color: #f0fdf4; padding: 12px 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🛡️ <b>防守秘訣：當量點 vs 滴定終點</b><br>
實驗時，我們會先在錐形瓶滴入酚酞指示劑（酸中無色）。當上方溶液滴下，酚酞<b>瞬間變成紫紅色且搖晃不褪色</b>的那一刻，代表任務完成，這在化學上精確稱為「<b>滴定終點</b>」（肉眼看見變色的瞬間）！這與 H<sup>+</sup> 和 OH<sup>-</sup> 數量完美平手的「<b>當量點</b>」（科學實際狀態）定義是完全不同的！
</div>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據這份機密報告，我們在做酸鹼滴定實驗時，看到「酚酞指示劑瞬間變色」而立刻關閉活塞停止實驗的那個瞬間，在化學上精確的名稱是什麼？",
        [
            "(A) 沸騰點", 
            "(B) 當量點", 
            "(C) 滴定終點", 
            "(D) 絕對中性點"
        ],
        index=None,
        key="reading_q5"
    )

    if q1 == "(C) 滴定終點":
        st.success("✅ 拆彈成功！「滴定終點」是我們肉眼看見變色的瞬間，別和實際平手的「當量點」搞混了！賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 滴定管沒關緊！這是一個超大變化球陷阱，趕快回去看綠色框框的防守秘訣！")
        return False
        
    return False
