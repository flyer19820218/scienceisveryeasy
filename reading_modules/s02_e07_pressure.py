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
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『在充滿極限挑戰的淘汰賽中，壓力無處不在。從女團腳下細跟高跟鞋產生的驚人壓強，到水上舞台底部承受的巨大液壓，物理定律從不手下留情。檢察官，請研讀這份涵蓋固、液、氣三態的壓力卷宗，並在下方的【三核互動實驗室】中，親眼見證海綿凹陷的極限、水柱的拋物線，以及大氣壓力的絕對防禦！』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：固體壓力與垂直作用力")
        
        st.markdown("　　在物理學中，「壓力」代表單位面積上所承受的力量大小（公式：$P = F / A$）。請注意，這裡的「力 ($F$)」絕對不是單純的總重量，它必須是與接觸面「**呈現 90 度直角**」的垂直作用力。大象雖然重達 3000 公斤，但四肢腳掌寬闊，力量被大幅分散；而 45 公斤的女團成員若穿著尖細的高跟鞋，力量集中在極小的點上，產生的「壓力 ($P$)」極其驚人，足以在地毯上踩出深坑！", unsafe_allow_html=True)

        st.markdown("#### 📁 檢方機密卷宗：液體壓力的深度陷阱與帕斯卡魔法")

        st.markdown("　　液體壓力來自於液體本身的重量。計算液體壓力時，公式非常簡單無情：**壓力 = 深度 × 密度 ($P = h \\times d$)**。這裡隱藏著考場上最致命的陷阱：所謂的「深度」，絕對、必須是**「從水面向下算」**的垂直距離！水壓只跟深度與密度有關，無論舞台上的水槽是寬如大海還是細如水管，只要深度一樣，底部的壓力就一模一樣。此外，水柱噴出時受地球引力影響會形成拋物線，水壓越大的開口，水噴得越遠。", unsafe_allow_html=True)
        
        st.markdown("　　若將液體裝在「密閉容器」中，便能觸發「**帕斯卡原理**」。當你在密閉液體的一端施加壓力時，這股壓力會「大小不變」地傳遞到液體的每一個角落。利用小活塞推動大活塞，就能達到以小搏大、撐起千斤重舞台道具的「省力」效果。但記住能量守恆定律：雖然省了力，卻必須付出推動極長距離的代價，絕對「不省功」。", unsafe_allow_html=True)

        st.markdown("#### 📁 檢方機密卷宗：大氣壓力的絕對防禦")

        st.markdown("　　我們生活在空氣的深海中，承受著空氣重量帶來的「大氣壓力」。經典的**馬德堡半球實驗**將兩個半球合在一起並抽真空，當內部沒有空氣壓力往外推時，外部龐大的大氣壓力就會將半球死死壓住，即使動用數匹馬也難以拉開！而義大利科學家**托里切利**則用水銀精準測量出它的數值：1 大氣壓 (1 atm) 剛好可以支撐起 **76 公分高的垂直水銀柱**。", unsafe_allow_html=True)

    st.write("---")
    
    # ==========================================
    # 🕹️ 實驗室 A：固體壓力
    # ==========================================
    st.markdown("#### 🛠️ 實驗室 A：固體壓力與海綿凹陷測試")
    st.info("👇 **請調整「接觸面積」與「施力角度」。注意！只有『垂直』壓下去的分力才會產生壓力，壓力越大，海綿凹陷越深！**")
    
    solid_html = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
        <h4 style="margin-top: 0; color: #334155;">🧱 固體壓強凹陷模擬器</h4>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: space-around; gap: 20px; margin-bottom: 20px;">
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; width: 45%;">
                <label style="font-weight: bold; color: #0f172a;">擺放方式 (受力面積 A)</label><br>
                <select id="area-select" style="width: 100%; margin-top: 10px; padding: 8px; border-radius: 4px; cursor: pointer; font-size: 16px;">
                    <option value="50">🧳 平放 (大面積, A=50)</option>
                    <option value="10">📱 直立 (小面積, A=10)</option>
                </select>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; width: 45%;">
                <label style="font-weight: bold; color: #0f172a;">施力角度 (總力 F=100)</label><br>
                <select id="angle-select" style="width: 100%; margin-top: 10px; padding: 8px; border-radius: 4px; cursor: pointer; font-size: 16px;">
                    <option value="90">⬇️ 垂直往下壓 (90度)</option>
                    <option value="60">↘️ 斜斜往下壓 (60度)</option>
                    <option value="30">➡️ 幾乎平推 (30度)</option>
                </select>
            </div>
        </div>

        <div style="display: flex; justify-content: space-around; background: #fef3c7; padding: 15px; border-radius: 8px; border: 1px solid #fde68a; margin-bottom: 20px;">
            <div>
                <div style="font-size: 14px; color: #92400e; font-weight: bold;">垂直作用力 (F⊥)</div>
                <div style="font-size: 24px; font-weight: bold; color: #b45309;"><span id="force-val">100</span> kgw</div>
            </div>
            <div>
                <div style="font-size: 14px; color: #065f46; font-weight: bold;">產生壓力 (P = F⊥/A)</div>
                <div style="font-size: 24px; font-weight: bold; color: #047857;"><span id="pressure-val">2.0</span></div>
            </div>
        </div>

        <div style="position: relative; width: 100%; max-width: 400px; height: 250px; margin: 0 auto; background: white; border: 1px solid #cbd5e1; border-radius: 8px; overflow: hidden; display: flex; justify-content: center; align-items: flex-end;">
            
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 60px; background-color: #fcd34d; border-top: 4px solid #f59e0b;"></div>
            
            <div id="dent-mask" style="position: absolute; bottom: 30px; width: 120px; height: 30px; background-color: white; border-radius: 0 0 50% 50%; transition: height 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), width 0.3s;"></div>

            <div id="solid-box" style="position: absolute; bottom: 60px; width: 100px; height: 40px; background-color: #475569; border: 2px solid #1e293b; border-radius: 2px; transition: bottom 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), width 0.3s, height 0.3s;"></div>

            <svg id="force-arrow" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 10; transition: all 0.3s;">
                <defs>
                    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                        <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626" />
                    </marker>
                </defs>
                <line id="f-line" x1="200" y1="20" x2="200" y2="120" stroke="#dc2626" stroke-width="4" marker-end="url(#arrowhead)" />
            </svg>
        </div>
    </div>

    <script>
        const areaSelect = document.getElementById('area-select');
        const angleSelect = document.getElementById('angle-select');
        const forceVal = document.getElementById('force-val');
        const pressureVal = document.getElementById('pressure-val');
        const solidBox = document.getElementById('solid-box');
        const dentMask = document.getElementById('dent-mask');
        const fLine = document.getElementById('f-line');

        function updateSolidPhysics() {
            let A = parseFloat(areaSelect.value);
            let angleDeg = parseFloat(angleSelect.value);
            let totalF = 100;
            
            let angleRad = angleDeg * (Math.PI / 180);
            let F_perp = totalF * Math.sin(angleRad);
            let P = F_perp / A;
            
            forceVal.innerText = F_perp.toFixed(1);
            pressureVal.innerText = P.toFixed(1);

            let boxWidth = A == 50 ? 120 : 40;
            let boxHeight = A == 50 ? 40 : 120;
            solidBox.style.width = boxWidth + 'px';
            solidBox.style.height = boxHeight + 'px';
            
            dentMask.style.width = (boxWidth + 20) + 'px';

            let dentDepth = (P / 10) * 25; // 壓力最大10，最深陷25px
            solidBox.style.bottom = (60 - dentDepth) + 'px';
            dentMask.style.height = (30 + dentDepth) + 'px';

            let endY = 250 - (60 - dentDepth) - boxHeight - 5; 
            let endX = 200;
            
            let arrowLen = 100;
            let startX = endX - arrowLen * Math.cos(angleRad);
            let startY = endY - arrowLen * Math.sin(angleRad);

            fLine.setAttribute('x1', startX);
            fLine.setAttribute('y1', startY);
            fLine.setAttribute('x2', endX);
            fLine.setAttribute('y2', endY);
        }

        areaSelect.addEventListener('change', updateSolidPhysics);
        angleSelect.addEventListener('change', updateSolidPhysics);
        updateSolidPhysics();
    </script>
    """
    components.html(solid_html, height=580)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 🕹️ 實驗室 B：液體壓力 (含右邊框與拋物線)
    # ==========================================
    st.markdown("#### 🛠️ 實驗室 B：液體壓力觀測水槽 (平拋拋物線)")
    st.info("👇 **請調整「水面高度」與「液體密度」，觀察水壓是如何決定拋物線水柱的射程！**")

    liquid_html = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        
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

            <div style="position: relative; width: 350px; height: 300px; margin-top: 20px;">
                
                <div style="position: absolute; top: 0; left: 0; width: 150px; height: 100%; border-left: 8px solid #475569; border-bottom: 8px solid #475569; border-right: 8px solid #475569; border-radius: 0 0 4px 4px; box-sizing: border-box; z-index: 10;">
                    <div style="position: absolute; right: -8px; top: 26px; width: 8px; height: 8px; background: white;"></div> <div style="position: absolute; right: -8px; top: 176px; width: 8px; height: 8px; background: white;"></div> <div style="position: absolute; right: -8px; top: 266px; width: 8px; height: 8px; background: white;"></div> </div>
                
                <div id="water-body" style="position: absolute; bottom: 8px; left: 8px; width: 134px; height: 80%; background-color: rgba(59, 130, 246, 0.6); transition: height 0.3s, background-color 0.3s; z-index: 5;"></div>
                
                <svg width="350" height="300" style="position: absolute; top: 0; left: 0; z-index: 1;">
                    <path id="path-C" d="" fill="none" stroke="rgba(59, 130, 246, 0.6)" stroke-width="6" stroke-linecap="round" style="transition: d 0.3s, stroke 0.3s;" />
                    <path id="path-B" d="" fill="none" stroke="rgba(59, 130, 246, 0.6)" stroke-width="6" stroke-linecap="round" style="transition: d 0.3s, stroke 0.3s;" />
                    <path id="path-A" d="" fill="none" stroke="rgba(59, 130, 246, 0.6)" stroke-width="6" stroke-linecap="round" style="transition: d 0.3s, stroke 0.3s;" />
                </svg>
            </div>
        </div>
    </div>

    <script>
        const levelInput = document.getElementById('water-level');
        const densitySelect = document.getElementById('liquid-density');
        const levelVal = document.getElementById('level-val');
        const waterBody = document.getElementById('water-body');
        
        const pathA = document.getElementById('path-A');
        const pathB = document.getElementById('path-B');
        const pathC = document.getElementById('path-C');
        
        const dataA = document.getElementById('data-A');
        const dataB = document.getElementById('data-B');
        const dataC = document.getElementById('data-C');

        // SVG 畫布 300px 高。 100cm 對應 300px (1cm = 3px)
        const H_A = 10; // y = 300 - 30 = 270
        const H_B = 40; // y = 300 - 120 = 180
        const H_C = 70; // y = 300 - 210 = 90

        function updateLiquid() {
            let L = parseInt(levelInput.value); // 0-100
            let d = parseFloat(densitySelect.value);
            levelVal.innerText = L;
            
            waterBody.style.height = L + '%';

            let liquidColor = "rgba(59, 130, 246, 0.6)"; 
            if (d == 1.2) liquidColor = "rgba(16, 185, 129, 0.6)"; 
            if (d == 0.8) liquidColor = "rgba(245, 158, 11, 0.6)"; 
            waterBody.style.backgroundColor = liquidColor;
            pathA.setAttribute('stroke', liquidColor);
            pathB.setAttribute('stroke', liquidColor);
            pathC.setAttribute('stroke', liquidColor);

            // 拋物線公式： R = 2 * sqrt(h * H) * density_factor
            function drawSpray(pathEl, holeHeight_cm, dataEl, label) {
                let depth = Math.max(0, L - holeHeight_cm);
                let p = depth * d;
                
                // 更新數據文字
                let colors = { A: '#15803d', B: '#b45309', C: '#b91c1c' };
                dataEl.innerHTML = `開口 ${label} (高 ${holeHeight_cm}cm)<br><span style="color: ${colors[label]};">深度 = ${depth} cm<br>壓力 = ${p.toFixed(1)}</span>`;

                let startX = 148; // 水槽右側緣
                let startY = 300 - (holeHeight_cm * 3); // 轉成 px
                
                if (depth > 0) {
                    // 水平射程 R = 2 * sqrt(深度 * 孔高) * 密度係數
                    let R_px = 2 * Math.sqrt(depth * holeHeight_cm) * d * 3; // 乘 3 轉成 px
                    let endX = startX + R_px;
                    let endY = 296; // 地板高度
                    
                    // 利用二次貝茲曲線畫拋物線 (控制點在起點的水平延伸)
                    pathEl.setAttribute('d', `M ${startX} ${startY} Q ${endX} ${startY} ${endX} ${endY}`);
                } else {
                    pathEl.setAttribute('d', `M ${startX} ${startY} Q ${startX} ${startY} ${startX} ${startY}`);
                }
            }

            drawSpray(pathA, H_A, dataA, 'A');
            drawSpray(pathB, H_B, dataB, 'B');
            drawSpray(pathC, H_C, dataC, 'C');
        }

        levelInput.addEventListener('input', updateLiquid);
        densitySelect.addEventListener('change', updateLiquid);
        updateLiquid();
    </script>
    """
    components.html(liquid_html, height=520)

    st.write("<br>", unsafe_allow_html=True)

    # ==========================================
    # 🕹️ 實驗室 C：馬德堡半球 (大氣壓力)
    # ==========================================
    st.markdown("#### 🛠️ 實驗室 C：馬德堡半球抽氣挑戰")
    st.info("👇 **啟動抽氣機降低內部壓力，然後拉動馬匹力量。看看大氣壓力能頂住多強的拉扯！**")

    magdeburg_html = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
        
        <div style="display: flex; justify-content: space-around; gap: 15px; margin-bottom: 20px;">
            <div style="width: 45%;">
                <label style="font-weight: bold; color: #dc2626;">🌪️ 抽氣機 (內部真空度): <span id="vac-val">0</span>%</label>
                <input type="range" id="vac-slider" min="0" max="100" value="0" step="10" style="width: 100%; margin-top: 10px; cursor: pointer;">
            </div>
            <div style="width: 45%;">
                <label style="font-weight: bold; color: #3b82f6;">🐎 馬匹拉力: <span id="pull-val">0</span> kgw</label>
                <input type="range" id="pull-slider" min="0" max="2000" value="0" step="100" style="width: 100%; margin-top: 10px; cursor: pointer;">
            </div>
        </div>

        <div style="background-color: #e2e8f0; padding: 10px; border-radius: 8px; margin-bottom: 20px; font-size: 16px;">
            外界大氣壓力 1 atm 🆚 半球內部壓力 <span id="int-p-val" style="color:#dc2626; font-weight:bold;">1.0</span> atm<br>
            目前大氣壓扣住半球的力量： <span id="hold-val" style="color:#0f172a; font-weight:bold; font-size: 20px;">0</span> kgw
        </div>

        <div style="position: relative; width: 100%; max-width: 400px; height: 120px; margin: 0 auto; display: flex; justify-content: center; align-items: center;">
            
            <div id="hemi-left" style="width: 60px; height: 100px; background: #64748b; border-radius: 50px 0 0 50px; border: 4px solid #334155; border-right: none; position: relative; transition: transform 0.2s;">
                <div style="position: absolute; left: -30px; top: 40px; width: 30px; height: 10px; background: #3b82f6;"></div> </div>
            
            <div id="hemi-right" style="width: 60px; height: 100px; background: #64748b; border-radius: 0 50px 50px 0; border: 4px solid #334155; border-left: 2px solid #0f172a; position: relative; transition: transform 0.2s;">
                <div style="position: absolute; right: -30px; top: 40px; width: 30px; height: 10px; background: #3b82f6;"></div> </div>

            <div id="pop-text" style="position: absolute; font-size: 40px; font-weight: bold; color: #ef4444; opacity: 0; transition: opacity 0.2s; text-shadow: 2px 2px 0px white;">POP!</div>
        </div>

        <button id="try-pull-btn" style="margin-top: 20px; background-color: #3b82f6; color: white; border: none; padding: 10px 30px; border-radius: 6px; font-weight: bold; font-size: 16px; cursor: pointer; transition: transform 0.1s;">💥 嘗試拉開！</button>
    </div>

    <script>
        const vacSlider = document.getElementById('vac-slider');
        const pullSlider = document.getElementById('pull-slider');
        const vacVal = document.getElementById('vac-val');
        const pullVal = document.getElementById('pull-val');
        const intPVal = document.getElementById('int-p-val');
        const holdVal = document.getElementById('hold-val');
        
        const hemiLeft = document.getElementById('hemi-left');
        const hemiRight = document.getElementById('hemi-right');
        const popText = document.getElementById('pop-text');
        const tryPullBtn = document.getElementById('try-pull-btn');

        const MAX_HOLD_FORCE = 1500; // 100% 真空時大氣壓提供的最高扣持力

        function updateGas() {
            let v = parseInt(vacSlider.value);
            let pull = parseInt(pullSlider.value);
            
            vacVal.innerText = v;
            pullVal.innerText = pull;
            
            let intP = 1.0 - (v / 100);
            intPVal.innerText = intP.toFixed(2);
            
            // 扣持力 = (外界壓 - 內部壓) * 常數
            let holdF = (v / 100) * MAX_HOLD_FORCE;
            holdVal.innerText = holdF.toFixed(0);

            // 恢復原狀
            hemiLeft.style.transform = "translateX(0px)";
            hemiRight.style.transform = "translateX(0px)";
            popText.style.opacity = 0;
        }

        vacSlider.addEventListener('input', updateGas);
        pullSlider.addEventListener('input', updateGas);

        tryPullBtn.addEventListener('click', () => {
            let v = parseInt(vacSlider.value);
            let pull = parseInt(pullSlider.value);
            let holdF = (v / 100) * MAX_HOLD_FORCE;

            if (pull > holdF) {
                // 拉開了！
                hemiLeft.style.transform = "translateX(-40px)";
                hemiRight.style.transform = "translateX(40px)";
                popText.style.opacity = 1;
            } else {
                // 拉不開，震動一下
                hemiLeft.style.transform = "translateX(-2px)";
                hemiRight.style.transform = "translateX(2px)";
                setTimeout(() => {
                    hemiLeft.style.transform = "translateX(0px)";
                    hemiRight.style.transform = "translateX(0px)";
                }, 150);
            }
        });
        
        tryPullBtn.addEventListener('mousedown', () => tryPullBtn.style.transform = 'scale(0.95)');
        tryPullBtn.addEventListener('mouseup', () => tryPullBtn.style.transform = 'scale(1)');

        updateGas();
    </script>
    """
    components.html(magdeburg_html, height=450)

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
