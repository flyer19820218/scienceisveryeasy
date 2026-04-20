# 檔案位置：reading_modules/s01_e09_equilibrium.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第九集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🕵️‍♂️ 大聯盟球探的機密報告：沒有盡頭的延長賽「動態平衡」")
    st.info("🎧 點擊播放，聽曉臻球探為你語音解密！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第9集_化學平衡_沒有盡頭的延長賽.mp3") 

    # HTML 標籤全部靠最左邊，不留縮排，避免被 Streamlit 當成程式碼區塊！
    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.7; color: #334155; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
<p>九局上半，比賽進入了永遠打不完的延長賽！在化學球場上，比賽分為兩種截然不同的賽制：</p>

<p><b>⚾ 露天球場 vs 巨蛋球場</b><br>
🔸 <b>不可逆反應</b>：就像在「<b>露天球場</b>」打球，球轟出全壘打牆飛進太平洋就永遠回不來了（例如：木材燃燒、氣體逸散），反應只能單向進行。<br>
🔸 <b>可逆反應</b>：必須在屋頂關閉的「<b>巨蛋球場（密閉系統）</b>」進行！氣體撞到屋頂會反彈回來，這時候場上就會同時出現上場守備（<b>正反應</b>）與退下休息（<b>逆反應</b>）兩種跑動方向！</p>

<p><b>⚾ 八字真言：巨觀靜止，微觀狂奔</b><br>
當裁判大喊「達到平衡」時，代表場上與休息室的「總人數」不再改變（<b>濃度固定</b>）。但這絕對不代表球員在睡覺！這是一場「<b>動態平衡</b>」，教練依然在瘋狂換人，只是上場的球員數剛好等於下場的球員數（<b>正反應速率 = 逆反應速率</b>），一進一出互相抵銷！</p>

<div style="background-color: #fffbeb; padding: 12px 15px; border-left: 5px solid #ef4444; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>裁判紅牌警告：段考最愛考的大魔王陷阱！</b><br>
很多人以為達到平衡時，場上與休息室的人數比例，會剛好等於化學戰術板上的「<b>係數比</b>」（例如 1:3:2），這是<b>大錯特錯</b>的！平衡時的濃度比例，有可能是任何數字比（取決於一開始帶了多少人），<b>「濃度固定不變」絕對不等於「濃度等於係數比」！</b>
</div>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🎖️ 球探資格測試")
    st.markdown("<span style='color: #64748b; font-size: 16px; font-weight: bold;'>👉 必須展現你的判斷力（答對這題），才能解鎖下方的【賽事挑戰系統】！</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據這份機密報告，關於「化學動態平衡」的敘述，下列哪一個觀念是完全正確的？",
        [
            "(A) 反應達到平衡時，所有分子球員都會停止跑動，這是一場完全靜止的比賽。", 
            "(B) 只要把反應物放在開放的露天球場，最後也一定能順利達到化學平衡。", 
            "(C) 達到平衡時，正反應速率會剛好等於逆反應速率，巨觀上各物質的濃度不再改變。", 
            "(D) 達到平衡時，反應物與生成物的濃度比例，一定會剛好等於化學式的係數比。"
        ],
        index=None,
        key="reading_q9"
    )

    if q1 == "(C) 達到平衡時，正反應速率會剛好等於逆反應速率，巨觀上各物質的濃度不再改變。":
        st.success("✅ 觀念滿分！「巨觀靜止，微觀狂奔」就是動態平衡的真諦！賽事大門已為你敞開！")
        return True 
    elif q1 is not None:
        st.error("❌ 嗶嗶！你被大魔王陷阱騙到了！趕快回去看紅色框框與八字真言的防守秘訣！")
        return False
        
    return False
