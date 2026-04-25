import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 CSS 美化
    st.markdown("""
        <style>
        div[class*="stRadio"] > label {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #1e293b !important;
        }
        div[class*="stRadio"] p {
            font-size: 20px !important;
            font-weight: 500 !important;
        }
        u {
            text-decoration: underline;
            text-underline-offset: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### ⚖️ 黎明物理法庭 S02E07：高壓淘汰賽之壓力物理全書")
    
    # 審判長對白
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『壓力不只是重量，更是力量與面積的博弈。從高跟鞋的陷落到馬德堡半球的對峙，物理規律決定了誰能留到最後。檢察官，請研讀這份實戰卷宗，並透過下方的互動實驗室找出隱藏的真相。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 PART 1：固體壓力與垂直作用力
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 1：固體壓力與垂直作用力")
    st.markdown("　　壓力（$P$）定義為單位面積（$A$）上所受到的**垂直作用力**（$F_\perp$）。這意味著同樣重量的物體，當你側放、直立或斜壓時，對地面產生的破壞力（下陷程度）是截然不同的。")

    # 🕹️ 實驗室 A：固體壓力
    st.info("👇 **【實驗室 A】調整「接觸面積」與「角度」。觀察藍色虛線的「垂直分力」如何決定海綿的下陷程度！**")
    
    solid_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <h5 style="margin:0 0 15px 0;">🧱 固體下陷與垂直分力實驗</h5>
        
        <div style="display: flex; justify-content: space-around; margin-bottom: 15px; gap: 10px;">
            <div style="flex:1;">
                <label style="font-size: 13px; font-weight: bold;">擺放面積 (A)</label>
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

        <div style="background: white; padding: 10px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #e2e8f0; display: flex; justify-content: space-around;">
            <div>垂直分力 F⊥: <b id="f-val" style="color: #3b82f6;">100</b> kgw</div>
            <div>壓力 P: <b id="p-val" style="color: #047857;">2.0</b></div>
        </div>

        <div style="position: relative; width: 100%; max-width: 350px; height: 260px; margin: 0 auto; background: white; border: 1px solid #cbd5e1; overflow: hidden; display: flex; align-items: flex-end; justify-content: center;">
            <div style="position: absolute; bottom: 0; width: 100%; height: 80px; background: #fcd34d; border-top: 3px solid #f59e0b; z-index: 1;"></div>
            
            <div id="box" style="position: absolute; bottom: 80px; width: 120px; height: 40px; background: #475569; border: 2px solid #1e293b; z-index: 10; transition: bottom 0.3s, width 0.3s, height 0.3s;"></div>
            
            <svg style="position: absolute; top:0; left:0; width: 100%; height: 100%; z-index: 20; pointer-events: none;">
                <defs>
                    <marker id="arrow-r" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#dc2626"/></marker>
                    <marker id="arrow-b" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#3b82f6"/></marker>
                </defs>
                <line id="line-f" x1="175" y1="20" x2="175" y2="100" stroke="#dc2626" stroke-width="4" marker-end="url(#arrow-r)" />
                <line id="line-p" x1="175" y1="20" x2="175" y2="100" stroke="#3b82f6" stroke-width="3" stroke-dasharray="5,3" marker-end="url(#arrow-b)" />
                <text id="txt-f" x="120" y="40" fill="#dc2626" font-size="12" font-weight="bold">總施力 F</text>
                <text id="txt-p" x="185" y="70" fill="#3b82f6" font-size="12" font-weight="bold">垂直分力 F⊥</text>
            </svg>
        </div>
    </div>
    <script>
        const areaEl = document.getElementById('area-sel');
        const angleEl = document.getElementById('angle-sel');
        const box = document.getElementById('box');
        const lineF = document.getElementById('line-f');
        const lineP = document.getElementById('line-p');
        const txtP = document.getElementById('txt-p');

        function update() {
            let A = parseFloat(areaEl.value);
            let deg = parseFloat(angleEl.value);
            let F = 100;
            let rad = deg * (Math.PI / 180);
            let F_perp = F * Math.sin(rad);
            let P = F_perp / A;
            
            document.getElementById('f-val').innerText = F_perp.toFixed(1);
            document.getElementById('p-val').innerText = P.toFixed(1);

            let w = A == 50 ? 120 : 40;
            let h = A == 50 ? 40 : 120;
            box.style.width = w + 'px';
            box.style.height = h + 'px';
            
            let dent = (P / 10) * 40; // 最大下陷 40px
            box.style.bottom = (80 - dent) + 'px';

            let endY = 260 - (80 - dent) - h - 5;
            let startX = 175 - 100 * Math.cos(rad);
            let startY = endY - 100 * Math.sin(rad);
            lineF.setAttribute('x1', startX); lineF.setAttribute('y1', startY);
            lineF.setAttribute('x2', 175); lineF.setAttribute('y2', endY);
            
            let perpStartY = endY - (100 * Math.sin(rad));
            lineP.setAttribute('x1', 175); lineP.setAttribute('y1', perpStartY);
            lineP.setAttribute('x2', 175); lineP.setAttribute('y2', endY);
            txtP.setAttribute('y', perpStartY + 30);
            txtP.style.opacity = deg == 90 ? 0 : 1;
        }
        areaEl.addEventListener('change', update);
        angleEl.addEventListener('change', update);
        update();
    </script>
    """
    components.html(solid_html, height=500)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 PART 2：液體壓力與深度
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 2：液體壓力的深度陷阱")
    st.markdown("　　液體壓力只與**深度**與**密度**有關（$P = h \times d$）。關鍵在於深度是從「水面向下算」。水壓越大的地方，噴出的水柱射程越遠。")

    # 🕹️ 實驗室 B：液體壓力
    st.info("👇 **【實驗室 B】觀察水柱。深度越深（離水面越遠），壓力越大，噴出的拋物線射程就越長！**")

    liquid_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <div style="display: flex; gap: 10px; margin-bottom: 15px;">
            <div style="flex:1;">水面高: <input type="range" id="lv" min="0" max="100" value="80" style="width:100%;"></div>
            <div style="flex:1;">液體密度: <select id="den"><option value="1">水 (1.0)</option><option value="1.2">鹽水 (1.2)</option></select></div>
        </div>

        <div style="position: relative; width: 320px; height: 300px; margin: 0 auto; display: flex; align-items: flex-end;">
            <div style="position: absolute; bottom: 0; left: 0; width: 120px; height: 100%; border-left: 6px solid #475569; border-bottom: 6px solid #475569; border-right: 6px solid #475569; z-index: 10;">
                <div style="position:absolute; right:-6px; top:26px; width:6px; height:8px; background:white;"></div> <div style="position:absolute; right:-6px; top:116px; width:6px; height:8px; background:white;"></div> <div style="position:absolute; right:-6px; top:206px; width:6px; height:8px; background:white;"></div> </div>
            <div id="water" style="position: absolute; bottom: 6px; left: 6px; width: 108px; height: 80%; background: rgba(59,130,246,0.5); z-index: 5;"></div>
            
            <svg width="320" height="300" style="position: absolute; top:0; left:0; z-index: 2;">
                <path id="pC" d="" fill="none" stroke="rgba(59,130,246,0.6)" stroke-width="5" />
                <path id="pB" d="" fill="none" stroke="rgba(59,130,246,0.6)" stroke-width="5" />
                <path id="pA" d="" fill="none" stroke="rgba(59,130,246,0.6)" stroke-width="5" />
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

            function draw(id, h_cm) {
                let depth = Math.max(0, L - h_cm);
                let startX = 120;
                let startY = 300 - (h_cm * 2.5);
                let path = document.getElementById(id);
                if (depth > 0) {
                    let R = 2 * Math.sqrt(depth * h_cm) * d * 1.5; 
                    path.setAttribute('d', `M ${startX} ${startY} Q ${startX+R} ${startY} ${startX+R} 296`);
                } else { path.setAttribute('d', ''); }
            }
            draw('pC', 90); // 洞的位置與座標對齊
            draw('pB', 54); 
            draw('pA', 18);
        }
        lvIn.addEventListener('input', updateLiq);
        denIn.addEventListener('change', updateLiq);
        updateLiq();
    </script>
    """
    components.html(liquid_html, height=420)

    st.write("<br>", unsafe_allow_html=True)

    # ==========================================
    # 📖 PART 3：馬德堡半球與大氣壓力
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 3：大氣壓力的絕對防禦")
    st.markdown("　　外界大氣壓力約為 $1.0 \, atm$。當我們把半球內部的空氣抽走，內外產生的巨大壓力差會讓半球緊緊咬合。")

    # 🕹️ 實驗室 C：馬德堡半球
    st.info("👇 **【實驗室 C】啟動抽氣機，觀察兩側拉環出現的「施力箭頭」。只有拉力大於大氣壓力的咬合力時，半球才會彈開！**")

    mag_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <div style="display: flex; gap: 10px; margin-bottom: 15px;">
            <div style="flex:1;">抽氣真空度: <input type="range" id="vac" min="0" max="100" value="0" style="width:100%;"></div>
            <div style="flex:1;">馬匹拉力: <input type="range" id="pull" min="0" max="2000" value="0" style="width:100%;"></div>
        </div>
        
        <div style="position: relative; width: 300px; height: 120px; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
            <svg width="300" height="120" style="position: absolute; top:0; left:0;">
                <defs><marker id="arr" markerWidth="10" markerHeight="10" refX="0" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#3b82f6"/></marker></defs>
                <line id="l-arr" x1="100" y1="60" x2="50" y2="60" stroke="#3b82f6" stroke-width="6" marker-end="url(#arr)" style="visibility:hidden;"/>
                <line id="r-arr" x1="200" y1="60" x2="250" y2="60" stroke="#3b82f6" stroke-width="6" marker-end="url(#arr)" style="visibility:hidden;"/>
            </svg>
            <div id="h1" style="width: 50px; height: 80px; background: #64748b; border-radius: 40px 0 0 40px; border: 3px solid #334155; transition: transform 0.2s;"></div>
            <div id="h2" style="width: 50px; height: 80px; background: #64748b; border-radius: 0 40px 40px 0; border: 3px solid #334155; border-left: 2px solid #0f172a; transition: transform 0.2s;"></div>
        </div>
        <button id="btn" style="margin-top: 10px; padding: 8px 20px; background: #3b82f6; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer;">💥 嘗試拉開</button>
    </div>
    <script>
        const btn = document.getElementById('btn');
        const lA = document.getElementById('l-arr');
        const rA = document.getElementById('r-arr');
        btn.addEventListener('click', () => {
            let v = parseInt(document.getElementById('vac').value);
            let p = parseInt(document.getElementById('pull').value);
            let limit = v * 15; // 假設門檻
            lA.style.visibility = p > 0 ? 'visible' : 'hidden';
            rA.style.visibility = p > 0 ? 'visible' : 'hidden';
            if(p > limit && v > 0) {
                document.getElementById('h1').style.transform = 'translateX(-30px)';
                document.getElementById('h2').style.transform = 'translateX(30px)';
            } else {
                document.getElementById('h1').style.transform = 'translateX(-2px)';
                setTimeout(() => { document.getElementById('h1').style.transform = 'translateX(0)'; }, 100);
            }
        });
    </script>
    """
    components.html(mag_html, height=350)

    st.write("---")
    
    # ==========================================
    # 💥 逆轉法庭交互區 (打臉辯方)
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
            st.success("💥 雙重異議成立！(OBJECTION!) \n\n法官敲下法槌：「檢察官勝訴！壓力定律不容扭曲！」")
            return True
        else:
            st.error("❌ 異議駁回！請重新觀察實驗結果，理清物理邏輯！")
            
    return False
