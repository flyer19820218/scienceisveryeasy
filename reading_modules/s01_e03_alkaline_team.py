# 檔案位置：reading_modules/ep3_alkaline_team.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第三集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：球場地下室的傳奇——鹼性後勤部隊解密")
    st.info("🎧 點擊播放，聽聽曉臻球評為您帶來的賽前分析！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第3集_鹼性後勤部隊_神奇藥水.mp3") 

    # ✨ 記者專欄版：HTML 標籤全部靠最左邊，不留縮排！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】在化學大聯盟激烈對決的舞台下方，隱藏著一支傳奇的「<b>鹼性後勤部隊</b>」。根據本報記者的深入調查，只要這些球員溶於水，必定會配戴上帶負電的「<b>氫氧根離子 (OH<sup>-</sup>)</b>」專屬臂章。他們有著鮮明的共同特徵：摸起來帶有滑膩感、嚐起來有苦味，更擁有「溶解油脂」的超能力（這也是洗碗精多呈現弱鹼性的主因）。當然，球場守則第一條：絕對禁止用手觸摸或品嚐未知化學物質！</p>

<p><b>⚾ 記者實測：三大陣營鑑定神器</b><br>
為了揪出隱藏在地下室的鹼性部隊，大聯盟配備了三款機密鑑定神器：<br>
1. <b>石蕊試紙</b>：鐵面無私的判官。遇到酸球隊會亮紅燈，但只要鹼性部隊一現身，他就會翻出專屬的「<b>藍色</b>」應援色！<br>
2. <b>酚酞試劑</b>：人稱隱形的粉紅刺客。平常像白開水一樣透明，一旦偵測到鹼性特有的氫氧根離子，會在一秒內瞬間引爆出極度鮮豔的「<b>紫紅色</b>」。<br>
3. <b>廣用指示劑</b>：終極的彩虹戰鬥儀。酸性陣營會呈現「紅、橙、黃」，中立無害的鄉民是「綠色」，而鹼性部隊則會發出「<b>藍、靛、紫</b>」的深邃光芒。</p>

<div style="background-color: #fff7ed; padding: 15px; border-left: 5px solid #f97316; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🔍 <b>場邊筆記：沒有臂章的特例球員</b><br>
記者在休息室聞到一股刺鼻的尿騷味，追查後發現是「<b>氨氣 (NH<sub>3</sub>)</b>」在作祟！令人驚訝的是，他的代號裡根本沒有 OH 臂章，但他極度容易溶於水，一碰到水就會<b>強行製造出氫氧根離子</b>，形成弱鹼性的「氨水」。這是本季最常考的超級變形特例！
</div>

<p><b>⚾ 後勤部隊的兩大王牌</b><br>
除了氨氣，鹼性陣營還有兩位重量級球員：<br>
1. <b>氫氧化鈉 (NaOH)</b>：重裝水管終結者（俗稱燒鹼或苛性鈉）。他擁有強烈溶解油脂的特性，能瞬間打通堵塞的水管。他還有一招可怕的被動技能「<b>潮解</b>」，會不斷吸收空氣中的水分讓自己表面變得溼答答。<br>
2. <b>氧化鈣 (CaO)</b>：海綿大師（俗稱生石灰）。吸水性極強，常出沒在食品包裝裡當乾燥劑。<b>千萬不能泡水喝</b>！他碰到水會放出大量高溫變成強鹼。而他的水溶液「<b>澄清石灰水</b>」，正是聯盟用來檢驗二氧化碳的唯一法寶。</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據記者的場邊筆記，哪一位球員雖然化學式裡沒有「OH」，但溶於水後卻能製造出氫氧根離子，屬於鹼性陣營的變形特例？",
        ["(A) 硫酸", "(B) 氫氧化鈉", "(C) 氧化鈣", "(D) 氨氣"],
        index=None,
        key="reading_q3" 
    )

    if q1 == "(D) 氨氣":
        st.success("✅ 採訪成功！你已經掌握了鹼性部隊最神秘的特例球員，正式解鎖賽事挑戰！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者搖頭：這個特例球員找錯了喔，快回去看橘色的『場邊筆記』！")
        return False
        
    return False
