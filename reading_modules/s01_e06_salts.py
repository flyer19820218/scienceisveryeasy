# 檔案位置：reading_modules/s01_e06_salts.py
import streamlit as st
import json

def render_reading_and_quiz():
    """渲染第六集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：球場清道夫的逆襲——五大無名英雄「鹽類」大揭密")
    st.info("🎧 點擊播放，聽聽曉臻球評為您轉播這場中場休息的精采花絮！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第6集_球場的五大無名英雄_快樂學習版.mp3") 

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】比賽進入中場休息，場務人員正忙著清理酸鹼大戰後遺留的裝備碎片。在化學界，這些碎片被統稱為「<b>鹽類</b>」。許多小球迷常誤以為「鹽類」就是速食店的炸薯條配料，但聯盟發出嚴厲警告：<b>化學上的鹽類只是酸鹼中和產物的統稱，有些帶有劇毒、有些甚至能做成炸藥，絕對不可隨意放進嘴裡！</b></p>

<p><b>⚾ 拯救世界的醫療雙雄</b><br>
記者在場邊發現了兩位不可或缺的醫療級英雄：<br>
1. <b>氯化鈉 (NaCl)</b>：也就是大家熟悉的<b>食鹽</b>。最不可思議的是，他是由「遇水會爆炸的金屬鈉」與「具有劇毒的氯氣」結合而成。兩個致命元素碰在一起，竟化身為無毒無害、甚至能用來打點滴救命的生理食鹽水！<br>
2. <b>硫酸鈣 (CaSO<sub>4</sub>)</b>：俗稱<b>石膏</b>。他微溶於水，一旦加水攪拌就會逐漸凝固變硬。醫療團隊靠他固定球員骨折，甚至連球迷在場邊吃的傳統豆花、豆腐，也少不了他作為凝固劑。</p>

<p><b>⚾ 神奇變身魔術：石灰三兄弟</b><br>
接下來是本聯盟最著名的變身家族，這是一個無限循環的魔術：<br>
🔸 <b>大哥「碳酸鈣」(CaCO<sub>3</sub>)</b>：俗稱灰石或大理石，質地堅硬。當他受到「<b>高溫加熱</b>」時，會吐出二氧化碳 (CO<sub>2</sub>)，瘦身變成二哥。<br>
🔸 <b>二哥「氧化鈣」(CaO)</b>：俗稱生石灰。他極度口渴，一「<b>喝水</b>」就會放出大量高溫（這正是自熱火鍋的原理），隨即變身成三弟。<br>
🔸 <b>三弟「氫氧化鈣」(Ca(OH)<sub>2</sub>)</b>：俗稱熟石灰。他的水溶液就是著名的「澄清石灰水」，只要對著他「<b>吹入二氧化碳</b>」，他就會產生白色混濁，完美變回大哥碳酸鈣的模樣！</p>
</div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：石灰三兄弟變身模擬器
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧪 戰術模擬中心：石灰家族變身循環")
    
    widget_spec = {
      "component": "LlmGeneratedComponent",
      "props": {
        "height": "600px",
        "prompt": "建立一個名為『石灰三兄弟變身魔術模擬器』的互動教學工具。畫面上顯示三個主要狀態節點，形成一個視覺化的循環圖：頂部是大哥『碳酸鈣 (CaCO3)』、右下是二哥『氧化鈣 (CaO)』、左下是三弟『氫氧化鈣 (Ca(OH)2)』。提供三個操作按鈕：1.『高溫加熱』、2.『加水』、3.『吹入二氧化碳』。使用者點擊按鈕時，觸發對應的化學變身流程，並動態高亮當前到達的節點與轉變路徑。例如：點擊『高溫加熱』時，狀態從『碳酸鈣』移動到『氧化鈣』並顯示『釋放二氧化碳 (CO2)』的提示；點擊『加水』時，移動到『氫氧化鈣』並顯示『放出大量高溫 (放熱)』；點擊『吹入二氧化碳』時，移動回『碳酸鈣』並顯示『產生白色混濁沉澱』。請確保介面直觀，形成一個無限循環的視覺體驗，並使用繁體中文。"
      }
    }
    st.components.v1.html(f"""
        <script>
            window.parent.postMessage({{
                type: 'streamlit:set_component_value',
                value: {json.dumps(widget_spec)}
            }}, '*');
        </script>
    """, height=0)
    
    st.write("*(請點擊上方的按鈕，親自驅動這場化學變身魔術，看看三兄弟是如何無限循環的！)*")

    st.markdown("""
<div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 19px; line-height: 1.8;">
🛡️ <b>防守秘訣：冰火不容的「蘇打兄弟檔」</b><br>
最後介紹裝備部最強的洗滌雙雄：<br>
<b>哥哥「碳酸鈉」(Na<sub>2</sub>CO<sub>3</sub>)</b>：俗稱蘇打或洗滌鹼。鹼性較強，性格剛硬不怕熱，去污能力一流，負責清洗球員滿是泥濘的球衣。<br>
<b>弟弟「碳酸氫鈉」(NaHCO<sub>3</sub>)</b>：俗稱小蘇打。水溶液呈弱鹼性，但他有一個致命弱點——<b>極度怕熱！</b>一遇到高溫就會立刻分解並吐出大量二氧化碳 (CO<sub>2</sub>)。因此，他專門用來撲滅球場熱狗攤的油鍋起火，或是當作發粉讓麵包膨脹鬆軟！
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導並體驗變身魔術後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據這份大聯盟專欄報導，關於化學上的「鹽類」，下列哪一個觀念是 **絕對錯誤的（踩中陷阱）**？",
        [
            "(A) 鹽類是酸鹼中和反應後所產生的化合物統稱。", 
            "(B) 所有的「鹽類」就等於餐桌上的食鹽，全部都可以拿來調味吃下肚。", 
            "(C) 食鹽（氯化鈉）是由危險的鈉與有毒的氯氣結合而成的安全物質。", 
            "(D) 小蘇打（碳酸氫鈉）也是一種鹽類，遇熱會產生二氧化碳可滅火。"
        ],
        index=None,
        key="reading_q6"
    )

    if q1 == "(B) 所有的「鹽類」就等於餐桌上的食鹽，全部都可以拿來調味吃下肚。":
        st.success("✅ 採訪成功！你成功避開了致命的文字陷阱，不是所有叫鹽類的都能吃！正式解鎖賽事挑戰！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者搖頭：裁判舉紅牌啦！你把炸藥當成炸薯條的鹽巴了，趕快回去看第一段的警告！")
        return False
        
    return False
