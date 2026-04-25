import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS 覆寫
    st.markdown("""
        <style>
        div[class*="stRadio"] > label { font-size: 20px !important; font-weight: bold !important; color: #1e293b !important; }
        div[class*="stRadio"] p { font-size: 20px !important; font-weight: 500 !important; }
        u { text-decoration: underline; text-underline-offset: 4px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### ⚖️ 黎明物理法庭 S02E07：高壓淘汰賽之壓力物理全書")
    
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『壓力不只是重量，更是力量與面積的博弈。從高跟鞋的陷落到馬德堡半球的對峙，物理規律決定了誰能留到最後。檢察官，請研讀這份實戰卷宗，並透過下方的互動實驗室找出隱藏的真相。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 PART 1：固體壓力區
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 1：固體壓力與垂直作用力")
    st.markdown("　　壓力（$P$）定義為單位面積（$A$）上所受到的**垂直作用力**（$F_\perp$）。這意味著同樣重量的物體，當你斜壓或改變受力面積時，對地面產生的下陷程度是截然不同的。只有垂直分力才是真正的「壓力之源」。")

    # 🕹️ 實驗室 A：固體壓力
    st.info("👇 **【實驗室 A】調整面積與角度。觀察藍色虛線的「垂直分力」，只有它能決定箱子陷進海綿的深度！**")
    
    solid_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <h5 style="margin:0 0 10px 0;">🧱 固體下陷與垂直分力實驗</h5>
        <div style="display: flex; justify-content: space-around; margin-bottom: 15px; gap: 10px;">
            <div style="flex:1;">
                <label style="font-size: 13px; font-weight: bold;">面積 (A)</label>
                <select id="area-sel" style="width: 100%; padding: 5px; border-radius: 4px;">
                    <option value="50">大面積 (平放)</option>
                    <option value="10">小面積 (直立)</option>
                </select>
            </div>
            <div style="flex:1;">
                <label style="font-size: 13px; font-weight: bold;">施力角度</label>
                <select id="angle-sel" style="width: 100%; padding: 5px; border-radius: 4px;">
                    <option value="90">垂直下壓 (90度)</option>
                    <option value="60">斜向壓 (60度)</option>
                    <option value="30">輕微斜壓 (30度)</option>
                </select>
            </div>
        </div>
        <div style="background: white; padding: 10px; border-radius: 8px; margin-bottom: 10px; border: 1px solid #e2e8f0; display: flex; justify-content: space-around; font-size: 14px;">
            <div>垂直分力 F⊥: <b id="f-val" style="color: #3b82f6;">100.0</b> kgw</div>
            <div>壓力 P: <b id="p-val" style="color: #047857;">2.0</b></div>
        </div>
        <div style="position: relative; width: 100%; max-width: 400px; height: 320px; margin: 0 auto; background: white; border: 1px solid #cbd5e1; border-radius: 8px; overflow: hidden; display: flex; align-items: flex-end; justify-content: center;">
            <div style="position: absolute; bottom: 0; width: 100%; height: 80px; background: #fcd34d; border-top: 3px solid #f59e0b; z-index: 1;"></div>
            <div id="box" style="position: absolute; bottom: 80px; width: 120px; height: 40px; background: #475569; border: 2px solid #1e293b; z-index: 10; transition: all 0.3s; border-radius: 2px;"></div>
            <svg style="position: absolute; top:0; left:0; width: 100%; height: 100%; z-index: 20; pointer-events: none;" viewBox="0 0 400 320">
                <defs>
                    <marker id="arr-r" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#dc2626"/></marker>
                    <marker id="arr-b" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#3b82f6"/></marker>
                </defs>
                <line id="line-f" x1="200" y1="50" x2="200" y2="150" stroke="#dc2626" stroke-width="5" marker-end="url(#arr-r)" style="transition: all 0.3s;" />
                <line id="line-p" x1="200" y1="50" x2="200" y2="150" stroke="#3b82f6" stroke-width="4" stroke-dasharray="8,4" marker-end="url(#arr-b)" style="transition: all 0.3s;" />
                <text id="txt-f" x="140" y="40" fill="#dc2626" font-size="14" font-weight="bold">總力 F</text>
                <text id="txt-p" x="215" y="100" fill="#3b82f6" font-size="14" font-weight="bold">分力 F⊥</text>
            </svg>
        </div>
    </div>
    <script>
        const areaEl = document.getElementById('area-sel');
        const angleEl = document.getElementById('angle-sel');
        const box = document.getElementById('box');
        const fLine = document.getElementById('line-f');
        const pLine = document.getElementById('line-p');
        const tP = document.getElementById('txt-p');
        const tF = document.getElementById('txt-f');

        function update() {
            let A = parseFloat(areaEl.value);
            let deg = parseFloat(angleEl.value);
            let rad = deg * (Math.PI / 180);
            let F_perp = 100 * Math.sin(rad);
            let P = F_perp / A;
            
            document.getElementById('f-val').innerText = F_perp.toFixed(1);
            document.getElementById('p-val').innerText = P.toFixed(1);

            let w = A == 50 ? 140 : 50;
            let h = A == 50 ? 50 : 140;
            box.style.width = w + 'px';
            box.style.height = h + 'px';
            
            let dent = (P / 10) * 45; 
            box.style.bottom = (80 - dent) + 'px';

            let targetY = 320 - (80 - dent) - h - 5;
            let startX = 200 - 120 * Math.cos(rad);
            let startY = targetY - 120 * Math.sin(rad);
            
            fLine.setAttribute('x1', startX); fLine.setAttribute('y1', startY);
            fLine.setAttribute('x2', 200); fLine.setAttribute('y2', targetY);
            tF.setAttribute('x', startX - 20); tF.setAttribute('y', startY - 10);

            let perpStartY = targetY - (120 * Math.sin(rad));
            pLine.setAttribute('x1', 200); pLine.setAttribute('y1', perpStartY);
            pLine.setAttribute('x2', 200); pLine.setAttribute('y2', targetY);
            tP.setAttribute('y', perpStartY + 40);
            tP.style.opacity = (deg == 90) ? 0 : 1;
        }
        areaEl.addEventListener('change', update);
        angleEl.addEventListener('change', update);
        update();
    </script>
    """
    components.html(solid_html, height=620)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 PART 2：液體壓力與深度
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 2：液體壓力的深度陷阱")
    st.markdown("　　液體壓力公式為 $P = h \times d$。深度是從「水面向下算」。水壓越大的開口，噴出的水柱射程越遠。")

    # 🕹️ 實驗室 B：液體壓力
    st.info("👇 **【實驗室 B】觀察水柱。深度越深（離水面越遠），壓力越大，射程就越長！**")

    liquid_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <div style="display: flex; gap: 10px; margin-bottom: 15px;">
            <div style="flex:1;">水面高: <input type="range" id="lv" min="0" max="100" value="85" style="width:100%;"></div>
            <div style="flex:1;">液體密度: <select id="den"><option value="1">純水 (1.0)</option><option value="1.2">鹽水 (1.2)</option></select></div>
        </div>
        <div style="position: relative; width: 340px; height: 320px; margin: 0 auto;">
            <div style="position: absolute; bottom: 0; left: 0; width: 140px; height: 300px; border: 6px solid #475569; border-top: none; z-index: 10; box-sizing: border-box;">
                <div style="position:absolute; right:-6px; top:30px; width:6px; height:10px; background:white;"></div> <div style="position:absolute; right:-6px; top:135px; width:6px; height:10px; background:white;"></div> <div style="position:absolute; right:-6px; top:240px; width:6px; height:10px; background:white;"></div> </div>
            <div id="water" style="position: absolute; bottom: 6px; left: 6px; width: 128px; height: 85%; background: rgba(59,130,246,0.5); z-index: 5; transition: height 0.3s;"></div>
            <svg width="340" height="320" style="position: absolute; top:0; left:0; z-index: 15; pointer-events: none;">
                <path id="pC" d="" fill="none" stroke="rgba(37,99,235,0.7)" stroke-width="6" stroke-linecap="round" />
                <path id="pB" d="" fill="none" stroke="rgba(37,99,235,0.7)" stroke-width="6" stroke-linecap="round" />
                <path id="pA" d="" fill="none" stroke="rgba(37,99,235,0.7)" stroke-width="6" stroke-linecap="round" />
            </svg>
        </div>
    </div>
    <script>
        const lvIn = document.getElementById('lv');
        const denIn = document.getElementById('den');
        const water = document.getElementById('water');
        function updateLiq() {
            let L = parseInt(lvIn.value);
            let d = parseFloat(denIn.value);
            water.style.height = L + '%';
            function draw(id, holeTopPx, holeHeightCm) {
                let depth = Math.max(0, L - (100 - (holeTopPx/3))); 
                let path = document.getElementById(id);
                if (depth > 0) {
                    let force = depth * d;
                    let R = Math.sqrt(depth * (100 - depth)) * d * 1.8; // 射程模擬
                    path.setAttribute('d', `M 140 ${holeTopPx+5} Q ${140+R*2} ${holeTopPx+5} ${140+R*2.5} 314`);
                } else { path.setAttribute('d', ''); }
            }
            draw('pC', 30, 90); 
            draw('pB', 135, 55); 
            draw('pA', 240, 20);
        }
        lvIn.addEventListener('input', updateLiq);
        denIn.addEventListener('change', updateLiq);
        updateLiq();
    </script>
    """
    components.html(liquid_html, height=450)

    st.write("<br>", unsafe_allow_html=True)

    # ==========================================
    # 📖 PART 3：大氣壓力區
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 3：大氣壓力的絕對防禦")
    st.markdown("　　馬德堡半球實驗將兩個半球抽真空。當內部壓力歸零時，外界龐大的大氣壓力會將半球合死。")

    # 🕹️ 實驗室 C：馬德堡半球
    st.info("👇 **【實驗室 C】啟動抽氣機，觀察兩側的「拉力箭頭」。箭頭越長代表馬匹出的力越大！**")

    mag_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <div style="display: flex; gap: 15px; margin-bottom: 15px;">
            <div style="flex:1;">真空度: <input type="range" id="vac" min="0" max="100" value="0" style="width:100%;"></div>
            <div style="flex:1;">拉力: <input type="range" id="pull" min="0" max="2000" value="0" step="50" style="width:100%;"></div>
        </div>
        <div style="position: relative; width: 360px; height: 160px; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
            <svg width="360" height="160" style="position: absolute; top:0; left:0; z-index: 5;">
                <defs><marker id="arr" markerWidth="10" markerHeight="10" refX="0" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#3b82f6"/></marker></defs>
                <line id="l-arr" x1="120" y1="80" x2="120" y2="80" stroke="#3b82f6" stroke-width="8" marker-end="url(#arr)" />
                <line id="r-arr" x1="240" y1="80" x2="240" y2="80" stroke="#3b82f6" stroke-width="8" marker-end="url(#arr)" />
            </svg>
            <div id="h1" style="width: 60px; height: 100px; background: #64748b; border-radius: 50px 0 0 50px; border: 4px solid #334155; transition: transform 0.2s; z-index: 10;"></div>
            <div id="h2" style="width: 60px; height: 100px; background: #64748b; border-radius: 0 50px 50px 0; border: 4px solid #334155; border-left: 2px solid #0f172a; transition: transform 0.2s; z-index: 10;"></div>
        </div>
        <button id="btn" style="margin-top: 10px; padding: 10px 30px; background: #2563eb; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer;">🐎 嘗試拉開半球</button>
    </div>
    <script>
        const vIn = document.getElementById('vac');
        const pIn = document.getElementById('pull');
        const lA = document.getElementById('l-arr');
        const rA = document.getElementById('r-arr');
        const h1 = document.getElementById('h1');
        const h2 = document.getElementById('h2');
        
        function update() {
            let p = parseInt(pIn.value);
            let len = p / 20; 
            lA.setAttribute('x2', 120 - len);
            rA.setAttribute('x2', 240 + len);
            h1.style.transform = 'translateX(0)';
            h2.style.transform = 'translateX(0)';
        }
        pIn.addEventListener('input', update);
        document.getElementById('btn').onclick = () => {
            let v = parseInt(vIn.value);
            let p = parseInt(pIn.value);
            let limit = v * 15;
            if (p > limit && v > 0) {
                h1.style.transform = 'translateX(-40px)';
                h2.style.transform = 'translateX(40px)';
            } else {
                h1.style.transform = 'translateX(-3px)';
                setTimeout(() => h1.style.transform = 'translateX(0)', 100);
            }
        };
        update();
    </script>
    """
    components.html(mag_html, height=350)

    st.write("---")
    
    # ==========================================
    # 💥 逆轉法庭交互區
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：『法官大人！水壓跟容器形狀絕對有關，大水池的水壓肯定比小管子重！還有馬德堡半球拉不開是因為半球太重了，跟空氣壓力無關！』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio("⚖️ 第一回合：關於液體壓力公式 P = h × d，何者正確？",
        ["A. 壓力大小只跟『深度』有關，與總水量或容器形狀『完全無關』。",
         "B. 總水量越多，壓力一定越大。",
         "C. 深度是從底部往上算的距離。"], index=None, key="q1")

    q2 = st.radio("⚖️ 第二回合：馬德堡半球實驗證明了什麼？",
        ["A. 半球很重。",
         "B. 大氣壓力的存在且威力強大。",
         "C. 內部空氣越多越難拉開。"], index=None, key="q2")
    
    if st.button("⚖️ 提出雙重異議 (Double Objection!)", use_container_width=True):
        if q1 and q2 and q1.startswith("A") and q2.startswith("B"):
            st.success("💥 雙重異議成立！(OBJECTION!) \n\n法官敲下法槌：「檢察官勝訴！物理鐵律不容扭曲！」")
            return True
        else:
            st.error("❌ 異議駁回！請重新觀察實驗結果，理清物理邏輯！")
            
    return False
