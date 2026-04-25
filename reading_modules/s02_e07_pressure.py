import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS 覆寫
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

    st.markdown("### ⚖️ 黎明物理法庭 S02E07：高壓淘汰賽之壓力物理全書")
    
    # 審判長對白
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『在充滿極限挑戰的淘汰賽中，壓力無處不在。從女團腳下細跟高跟鞋產生的驚人壓強，到水上舞台底部承受的巨大液壓，物理定律從不手下留情。檢察官，請研讀這份涵蓋固、液、氣三態的壓力卷宗，並在下方的【互動實驗室】中，親眼見證水壓「深度」的殘酷陷阱！』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：固體壓力與垂直作用力")
        
        st.markdown("　　在物理學中，「壓力」代表單位面積上所承受的力量大小（公式：$P = F / A$）。請注意，這裡的「力 ($F$)」絕對不是單純的體重，它必須是與接觸面「**呈現 90 度直角**」的垂直作用力。大象雖然重達 3000 公斤，但四肢腳掌寬闊，力量被大幅分散；而 45 公斤的女團成員若穿著尖細的高跟鞋，力量集中在極小的點上，產生的「壓力 ($P$)」極其驚人，足以在地毯上踩出深坑！", unsafe_allow_html=True)

        st.markdown("#### 📁 檢方機密卷宗：液體壓力的深度陷阱與帕斯卡魔法")

        st.markdown("　　液體壓力來自於液體本身的重量。計算液體壓力時，公式非常簡單無情：**壓力 = 深度 × 密度 ($P = h \\times d$)**。這裡隱藏著考場上最致命的陷阱：所謂的「深度」，絕對、必須是**「從水面向下算」**的垂直距離！水壓只跟深度與密度有關，無論舞台上的水槽是寬如大海還是細如水管，只要深度一樣，底部的壓力就一模一樣（這也是連通管原理的基礎）。此外，液體壓力沒有特定方向，但它接觸到容器邊緣時，必定會與接觸面**保持垂直**。", unsafe_allow_html=True)
        
        st.markdown("　　若將液體裝在「密閉容器」中，便能觸發「**帕斯卡原理**」。當你在密閉液體的一端施加壓力時，這股壓力會「大小不變」地傳遞到液體的每一個角落。利用小活塞推動大活塞，就能達到以小搏大、撐起千斤重舞台道具的「省力」效果。但記住能量守恆定律：雖然省了力，卻必須付出推動極長距離的代價，絕對「不省功」。", unsafe_allow_html=True)

        st.markdown("#### 📁 檢方機密卷宗：大氣壓力的絕對防禦")

        st.markdown("　　我們生活在空氣的深海中，承受著空氣重量帶來的「大氣壓力」。經典的**馬德堡半球實驗**證明了大氣壓力的存在且威力驚人；而義大利科學家**托里切利**則用水銀精準測量出它的數值：1 大氣壓 (1 atm) 剛好可以支撐起 **76 公分高的垂直水銀柱**。只要玻璃管不漏氣，無論管子多粗或傾斜到什麼角度，大氣壓能撐起的水銀「垂直高度」永遠是 76 公分！", unsafe_allow_html=True)

    st.write("---")
    
    # ==========================================
    # 🕹️ HTML5 互動實驗室 (液體壓力模擬器)
    # ==========================================
    st.markdown("#### 🛠️ 互動實驗室：水下壓力的深度陷阱")
    st.info("👇 **請調整「水面高度」與「液體密度」，觀察水槽壁上 A、B、C 三個開口的噴水狀況。特別注意「深度」是如何計算的，以及它如何決定了噴水的距離！**")
    
    html_code = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h4 style="margin-top: 0; color: #334155; text-align: center;">🌊 液體壓力觀測水槽</h4>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-bottom: 20px;">
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; min-width: 200px;">
                <label style="font-weight: bold; color: #0f172a;">水面總高度: <span id="level-val" style="color: #3b82f6;">80</span> cm</label>
                <input type="range" id="water-level" min="0" max="100" value="80" step="5" style="width: 100%; margin-top: 10px; cursor: pointer;">
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; min-width: 200px;">
                <label style="font-weight: bold; color: #0f172a;">液體種類 (密度 d)</label><br>
                <select id="liquid-density" style="width: 100%; margin-top: 10px; padding: 5px; border-radius: 4px; cursor: pointer; font-size: 14px;">
                    <option value="1.0">純水 (d = 1.0 g/cm³)</option>
                    <option value="1.2">食鹽水 (d = 1.2 g/cm³)</option>
                    <option value="0.8">酒精 (d = 0.8 g/cm³)</option>
                </select>
            </div>
        </div>

        <div style="position: relative; width: 100%; max-width: 500px; height: 350px; margin: 0 auto; display: flex;">
            
            <div style="width: 150px; display: flex; flex-direction: column; justify-content: space-between; padding-bottom: 30px;">
                <div id="data-C" style="background: #fee2e2; padding: 8px; border-radius: 6px; font-size: 13px; font-weight: bold; border: 1px solid #f87171;">
                    開口 C (高 70cm)<br><span style="color: #b91c1c;">深度 = 0 cm<br>壓力 = 0.0</span>
                </div>
                <div id="data-B" style="background: #fef3c7; padding: 8px; border-radius: 6px; font-size: 13px; font-weight: bold; border: 1px solid #fcd34d;">
                    開口 B (高 40cm)<br><span style="color: #b45309;">深度 = 0 cm<br>壓力 = 0.0</span>
                </div>
                <div id="data-A" style="background: #dcfce7; padding: 8px; border-radius: 6px; font-size: 13px; font-weight: bold; border: 1px solid #86efac;">
                    開口 A (高 10cm)<br><span style="color: #15803d;">深度 = 0 cm<br>壓力 = 0.0</span>
                </div>
            </div>

            <div style="position: relative; width: 350px; height: 300px; border-bottom: 8px solid #475569; border-left: 8px solid #475569; margin-top: 20px;">
                
                <div id="water-body" style="position: absolute; bottom: 0; left: 0; width: 100px; height: 80%; background-color: rgba(59, 130, 246, 0.4); border-top: 3px solid #2563eb; transition: height 0.2s, background-color 0.3s;"></div>
                
                <div style="position: absolute; bottom: 70%; left: 96px; width: 12px; height: 10px; background: #cbd5e1; border-radius: 2px;"></div>
                <div id="spray-C" style="position: absolute; bottom: 70%; left: 108px; width: 0px; height: 10px; background: rgba(59, 130, 246, 0.4); border-radius: 0 10px 10px 0; transition: width 0.2s, background-color 0.3s;"></div>

                <div style="position: absolute; bottom: 40%; left: 96px; width: 12px; height: 10px; background: #cbd5e1; border-radius: 2px;"></div>
                <div id="spray-B" style="position: absolute; bottom: 40%; left: 108px; width: 0px; height: 10px; background: rgba(59, 130, 246, 0.4); border-radius: 0 10px 10px 0; transition: width 0.2s, background-color 0.3s;"></div>

                <div style="position: absolute; bottom: 10%; left: 96px; width: 12px; height: 10px; background: #cbd5e1; border-radius: 2px;"></div>
                <div id="spray-A" style="position: absolute; bottom: 10%; left: 108px; width: 0px; height: 10px; background: rgba(59, 130, 246, 0.4); border-radius: 0 10px 10px 0; transition: width 0.2s, background-color 0.3s;"></div>
                
                <div id="depth-marker" style="position: absolute; right: -20px; top: 20%; height: 0%; border-left: 2px dashed #0f172a; display: none;"></div>
            </div>
        </div>

        <div style="text-align: center; margin-top: 15px;">
            <button id="reset-btn" style="background-color: #64748b; color: white; border: none; padding: 8px 20px; border-radius: 6px; font-weight: bold; cursor: pointer;">🔄 重置水槽</button>
        </div>
    </div>

    <script>
        const levelInput = document.getElementById('water-level');
        const densitySelect = document.getElementById('liquid-density');
        const levelVal = document.getElementById('level-val');
        const waterBody = document.getElementById('water-body');
        
        const sprayA = document.getElementById('spray-A');
        const sprayB = document.getElementById('spray-B');
        const sprayC = document.getElementById('spray-C');
        
        const dataA = document.getElementById('data-A');
        const dataB = document.getElementById('data-B');
        const dataC = document.getElementById('data-C');

        // 開口離底部的真實高度 (100% = 100cm)
        const H_A = 10;
        const H_B = 40;
        const H_C = 70;

        function updateTank() {
            let L = parseInt(levelInput.value);
            let d = parseFloat(densitySelect.value);
            levelVal.innerText = L;
            
            // 更新水體高度 (1% = 1cm)
            waterBody.style.height = L + '%';

            // 顏色隨密度改變
            let liquidColor = "rgba(59, 130, 246, 0.4)"; // 水 (藍)
            if (d == 1.2) liquidColor = "rgba(16, 185, 129, 0.4)"; // 鹽水 (綠)
            if (d == 0.8) liquidColor = "rgba(245, 158, 11, 0.4)"; // 酒精 (橘)
            waterBody.style.backgroundColor = liquidColor;

            // 計算與更新開口 A
            let depthA = Math.max(0, L - H_A);
            let pA = depthA * d;
            dataA.innerHTML = `開口 A (高 10cm)<br><span style="color: #15803d;">深度 = ${depthA} cm<br>壓力 = ${pA.toFixed(1)}</span>`;
            sprayA.style.width = (Math.sqrt(depthA) * 15) + 'px'; // 開根號做視覺縮放
            sprayA.style.backgroundColor = liquidColor;

            // 計算與更新開口 B
            let depthB = Math.max(0, L - H_B);
            let pB = depthB * d;
            dataB.innerHTML = `開口 B (高 40cm)<br><span style="color: #b45309;">深度 = ${depthB} cm<br>壓力 = ${pB.toFixed(1)}</span>`;
            sprayB.style.width = (Math.sqrt(depthB) * 15) + 'px';
            sprayB.style.backgroundColor = liquidColor;

            // 計算與更新開口 C
            let depthC = Math.max(0, L - H_C);
            let pC = depthC * d;
            dataC.innerHTML = `開口 C (高 70cm)<br><span style="color: #b91c1c;">深度 = ${depthC} cm<br>壓力 = ${pC.toFixed(1)}</span>`;
            sprayC.style.width = (Math.sqrt(depthC) * 15) + 'px';
            sprayC.style.backgroundColor = liquidColor;
        }

        levelInput.addEventListener('input', updateTank);
        densitySelect.addEventListener('change', updateTank);
        
        document.getElementById('reset-btn').addEventListener('click', () => {
            levelInput.value = 80;
            densitySelect.value = "1.0";
            updateTank();
        });

        // 初始繪製
        updateTank();
    </script>
    """
    components.html(html_code, height=600)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    # 辯護律師對白
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！檢方對於液體壓力與大氣壓力的說法完全違反常識！<br><br><b>【關於水壓】</b> 舞台上的大水池面積那麼大、裝了幾十噸的水！底部的水壓絕對比只有一根吸管粗的細水管大上一萬倍！壓力就是看總水量啊！<br><br><b>【關於大氣壓】</b> 托里切利實驗說大氣壓能撐起 76 公分的水銀柱。但如果我們換成『超粗』的玻璃管，水銀變重了，大氣壓肯定撐不到 76 公分！如果把管子傾斜，水銀柱的垂直高度一定也會變矮！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "⚖️ 第一回合：請指出辯方對「液體壓力」的致命謬誤：",
        [
            "A. 「異議！液體壓力公式是 P = 深度 × 密度。壓力大小只跟『深度』有關，與容器的形狀、面積或總水量『完全無關』！」",
            "B. 「異議！大水池的水壓確實比較大，但是因為水的密度會因為體積變大而變小，所以兩者剛好抵消！」",
            "C. 「異議！壓力是看距離底部的多高，水池很深，所以底部壓力會變小！」"
        ],
        index=None,
        key="q1"
    )

    st.write("<br>", unsafe_allow_html=True)

    q2 = st.radio(
        "⚖️ 第二回合：請指出辯方對「托里切利實驗」的致命錯誤：",
        [
            "A. 「異議！大氣壓只能撐起 76 公分，若換成粗管子水銀會自動蒸發來減輕重量！」",
            "B. 「異議！大氣壓力能支撐的是液體產生的『垂直壓力』。只要是同一個大氣壓，無論管子多粗、形狀如何或是否傾斜，水銀的『垂直高度』永遠是 76 公分！」",
            "C. 「異議！大氣壓力是因為地球自轉產生的，所以管子傾斜時，水銀會跟著地球引力流出來！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("⚖️ 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備！")
        elif q1.startswith("A") and q2.startswith("B"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！從觀測水槽中可以鐵證如山地看出，壓力只受『深度』支配，與寬度無關。而托里切利實驗中的大氣壓力支撐的正是『垂直液體壓力』，管子的粗細與傾斜完全不影響垂直高度。辯方律師的常識不過是未經科學檢驗的錯覺！」\n\n✅ 成功戳破所有謊言，審判勝利，成功捍衛了壓力學的物理真相！")
            return True
        else:
            error_msg = "❌ 異議駁回！法官認為你的推理有破綻：\n"
            if not q1.startswith("A"):
                error_msg += "\n👉 **【關於液體壓力】** 請重新閱讀卷宗，公式 $P=h\\times d$ 中，到底有沒有包含『面積』或『總水量』？"
            if not q2.startswith("B"):
                error_msg += "\n👉 **【關於托里切利實驗】** 大氣壓力撐起的是一個『垂直壓力』，改變管子粗細真的會改變支撐的垂直高度嗎？"
            st.error(error_msg)
            
    return False
