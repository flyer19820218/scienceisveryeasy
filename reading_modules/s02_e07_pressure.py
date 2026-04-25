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
    
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『壓力不只是重量，更是力量與面積的博弈。從高跟鞋的陷落到馬德堡半球的對峙，物理規律決定了誰能留到最後。檢察官，請研讀這份實戰卷宗，並透過下方的互動實驗室找出隱藏的真相。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 PART 1：固體壓力與垂直作用力
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 1：固體壓力與垂直作用力")
    st.markdown("　　壓力（$P$）定義為單位面積（$A$）上所受到的**垂直作用力**（$F_\perp$）。這意味著同樣重量的物體，當你斜壓或改變受力面積時，對地面產生的下陷程度是截然不同的。只有垂直分力才是真正的「壓力之源」。")

    # 🕹️ 實驗室 A：固體壓力
    st.info("👇 **【實驗室 A】調整「接觸面積」與「角度」。觀察藍色虛線的「垂直分力」，只有它能決定箱子陷進海綿的深度！**")
    
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

        <div style="position: relative; width: 100%; max-width: 400px; height: 350px; margin: 0 auto; background: white; border: 1px solid #cbd5e1; overflow: hidden; display: flex; align-items: flex-end; justify-content: center; border-radius: 8px;">
            <div style="position: absolute; bottom: 0; width: 100%; height: 80px; background: #fcd34d; border-top: 3px solid #f59e0b; z-index: 1;"></div>
            <div id="box" style="position: absolute; width: 120px; height: 40px; background: #475569; border: 2px solid #1e293b; z-index: 10; transition: bottom 0.3s, width 0.3s, height 0.3s, margin-left 0.3s;"></div>
            <svg id="force-svg" style="position: absolute; top:0; left:0; width: 100%; height: 100%; z-index: 20; pointer-events: none;" viewBox="0 0 400 350">
                <defs>
                    <marker id="arrow-r" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#dc2626"/></marker>
                    <marker id="arrow-b" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#3b82f6"/></marker>
                </defs>
                <line id="line-f" x1="200" y1="20" x2="200" y2="100" stroke="#dc2626" stroke-width="5" marker-end="url(#arrow-r)" style="transition: all 0.3s;" />
                <line id="line-p" x1="200" y1="20" x2="200" y2="100" stroke="#3b82f6" stroke-width="4" stroke-dasharray="6,4" marker-end="url(#arrow-b)" style="transition: all 0.3s;" />
                <text id="txt-f" x="140" y="40" fill="#dc2626" font-size="14" font-weight="bold" style="transition: all 0.3s;">總施力 F</text>
                <text id="txt-p" x="210" y="70" fill="#3b82f6" font-size="14" font-weight="bold" style="transition: all 0.3s;">F⊥</text>
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

        function updateSolid() {
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
            
            let dent = (P / 10) * 50; 
            box.style.bottom = (80 - dent) + 'px';
            box.style.left = (200 - w/2) + 'px';

            let targetY = 350 - (80 - dent) - h - 5; 
            let startX = 200 - 140 * Math.cos(rad);
            let startY = targetY - 140 * Math.sin(rad);
            
            fLine.setAttribute('x1', startX); fLine.setAttribute('y1', startY);
            fLine.setAttribute('x2', 200); fLine.setAttribute('y2', targetY);
            tF.setAttribute('x', startX - 25); tF.setAttribute('y', startY - 10);
            
            let perpStartY = targetY - (140 * Math.sin(rad));
            pLine.setAttribute('x1', 200); pLine.setAttribute('y1', perpStartY);
            pLine.setAttribute('x2', 200); pLine.setAttribute('y2', targetY);
            tP.setAttribute('y', perpStartY + 30);
            tP.style.opacity = deg == 90 ? 0 : 1;
        }
        areaEl.addEventListener('change', updateSolid);
        angleEl.addEventListener('change', updateSolid);
        updateSolid();
    </script>
    """
    components.html(solid_html, height=580)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 PART 2：液體壓力與深度
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 2：液體壓力的深度陷阱")
    st.markdown("　　液體壓力只與**深度**與**密度**有關（$P = h \\times d$）。關鍵在於深度是從「水面向下算」。水壓越大的地方，噴出的水柱射程越遠。")

    # 🕹️ 實驗室 B：液體壓力
    st.info("👇 **【實驗室 B】觀察水柱。可以把水加到滿(100cm)！深度越深（離水面越遠），壓力越大，射程就越長！**")

    liquid_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <h5 style="margin:0 0 10px 0;">🌊 液體壓力觀測水槽</h5>
        <div style="display: flex; gap: 10px; margin-bottom: 15px;">
            <div style="flex:1;">水面高: <span id="lv-txt" style="color:#3b82f6;font-weight:bold;">100</span> cm<input type="range" id="lv" min="0" max="100" value="100" step="5" style="width:100%;"></div>
            <div style="flex:1;">液體密度: <select id="den"><option value="1">純水 (1.0)</option><option value="1.2">鹽水 (1.2)</option><option value="0.8">酒精 (0.8)</option></select></div>
        </div>

        <div style="position: relative; width: 100%; max-width: 450px; height: 360px; margin: 0 auto; display: flex; align-items: flex-end;">
            
            <div style="position: absolute; left: 0; bottom: 200px; font-size: 12px; font-weight: bold; background: #fee2e2; border: 1px solid #f87171; padding: 4px; border-radius: 4px; z-index: 20;" id="label-c">C<br>P=0</div>
            <div style="position: absolute; left: 0; bottom: 110px; font-size: 12px; font-weight: bold; background: #fef3c7; border: 1px solid #fcd34d; padding: 4px; border-radius: 4px; z-index: 20;" id="label-b">B<br>P=0</div>
            <div style="position: absolute; left: 0; bottom: 20px; font-size: 12px; font-weight: bold; background: #dcfce7; border: 1px solid #86efac; padding: 4px; border-radius: 4px; z-index: 20;" id="label-a">A<br>P=0</div>

            <div style="position: absolute; bottom: 0; left: 50px; width: 80px; height: 320px; border-left: 3px solid #475569; border-bottom: 3px solid #475569; border-right: 3px solid #475569; z-index: 10; box-sizing: border-box;">
                
                <div style="position:absolute; right:-3px; bottom:208px; width:3px; height:4px; background:white;"></div> 
                <div style="position:absolute; right:-3px; bottom:118px; width:3px; height:4px; background:white;"></div> 
                <div style="position:absolute; right:-3px; bottom:28px; width:3px; height:4px; background:white;"></div> 
            </div>
            
            <div id="water" style="position: absolute; bottom: 3px; left: 53px; width: 74px; height: 300px; background: rgba(59,130,246,0.6); z-index: 5; transition: height 0.2s, background 0.3s;"></div>
            
            <svg width="450" height="360" style="position: absolute; top:0; left:0; z-index: 2; pointer-events: none;">
                <path id="pC" d="" fill="none" stroke="rgba(59,130,246,0.7)" stroke-width="4" stroke-linecap="round"/>
                <path id="pB" d="" fill="none" stroke="rgba(59,130,246,0.7)" stroke-width="4" stroke-linecap="round"/>
                <path id="pA" d="" fill="none" stroke="rgba(59,130,246,0.7)" stroke-width="4" stroke-linecap="round"/>
            </svg>
        </div>
    </div>
    <script>
        const lvIn = document.getElementById('lv');
        const denIn = document.getElementById('den');
        const water = document.getElementById('water');
        
        function updateLiq() {
            let L = parseInt(lvIn.value); // 0-100 cm
            let d = parseFloat(denIn.value);
            document.getElementById('lv-txt').innerText = L;
            
            // 1cm = 3px，水高 L * 3 px
            water.style.height = (L * 3) + 'px';
            
            let color = "rgba(59,130,246,0.6)";
            if(d == 1.2) color = "rgba(16,185,129,0.6)";
            if(d == 0.8) color = "rgba(245,158,11,0.6)";
            water.style.background = color;
            document.getElementById('pC').setAttribute('stroke', color);
            document.getElementById('pB').setAttribute('stroke', color);
            document.getElementById('pA').setAttribute('stroke', color);

            // SVG 高度 360，底部(Y=360)。但水槽底板有 3px 的邊框，所以水槽的「內部地板」是 Y = 357。
            // 洞口 Y 座標 (從頂部往下算) = 357 - (高度_cm * 3)
            function draw(id, holeH_cm, labelId) {
                let depth = Math.max(0, L - holeH_cm); 
                let p = depth * d;
                let path = document.getElementById(id);
                document.getElementById(labelId).innerHTML = labelId.replace('label-','') + '<br>P=' + p.toFixed(1);

                if (depth > 0) {
                    let startX = 130; // 容器右側外緣 (50 + 80)
                    let startY = 357 - (holeH_cm * 3); // 🌟 精準對準洞口中心 Y 座標
                    let R = Math.sqrt(depth * holeH_cm) * d * 3.5; // 射程計算
                    
                    // 落水點在地板 Y=357
                    path.setAttribute('d', `M ${startX} ${startY} Q ${startX+R*0.8} ${startY} ${startX+R*1.2} 357`);
                } else { 
                    path.setAttribute('d', ''); 
                }
            }
            
            draw('pC', 70, 'label-c');
            draw('pB', 40, 'label-b');
            draw('pA', 10, 'label-a');
        }
        lvIn.addEventListener('input', updateLiq);
        denIn.addEventListener('change', updateLiq);
        updateLiq();
    </script>
    """
    components.html(liquid_html, height=500)

    st.write("<br>", unsafe_allow_html=True)

    # ==========================================
    # 📖 PART 3：馬德堡半球與大氣壓力
    # ==========================================
    st.markdown("#### 📁 檢方機密卷宗 3：大氣壓力的絕對防禦")
    st.markdown("　　外界大氣壓力約為 $1.0 \, atm$。當我們把半球內部的空氣抽走，內外產生的巨大壓力差會讓半球緊緊咬合。")

    # 🕹️ 實驗室 C：馬德堡半球
    st.info("👇 **【實驗室 C】啟動抽氣機，觀察兩側出現的「紅色拉力箭頭」。只有拉力大於大氣壓力的咬合力時，半球才會被拉開！**")

    mag_html = """
    <div style="font-family: sans-serif; padding: 15px; background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; text-align: center;">
        <h5 style="margin:0 0 10px 0;">🐴 馬德堡半球對抗賽</h5>
        <div style="display: flex; gap: 15px; margin-bottom: 10px;">
            <div style="flex:1;">抽氣真空度: <span id="v-txt" style="color:#dc2626;font-weight:bold;">0</span>%<input type="range" id="vac" min="0" max="100" value="0" step="10" style="width:100%;"></div>
            <div style="flex:1;">馬匹拉力: <span id="p-txt" style="color:#3b82f6;font-weight:bold;">0</span> kgw<input type="range" id="pull" min="0" max="2000" value="0" step="100" style="width:100%;"></div>
        </div>
        
        <div style="position: relative; width: 100%; max-width: 400px; height: 160px; margin: 0 auto; display: flex; align-items: center; justify-content: center; background: white; border-radius: 8px; border: 1px solid #cbd5e1; overflow:hidden;">
            <svg width="400" height="160" style="position: absolute; top:0; left:0; z-index: 5;">
                <defs><marker id="arr-r" markerWidth="8" markerHeight="8" refX="0" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#ef4444"/></marker></defs>
                <line id="l-arr" x1="160" y1="80" x2="160" y2="80" stroke="#ef4444" stroke-width="6" marker-end="url(#arr-r)" style="visibility:hidden;"/>
                <line id="r-arr" x1="240" y1="80" x2="240" y2="80" stroke="#ef4444" stroke-width="6" marker-end="url(#arr-r)" style="visibility:hidden;"/>
            </svg>
            <div id="h1" style="width: 50px; height: 90px; background: #64748b; border-radius: 45px 0 0 45px; border: 3px solid #1e293b; border-right:none; transition: transform 0.2s; z-index: 10;"></div>
            <div id="h2" style="width: 50px; height: 90px; background: #64748b; border-radius: 0 45px 45px 0; border: 3px solid #1e293b; border-left: 2px solid #0f172a; transition: transform 0.2s; z-index: 10;"></div>
            <div id="pop" style="position:absolute; font-size:40px; font-weight:bold; color:#ef4444; opacity:0; z-index: 15;">POP!</div>
        </div>
        
        <div style="margin-top: 15px; font-size: 14px; font-weight: bold;">大氣壓扣持力：<span id="hold-val" style="font-size:18px; color:#1e293b;">0</span> kgw</div>
        <button id="btn" style="margin-top: 10px; padding: 10px 30px; background: #2563eb; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer;">💥 嘗試拉開</button>
    </div>
    <script>
        const btn = document.getElementById('btn');
        const lA = document.getElementById('l-arr');
        const rA = document.getElementById('r-arr');
        const vIn = document.getElementById('vac');
        const pIn = document.getElementById('pull');
        
        function updateMag() {
            let v = parseInt(vIn.value);
            let p = parseInt(pIn.value);
            document.getElementById('v-txt').innerText = v;
            document.getElementById('p-txt').innerText = p;
            
            let hold = v * 15; // 假設極限1500
            document.getElementById('hold-val').innerText = hold;

            let len = p / 20; 
            if(p > 0) {
                lA.style.visibility = 'visible';
                rA.style.visibility = 'visible';
                lA.setAttribute('x2', 150 - len);
                rA.setAttribute('x2', 250 + len);
            } else {
                lA.style.visibility = 'hidden';
                rA.style.visibility = 'hidden';
            }
            
            document.getElementById('h1').style.transform = 'translateX(0)';
            document.getElementById('h2').style.transform = 'translateX(0)';
            document.getElementById('pop').style.opacity = 0;
        }
        
        vIn.addEventListener('input', updateMag);
        pIn.addEventListener('input', updateMag);
        
        btn.addEventListener('click', () => {
            let v = parseInt(vIn.value);
            let p = parseInt(pIn.value);
            let limit = v * 15;
            
            if(p > limit && p > 0) {
                document.getElementById('h1').style.transform = 'translateX(-40px)';
                document.getElementById('h2').style.transform = 'translateX(40px)';
                document.getElementById('pop').style.opacity = 1;
            } else {
                document.getElementById('h1').style.transform = 'translateX(-3px)';
                document.getElementById('h2').style.transform = 'translateX(3px)';
                setTimeout(() => {
                    document.getElementById('h1').style.transform = 'translateX(0)';
                    document.getElementById('h2').style.transform = 'translateX(0)';
                }, 150);
            }
        });
        updateMag();
    </script>
    """
    components.html(mag_html, height=450)

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
