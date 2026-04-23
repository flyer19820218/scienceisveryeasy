import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    st.markdown("### ⚖️ 黎明化學法庭 S02E02：巨無霸天團的戰袍試煉")
    
    # 審判長對白 (加入私名號 <u> 與 HTML 排版)
    st.markdown("<div style='background-color: #e0f2fe; padding: 15px; border-radius: 8px; color: #0369a1; border-left: 5px solid #0284c7; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『在演藝圈，你的結構決定了你的身價。今天我們要審判的主角，是由成千上萬個單體緊緊鎖在一起的巨型天團——聚合物。檢察官，請出示證據。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區 (法庭證據檔案)
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：聚合物的兩大陣營")
        
        st.markdown("　　如果說小分子是單打獨鬥的個體，那麼「聚合物」（又稱高分子化合物）就是由成千上萬個小分子（單體），透過共價鍵緊緊鎖在一起的巨型天團。這些天團的分子量極其龐大，起跳便是一萬以上。在化學界的舞台上，聚合物主要分為「天然」與「合成」兩大名門派系。", unsafe_allow_html=True)

        st.markdown("　　天然聚合物是大自然的完美傑作。其中包含由「葡萄糖」組成的醣類家族（如提供能量的澱粉、支撐植物骨架的纖維素）；以及由「胺基酸」組成的蛋白質家族（如蠶絲、羊毛、頭髮與皮膚）。此外，還有從樹汁中萃取，具備極強彈性的天然橡膠。相對於此，合成聚合物則是人類從石油提煉、在實驗室人工打造的強力新星，包含了合成纖維、合成橡膠以及廣泛使用的塑膠。", unsafe_allow_html=True)

        st.markdown("#### 🧪 戰袍的殘酷洗禮與燃燒鑑定")
        
        st.markdown("　　在舞台上，戰袍的材質決定了保養的命運。動物纖維（如純羊毛、蠶絲）的本質是高貴的「蛋白質」。蛋白質的致命傷便是「鹼性物質」，一旦使用強效的鹼性肥皂清洗，戰袍便會瞬間縮水、變形甚至糊化，因此只能使用中性洗潔劑。", unsafe_allow_html=True)

        st.markdown("　　若要查明未知的布料成分，最殘酷的鑑定法便是「燃燒」。植物纖維（纖維素）燃燒時帶有燒紙或枯葉的氣味，灰燼一碰即碎；動物纖維（蛋白質）則會散發出刺鼻的腐臭味，猶如烤焦的羽毛或頭髮；而合成纖維遇到高溫會立刻熔化縮成一團，燃燒後捲曲成堅硬的黑色結塊，並伴隨濃烈的塑膠味。", unsafe_allow_html=True)

    st.write("---")

    # ==========================================
    # 🧬 HTML5 互動引擎區 (塑膠雙雄加溫模擬)
    # ==========================================
    st.markdown("#### 🧬 呈堂證供：塑膠雙雄的合約結構")
    
    st.markdown("　　除了布料，我們腳下的舞台與道具也是學問。塑膠依據其內部的分子鏈結結構，分為兩種截然不同的命運。**熱塑性塑膠**擁有「鏈狀結構」，它們彼此獨立，加熱後會軟化變形，因此可以回收重塑（如寶特瓶 PET）。而**熱固性塑膠**則擁有強烈的「網狀結構」，一經成型便死死鎖住，加熱也不會熔化，無法回收重塑（如輪胎、防彈玻璃）。", unsafe_allow_html=True)
    
    st.markdown("　　**請檢察官親手拉動下方的「溫度控制器」**，觀察這兩種結構在高溫下的微觀反應差異：", unsafe_allow_html=True)
    
    html_code = """
    <div style="display: flex; justify-content: space-around; font-family: sans-serif; gap: 10px; margin-bottom: 15px;">
        <div style="text-align: center; background: #fdfcf9; padding: 10px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-top: 0; font-size: 18px;">證物 A：熱塑性塑膠</h4>
            <p style="font-size: 13px; color: #dc2626; font-weight: bold; margin-bottom: 5px;">鏈狀結構 (可回收)</p>
            <canvas id="canvas-thermo" width="250" height="200" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; width: 100%;"></canvas>
        </div>
        <div style="text-align: center; background: #fdfcf9; padding: 10px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-top: 0; font-size: 18px;">證物 B：熱固性塑膠</h4>
            <p style="font-size: 13px; color: #dc2626; font-weight: bold; margin-bottom: 5px;">網狀結構 (不可回收)</p>
            <canvas id="canvas-set" width="250" height="200" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; width: 100%;"></canvas>
        </div>
    </div>
    <div style="text-align: center; background: #1e293b; color: white; padding: 15px; border-radius: 8px;">
        <label for="tempSlider" style="font-size: 16px; font-weight: bold; margin-right: 10px;">🔥 溫度控制器：</label>
        <input type="range" id="tempSlider" min="0" max="100" value="0" style="width: 50%; vertical-align: middle;">
        <span id="tempValue" style="display:inline-block; width: 40px; font-weight: bold; margin-left: 10px;">25°C</span>
    </div>

    <script>
        const canvasThermo = document.getElementById('canvas-thermo');
        const ctxThermo = canvasThermo.getContext('2d');
        const canvasSet = document.getElementById('canvas-set');
        const ctxSet = canvasSet.getContext('2d');
        const slider = document.getElementById('tempSlider');
        const tempValue = document.getElementById('tempValue');

        let temp = 0;
        let time = 0;

        slider.addEventListener('input', function(e) {
            temp = parseInt(e.target.value);
            let displayTemp = 25 + temp * 2; 
            tempValue.innerText = displayTemp + "°C";
        });

        function drawThermo() {
            ctxThermo.clearRect(0, 0, canvasThermo.width, canvasThermo.height);
            ctxThermo.lineWidth = 4;
            ctxThermo.lineCap = 'round';
            
            // 畫 4 條獨立的鏈狀分子
            for(let i=0; i<4; i++) {
                let yBase = 40 + i * 40;
                // 溫度越高，鏈越往下滑動且越扭曲 (軟化熔化)
                let yOffset = temp > 50 ? (temp - 50) * (i * 0.5) : 0; 
                let wobble = temp * 0.2;

                ctxThermo.beginPath();
                ctxThermo.strokeStyle = '#3b82f6';
                for(let x=20; x<canvasThermo.width-20; x+=10) {
                    let wave = Math.sin(x * 0.05 + time + i) * wobble;
                    if(x === 20) ctxThermo.moveTo(x, yBase + yOffset + wave);
                    else ctxThermo.lineTo(x, yBase + yOffset + wave);
                }
                ctxThermo.stroke();
            }
        }

        function drawSet() {
            ctxSet.clearRect(0, 0, canvasSet.width, canvasSet.height);
            ctxSet.lineWidth = 3;
            ctxSet.strokeStyle = '#dc2626';
            ctxSet.fillStyle = '#991b1b';
            
            let cols = 5; let rows = 4;
            let xStep = canvasSet.width / cols;
            let yStep = canvasSet.height / rows;
            
            let shake = temp * 0.05; // 溫度變高只會震動，不會散開

            ctxSet.beginPath();
            // 畫網狀連結線
            for(let r=1; r<rows; r++) {
                for(let c=1; c<cols; c++) {
                    let x = c * xStep + (Math.random()-0.5)*shake;
                    let y = r * yStep + (Math.random()-0.5)*shake;
                    
                    if(c < cols-1) {
                        ctxSet.moveTo(x, y);
                        ctxSet.lineTo((c+1)*xStep + (Math.random()-0.5)*shake, r*yStep + (Math.random()-0.5)*shake);
                    }
                    if(r < rows-1) {
                        ctxSet.moveTo(x, y);
                        ctxSet.lineTo(c*xStep + (Math.random()-0.5)*shake, (r+1)*yStep + (Math.random()-0.5)*shake);
                    }
                }
            }
            ctxSet.stroke();
            
            // 畫交聯點 (原子團)
            for(let r=1; r<rows; r++) {
                for(let c=1; c<cols; c++) {
                    let x = c * xStep + (Math.random()-0.5)*shake;
                    let y = r * yStep + (Math.random()-0.5)*shake;
                    ctxSet.beginPath();
                    ctxSet.arc(x, y, 5, 0, Math.PI*2);
                    ctxSet.fill();
                }
            }
        }

        function animate() {
            time += 0.1;
            drawThermo();
            drawSet();
            requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(html_code, height=360)
    st.write("---")

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區 (雙重打臉時刻)
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！檢方對於服裝與舞台道具的指控根本是一派胡言！<br><br><b>【關於戰袍毀損案】</b> 我的當事人拿強效的『鹼性肥皂』去洗那件昂貴的純羊毛戰袍，結果衣服大縮水！這證明了那件衣服根本不是天然的動物纖維，而是便宜的假貨！<br><br><b>【關於舞台弊案】</b> 檢方指控我們的舞台地板極度不環保。但事實上，我們採購的是最高級的『熱固性塑膠』！這種材質不僅堅固，等巡迴演唱會結束後，還可以『加熱熔化、回收重塑』成下一次的舞台道具，這可是最環保的選擇！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # 問題 1：打臉戰袍清洗
    st.markdown("##### ⚖️ 第一回合：針對【戰袍毀損案】的異議")
    q1 = st.radio(
        "請指出辯方對「羊毛纖維性質」的無知盲點：",
        [
            "A. 「異議！羊毛的成分是『纖維素』，遇到鹼性本來就會縮水，這證明它是真的植物纖維！」",
            "B. 「異議！羊毛是天然的『蛋白質』！蛋白質最怕的就是強鹼，遇到強鹼縮水變形，恰恰證明了它就是貨真價實的純動物纖維！」",
            "C. 「異議！羊毛燃燒後會有塑膠味，所以它應該不怕鹼性肥皂，辯方在說謊！」"
        ],
        index=None,
        key="q1"
    )

    # 問題 2：打臉塑膠結構
    st.markdown("##### ⚖️ 第二回合：針對【舞台環保弊案】的異議")
    q2 = st.radio(
        "請指出辯方對「塑膠合約結構」的致命錯誤：",
        [
            "A. 「異議！熱固性塑膠是強烈的『網狀結構』！一旦成型定型，就算加熱也『絕對無法熔化』，根本不可能回收重塑，辯方在公然作偽證！」",
            "B. 「異議！只有熱固性塑膠可以回收，但前提是必須加入強酸溶解，不能用加熱的方式！」",
            "C. 「異議！熱固性塑膠是『鏈狀結構』，加熱後會氣化消失，根本連回收的殘渣都不會剩下！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("💥 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備，再拍桌抗議！")
        elif q1.startswith("B") and q2.startswith("A"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官重重敲下法槌：「檢察官說得完全正確！羊毛是蛋白質畏懼強鹼，而熱固性塑膠是無法熔化的網狀結構！辯方律師的化學常識簡直一塌糊塗！」\n\n✅ 成功戳破所有謊言，審判勝利，準備進入實戰演練！")
            return True
        else:
            # 針對答錯的地方給予個別提示
            error_msg = "❌ 異議駁回！法官認為你的論述有破綻：\n"
            if not q1.startswith("B"):
                error_msg += "\n👉 **【關於戰袍案】** 請重新翻閱卷宗，確認『羊毛』是植物纖維還是動物纖維？它對應的成分與弱點是什麼？"
            if not q2.startswith("A"):
                error_msg += "\n👉 **【關於舞台案】** 請親自拉動上方的溫度控制器，確認『熱固性塑膠』的結構在高溫下究竟會不會熔化滑動？"
            st.error(error_msg)
            
    return False
