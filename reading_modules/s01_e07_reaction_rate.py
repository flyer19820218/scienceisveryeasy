# 檔案位置：reading_modules/s01_e07_reaction_rate.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第七集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：超音速跑壘與「雙重爆發」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第7集_超音速跑者與雙重爆發.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>比賽來到 Lucky Seven 第七局！這局我們要拿出測速槍，測量這群化學新秀的爆發力（<b>反應速率</b>）。雖然我們看不到微小的分子，但只要球場上出現「<b>氣體產生、顏色變化、沉澱物</b>」，就代表反應正在激烈進行！</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>裁判紅牌警告：時間與速率的致命陷阱！</b><br>
千萬別以為「花的時間越久，反應越激烈」！在化學賽場上，<b>時間越短，代表速度越快！</b>反應速率跟時間是完全「<b>成反比</b>」的，所以我們通常用時間的倒數（<b>1 / t</b>）來代表反應速率！
</div>

<p><b>⚾ 得分絕對核心：碰撞學說</b><br>
球員在場上不能只是擦棒被捕，必須發生「<b>有效碰撞</b>」才能成功引發反應！這需要滿足兩大嚴格條件：<br>
1. <b>正確的碰撞方向</b>：就像打者必須精準擊中球棒的「甜蜜點」。<br>
2. <b>突破活化能門檻</b>：打者必須全力揮擊，擁有足夠的「能量」才能把球扛出全壘打牆！</p>

<p><b>⚾ 溫度的「雙重爆發」加成</b><br>
如果讓球場溫度飆高，球員的腎上腺素會狂飆，這會帶來可怕的雙重效果：<br>
第一，球員跑得更快，<b>增加了互相碰撞的次數</b>。<br>
第二，球員能量更高，<b>更容易突破「活化能」的門檻</b>。<br>
次數與能量的相乘效果，會讓反應速率像全壘打仰角一樣，畫出一條向上飆升的「<b>二次曲線</b>」！</p>

<div style="background-color: #f0fdf4; padding: 12px 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🛡️ <b>防守秘訣：球員天生素質（活性）</b><br>
除了溫度，球員本身的「<b>活性</b>」也決定了反應的難易度。超級快腿「<b>鈉 (Na)</b>」碰到水就激烈爆炸；但不動老將「<b>黃金 (Au)</b>」活性極小，不管怎麼催促都不會起反應！
</div>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據球探報告，我們利用觀察「沉澱物蓋住本壘板所花費的時間」來測量反應快慢時，下列哪一個觀念是正確的？",
        [
            "(A) 花費的時間越長，代表反應速率越快。", 
            "(B) 花費的時間長短，與反應速率完全無關。", 
            "(C) 溫度越高，球員跑得越快，所以測量到的時間會變長。", 
            "(D) 反應速率與時間成反比，通常用時間的倒數 (1/t) 來代表反應速率。"
        ],
        index=None,
        key="reading_q7"
    )

    if q1 == "(D) 反應速率與時間成反比，通常用時間的倒數 (1/t) 來代表反應速率。":
        st.success("✅ 測速精準！時間越短、速度越快，所以速率看的是時間的倒數。賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 嗶嗶！你踩中曉臻被吹哨的陷阱啦！趕快回去看紅色框框的警告！")
        return False
        
    return False
