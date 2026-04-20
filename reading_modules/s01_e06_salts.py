# 檔案位置：reading_modules/s01_e06_salts.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第六集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：球場的五大無名英雄")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第6集_球場的五大無名英雄_快樂學習版.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>中場休息時間到！場務人員正在清理酸鹼大戰後遺留的裝備碎片，這些碎片在化學上統稱為「<b>鹽類</b>」。但千萬注意，鹽類的功能五花八門，絕對不是只能拿來炸薯條！</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>裁判紅牌警告：致命的文字陷阱！</b><br>
化學上的「鹽類」只是酸鹼中和產物的統稱！有些鹽類有劇毒、有些能做成炸藥。我們吃的食鹽只是千千萬萬種鹽類的其中一員，<b>絕對不能以為只要叫「鹽類」就可以吃下肚！</b>
</div>

<p><b>⚾ 拯救世界的醫療雙雄</b><br>
1. <b>氯化鈉 (NaCl)</b>：俗稱<b>食鹽</b>。由會爆炸的鈉金屬與劇毒的氯氣結合，卻變成無毒無害、維持生命的 MVP（生理食鹽水）。<br>
2. <b>硫酸鈣 (CaSO<sub>4</sub>)</b>：俗稱<b>石膏</b>。微溶於水，加水會凝固變硬。用來固定骨折、做粉筆，甚至是你吃的傳統豆花、豆腐的凝固劑！</p>

<p><b>⚾ 神奇變身：石灰三兄弟</b><br>
這是一個會無限循環的變身魔術：<br>
🔸 <b>大哥「碳酸鈣」(CaCO<sub>3</sub>)</b>：灰石/大理石。加熱後吐出 CO<sub>2</sub>，瘦身變成二哥。<br>
🔸 <b>二哥「氧化鈣」(CaO)</b>：生石灰。喝水後放出大量高溫（自熱火鍋原理），變身成三弟。<br>
🔸 <b>三弟「氫氧化鈣」(Ca(OH)<sub>2</sub>)</b>：熟石灰。溶於水就是「澄清石灰水」，吹入 CO<sub>2</sub> 變混濁後，又完美變回大哥碳酸鈣！</p>

<div style="background-color: #f0fdf4; padding: 12px 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🛡️ <b>防守秘訣：最強「蘇打兄弟檔」</b><br>
<b>哥哥「碳酸鈉」(Na<sub>2</sub>CO<sub>3</sub>)</b>：俗稱蘇打/洗滌鹼。鹼性強，不怕熱，去污能力一流，負責<b>洗衣服</b>。<br>
<b>弟弟「碳酸氫鈉」(NaHCO<sub>3</sub>)</b>：俗稱小蘇打。弱鹼性，<b>極度怕熱</b>！一遇熱就分解吐出大量 CO<sub>2</sub>，專門用來<b>撲滅油鍋起火</b>，或當發粉讓<b>麵包膨脹鬆軟</b>！
</div>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據這份機密報告，關於化學上的「鹽類」，下列哪一個觀念是 **絕對錯誤的（踩中陷阱）**？",
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
        st.success("✅ 避開陷阱！化學上的「鹽類」有些可是有毒或會爆炸的，絕對不能亂吃。賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 嗶嗶！裁判舉紅牌啦！趕快回去看紅色框框的「致命文字陷阱」！")
        return False
        
    return False
