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

    st.markdown("### ⚖️ 黎明物理法庭 S02E08：水上舞台的最終出道宣言")
    
    # 審判長對白
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『這是最終的舞台，也是最嚴苛的試煉。當練習生躍入水中，地球的重力與液體的浮力將進行最後的殊死戰。沉淪或是浮起，全由阿基米德的鐵律來判決。檢察官，請研讀這份最終卷宗，並在下方的【互動實驗室】中，親自解開鋼鐵巨輪為何能漂浮的逆天之謎！』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：阿基米德原理與排水法")
        
        st.markdown("　　當物體泡入液體中，液體會給予物體一個向上的托力，這就是「**浮力**」。古希臘學者阿基米德在泡澡時發現了計算浮力的最高鐵律：**物體受到的浮力，必定等於它所排開的液體重量**。換成公式就是：浮力 = 沒入水中的體積 × 液體的密度 ($B = V_{下} \\times d_{液}$)。", unsafe_allow_html=True)

        st.markdown("　　這項發現讓他成功破解了皇冠摻假的千古之謎。因為黃金的密度比白銀大，若是重量相同的純金與白銀，白銀的「體積」會比較大。如果工匠在皇冠裡偷摻了白銀，皇冠的總體積就會變大，丟入水中排開的水量也會變多，受到的浮力自然就比純金塊還大！", unsafe_allow_html=True)
        
        st.markdown("#### 📁 檢方機密卷宗：沉體與浮體的殘酷審判")

        st.markdown("　　在水上舞台，物體只有兩種命運：**沉底**或**漂浮**。當物體的密度大於液體密度時，就會成為「**沉體**」。此時物體完全沒入水中，排開液體的體積等於自身的總體積。但殘酷的是，即使它用盡全力排開水分獲得浮力，這股向上的浮力依然敵不過它自身向下的重力 ($B < W$)，最終只能無情下沉。", unsafe_allow_html=True)

        st.markdown("　　相反地，當物體的密度小於液體時，它會成為「**浮體**」。浮體會停留在水面上，此時它達到完美的二力平衡狀態：**向上的浮力，完完全全等於向下的重力 ($B = W$)**！這裡隱藏著考試最愛出的「死海陷阱」：很多人以為在死海浮起來是因為死海給了「更大的浮力」。大錯特錯！只要你是浮著的，不管是死海還是游泳池，浮力永遠等於你的體重。死海只是因為密度極高，你只需要排開「一點點體積」的水，就能獲得足夠的浮力，讓你大部分的身體都能露出水面而已。", unsafe_allow_html=True)

        st.markdown("#### 📁 檢方機密卷宗：鋼鐵巨輪的逆天改命")

        st.markdown("　　鐵的密度高達 7.8 g/cm³，實心鐵塊丟入水中必沉無疑。但為什麼重達數萬噸的鋼鐵郵輪卻能安然漂浮？答案在於「**結構改變命運**」。工程師將船體打造成巨大的「**空心**」結構。雖然總質量不變，但船的總體積被暴增了數百倍！當這艘空心鐵船壓入水中時，龐大的體積能排開極其驚人的水量，從而獲得巨大的浮力 ($B = W$)。這就是人類利用阿基米德原理，逆轉密度法則的偉大傑作。", unsafe_allow_html=True)

    st.write("---")
    
    # ==========================================
    # 🕹️ HTML5 互動實驗室 (浮力觀測站)
    # ==========================================
    st.markdown("#### 🛠️ 互動實驗室：阿基米德水上觀測站")
    st.info("👇 **請選擇不同的「測試物體」與「液體」，觀察物體是沉是浮！特別留意右側的【重力】與【浮力】數值是否達到平衡。**")
    
    html_code = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h4 style="margin-top: 0; color: #334155; text-align: center;">🛳️ 阿基米德浮力觀測站</h4>
        
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-bottom: 20px;">
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; width: 45%;">
                <label style="font-weight: bold; color: #0f172a;">1️⃣ 選擇測試物體</label><br>
                <select id="obj-select" style="width: 100%; margin-top: 10px; padding: 8px; border-radius: 4px; cursor: pointer; font-size: 16px;">
                    <option value="wood">🪵 實心木塊 (重 60g, 體積 100cm³)</option>
                    <option value="iron">🪨 實心鐵塊 (重 780g, 體積 100cm³)</option>
                    <option value="boat">⛴️ 空心鐵船 (重 780g, 體積 1000cm³)</option>
                </select>
            </div>
            <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; width: 45%;">
                <label style="font-weight: bold; color: #0f172a;">2️⃣ 選擇液體池</label><br>
                <select id="liq-select" style="width: 100%; margin-top: 10px; padding: 8px; border-radius: 4px; cursor: pointer; font-size: 16px;">
                    <option value="1.0">💧 純水 (密度 d = 1.0)</option>
                    <option value="1.2">🌊 死海鹽水 (密度 d = 1.2)</option>
                    <option value="0.8">🧪 酒精 (密度 d = 0.8)</option>
                </select>
            </div>
        </div>

        <div style="display: flex; justify-content: space-around; background: #fef3c7; padding: 15px; border-radius: 8px; border: 1px solid #fde68a; margin-bottom: 20px; font-size: 18px; font-weight: bold;">
            <div style="color: #b45309; text-align: center;">⬇️ 向下重力 (W)<br><span id="weight-val" style="font-size: 24px;">60</span> gw</div>
            <div id="status-val" style="color: #1e293b; text-align: center; font-size: 22px; padding-top: 10px;">浮體平衡<br>(B = W)</div>
            <div style="color: #047857; text-align: center;">⬆️ 向上浮力 (B)<br><span id="buoyancy-val" style="font-size: 24px;">60</span> gw</div>
        </div>

        <div style="position: relative; width: 100%; max-width: 400px; height: 250px; margin: 0 auto; background: white; border: 2px solid #cbd5e1; border-radius: 8px; overflow: hidden;">
            <div id="liquid-bg" style="position: absolute; bottom: 0; left: 0; width: 100%; height: 60%; background-color: rgba(59, 130, 246, 0.4); border-top: 3px solid #3b82f6; transition: background-color 0.5s;"></div>
            
            <div id="the-object" style="position: absolute; left: 50%; transform: translateX(-50%); top: 10%; width: 80px; height: 80px; background-color: #d97706; color: white; display: flex; justify-content: center; align-items: center; font-weight: bold; font-size: 24px; border-radius: 8px; transition: top 0.8s cubic-bezier(0.34, 1.56, 0.64, 1), height 0.5s, width 0.5s; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
                🪵
            </div>
            
            <div style="position: absolute; left: 10px; top: 40%; font-size: 12px; font-weight: bold; color: #1e293b; border-bottom: 1px dashed #1e293b; width: 95%;">水面</div>
        </div>

        <div id="explain-panel" style="margin-top: 15px; padding: 15px; background: #f1f5f9; border-radius: 8px; font-size: 15px; color: #334155; line-height: 1.6; font-weight: 500;">
            </div>
    </div>

    <script>
        const objSelect = document.getElementById('obj-select');
        const liqSelect = document.getElementById('liq-select');
        const weightVal = document.getElementById('weight-val');
        const buoyancyVal = document.getElementById('buoyancy-val');
        const statusVal = document.getElementById('status-val');
        const liquidBg = document.getElementById('liquid-bg');
        const theObject = document.getElementById('the-object');
        const explainPanel = document.getElementById('explain-panel');

        // 物體資料庫
        const objData = {
            'wood': { mass: 60, vol: 100, icon: '🪵', color: '#d97706', width: '80px', height: '80px', name: '實心木塊' },
            'iron': { mass: 780, vol: 100, icon: '🪨', color: '#475569', width: '60px', height: '60px', name: '實心鐵塊' },
            'boat': { mass: 780, vol: 1000, icon: '⛴️', color: '#94a3b8', width: '160px', height: '60px', name: '空心鐵船' }
        };

        function simulate() {
            const obj = objData[objSelect.value];
            const d_liq = parseFloat(liqSelect.value);
            
            // 液體顏色變化
            if(d_liq == 1.0) liquidBg.style.backgroundColor = "rgba(59, 130, 246, 0.4)";
            if(d_liq == 1.2) liquidBg.style.backgroundColor = "rgba(16, 185, 129, 0.4)";
            if(d_liq == 0.8) liquidBg.style.backgroundColor = "rgba(245, 158, 11, 0.4)";

            // 更新物體外觀
            theObject.innerText = obj.icon;
            theObject.style.backgroundColor = obj.color;
            theObject.style.width = obj.width;
            theObject.style.height = obj.height;

            // 物理計算
            let W = obj.mass; // 重量
            let d_obj = obj.mass / obj.vol; // 密度
            
            weightVal.innerText = W;

            let B = 0;
            let V_sub = 0;
            let isFloating = false;

            if (d_obj > d_liq) {
                // 沉體 (密度大於液體)
                isFloating = false;
                V_sub = obj.vol; // 全沒入
                B = V_sub * d_liq;
                
                statusVal.innerHTML = "<span style='color:#ef4444;'>沉體下沉<br>(B &lt; W)</span>";
                buoyancyVal.innerText = B.toFixed(1);
                buoyancyVal.style.color = "#ef4444";
                
                // 動畫：沉底 (容器高度250px，水線40%，底部約95%)
                theObject.style.top = "70%"; 
                
                explainPanel.innerHTML = `🚨 <b>審判結果：下沉！</b><br>因為 ${obj.name} 的密度 (${d_obj.toFixed(2)}) 大於液體密度 (${d_liq})。它全身沒入水中，排開了 ${V_sub} cm³ 的水，獲得了 ${B.toFixed(1)} gw 的浮力。但浮力依然打不過 ${W} gw 的重力，只能沉底。`;

            } else {
                // 浮體 (密度小於等於液體)
                isFloating = true;
                B = W; // 浮力必定等於重力
                V_sub = B / d_liq; // 根據阿基米德原理反推沒入體積
                
                statusVal.innerHTML = "<span style='color:#10b981;'>浮體平衡<br>(B = W)</span>";
                buoyancyVal.innerText = B.toFixed(1);
                buoyancyVal.style.color = "#047857";
                
                // 動畫：漂浮在水線附近 (水線在 top: 40%)
                // 根據沒入比例微調位置
                let subRatio = V_sub / obj.vol;
                let floatTop = 40 - (parseFloat(obj.height) / 2.5) * (1 - subRatio); 
                theObject.style.top = Math.max(10, floatTop) + "%";
                
                let extraTxt = "";
                if(objSelect.value === 'boat') {
                    extraTxt = `<br>✨ <b>鐵船奇蹟</b>：鐵的密度高達 7.8，但做成空心後，將總體積撐大到 1000cm³，平均密度降到 0.78，成功逆轉命運成為浮體！`;
                }

                explainPanel.innerHTML = `✅ <b>審判結果：漂浮！</b><br>這是一個浮體，此時達到二力平衡：<b>向上的浮力完完全全等於向下的重力 (${B} gw)</b>！它只需要排開 ${V_sub.toFixed(1)} cm³ 的水就足以支撐體重。${extraTxt}`;
            }
        }

        objSelect.addEventListener('change', simulate);
        liqSelect.addEventListener('change', simulate);
        
        // 初始執行
        simulate();
    </script>
    """
    components.html(html_code, height=650)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    # 辯護律師對白
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！檢察官的理化知識根本是三流的！<br><br><b>【關於鐵船漂浮】</b> 鐵這麼重的東西怎麼可能浮起來？實心鐵塊會沉，做成船能浮，絕對是因為船裡裝了巨大的引擎給了向上的動力，跟什麼阿基米德一點關係都沒有！<br><br><b>【關於死海浮力】</b> 我的當事人去死海游泳，能輕鬆浮在水面上，這鐵定是因為死海給他的『浮力』遠遠大於在游泳池裡受到的浮力！浮力越大，人浮得越高，這是連三歲小孩都知道的常識！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "⚖️ 第一回合：請指出辯方對「鐵船漂浮原理」的致命謬誤：",
        [
            "A. 「異議！鐵船能浮是因為海水裡有鹽分，如果在淡水裡鐵船還是會沉下去！」",
            "B. 「異議！鐵塊雖重，但打造成『空心』的船體後，極大化了『排開液體的體積』。根據阿基米德原理，排開的水量暴增，換取了足以抗衡自身重量的巨大浮力，這才是鋼鐵巨輪漂浮的真相！」",
            "C. 「異議！鐵船能浮是因為船的底部塗了防水漆，阻絕了液體壓力！」"
        ],
        index=None,
        key="q1"
    )

    st.write("<br>", unsafe_allow_html=True)

    q2 = st.radio(
        "⚖️ 第二回合：請指出辯方對「死海浮力（浮體觀念）」的經典錯誤：",
        [
            "A. 「異議！只要人是浮在水面上（浮體），達到二力平衡，『向上的浮力必定永遠等於人自身的體重』！死海只是因為密度大，讓人排開的水量『變少』就能達到體重平衡，但受到的總浮力跟在一般泳池裡是一模一樣的！」",
            "B. 「異議！死海的浮力確實比較大，但是因為死海的水溫比較高，所以熱脹冷縮導致人體變輕了！」",
            "C. 「異議！人在死海會浮起來是因為死海沒有重力，所以不需要浮力！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("⚖️ 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備！")
        elif q1.startswith("B") and q2.startswith("A"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！阿基米德原理證明了體積與排水量的神蹟，讓空心鐵船得以漂浮。而浮體的鐵律『浮力等於重量』更是打破了死海浮力較大的經典迷思。辯方律師的論點在嚴謹的物理公式前不攻自破！」\n\n🎉 **全劇終！恭喜檢察官，你已經成功擊破《黎明韓流》所有的力學詭計，成功守護了科學大聯盟的榮耀！** 🎉")
            return True
        else:
            error_msg = "❌ 異議駁回！法官認為你的推理有破綻：\n"
            if not q1.startswith("B"):
                error_msg += "\n👉 **【關於鐵船原理】** 請回憶剛才的實驗，實心鐵塊跟空心鐵船的『體積』差了多少？這對排開的水量有什麼影響？"
            if not q2.startswith("A"):
                error_msg += "\n👉 **【關於死海浮力】** 這是必考陷阱！只要是『浮體』，不論在哪裡，向上的浮力與向下的重量必定是什麼關係？"
            st.error(error_msg)
            
    return False
