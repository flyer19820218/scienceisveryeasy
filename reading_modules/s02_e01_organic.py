import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS 覆寫：強制題目與選項「一樣大」
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
        /* 3. 增加選項間的垂直間距，避免文字太擠 */
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

    st.markdown("### ⚖️ 黎明化學法庭 S02E01：碳基生命的審判")
    
    # 審判長對白
    st.markdown("<div style='background-color: #e0f2fe; padding: 15px; border-radius: 8px; color: #0369a1; border-left: 5px solid #0284c7; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『法庭之上，沒有模稜兩切的狡辯。證據與化學鐵律，是判決的唯一標準。檢察官，準備好揭穿辯方的謊言了嗎？』</div>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區 (法庭證據檔案)
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：有機化學的本質與迷思")
        st.markdown("　　在科學發展的早期，化學家們普遍被一種稱為「生命力理論」的神秘面紗所籠罩。他們固執地認為，凡是有機化合物，必然只能由具有生命力的生物體製造出來。然而，這個延續已久的神話在 1828 年被德國科學家<u>烏拉</u>徹底擊碎。他在實驗室中，僅僅透過加熱無機物，就成功合成出了原本只存在於生物體內的有機物——「尿素」。這一擊不僅宣告了生命力理論的終結，也迫使科學界重新定義有機化學。", unsafe_allow_html=True)
        st.markdown("　　現代法庭將有機化合物定義為「含碳的化合物」。然而，即便流著碳元素的血脈，化學界中仍存在著所謂的「四大叛徒」。一氧化碳 (CO)、二氧化碳 (CO₂)、構成大理石主要成分的碳酸鹽類 (如 CaCO₃)，以及劇毒的氰化物 (如 KCN)。這四名嫌疑犯雖然結構中都清晰可見碳元素，但由於它們的化學行為更接近無機物，因此在法理上被嚴格地排除在有機物名單之外。認清這些叛徒，是避免冤假錯案的首要任務。", unsafe_allow_html=True)

        st.markdown("#### 🧪 破壞性鑑識：乾餾與燃燒")
        st.markdown("　　為了撥開物質外表的偽裝，我們必須動用破壞性的檢驗手段。最經典的鑑識法是「乾餾」：將物質用鋁箔紙包覆並「隔絕空氣加熱」。在這個封閉的高溫刑求下，物質會被迫解體。逸出的氣體中包含了可燃的一氧化碳、甲烷與氫氣；流出的液體除了黑色焦油，最關鍵的是會產生能使石蕊試紙變紅的「醋酸」；最後留在原地的黑色殘渣，就是純粹的碳元素。", unsafe_allow_html=True)
        st.markdown("　　另一種直覺的判定法是「燃燒檢驗」。當氣體通入澄清石灰水產生混濁時，證明了二氧化碳 (CO₂) 的存在，進而推導出原物質含有「碳」元素；而當氣體與乾燥的藍色氯化亞鈷試紙接觸，使其轉變為粉紅色時，則證明了水分子 (H₂O) 的生成，這代表原物質的骨架中隱藏著「氫」元素。", unsafe_allow_html=True)

    st.write("---")

    # ==========================================
    # 🧬 3D 引擎區 (法庭呈堂證供)
    # ==========================================
    st.markdown("#### 🧬 呈堂證供：同分異構物的雙面嬌娃")
    
    st.markdown("　　在有機化學的犯罪現場，存在著一種極其狡猾的現象：**同分異構**。這代表兩名嫌犯雖然擁有一模一樣的原子種類與數量（分子式相同，都是 C₂H₆O），但因為原子在空間中的「排列結構」截然不同，導致它們在物理與化學性質上出現了天差地遠的表現。", unsafe_allow_html=True)
    
    st.markdown("　　請檢察官親手旋轉下方的 3D 證物：左邊是常溫下為液體、可作為消毒與飲用的**乙醇**；右邊則是常溫下為氣體、作為燃料使用的**甲醚**。在法庭上，長得一樣（分子式相同），絕對不代表無罪！", unsafe_allow_html=True)
    
    html_code = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
    <div style="display: flex; justify-content: space-around; font-family: sans-serif; gap: 10px;">
        <div style="text-align: center; background: #fdfcf9; padding: 10px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-top: 0; font-size: 18px;">證物 A：乙醇 (Ethanol)</h4>
            <div id="container-ethanol" style="height: 250px; width: 100%; position: relative;"></div>
            <p style="font-size: 13px; color: #64748b; margin-top: 5px;">骨架：C - C - O (液體，可消毒)</p>
        </div>
        <div style="text-align: center; background: #fdfcf9; padding: 10px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-top: 0; font-size: 18px;">證物 B：甲醚 (Dimethyl Ether)</h4>
            <div id="container-ether" style="height: 250px; width: 100%; position: relative;"></div>
            <p style="font-size: 13px; color: #64748b; margin-top: 5px;">骨架：C - O - C (氣體，作燃料)</p>
        </div>
    </div>
    <div style="text-align: center; background: #1e293b; color: white; padding: 8px; border-radius: 8px; font-size: 14px; margin-top: 15px;">
        👆 <b>檢視證物</b>：按住滑鼠拖曳可 360° 旋轉立體分子，滾輪可縮放。<br>
        ( <b>⚫灰</b>：碳 C | <b>🔴紅</b>：氧 O | <b style="color:#60a5fa;">🔵藍</b>：氫 H )
    </div>
    <script>
        $(document).ready(function() {
            let config = {stick: {radius: 0.15, colorscheme: 'Jmol'}, sphere: {scale: 0.3, colorscheme: 'Jmol'}};
            let h_config = {stick: {radius: 0.15, color: '#3b82f6'}, sphere: {scale: 0.3, color: '#3b82f6'}};
            
            let v1 = $3Dmol.createViewer("container-ethanol", {backgroundColor: "white"});
            $3Dmol.download("cid:702", v1, {}, function() {
                v1.setStyle({}, config); v1.setStyle({elem: 'H'}, h_config);
                v1.zoomTo(); v1.render();
            });

            let v2 = $3Dmol.createViewer("container-ether", {backgroundColor: "white"});
            $3Dmol.download("cid:8254", v2, {}, function() {
                v2.setStyle({}, config); v2.setStyle({elem: 'H'}, h_config);
                v2.zoomTo(); v2.render();
            });
        });
    </script>
    """
    components.html(html_code, height=450)
    st.write("---")

    # ==========================================
    # 📖 續讀：四大家族 (強化烴類描述)
    # ==========================================
    with st.container():
        st.markdown("#### 🎭 犯罪集團的四大分支")
        
        st.markdown("　　當確認了有機物的身份後，檢方通常會依據嫌犯身上的「特徵原子團」進行分類歸檔。首先是**【烴類集團】**，它們只由碳（C）與氫（H）兩種元素組成，沒有其他雜質。這個集團的物理狀態有著嚴格的規律：**碳原子數目越少，常溫下呈現「氣態」**（例如只有 1 個碳的甲烷 CH₄，是天然氣的主力）；而**隨著碳數不斷增加，它們會逐漸變得沉重，轉為「液態」，甚至是「固態」**。", unsafe_allow_html=True)
        
        st.markdown("　　接著是**【醇類集團】**，帶有羥基 (-OH)。雖然乙醇 (C₂H₅OH) 是安全的，但名稱極為相似的「甲醇 (CH₃OH)」卻是劇毒的工業用木精，誤食會導致失明或死亡！**【有機酸集團】**帶有羧基 (-COOH)，能讓溶液呈現酸性，如螞蟻分泌的甲酸與廚房的醋酸。最後，由有機酸與醇類在濃硫酸 (催化與脫水) 的逼迫下，會結合出具有水果香氣、密度比水小且難溶於水的**【酯類集團】**。", unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區 (雙重打臉時刻)
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！警方在現場查獲了兩樣證物，檢方的指控根本不合邏輯！<br><br><b>【關於證物一：不明液體】</b> 檢方說這是一桶極度危險的烴類液體！但我的當事人說，這桶『液體』其實只是天然氣的主成分『甲烷 (CH₄)』！既然是甲烷，那就非常安全了！<br><br><b>【關於證物二：毒酒案】</b> 檢方指控我的當事人用標示為 <b>CH₃OH</b> 的液體企圖謀殺！但 CH₃OH 也是醇類，跟我們常喝的乙醇一樣！而且我們隔絕空氣加熱後，收集到的液體能讓『藍色氯化亞鈷試紙變粉紅色』，這證明了它產生了酸性的醋酸，所以這只是一瓶無害的食用醋！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # 問題 1：打臉烴類狀態
    st.markdown("##### ⚖️ 第一回合：針對【證物一 (烴類)】的異議")
    q1 = st.radio(
        "請指出辯方對「甲烷狀態」的無知盲點：",
        [
            "A. 「異議！甲烷含有氧原子，根本不是烴類！」",
            "B. 「異議！甲烷 (CH₄) 只有 1 個碳原子，碳數極少，常溫下絕對是『氣態』！它怎麼可能是一桶『液體』，辯方在說謊！」",
            "C. 「異議！烴類的碳數越少，狀態越重。所以甲烷常溫下應該是『固態』，不可能是液體！」"
        ],
        index=None,
        key="q1"
    )

    # 問題 2：打臉甲醇與檢驗法
    st.markdown("##### ⚖️ 第二回合：針對【證物二 (毒酒案)】的異議")
    q2 = st.radio(
        "請指出辯方對「甲醇毒性與試紙檢驗」的致命錯誤：",
        [
            "A. 「異議！CH₃OH 是劇毒的『甲醇 (木精)』！且氯化亞鈷試紙變粉紅色證明的是產生了『水 (H₂O)』，根本不是醋酸！」",
            "B. 「異議！甲醇跟乙醇是同分異構物，性質完全一樣，所以被害人是自己醉倒的，跟液體無關！」",
            "C. 「異議！隔絕空氣加熱是燃燒法，應該用澄清石灰水來檢驗，辯方律師的檢驗流程完全違法！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("💥 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備，再拍桌抗議！")
        elif q1.startswith("B") and q2.startswith("A"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官重重敲下法槌：「檢察官說得完全正確！甲烷常溫下是氣體，甲醇是劇毒，而氯化亞鈷檢驗的是水分！辯方律師的化學常識簡直一塌糊塗！」\n\n✅ 成功戳破所有謊言，審判勝利，準備進入實戰演練！")
            return True
        else:
            # 針對答錯的地方給予個別提示
            error_msg = "❌ 異議駁回！法官認為你的論述有破綻：\n"
            if not q1.startswith("B"):
                error_msg += "\n👉 **【關於證物一】** 請重新翻閱卷宗，確認烴類的『碳數多寡』與『物理狀態 (氣/液/固)』的關係！"
            if not q2.startswith("A"):
                error_msg += "\n👉 **【關於證物二】** 請重新確認 CH₃OH 的『真實毒性』，以及藍色氯化亞鈷試紙究竟是檢驗什麼物質的？"
            st.error(error_msg)
            
    return False
