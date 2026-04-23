import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS 覆寫：強制題目與選項「一樣大 (20px)」並美化排版
    st.markdown("""
        <style>
        /* 1. 調整題目標題 (Label) */
        div[class*="stRadio"] > label {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #1e293b !important;
            line-height: 1.6 !important;
            margin-bottom: 15px !important;
        }
        /* 2. 調整選項文字 (Paragraph) */
        div[class*="stRadio"] p {
            font-size: 20px !important;
            font-weight: 500 !important;
            color: #334155 !important;
        }
        /* 3. 增加選項間的垂直間距 */
        div[class*="stRadio"] [data-testid="stWidgetSelectionColumn"] {
            gap: 15px !important;
        }
        /* 私名號優化 */
        u {
            text-decoration: underline;
            text-underline-offset: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### ⚖️ 黎明化學法庭 S02E03：後台的生存法則")
    
    # 審判長對白
    st.markdown("<div style='background-color: #e0f2fe; padding: 15px; border-radius: 8px; color: #0369a1; border-left: 5px solid #0284c7; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『偶像的體力管理與潔淨外表，都是專業的一部分。從後台的便當防腐，到卸除沉重的舞台妝，化學律令無處不在。檢察官，請出示生存卷宗。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區 (被洗掉的硬水內容已補齊)
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：食品保存與皂化反應")
        
        st.markdown("　　在後台，食材的保存是關鍵。真空包裝透過抽乾空氣來阻絕氧氣（O₂），防止氧化與細菌孳生。醃漬法則利用「滲透壓」原理，以高濃度的鹽或糖將細菌體內水分抽乾，使其脫水死亡。而低溫殺菌法（攝氏 62 到 65 度）則能消滅致病菌並保留鮮奶風味。此外，發酵作用則是刻意利用微生物分解食物，釀造出醬油與醋等精華。", unsafe_allow_html=True)

        st.markdown("　　而卸妝用的肥皂，誕生於「皂化反應」。將油脂與強鹼（氫氧化鈉 NaOH）加熱後，會產生肥皂（脂肪酸鈉）與副產物甘油。在反應中，加入「酒精」並非作為催化劑，而是擔任「助溶劑」的角色，讓油脂與鹼水均勻混合。反應結束後，加入飽和食鹽水進行「鹽析」，肥皂會因密度較小且不溶於食鹽水而浮在表面，方便撈取。", unsafe_allow_html=True)
        
        st.markdown("#### 📁 檢方機密卷宗：去汙原理與硬水危機")

        st.markdown("　　清潔劑分子的構造極為獨特：長長的碳鏈是「親油端」，專門咬住油垢；帶電的一頭則是「親水端」，緊緊抓住水分子。當水沖下時，親水端會被水流帶動，連帶將咬住油垢的親油端一起拔離表面，這就是去汙的原理。", unsafe_allow_html=True)

        st.markdown("　　然而，肥皂有一個致命弱點：**硬水**。若水質中含有大量的「鈣離子 (Ca²⁺)」與「鎂離子 (Mg²⁺)」（如深山泉水、地下水或海水），這些離子會與肥皂結合，產生白色的塊狀「沉澱物」，導致肥皂完全失去洗淨力。要解決這個危機，必須改用由石化原料製成的「合成清潔劑」（如洗面乳、洗衣精），因為合成清潔劑完全不受硬水影響，依然能發揮強大的洗淨力。", unsafe_allow_html=True)

    st.write("---")

    # ==========================================
    # 🧬 結構視覺化區 (四格漫畫式專業圖解 - 還原 image_8.png 佈局)
    # ==========================================
    st.markdown("#### 🧬 呈堂證供：去汙機器人的【四步拔除】漫畫式圖解")
    st.markdown("　　請檢察官仔細觀察這份還原現場的專業四格圖解，它清晰展示了肥皂分子如何一步步咬住油垢，並形成「微胞」結構將其拔離表面的暴力美學。", unsafe_allow_html=True)
    
    html_code = """
    <div style="display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 15px; font-family: sans-serif; background: #fdfcf9; padding: 15px; border-radius: 12px; border: 2px solid #e2e8f0;">
        <div style="text-align: center; background: white; padding: 10px; border-radius: 12px; border: 1px solid #cbd5e1;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 5px; margin-bottom: 5px;">
                <div style="width: 25px; height: 25px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px;">1</div>
                <h4 style="color: #1e293b; margin: 0; font-size: 16px;">沾附於表面</h4>
            </div>
            <div style="position: relative; height: 150px; background: white; border-bottom: 6px solid #475569; overflow: hidden; border-radius: 8px;">
                <div style="position: absolute; bottom: 0; left: 25%; width: 50%; height: 50px; background: #f59e0b; border-radius: 50% 50% 0 0;"></div>
            </div>
            <p style="font-size: 12px; color: #64748b; margin-top: 5px;">油污沾附在物體表面</p>
        </div>
        
        <div style="text-align: center; background: white; padding: 10px; border-radius: 12px; border: 1px solid #cbd5e1;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 5px; margin-bottom: 5px;">
                <div style="width: 25px; height: 25px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px;">2</div>
                <h4 style="color: #1e293b; margin: 0; font-size: 16px;">親油端咬住油</h4>
            </div>
            <div style="position: relative; height: 150px; background: white; border-bottom: 6px solid #475569; overflow: hidden; border-radius: 8px;">
                <div style="position: absolute; bottom: 0; left: 25%; width: 50%; height: 50px; background: #f59e0b; border-radius: 50% 50% 0 0;"></div>
                <div style="position: absolute; bottom: 30px; left: 20px; transform: rotate(45deg); display: flex; align-items: center;">
                    <div style="width: 35px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
                <div style="position: absolute; bottom: 30px; right: 20px; transform: rotate(135deg); display: flex; align-items: center;">
                    <div style="width: 35px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
                <div style="position: absolute; bottom: 50px; left: 45%; transform: rotate(90deg); display: flex; align-items: center;">
                    <div style="width: 35px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
            </div>
            <p style="font-size: 12px; color: #64748b; margin-top: 5px;">親油端(灰)咬住油，向內拉扯</p>
        </div>

        <div style="text-align: center; background: white; padding: 10px; border-radius: 12px; border: 1px solid #cbd5e1;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 5px; margin-bottom: 5px;">
                <div style="width: 25px; height: 25px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px;">3</div>
                <h4 style="color: #1e293b; margin: 0; font-size: 16px;">拔離表面</h4>
            </div>
            <div style="position: relative; height: 150px; background: white; border-bottom: 6px solid #cbd5e1; overflow: hidden; border-radius: 8px;">
                <div style="position: absolute; bottom: 20px; left: 25%; width: 50%; height: 60px; background: radial-gradient(circle, #fbdf85, #f59e0b); border-radius: 50%; box-shadow: 0 0 10px rgba(245, 158, 11, 0.4);"></div>
                <div style="position: absolute; bottom: 65px; left: 10px; transform: rotate(30deg); display: flex; align-items: center;">
                    <div style="width: 30px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
                <div style="position: absolute; bottom: 65px; right: 10px; transform: rotate(150deg); display: flex; align-items: center;">
                    <div style="width: 30px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
                <div style="position: absolute; bottom: 10px; left: 45%; transform: rotate(-90deg); display: flex; align-items: center;">
                    <div style="width: 30px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
            </div>
            <p style="font-size: 12px; color: #64748b; margin-top: 5px;">親水端(藍)抓水，將油拔離</p>
        </div>

        <div style="text-align: center; background: white; padding: 10px; border-radius: 12px; border: 1px solid #cbd5e1;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 5px; margin-bottom: 5px;">
                <div style="width: 25px; height: 25px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 14px;">4</div>
                <h4 style="color: #1e293b; margin: 0; font-size: 16px;">恢復潔淨</h4>
            </div>
            <div style="position: relative; height: 150px; background: white; border-bottom: 6px solid #cbd5e1; overflow: hidden; border-radius: 8px;">
                <div style="position: absolute; top: 15px; left: 50%; transform: translateX(-50%); width: 45px; height: 45px; background: #f59e0b; border-radius: 50%;"></div>
                <div style="position: absolute; top: 30px; left: 15px; transform: rotate(180deg); display: flex; align-items: center;">
                    <div style="width: 25px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
                <div style="position: absolute; top: 30px; right: 15px; transform: rotate(0deg); display: flex; align-items: center;">
                    <div style="width: 25px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
                <div style="position: absolute; top: 0px; left: 45%; transform: rotate(-90deg); display: flex; align-items: center;">
                    <div style="width: 25px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
                <div style="position: absolute; top: 55px; left: 45%; transform: rotate(90deg); display: flex; align-items: center;">
                    <div style="width: 25px; height: 4px; background: #64748b;"></div><div style="width: 10px; height: 10px; background: #3b82f6; border-radius: 50%;"></div>
                </div>
            </div>
            <p style="font-size: 12px; color: #64748b; margin-top: 5px;">油污被徹底包圍並沖走</p>
        </div>
    </div>
    """
    # 🌟 這裡高度設定為 500，確保四格圖完整顯示
    components.html(html_code, height=500)
    st.write("---")

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區 (打臉時刻)
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    # 辯護律師對白
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！檢方對於後台管理與野外實境秀的控訴完全失實！<br><br><b>【關於皂化反應】</b> 我的當事人雖然在煮肥皂時倒入大量酒精，那是因為酒精是強效『催化劑』，能讓反應瞬間完成！這可是一項化學創新！<br><br><b>【關於硬水危機】</b> 練習生去深山洗澡洗不乾淨，是因為山泉水（硬水）中含有大量的『鈉離子』！鈉會跟肥皂產生白色沉澱，導致肥皂失效。這時候應該要改用『低溫殺菌』後的鮮奶洗臉，才能發揮最強效去汙！」</div>", unsafe_allow_html=True)
    
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
    
    if st.button("⚖️ 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備！")
        elif q1.startswith("A") and q2.startswith("A"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！酒精是助溶劑而非催化劑，硬水則是含有鈣鎂離子。辯方律師，你的生存常識該補課了！」\n\n✅ 成功戳破所有謊言，審判勝利，準備進入實戰演練！")
            return True
        else:
            # 針對答錯的地方給予個別提示
            error_msg = "❌ 異議駁回！法官認為你的推理有破綻：\n"
            if not q1.startswith("A"):
                error_msg += "\n👉 **【關於皂化案】** 請重新確認酒精在油水反應中究竟起到了什麼作用？"
            if not q2.startswith("A"):
                error_msg += "\n👉 **【關於硬水案】** 請確認硬水的離子組成，以及哪種清潔劑能在硬水中發揮威力？"
            st.error(error_msg)
            
    return False
