import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS 覆寫：強制題目與選項「一樣大 (20px)」並美化排版
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

    st.markdown("### ⚖️ 黎明物理法庭 S02E04：玉山出道的減重騙局？")
    
    # 審判長對白
    st.markdown("<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; color: #166534; border-left: 5px solid #15803d; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『在光鮮亮麗的舞台背後，一切皆受制於力學法則。從練舞時肌肉的形變，到宣稱在玉山能瞬間減重的荒謬言論，物理的真相不容扭曲。檢察官，請透過這份卷宗拆穿謊言，並在下方的【互動實驗室】中，親自驗證虎克定律的核心陷阱。』</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 📖 深度素養閱讀區
    # ==========================================
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：力的效應與殘酷的「質量」真相")
        
        st.markdown("　　在演藝圈的殘酷訓練中，「力」雖然看不見，卻無處不在。力主要產生兩種明顯的效應：一是「**運動狀態的改變**」，例如練習生起跳、深蹲或舞台走位；二是「**形狀的改變**」，例如拉筋劈腿時身體產生的形變。力又分為兩大門派：必須碰觸物體才能發揮作用的「**接觸力**」（如鞋底與舞台的摩擦力），以及不須接觸的「**非接觸力／超距力**」（如地球引力）。", unsafe_allow_html=True)

        st.markdown("　　近期有經紀公司宣稱，將練習生帶到海拔 3952 公尺的玉山主峰特訓，體重計上的數字明顯減少，這被包裝為「玉山減重法」。**然而，這是物理學上的無恥騙局！** 在物理世界中，「**質量**」是純量，代表身體真正含有的物質（如脂肪與肌肉）多寡。無論你是在平地、玉山還是月球，物體本身的質量絕對不會改變。而體重計量測出的其實是「**重量**」，它是一種向量，代表地球引力對物體的拉扯力。在玉山山頂，因為距離地心變遠，地球的引力微幅下降，導致重量變輕。但這只不過是引力變化造成的假象，一旦回到平地舞台，引力恢復，數字立刻打回原形，真實的脂肪一公克都沒少！", unsafe_allow_html=True)
        
        st.markdown("#### 📁 檢方機密卷宗：虎克定律的陷阱與彈性極限")

        st.markdown("　　為了解析物體受力的規律，十七世紀的科學家虎克提出了一個偉大的法則：在彈性限度內，彈簧的「**伸長量**」與所受的「**拉力**」成正比（用力越猛，拉得越長）。這裡隱藏著力學考試中最致命的陷阱：計算時絕對、必須只能使用「**伸長量**」（也就是拉長後的總長度減去初始的原長），千萬不能直接拿「總長度」來計算比例！", unsafe_allow_html=True)

        st.markdown("　　然而，任何彈簧（包含人體的韌帶）都有其承受的底線，這條底線稱為「**彈性極限**」。一旦對物體施加的拉力超越了這個極限，物體就會產生「**永久形變**」，即使鬆手也再也彈不回來。這在現實中，就像是練習生為了追求極致的舞蹈動作，瞬間過度拉扯身體，造成了無法挽回的永久職業傷害。此外，若長期過度受力變形拉扯，即使沒有瞬間超過極限，也會發生「**彈性疲乏**」，宣告生涯報銷。", unsafe_allow_html=True)

    st.write("---")
    
    # ==========================================
    # 🕹️ HTML5 互動實驗室 (Streamlit Components)
    # ==========================================
    st.markdown("#### 🛠️ 互動實驗室：虎克定律與極限測試")
    st.info("👇 **請拖解下方的滑桿，觀察拉力對彈簧的影響。注意「伸長量」與「總長度」的差別，並試著挑戰超過彈簧的極限！**")
    
    html_code = """
    <div style="font-family: 'Helvetica Neue', sans-serif; padding: 20px; background-color: #f8fafc; border-radius: 12px; border: 2px solid #cbd5e1; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h4 style="margin-top: 0; color: #334155;">📐 彈簧拉伸檢測儀</h4>
        <label style="font-size: 16px; font-weight: bold; color: #0f172a;">施加拉力 (gw): <span id="force-val" style="color: #2563eb;">0</span> gw</label><br>
        <input type="range" id="force" min="0" max="150" value="0" step="10" style="width: 100%; margin-top: 10px; cursor: pointer;">
        
        <div style="background-color: white; padding: 15px; border-radius: 8px; margin-top: 15px; border: 1px solid #e2e8f0; display: flex; justify-content: space-around; text-align: center;">
            <div>
                <div style="font-size: 14px; color: #64748b;">初始原長</div>
                <div style="font-size: 20px; font-weight: bold; color: #334155;">10.0 cm</div>
            </div>
            <div>
                <div style="font-size: 14px; color: #ea580c; font-weight: bold;">伸長量 (ΔX)</div>
                <div id="stretch-val" style="font-size: 20px; font-weight: bold; color: #ea580c;">0.0 cm</div>
            </div>
            <div>
                <div style="font-size: 14px; color: #64748b;">總長度</div>
                <div id="total-val" style="font-size: 20px; font-weight: bold; color: #334155;">10.0 cm</div>
            </div>
        </div>

        <div style="margin-top: 20px; display: flex; flex-direction: column; align-items: center; min-height: 220px;">
            <div style="width: 100px; height: 10px; background-color: #475569; border-radius: 2px;"></div>
            <div id="spring" style="width: 30px; height: 50px; background: repeating-linear-gradient(0deg, #94a3b8, #94a3b8 6px, transparent 6px, transparent 12px); transition: height 0.3s ease-out; margin-top: 0;"></div>
            <div id="weight" style="width: 60px; height: 40px; background-color: #3b82f6; color: white; text-align: center; line-height: 40px; font-weight: bold; border-radius: 4px; transition: background-color 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">0 gw</div>
        </div>

        <div id="warning" style="margin-top: 15px; padding: 10px; background-color: #fef2f2; color: #dc2626; border: 1px solid #f87171; border-radius: 6px; font-weight: bold; text-align: center; display: none;">
            ⚠️ 警告：施力已超越「彈性極限」！<br>彈簧發生「永久形變」，無法恢復原狀！
        </div>
    </div>

    <script>
        const forceInput = document.getElementById('force');
        const forceVal = document.getElementById('force-val');
        const stretchVal = document.getElementById('stretch-val');
        const totalVal = document.getElementById('total-val');
        const spring = document.getElementById('spring');
        const weight = document.getElementById('weight');
        const warning = document.getElementById('warning');
        
        let isBroken = false;

        forceInput.addEventListener('input', function() {
            let f = parseInt(this.value);
            forceVal.innerText = f;
            weight.innerText = f + ' gw';
            
            // 假設每 10gw 伸長 1cm，彈性極限設為 100gw
            if (!isBroken) {
                if (f <= 100) {
                    let stretch = f * 0.1;
                    stretchVal.innerText = stretch.toFixed(1) + ' cm';
                    totalVal.innerText = (10 + stretch).toFixed(1) + ' cm';
                    // 基礎高度 50px，每公分增加 5px
                    spring.style.height = (50 + stretch * 8) + 'px';
                    warning.style.display = 'none';
                    weight.style.backgroundColor = '#3b82f6';
                } else {
                    // 超過極限，弄壞彈簧
                    isBroken = true;
                    warning.style.display = 'block';
                    stretchVal.innerText = "變形失準";
                    totalVal.innerText = "變形失準";
                    spring.style.height = '180px'; 
                    spring.style.background = 'repeating-linear-gradient(0deg, #ef4444, #ef4444 2px, transparent 2px, transparent 25px)';
                    weight.style.backgroundColor = '#ef4444';
                }
            } else {
                // 如果已經壞了，拉力改變，但長度回不去了
                if (f === 0) {
                    spring.style.height = '150px'; // 永久形變，回不到 50px
                    stretchVal.innerText = "無法恢復";
                    totalVal.innerText = "無法恢復";
                } else {
                    spring.style.height = (150 + f * 0.3) + 'px'; // 壞掉後亂伸長
                }
            }
        });
    </script>
    """
    components.html(html_code, height=550)

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    # 辯護律師對白
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！這份卷宗根本是惡意打壓！<br><br><b>【關於玉山減重】</b> 我的當事人在玉山上量體重真的變輕了！體重計數字減少就是瘦了！重量變輕，就代表體內的脂肪『質量』也跟著憑空消失了！這就是物理奇蹟！<br><br><b>【關於虎克定律】</b> 我們在練舞時，劈腿拉出來的『總長度』就代表實力！虎克定律早就說了，拉力跟『總長度』成正比！為了最完美的表演，就算突破身體的『彈性極限』也是一種自我進化！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "⚖️ 第一回合：請指出辯方對「玉山減重（質量與重量）」的謬誤：",
        [
            "A. 「異議！體重計上變輕的是受引力影響的『重量（向量）』，但代表身體真正肉量脂肪的『質量（純量）』根本沒變，下山就打回原形了！」",
            "B. 「異議！玉山因為空氣稀薄，導致人體的浮力增加，其實質量有減少，只是律師算錯公式了！」",
            "C. 「異議！在玉山數字變小是因為高山上的摩擦力變小，跟質量或重量根本毫無關聯！」"
        ],
        index=None,
        key="q1"
    )

    st.write("<br>", unsafe_allow_html=True)

    q2 = st.radio(
        "⚖️ 第二回合：請指出辯方對「虎克定律與極限」的致命錯誤：",
        [
            "A. 「異議！虎克定律是拉力與『總長度』成正比！而且突破彈性極限人體會進入無重力狀態！」",
            "B. 「異議！虎克定律看的是『伸長量』而非總長度！且對物體施力超越『彈性極限』會造成無法恢復的永久形變，那是職業傷害，絕非進化！」",
            "C. 「異議！虎克定律是指重力跟質量成正比，只要不斷拉伸，彈簧的質量就會越來越大！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("⚖️ 提出雙重異議 (Double Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備！")
        elif q1.startswith("A") and q2.startswith("B"):
            st.success("💥 雙重異議成立！(OBJECTION!)\n\n法官敲下法槌：「檢察官說得完全正確！從互動實驗中也能清楚看見，超過彈性極限只會帶來永久的破壞。質量與重量的區別，以及伸長量的陷阱，在力學鐵證前不攻自破！」\n\n✅ 成功戳破所有謊言，審判勝利，成功捍衛物理學的真相！")
            return True
        else:
            error_msg = "❌ 異議駁回！法官認為你的推理有破綻：\n"
            if not q1.startswith("A"):
                error_msg += "\n👉 **【關於玉山減重】** 請重新確認「重量（受引力影響）」與「質量（物質真正含量）」的區別！"
            if not q2.startswith("B"):
                error_msg += "\n👉 **【關於虎克定律】** 請回憶剛才的互動實驗，成正比的是哪一個長度？超過極限會發生什麼事？"
            st.error(error_msg)
            
    return False
