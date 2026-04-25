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

    st.markdown("### ⚖️ 黎明物理法庭 S02E05：逆重力舞台的力學密碼")
    
    # 審判長對白
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『在絢麗的選秀舞台上，每一次完美的雙人托舉、每一次驚險的高空吊鋼絲，背後都是精準的力學計算。當多股力量同時作用在練習生身上時，物理法則會將它們化為一股決定命運的「合力」。檢察官，請透過這份卷宗揭開力圖的秘密，並在下方的【互動實驗室】中，親手找出突破逆重力的關鍵角度。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：力的合成與平行四邊形法")
        
        st.markdown("　　在舞台上，往往不會只有單一的力量在作用。當兩位伴舞試圖把 C 位隊友往上拋時，這兩股推力會結合成一個整體的效應，物理學上稱之為「**合力**」。若兩人力道皆為 30kgw 且方向完全相同（夾角為 0 度），合力就會達到最大的 60kgw，隊友瞬間就能飛上天。相反地，如果兩人在兩側互推（夾角為 180 度），力量就會互相抵銷，合力變為最小的 0kgw。", unsafe_allow_html=True)

        st.markdown("　　但如果在雙人托舉時，兩人站得很開，雙手斜斜地往內推呢？這時就必須動用「**平行四邊形法**」來計算。我們將這兩股力畫成兩個箭頭（長度代表大小，箭頭代表方向）。以此兩箭頭為邊，畫出一個虛線的平行四邊形，這個平行四邊形**中間的對角線**，就是真正發揮作用的「合力」！此時物理學的鐵律便顯現出來：**『兩力夾角愈大，合力愈小』**。斜向推力在左右方向會互相抵銷變成內耗，導致真正向上的合力縮水，C 位隊友自然就飛不起來了。", unsafe_allow_html=True)
        
        st.markdown("#### 📁 檢方機密卷宗：二力平衡與死亡鋼絲陷阱")

        st.markdown("　　當一個物體受到的所有合力為零時，它的運動狀態不會改變，這稱為「**力平衡**」。要達成最基本的「二力平衡」，必須嚴格遵守四大鐵律：**同物（作用在同一物體上）、等大（力量大小相等）、反向（方向相反）、同線（作用在同一直線上）**。此時物體會維持靜止，或以等速度進行直線運動。", unsafe_allow_html=True)

        st.markdown("　　在演唱會的高空吊鋼絲橋段中，常隱藏著致命的夾角陷阱。假設導演用兩條垂直平行的鋼絲吊起 60kgw 的練習生。此時兩條鋼絲完全向上，每條只需分擔 30kgw 的拉力。但為了視覺上的華麗，導演將兩根鋼絲在上方拉開，呈現極大的「V 字型」。這時危險就降臨了！因為鋼絲有了夾角，部分的拉力在水平方向互相抵銷。為了維持垂直方向依然有 60kgw 的向上合力來對抗重力，V 字型鋼絲**本身的張力（拉力）勢必得大幅暴增**。角度越開，鋼絲承受的撕裂力就越恐怖，甚至有斷裂的致命危險！", unsafe_allow_html=True)

    st.write("---")
    
    # ==========================================
    # 🕹️ HTML5 互動實驗室 (向量合成)
    # ==========================================
    st.markdown("#### 🛠️ 互動實驗室：合力與極限角度測試")
    st.info("👇 **請拖曳下方的滑桿改變兩股力 (F1 與 F2) 的夾角。觀察中間紅色的「合力」長度會如何變化，並留意最大與最小合力出現的時機！**")
    
    html_code = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center;">
        <h4 style="margin-top: 0; color: #334155;">📐 平行四邊形合力觀測儀</h4>
        
        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 15px;">
            <div style="background: white; padding: 10px 20px; border-radius: 8px; border: 1px solid #e2e8f0;">
                <span style="color: #3b82f6; font-weight: bold;">F1 = 40 kgw</span>
            </div>
            <div style="background: white; padding: 10px 20px; border-radius: 8px; border: 1px solid #e2e8f0;">
                <span style="color: #10b981; font-weight: bold;">F2 = 30 kgw</span>
            </div>
        </div>

        <label style="font-size: 16px; font-weight: bold; color: #0f172a;">調整兩力夾角: <span id="angle-val" style="color: #ea580c;">60</span> 度</label><br>
        <input type="range" id="angle" min="0" max="180" value="60" step="5" style="width: 100%; max-width: 400px; margin: 10px 0; cursor: pointer;">
        
        <div style="background-color: #fef3c7; padding: 15px; border-radius: 8px; margin: 15px auto; border: 1px solid #fde68a; width: 100%; max-width: 400px; font-size: 18px;">
            <span style="color: #92400e; font-weight: bold;">當前合力 (R): <span id="resultant-val" style="font-size: 24px; color: #b45309;">60.8</span> kgw</span>
        </div>

        <div style="position: relative; width: 100%; max-width: 400px; height: 300px; margin: 0 auto; background: white; border: 1px solid #cbd5e1; border-radius: 8px; overflow: hidden; display: flex; justify-content: center; align-items: center;">
            <svg id="vector-canvas" width="100%" height="100%" viewBox="-150 -150 300 300">
                <g stroke="#f1f5f9" stroke-width="1">
                    <line x1="-150" y1="0" x2="150" y2="0" />
                    <line x1="0" y1="-150" x2="0" y2="150" />
                </g>

                <path id="para-lines" d="" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5,5" />
                
                <defs>
                    <marker id="head-f1" orient="auto" markerWidth="6" markerHeight="8" refX="5" refY="4">
                        <path d="M0,0 V8 L6,4 Z" fill="#3b82f6" />
                    </marker>
                    <marker id="head-f2" orient="auto" markerWidth="6" markerHeight="8" refX="5" refY="4">
                        <path d="M0,0 V8 L6,4 Z" fill="#10b981" />
                    </marker>
                    <marker id="head-r" orient="auto" markerWidth="8" markerHeight="10" refX="6" refY="5">
                        <path d="M0,0 V10 L8,5 Z" fill="#dc2626" />
                    </marker>
                </defs>

                <line id="line-f1" x1="0" y1="0" x2="0" y2="0" stroke="#3b82f6" stroke-width="4" marker-end="url(#head-f1)" />
                <line id="line-f2" x1="0" y1="0" x2="0" y2="0" stroke="#10b981" stroke-width="4" marker-end="url(#head-f2)" />
                <line id="line-r" x1="0" y1="0" x2="0" y2="0" stroke="#dc2626" stroke-width="5" marker-end="url(#head-r)" />
                
                <circle cx="0" cy="0" r="5" fill="#0f172a" />
            </svg>
        </div>

        <div id="status-msg" style="margin-top: 15px; padding: 10px; border-radius: 6px; font-weight: bold; font-size: 15px; display: none;"></div>
        
    </div>

    <script>
        const angleInput = document.getElementById('angle');
        const angleVal = document.getElementById('angle-val');
        const resultantVal = document.getElementById('resultant-val');
        
        const lineF1 = document.getElementById('line-f1');
        const lineF2 = document.getElementById('line-f2');
        const lineR = document.getElementById('line-r');
        const paraLines = document.getElementById('para-lines');
        const statusMsg = document.getElementById('status-msg');

        // 固定力的大小 (畫面上的像素比例，1 kgw = 2px)
        const F1 = 40;
        const F2 = 30;
        const scale = 2; 

        function drawVectors(angleDeg) {
            angleVal.innerText = angleDeg;
            
            // 將角度轉為弧度，為了讓合力朝上，F1 放在 y 軸左側，F2 放在 y 軸右側對稱
            let halfAngleRad = (angleDeg / 2) * (Math.PI / 180);
            
            // 計算 F1 的終點 (向左斜上方)
            let f1x = -F1 * scale * Math.sin(halfAngleRad);
            let f1y = -F1 * scale * Math.cos(halfAngleRad);
            
            // 計算 F2 的終點 (向右斜上方)
            let f2x = F2 * scale * Math.sin(halfAngleRad);
            let f2y = -F2 * scale * Math.cos(halfAngleRad);

            // 計算合力 R 的終點 (F1x+F2x, F1y+F2y)
            let rx = f1x + f2x;
            let ry = f1y + f2y;

            // 畫線
            lineF1.setAttribute('x2', f1x);
            lineF1.setAttribute('y2', f1y);
            
            lineF2.setAttribute('x2', f2x);
            lineF2.setAttribute('y2', f2y);
            
            lineR.setAttribute('x2', rx);
            lineR.setAttribute('y2', ry);

            // 畫虛線平行四邊形
            let pathStr = `M ${f1x} ${f1y} L ${rx} ${ry} M ${f2x} ${f2y} L ${rx} ${ry}`;
            paraLines.setAttribute('d', pathStr);

            // 計算合力大小 (餘弦定理公式： R = sqrt(F1^2 + F2^2 + 2*F1*F2*cos(θ)))
            let angleRadTotal = angleDeg * (Math.PI / 180);
            let R_val = Math.sqrt(F1*F1 + F2*F2 + 2*F1*F2*Math.cos(angleRadTotal));
            resultantVal.innerText = R_val.toFixed(1);

            // 判斷並顯示極值提醒
            statusMsg.style.display = 'block';
            if (angleDeg == 0) {
                statusMsg.innerHTML = "🚀 夾角 0 度：達到【最大合力】！(方向相同，直接相加 40+30=70)";
                statusMsg.style.backgroundColor = "#dcfce7";
                statusMsg.style.color = "#166534";
                statusMsg.style.border = "1px solid #22c55e";
            } else if (angleDeg == 180) {
                statusMsg.innerHTML = "💥 夾角 180 度：降至【最小合力】！(方向相反，互相抵銷 40-30=10)";
                statusMsg.style.backgroundColor = "#fee2e2";
                statusMsg.style.color = "#991b1b";
                statusMsg.style.border = "1px solid #ef4444";
            } else {
                statusMsg.innerHTML = "⚖️ 鐵律發威：兩力【夾角越開，合力越小】！";
                statusMsg.style.backgroundColor = "#f1f5f9";
                statusMsg.style.color = "#475569";
                statusMsg.style.border = "1px solid #cbd5e1";
            }
        }

        // 初始化
        drawVectors(60);

        // 綁定滑桿事件
        angleInput.addEventListener('input', function() {
            drawVectors(parseInt(this.value));
        });
    </script>
    """
    components.html(html_code, height=650)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    # 辯護律師對白
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！這份報告簡直荒謬至極！<br><br><b>【關於合力計算】</b> 雙人托舉時，只要兩人出的力夠大就好，『角度』根本不影響合力！就像買東西一樣，30 塊加 30 塊永遠等於 60 塊，夾角 180 度時合力當然也是 60！<br><br><b>【關於死亡鋼絲】</b> 把吊鋼絲拉成 V 字型，是為了把重量『分散』給空氣！所以鋼絲張開的角度越大，鋼絲承受的拉力反而會變『小』，這絕對是最安全的做法！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "⚖️ 第一回合：請指出辯方對「夾角與合力關係」的謬誤：",
        [
            "A. 「異議！物理學鐵律：兩力『夾角越小，合力越小』。夾角 180 度時會互相疊加變成最大合力！」",
            "B. 「異議！合力的大小取決於兩力的夾角。夾角 0 度時為最大合力；夾角 180 度時，力量完全反向抵銷，會產生『最小合力』！」",
            "C. 「異議！平推時合力永遠是 0，因為重力會把力量吸走！」"
        ],
        index=None,
        key="q1"
    )

    st.write("<br>", unsafe_allow_html=True)

    q2 = st.radio(
        "⚖️ 第二回合：請指出辯方對「V字鋼絲拉力」的致命錯誤：",
        [
            "A. 「異議！當鋼絲張開呈 V 字型時，部分力量在水平方向互相抵銷。為了維持向上的合力抗衡體重，角度越開，鋼絲本身的『張力（拉力）』必須大幅增加，極易斷裂！」",
            "B. 「異議！V 字型的鋼絲不會斷裂，但會導致練習生失去重心，所以應該改用單手吊鋼絲！」",
            "C. 「異議！鋼絲的張開角度越大，拉力確實會變小，但是會產生龐大的摩擦力讓鋼絲起火燃燒！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("⚖️ 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備！")
        elif q1.startswith("B") and q2.startswith("A"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！從互動實驗中也能清楚看見，夾角 180 度時合力幾乎抵銷殆盡。而為了維持相同的向上托力，V字鋼絲的角度越開，繩索需承受的張力就越龐大。辯方律師缺乏基本力學常識，置練習生安全於不顧！」\n\n✅ 成功戳破所有謊言，審判勝利，成功捍衛了舞台安全的物理防線！")
            return True
        else:
            error_msg = "❌ 異議駁回！法官認為你的推理有破綻：\n"
            if not q1.startswith("B"):
                error_msg += "\n👉 **【關於合力計算】** 請回憶剛才的實驗室，當滑桿拉到 180 度時，合力是最大還是最小？"
            if not q2.startswith("A"):
                error_msg += "\n👉 **【關於死亡鋼絲】** 鋼絲斜拉時會產生無效的水平內耗力，為了撐起相同的體重，鋼絲本身需要出更多力還是更少力？"
            st.error(error_msg)
            
    return False
