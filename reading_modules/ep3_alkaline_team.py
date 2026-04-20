# 檔案位置：reading_modules/ep3_alkaline_team.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第三集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：傳奇的「鹼性後勤部隊」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第3集_鹼性後勤部隊_神奇藥水.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>在激烈對決的球場地下室，隱藏著一支傳奇的「<b>鹼性後勤部隊</b>」。只要他們溶於水，必定會解離出帶負電的「<b>氫氧根離子 (OH<sup>-</sup>)</b>」，這就是他們的專屬臂章！</p>

<p>這群無名英雄有幾個鮮明的共同特徵：摸起來帶有<b>滑膩感</b>、嚐起來有<b>苦味</b>，而且擁有<b>「溶解油脂」</b>的超能力（這就是為什麼洗碗精通常是弱鹼性）。但記住，球場上絕對禁止用手觸摸或品嚐未知化學物質！</p>

<p><b>⚾ 三大陣營鑑定神器</b><br>
要揪出鹼性部隊，我們有三件大聯盟機密神器：<br>
1. <b>石蕊試紙</b>：鐵面無私的判官。遇到酸會變紅色，遇到鹼性部隊則會亮出專屬的「<b>藍色</b>」應援色！<br>
2. <b>酚酞試劑</b>：隱形的粉紅刺客。平常像白開水一樣透明，一旦偵測到鹼性的氫氧根離子，會在一秒內瞬間引爆出極度鮮豔的「<b>紫紅色</b>」！<br>
3. <b>廣用指示劑</b>：終極彩虹戰鬥儀。不僅能分陣營，還能測戰鬥力！酸性是「紅、橙、黃」，中立鄉民是安全的「綠色」，鹼性則是「<b>藍、靛、紫</b>」。</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #f59e0b; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🔍 <b>曉臻球探的特例筆記：</b><br>休息室刺鼻的尿騷味來自「<b>氨氣 (NH<sub>3</sub>)</b>」。注意看，他的代號裡根本沒有 OH 臂章！但這是一個必考特例：他極度容易溶於水，一碰到水就會<b>強行製造出氫氧根離子</b>，形成弱鹼性的氨水（常作為玻璃清潔劑）。
</div>

<p><b>⚾ 後勤部隊的兩大王牌</b><br>
1. <b>氫氧化鈉 (NaOH)</b>：重裝水管終結者（俗稱燒鹼/苛性鈉）。擁有強烈溶解油脂的特性，能打通堵塞的水管。他有一招可怕的被動技能叫「<b>潮解</b>」——會吸收空氣中的水分讓自己表面變得溼答答。<br>
2. <b>氧化鈣 (CaO)</b>：海綿大師（俗稱生石灰）。吸水性極強，常做乾燥劑。但<b>千萬不能泡水喝</b>！他碰到水會放出大量高溫，變成具腐蝕性的強鹼。他的水溶液就是用來檢驗二氧化碳的「<b>石灰水</b>」。</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據報告中的特例筆記，哪一位球員雖然身上沒有戴著「OH」臂章，但溶於水後卻能製造出氫氧根離子，屬於鹼性陣營？",
        ["(A) 硫酸", "(B) 氫氧化鈉", "(C) 氧化鈣", "(D) 氨氣"],
        index=None,
        key="reading_q3" # 獨立的 Key，防止衝突
    )

    if q1 == "(D) 氨氣":
        st.success("✅ 判斷正確！氨氣 (NH3) 是大聯盟最神奇的鹼性特例。賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 觀念陷阱被踩中了！趕快回去看黃色框框的特例筆記！")
        return False
        
    return False
