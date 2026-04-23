import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    st.markdown("### ⚖️ 黎明化學法庭 S02E01：碳基生命的審判")
    st.info("💡 **審判長 黎明**：『法庭之上，沒有模稜兩可的狡辯。證據與化學鐵律，是判決的唯一標準。檢察官，準備好揭穿辯方的謊言了嗎？』")
    
    # ==========================================
    # 📖 深度素養閱讀區 (法庭證據檔案)
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：有機化學的本質與迷思")
        
        st.write("""
        在科學發展的早期，化學家們普遍被一種稱為「生命力理論」的神秘面紗所籠罩。他們固執地認為，凡是有機化合物，必然只能由具有生命力的生物體製造出來。然而，這個延續已久的神話在 1828 年被德國科學家烏拉徹底擊碎。他在實驗室中，僅僅透過加熱無機物，就成功合成出了原本只存在於生物體內的有機物——「尿素」。這一擊不僅宣告了生命力理論的終結，也迫使科學界重新定義有機化學。
        """)

        st.write("""
        現代法庭將有機化合物定義為「含碳的化合物」。然而，即便流著碳元素的血脈，化學界中仍存在著所謂的「四大叛徒」。一氧化碳 (CO)、二氧化碳 (CO₂)、構成大理石主要成分的碳酸鹽類 (如 CaCO₃)，以及劇毒的氰化物 (如 KCN)。這四名嫌疑犯雖然結構中都清晰可見碳元素，但由於它們的化學行為更接近無機物，因此在法理上被嚴格地排除在有機物名單之外。認清這些叛徒，是避免冤假錯案的首要任務。
        """)

        st.markdown("#### 🧪 破壞性鑑識：乾餾與燃燒")
        st.write("""
        為了撥開物質外表的偽裝，我們必須動用破壞性的檢驗手段。最經典的鑑識法是「乾餾」：將物質用鋁箔紙包覆並「隔絕空氣加熱」。在這個封閉的高溫刑求下，物質會被迫解體。逸出的氣體中包含了可燃的一氧化碳、甲烷與氫氣；流出的液體除了黑色焦油，最關鍵的是會產生能使石蕊試紙變紅的「醋酸」；最後留在原地的黑色殘渣，就是純粹的碳元素。
        """)

        st.write("""
        另一種直覺的判定法是「燃燒檢驗」。當氣體通入澄清石灰水產生混濁時，證明了二氧化碳 (CO₂) 的存在，進而推導出原物質含有「碳」元素；而當氣體與乾燥的藍色氯化亞鈷試紙接觸，使其轉變為粉紅色時，則證明了水分子 (H₂O) 的生成，這代表原物質的骨架中隱藏著「氫」元素。
        """)

    st.write("---")

    # ==========================================
    # 🧬 3D 引擎區 (法庭呈堂證供)
    # ==========================================
    st.markdown("#### 🧬 呈堂證供：同分異構物的雙面嬌娃")
    st.write("""
    在有機化學的犯罪現場，存在著一種極其狡猾的現象：**同分異構**。這代表兩名嫌犯雖然擁有一模一樣的原子種類與數量（分子式相同，都是 C₂H₆O），但因為原子在空間中的「排列結構」截然不同，導致它們在物理與化學性質上出現了天差地遠的表現。
    
    請檢察官親手旋轉下方的 3D 證物：左邊是常溫下為液體、可作為消毒與飲用的**乙醇**；右邊則是常溫下為氣體、作為燃料使用的**甲醚**。在法庭上，長得一樣（分子式相同），絕對不代表無罪！
    """)
    
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
    components.html(html_code, height=400)
    st.write("---")

    # ==========================================
    # 📖 續讀：四大家族
    # ==========================================
    with st.container():
        st.markdown("#### 🎭 犯罪集團的四大分支")
        st.write("""
        當確認了有機物的身份後，檢方通常會依據嫌犯身上的「特徵原子團」進行分類歸檔。
        **烴類集團**只由碳與氫組成，碳數少的甲烷 (CH₄) 是天然氣的氣態主力，碳數越多則轉為液態甚至固態。
        **醇類集團**帶有羥基 (-OH)。請特別注意，雖然乙醇 (C₂H₅OH) 是安全的，但名稱極為相似的「甲醇 (CH₃OH)」卻是劇毒的工業用木精，誤食會導致失明或死亡！
        **有機酸集團**帶有羧基 (-COOH)，能讓溶液呈現酸性，如螞蟻分泌的甲酸與廚房的醋酸。
        最後，由有機酸與醇類在濃硫酸 (催化與脫水) 的逼迫下，會結合出具有水果香氣、密度比水小且難溶於水的**酯類集團**。
        """)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區 (打臉時刻)
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的偽證！")
    st.error("🗣️ **辯護律師 韓流**：\n> 「法官大人！檢方指控我的當事人用標示為 **CH₃OH** 的液體企圖謀殺，這簡直是無稽之談！CH₃OH 也是醇類，跟我們常喝的乙醇一樣，頂多就是讓人喝醉而已！\n> \n> 而且，我們在實驗室把這瓶液體『隔絕空氣加熱』後，收集到的液體能讓『藍色氯化亞鈷試紙變粉紅色』！這證明了它產生了酸性的醋酸，所以這只是一瓶無害的食用醋！我的當事人是無辜的！」")
    
    q1 = st.radio(
        "身為王牌檢察官，請立刻拍桌大喊「異議阿里（Objection）！」，並用化學鐵律給予致命一擊：",
        [
            "A. 「異議！CH₃OH 是酯類，不可能讓人喝醉！而且氯化亞鈷試紙變色證明的是產生了二氧化碳！」",
            "B. 「異議！甲醇跟乙醇是同分異構物，性質完全一樣，所以被害人是自己醉倒的，跟液體無關！」",
            "C. 「異議！CH₃OH 是劇毒的『甲醇 (木精)』，會致盲甚至喪命！而且氯化亞鈷試紙變粉紅色證明的是產生了『水』，根本不是醋酸！」",
            "D. 「異議！隔絕空氣加熱是燃燒法，應該用澄清石灰水來檢驗，辯方律師的檢驗流程完全違法！」"
        ],
        index=None
    )
    
    if st.button("⚖️ 提出異議 (Objection!)", use_container_width=True):
        if q1 is None:
            st.warning("檢察官，請先選擇你要提出的反駁論點！")
        elif q1.startswith("C"):
            st.success("💥 異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！甲醇是劇毒，而氯化亞鈷檢驗的是水分，辯護律師的化學常識簡直一塌糊塗！」\n\n✅ 成功戳破謊言，審判勝利，準備進入實戰演練！")
            return True
        else:
            st.error("❌ 異議駁回！\n\n法官皺眉：「檢察官，你的化學邏輯漏洞百出。請重新翻閱『破壞性鑑識』與『犯罪集團分支』的卷宗，搞清楚甲醇的毒性與試紙的對應關係！」")
            
    return False
