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

    st.markdown("### ⚖️ 黎明物理法庭 S02E06：防滑生死戰與摩擦力之謎")
    
    # 審判長對白
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『在光鮮亮麗的舞台上，一次滑倒就可能毀掉整個表演。摩擦力，這個永遠與運動唱反調的隱形守護者，究竟受什麼法則支配？檢察官，請研讀這份摩擦力卷宗，並在下方的【互動實驗室】中親自推動沉重的舞台音箱，找出靜摩擦力與動摩擦力的黃金交叉點！』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：靜與動的摩擦力極限")
        
        st.markdown("　　摩擦力是一種接觸力，其天職就是「**永遠和物體運動的趨勢唱反調**」（方向相反）。當工作人員用力推舞台上沉重的音箱卻「文風不動」時，地面會給予音箱一個與推力大小相等、方向相反的「**靜摩擦力**」來互相抵銷。隨著推力逐漸加大，靜摩擦力也會跟著等比例變大。直到音箱被推動的那一瞬間，阻力達到了極限的頂峰，物理學上稱為「**最大靜摩擦力**」。", unsafe_allow_html=True)

        st.markdown("　　奇妙的事情發生了！一旦音箱順利突破極限開始滑行，摩擦力就會從頂峰瞬間掉下來，變成一個固定不變的數值，稱為「**動摩擦力**」。只要物體處於滑動狀態，不管你推得多快，動摩擦力永遠是一個定值。這也就是為什麼我們推重物時，剛啟動那一下最費力，一旦推動後反而會覺得稍微輕鬆一點。", unsafe_allow_html=True)
        
        st.markdown("#### 📁 檢方機密卷宗：摩擦力的兩大真理與致命迷思")

        st.markdown("　　影響最大靜摩擦力與動摩擦力的關鍵因素只有兩個：一是「**接觸面的粗糙程度**」，例如穿著鞋底刻紋較深的舞蹈鞋，能增加粗糙度提升防滑效果；二是「**正向力**」（垂直壓在接觸面上的力量），例如在音箱上多坐一個人增加重量，向下壓迫的力量變大，推起來就會更費力。", unsafe_allow_html=True)

        st.markdown("　　這裡隱藏著考場上最容易讓人上當的迷思：**摩擦力的大小與「接觸面積」一點關係都沒有！** 無論你是把長方體音箱平放、側放還是直立推動，只要總重量與地面的粗糙度不變，受到的摩擦力就完全一模一樣。此外，若想大幅省力，可以在音箱底部裝上輪子，以「滾動摩擦」代替「滑動摩擦」，就能將阻力降到最低。", unsafe_allow_html=True)

    st.write("---")
    
    # ==========================================
    # 🕹️ HTML5 互動實驗室 (結合經典力圖)
    # ==========================================
    st.markdown("#### 🛠️ 互動實驗室：推動沉重的舞台音箱")
    st.info("👇 **請緩慢拖曳「推力滑桿」，並同時觀察下方的【摩擦力關係圖】！看看紅點是如何爬上斜坡，再瞬間掉入平原的！**")
    
    html_code = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
        <h4 style="margin-top: 0; color: #334155;">📦 舞台音箱推力測試儀</h4>
        
        <div style="display: flex; justify-content: space-around; background: white; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 20px;">
            <div>
                <div style="font-size: 14px; color: #64748b; font-weight: bold;">你的推力 (向右)</div>
                <div style="font-size: 24px; font-weight: bold; color: #3b82f6;"><span id="push-val">0</span> kgw</div>
            </div>
            <div>
                <div style="font-size: 14px; color: #64748b; font-weight: bold;">目前狀態</div>
                <div id="status-badge" style="font-size: 18px; font-weight: bold; color: white; background-color: #64748b; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-top: 5px;">靜止不動</div>
            </div>
            <div>
                <div style="font-size: 14px; color: #64748b; font-weight: bold;">摩擦力 (向左)</div>
                <div style="font-size: 24px; font-weight: bold; color: #ef4444;"><span id="fric-val">0</span> kgw</div>
            </div>
        </div>

        <input type="range" id="push-force" min="0" max="100" value="0" step="1" style="width: 100%; max-width: 500px; margin: 10px 0; cursor: pointer;">
        
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; align-items: flex-start; margin-top: 20px;">
            
            <div style="position: relative; width: 100%; max-width: 400px; height: 160px; background: #e2e8f0; border-bottom: 6px solid #475569; overflow: hidden; border-radius: 8px 8px 0 0;">
                <div id="box" style="position: absolute; left: 160px; bottom: 0; width: 80px; height: 80px; background-color: #1e293b; color: white; display: flex; justify-content: center; align-items: center; font-weight: bold; border-radius: 4px; border: 2px solid #0f172a; transition: left 0.1s linear; z-index: 5;">
                    音箱
                </div>
                
                <div id="arrow-push" style="position: absolute; left: 60px; bottom: 40px; height: 8px; background-color: #3b82f6; width: 0px; transition: width 0.1s linear; z-index: 10;">
                    <div style="position: absolute; right: -12px; top: -11px; width: 0; height: 0; border-top: 15px solid transparent; border-bottom: 15px solid transparent; border-left: 15px solid #3b82f6;"></div>
                </div>

                <div id="arrow-fric" style="position: absolute; left: 240px; bottom: 8px; height: 6px; background-color: #ef4444; width: 0px; transition: width 0.1s linear, left 0.1s linear; z-index: 15;">
                    <div style="position: absolute; left: -10px; top: -12px; width: 0; height: 0; border-top: 15px solid transparent; border-bottom: 15px solid transparent; border-right: 15px solid #ef4444;"></div>
                </div>
            </div>

            <div style="width: 100%; max-width: 400px; background: white; padding: 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                <div style="font-size: 15px; color: #475569; font-weight: bold; margin-bottom: 10px;">📈 摩擦力變化關係圖</div>
                <svg width="100%" height="200" viewBox="0 0 320 180" style="background: #f8fafc; border-radius: 6px;">
                    <line x1="40" y1="110" x2="300" y2="110" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4,4"/>
                    <polyline points="40,20 40,150 300,150" fill="none" stroke="#64748b" stroke-width="2"/>
                    
                    <text x="140" y="175" font-size="13" fill="#475569" font-weight="bold">推力 (外力)</text>
                    <text x="15" y="100" font-size="13" fill="#475569" font-weight="bold" transform="rotate(-90 15,100)">摩擦力</text>
                    
                    <polyline points="40,150 184,30 184,60 280,60" fill="none" stroke="#94a3b8" stroke-width="3" stroke-linejoin="round"/>
                    
                    <text x="135" y="22" font-size="12" fill="#dc2626" font-weight="bold">最大靜摩擦力</text>
                    <text x="210" y="52" font-size="12" fill="#10b981" font-weight="bold">動摩擦力</text>
                    <text x="70" y="100" font-size="12" fill="#f59e0b" font-weight="bold" transform="rotate(-38 70,100)">靜摩擦力</text>
                    
                    <circle id="chart-dot" cx="40" cy="150" r="7" fill="#ef4444" stroke="white" stroke-width="2" style="transition: cx 0.1s, cy 0.1s;"/>
                </svg>
            </div>
            
        </div>
        
        <div style="margin-top: 15px;">
            <button id="reset-btn" style="background-color: #64748b; color: white; border: none; padding: 8px 20px; border-radius: 6px; font-weight: bold; cursor: pointer;">🔄 歸零重置</button>
        </div>
    </div>

    <script>
        const pushInput = document.getElementById('push-force');
        const pushVal = document.getElementById('push-val');
        const fricVal = document.getElementById('fric-val');
        const statusBadge = document.getElementById('status-badge');
        
        const box = document.getElementById('box');
        const arrowPush = document.getElementById('arrow-push');
        const arrowFric = document.getElementById('arrow-fric');
        const chartDot = document.getElementById('chart-dot');
        const resetBtn = document.getElementById('reset-btn');

        // 物理常數設定
        const MAX_STATIC_FRIC = 60;
        const KINETIC_FRIC = 45;
        
        let boxPos = 160;
        let isMoving = false;
        let animationId = null;

        function updatePhysics() {
            let F = parseInt(pushInput.value);
            pushVal.innerText = F;
            
            // 繪製推力箭頭長度 (比例 1kgw = 1.5px)
            arrowPush.style.width = (F * 1.5) + 'px';
            arrowPush.style.left = (boxPos - (F * 1.5)) + 'px'; 

            let currentFric = 0;

            if (F == 0) {
                isMoving = false;
                currentFric = 0;
                statusBadge.innerText = "靜止不動";
                statusBadge.style.backgroundColor = "#64748b";
                arrowFric.style.width = '0px';
                box.style.transform = "translateX(0px)";
            }
            else if (F < MAX_STATIC_FRIC) {
                isMoving = false;
                currentFric = F;
                statusBadge.innerText = "靜止 (靜摩擦力)";
                statusBadge.style.backgroundColor = "#f59e0b";
                
                arrowFric.style.width = (F * 1.5) + 'px';
                arrowFric.style.left = (boxPos + 80) + 'px'; 
                
                box.style.transform = "translateX(0px)";
            } 
            else if (F == MAX_STATIC_FRIC) {
                isMoving = false;
                currentFric = F;
                statusBadge.innerText = "即將滑動 (最大靜摩擦)";
                statusBadge.style.backgroundColor = "#dc2626"; 
                
                arrowFric.style.width = (F * 1.5) + 'px';
                arrowFric.style.left = (boxPos + 80) + 'px';
                
                box.style.transform = "translateX(" + (Math.random() * 4 - 2) + "px)";
            } 
            else {
                isMoving = true;
                currentFric = KINETIC_FRIC;
                statusBadge.innerText = "滑動中 (動摩擦力)";
                statusBadge.style.backgroundColor = "#10b981"; 
                
                arrowFric.style.width = (KINETIC_FRIC * 1.5) + 'px';
                arrowFric.style.left = (boxPos + 80) + 'px';
                
                if(!animationId) slideBox();
            }

            fricVal.innerText = currentFric;

            // 🌟 更新 SVG 圖表上的紅點位置
            // X 軸縮放: 40 + (F * 2.4)
            // Y 軸縮放: 150 - (Fric * 2)
            let cx = 40 + (F * 2.4);
            let cy = 150 - (currentFric * 2);
            chartDot.setAttribute('cx', cx);
            chartDot.setAttribute('cy', cy);

            if (!isMoving && animationId) {
                cancelAnimationFrame(animationId);
                animationId = null;
            }
        }

        // 箱子滑動動畫
        function slideBox() {
            if (!isMoving) return;
            
            boxPos += 2; 
            if (boxPos > 450) {
                boxPos = -80; 
            }
            
            box.style.left = boxPos + 'px';
            
            let F = parseInt(pushInput.value);
            arrowPush.style.left = (boxPos - (F * 1.5)) + 'px';
            arrowFric.style.left = (boxPos + 80) + 'px';
            
            animationId = requestAnimationFrame(slideBox);
        }

        pushInput.addEventListener('input', updatePhysics);
        
        resetBtn.addEventListener('click', function(){
            pushInput.value = 0;
            boxPos = 160;
            box.style.left = boxPos + 'px';
            updatePhysics();
        });

    </script>
    """
    components.html(html_code, height=750)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    # 辯護律師對白
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！這份報告簡直是胡說八道！<br><br><b>【關於防滑鞋底】</b> 我的當事人為了防滑，特地換了底部『面積像船一樣大』的特製鞋子！接觸面積越大當然越防滑，摩擦力越大，這可是常識！<br><br><b>【關於推動重物】</b> 昨天工作人員推著音箱在舞台上跑，推得越大力音箱越跑越快，這證明了只要速度越來越快，『動摩擦力』就會跟著越來越大！這根本是謀殺！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "⚖️ 第一回合：請指出辯方對「鞋底面積與摩擦力」的謬誤：",
        [
            "A. 「異議！物理鐵律：摩擦力大小只與『正向力(重量)』和『接觸面粗糙度』有關，與『接觸面積』一點關係都沒有！換大鞋底根本沒用！」",
            "B. 「異議！面積大反而會讓摩擦力變小，因為壓力被分散了！」",
            "C. 「異議！鞋底面積大會產生向上的空氣浮力，導致摩擦力完全消失！」"
        ],
        index=None,
        key="q1"
    )

    st.write("<br>", unsafe_allow_html=True)

    q2 = st.radio(
        "⚖️ 第二回合：請指出辯方對「滑動速度與動摩擦力」的致命錯誤：",
        [
            "A. 「異議！動摩擦力一旦啟動物體後，就會消失變成零，所以才會越跑越快！」",
            "B. 「異議！只要物體處於滑動狀態，『動摩擦力』就是一個固定不變的定值！絕對不會因為你推得更大力、速度更快而跟著變大！」",
            "C. 「異議！動摩擦力永遠大於最大靜摩擦力，所以越推越費力是正常的！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("⚖️ 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備！")
        elif q1.startswith("A") and q2.startswith("B"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！從實驗室的圖表能清楚看見，突破最大靜摩擦力後，動摩擦力就會掉落並維持水平線（定值），絕不會隨速度或推力增加。同時，接觸面積也無法改變摩擦力的極限。辯方律師的常識完全違反了力學法則！」\n\n✅ 成功戳破所有謊言，審判勝利，成功捍衛了摩擦力的物理真相！")
            return True
        else:
            error_msg = "❌ 異議駁回！法官認為你的推理有破綻：\n"
            if not q1.startswith("A"):
                error_msg += "\n👉 **【關於接觸面積】** 請重新閱讀卷宗，摩擦力的大小真的跟接觸面積有關嗎？"
            if not q2.startswith("B"):
                error_msg += "\n👉 **【關於動摩擦力】** 請回憶剛才的互動圖表，紅點掉下斜坡後，走的是什麼形狀的線？"
            st.error(error_msg)
            
    return False
