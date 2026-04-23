import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS 覆寫：強制題目與選項「一樣大 (20px)」
    st.markdown("""
        <style>
        div[class*="stRadio"] > label {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #1e293b !important;
            line-height: 1.6 !important;
            margin-bottom: 15px !important;
        }
        div[class*="stRadio"] p {
            font-size: 20px !important;
            font-weight: 500 !important;
            color: #334155 !important;
        }
        div[class*="stRadio"] [data-testid="stWidgetSelectionColumn"] {
            gap: 15px !important;
        }
        u {
            text-decoration: underline;
            text-underline-offset: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### ⚖️ 黎明化學法庭 S02E03：後台的生存法則")
    
    st.markdown("<div style='background-color: #e0f2fe; padding: 15px; border-radius: 8px; color: #0369a1; border-left: 5px solid #0284c7; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『偶像的體力管理與潔淨外表，都是專業的一部分。從後台的便當防腐，到卸除沉重的舞台妝，化學律令無處不在。檢察官，請出示生存卷宗。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區 (法庭證據檔案)
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：食品保存與皂化反應")
        
        st.markdown("　　在後台，食材的保存是關鍵。真空包裝透過抽乾空氣來阻絕氧氣（O₂），防止氧化與細菌孳生。醃漬法則利用「滲透壓」原理，以高濃度的鹽或糖將細菌體內水分抽乾，使其脫水死亡。而低溫殺菌法（攝氏 62 到 65 度）則能消滅致病菌並保留鮮奶風味。此外，發酵作用則是刻意利用微生物分解食物，釀造出醬油與醋等精華。", unsafe_allow_html=True)

        st.markdown("　　而卸妝用的肥皂，誕生於「皂化反應」。將油脂與強鹼（氫氧化鈉 NaOH）加熱後，會產生肥皂（脂肪酸鈉）與副產物甘油。在反應中，加入「酒精」並非作為催化劑，而是擔任「助溶劑」的角色，讓油脂與鹼水均勻混合。反應結束後，加入飽和食鹽水進行「鹽析」，肥皂會因密度較小且不溶於食鹽水而浮在表面，方便撈取。", unsafe_allow_html=True)

    st.write("---")

    # ==========================================
    # 🧬 結構視覺化區 (去汙原理)
    # ==========================================
    st.markdown("#### 🧬 呈堂證供：去汙機器人的暴力美學")
    st.markdown("　　清潔劑分子的構造極為獨特：長長的碳鏈是「親油端」，專門咬住油垢；帶電的一頭則是「親水端」，緊緊抓住水分子。當水沖下時，油垢就會被硬生生地拔離表面。", unsafe_allow_html=True)
    
    html_code = """
    <div style="text-align: center; background: #fdfcf9; padding: 20px; border-radius: 12px; border: 2px solid #e2e8f0; font-family: sans-serif;">
        <h4 style="color: #1e293b; margin-bottom: 15px;">清潔劑分子 (去汙示意圖)</h4>
        <div style="position: relative; height: 180px; background: white; border: 1px solid #cbd5e1; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            <div style="position: absolute; width: 80px; height: 80px; background: #fbbf24; border-radius: 50%; opacity: 0.8; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #92400e; z-index: 1;">油垢</div>
            
            <div style="position: absolute; left: 20%; top: 30%; transform: rotate(-30deg); display: flex; align-items: center; z-index: 2;">
                <div style="width: 60px; height: 4px; background: #64748b;"></div> <div style="width: 15px; height: 15px; background: #3b82f6; border-radius: 50%;"></div> </div>
            
            <div style="position: absolute; right: 20%; bottom: 30%; transform: rotate(150deg); display: flex; align-items: center; z-index: 2;">
                <div style="width: 60px; height: 4px; background: #64748b;"></div>
                <div style="width: 15px; height: 15px; background: #3b82f6; border-radius: 50%;"></div>
            </div>
        </div>
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 15px; font-size: 14px;">
            <div style="display: flex; align-items: center; gap: 5px;">
                <div style="width: 20px; height: 4px; background: #64748b;"></div> 灰色：親油端 (抓油)
            </div>
            <div style="display: flex; align-items: center; gap: 5px;">
                <div style="width: 15px; height: 15px; background: #3b82f6; border-radius: 50%;"></div> 藍色：親水端 (抓水)
            </div>
        </div>
    </div>
    """
    components.html(html_code, height=280)
    st.write("---")

    # ==========================================
    # 💥 逆轉法庭交互區 (雙重打臉時刻)
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！檢方對於後台管理與野外實境秀的控訴完全失實！<br><br><b>【關於皂化反應】</b> 我的當事人雖然在煮肥皂時倒入大量酒精，但那是因為酒精是強效『催化劑』，能讓反應瞬間完成！這可是一項化學創新！<br><br><b>【關於硬水危機】</b> 練習生去深山洗澡洗不乾淨，那是因為山泉水（硬水）中含有大量的『鈉離子』！這些鈉離子會跟肥皂產生白色沉澱，導致肥皂失效。這時候應該要改用『低溫殺菌』後的鮮奶來洗臉，才能發揮最強的洗淨力！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "⚖️ 第一回合：請指出辯方對「皂化反應試劑」的誤解：",
        [
            "A. 「異議！酒精在皂化反應中並非催化劑，而是扮演『助溶劑』的角色，目的是讓互不相溶的油與鹼水均勻混合！」",
            "B. 「異議！酒精是用來進行『鹽析』的，目的是讓甘油浮在水面上，辯方搞錯了實驗步驟！」",
            "C. 「異議！酒精是用來防腐的，跟皂化反應完全無關！」"
        ],
        index=None,
        key="q1"
    )

    st.write("<br>", unsafe_allow_html=True)

    q2 = st.radio(
        "⚖️ 第二回合：請指出辯方對「硬水與清潔劑」的致命錯誤：",
        [
            "A. 「異議！硬水是指含有大量『鈣、鎂離子』的水！而真正不受硬水影響、能強效去汙的是『合成清潔劑』，並非鮮奶！」",
            "B. 「異議！硬水是因為含有氧氣過多，導致肥皂被氧化，應該改用真空包裝過的肥皂！」",
            "C. 「異議！硬水是指低溫殺菌後的水，會讓肥皂結冰，導致無法產生泡沫！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("⚖️ 提出雙重異議 (Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備！")
        elif q1.startswith("A") and q2.startswith("A"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！酒精是助溶劑而非催化劑，硬水則是含有鈣鎂離子。辯方律師，你的生存常識該補課了！」\n\n✅ 成功戳破所有謊言，審判勝利，準備進入實戰演練！")
            return True
        else:
            error_msg = "❌ 異議駁回！法官認為你的推理有破綻：\n"
            if not q1.startswith("A"):
                error_msg += "\n👉 **【關於皂化案】** 請重新確認酒精在油水反應中究竟起到了什麼作用？"
            if not q2.startswith("A"):
                error_msg += "\n👉 **【關於硬水案】** 請確認硬水的定義，以及哪種清潔劑能在硬水中發揮威力？"
            st.error(error_msg)
            
    return False
