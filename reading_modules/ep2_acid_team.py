# 檔案位置：reading_modules/ep2_acid_team.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第二集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：火力最猛的「酸球隊」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/曉臻解說_酸球隊.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>歡迎來到二局上半！現在進攻的是聯盟裡攻擊火力最兇猛、脾氣最火爆的隊伍——「<b>酸球隊</b>」。我們生活中喝的汽水、吃的檸檬都有酸味，但請記得，在化學球場上<b>絕對不能用舌頭去嚐這些職業球員</b>，因為他們大多具有強烈的腐蝕性！</p>

<p><b>⚾ 招牌武器：氫離子直球</b><br>
只要是酸球隊的正式球員，溶於水之後，必定會解離出帶正電的「<b>氫離子 (H<sup>+</sup>)</b>」。這就是他們用來攻擊對手的最強直球！當這顆直球打中<b>活性金屬</b>防守員時，會發生極度劇烈的反應，金屬瞬間被溶解，並轟出一支「<b>氫氣 (H<sub>2</sub>) 全壘打</b>」！</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>球探防守警告：觀念大陷阱！</b><br>
遇到金屬會產生氫氣，但如果酸球隊遇到的是「<b>碳酸鈣</b>」（例如大理石或貝殼），產生的絕對不是氫氣，而是「<b>二氧化碳 (CO<sub>2</sub>)</b>」！這個防守弱點必須死死記住！
</div>

<p><b>⚾ 三大強酸先發王牌</b><br>
酸球隊有三位幾乎百分之百解離的恐怖先發投手：<br>
1. <b>硫酸 (H<sub>2</sub>SO<sub>4</sub>)</b>：化學工業之母，擁有可怕的「<b>脫水性</b>」，能把白糖瞬間抽乾變成焦黑的碳柱。稀釋它時，<b>絕對只能「把酸加進水裡」並攪拌</b>，反過來會導致強酸沸騰飛濺！<br>
2. <b>鹽酸 (HCl)</b>：氯化氫的水溶液。工業用鹽酸因為含有鐵離子雜質而呈微黃色。<b>洗廁所時絕對不可與漂白水混合，否則會產生劇毒的「氯氣」！</b><br>
3. <b>硝酸 (HNO<sub>3</sub>)</b>：脾氣古怪的刺客，非常怕光，照光會分解出有毒的紅棕色二氧化氮，所以必須裝在<b>深褐色瓶子</b>裡。若把濃硝酸與濃鹽酸以 1:3 混合，就會變成連黃金都能溶解的「<b>王水</b>」。
</p>

<p><b>⚾ 板凳救援老將：醋酸 (CH<sub>3</sub>COOH)</b><br>
到了比賽後半段，球隊會派上「弱酸」球員——醋酸（乙酸）。純度極高的醋酸在 17°C 左右就會結冰，所以又叫「<b>冰醋酸</b>」。千萬別以為你可以直接喝它，我們平常吃的食用醋，其實只是濃度 3%~5% 的極度稀釋水溶液而已！</p>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據這份機密報告，當酸球隊遇到含有「碳酸鈣」的防守員（例如大理石、貝殼）時，會產生什麼氣體？",
        ["(A) 劇毒的氯氣", "(B) 助燃的氧氣", "(C) 可怕的氫氣", "(D) 二氧化碳"],
        index=None,
        key="reading_q2" # 注意：Key 必須與第一集不同，避免 Streamlit 狀態衝突
    )

    if q1 == "(D) 二氧化碳":
        st.success("✅ 判斷正確！遇到金屬才是氫氣，遇到大理石是二氧化碳。賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 觀念陷阱被踩中了！趕快回去看紅色框框的防守警告區塊！")
        return False
        
    return False
