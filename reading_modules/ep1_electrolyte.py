import streamlit as st

def render_reading_and_quiz():
    """渲染第一集閱讀素養，過關回傳 True"""
    
    st.markdown("### 📖 課前戰術板：超級新秀「電解質」的秘密戰術")
    st.info("🎧 點擊播放，聽曉臻助教教你怎麼畫重點！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/曉臻解說_電解質.mp3") 

    # ✨ 完整文章回歸！保留了故事感與精美排版
    st.markdown("""
    <div style="background-color: #f8fafc; padding: 30px; border-radius: 12px; border: 1px solid #e2e8f0; font-size: 20px; line-height: 1.8; color: #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
        <p>在化學大聯盟的賽季初，一位名叫「<b>電解質</b>」的超級新秀剛登板就引起了全場轟動。講到電解質，許多人腦海中閃過的第一個畫面，可能是運動後大口灌下的運動飲料。但在競爭激烈的化學球場上，要能披上「電解質」這件球衣，必須通過裁判嚴格的兩大考驗：</p>
        
        <ol style="margin-top: 10px; margin-bottom: 20px;">
            <li><span style='color: #E65100; font-weight: bold; font-size: 22px;'>必須能溶於水</span></li>
            <li><span style='color: #E65100; font-weight: bold; font-size: 22px;'>其水溶液必須能夠導電</span></li>
        </ol>
        
        <div style="background-color: #fffbeb; padding: 15px 20px; border-left: 6px solid #f59e0b; margin: 20px 0; border-radius: 4px; font-size: 19px;">
            🔍 <b>曉臻教練提醒陷阱：</b><br>有些人可能會誤以為「只要能導電就是電解質」。銅線跟鐵絲雖然導電能力極佳，但把它們丟進水裡，它們並不會溶解。所以<b>金屬雖然是導電高手，但絕對不是電解質！</b>
        </div>
        
        <p><b>⚾ 百年戰術：阿瑞尼斯的解離說</b><br>
        電解質之所以能在水中導電，關鍵在於百年前由阿瑞尼斯教練提出的「解離說」戰術。當電解質球員跳進水中時，他們會立刻兵分兩路，拆解成帶正電的「<b>陽離子</b>」以及帶負電的「<b>陰離子</b>」。這些在水中自由移動的離子，就像是勤奮的無名英雄，負責在水中接力傳遞電流。</p>

        <p><b>⚾ 不合群的球員與全明星陣容</b><br>
        當然，球場上也有被稱為「<b>非電解質</b>」的球員，例如<b>糖水和酒精</b>。它們雖然能完美溶於水，但非常頑固，死都不肯拆解出離子，所以水溶液完全無法導電。</p>

        <p>那運動飲料裡到底藏了什麼神級球員呢？最關鍵的明星就是我們熟悉的食鹽（氯化鈉，NaCl）。在大聯盟裡，<b>「酸、鹼、鹽」</b>三大家族就是最頂尖的電解質大軍。而且不管他們怎麼解離，水溶液中正、負離子的總電量永遠會相等，維持著完美的防守陣型——這就叫做<b>「電中性」</b>！</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 戰術板隨堂測驗")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 必須答對這題，才能解鎖下方的【賽事挑戰系統】喔！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據文章，下列哪一個家族 **不屬於** 電解質大軍？",
        ["(A) 酸類家族", "(B) 鹽類家族", "(C) 酒精與糖水家族", "(D) 鹼類家族"],
        index=None,
        key="reading_q1"
    )

    if q1 == "(C) 酒精與糖水家族":
        st.success("✅ 答對了！糖水和酒精是頑固的非電解質。戰術板解鎖成功！")
        return True 
    elif q1 is not None:
        st.error("❌ 找錯人了喔，再看一下文章的陷阱區！")
        return False
        
    return False
