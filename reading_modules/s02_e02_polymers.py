import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS 覆寫：強制題目與選項「一樣大 (20px)」
    st.markdown("""
        <style>
        /* 1. 調整題目標題 (Label) */
        div[class*="stRadio"] > label {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #1e293b !important;
            line-height: 1.6 !important;
            margin-bottom: 15px !important;
        }
        /* 2. 調整選項文字 (Paragraph) */
        div[class*="stRadio"] p {
            font-size: 20px !important;
            font-weight: 500 !important;
            color: #334155 !important;
        }
        /* 3. 增加選項間的垂直間距 */
        div[class*="stRadio"] [data-testid="stWidgetSelectionColumn"] {
            gap: 15px !important;
        }
        /* 私名號優化 */
        u {
            text-decoration: underline;
            text-underline-offset: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### ⚖️ 黎明化學法庭 S02E02：巨無霸天團的戰袍試煉")
    
    # 審判長對白
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
    # 🧬 結構視覺化區 (鏈狀 vs 網狀)
    # ==========================================
    st.markdown("#### 🧬 呈堂證供：塑膠結構的真相")
    st.markdown("　　請檢察官仔細觀察這兩種塑膠的微觀結構差異。左側的**鏈狀結構**分子間彼此獨立；右側的**網狀結構**分子間存在強大的橫向交聯。", unsafe_allow_html=True)
    
    html_code = """
    <div style="display: flex; justify-content: space-around; font-family: sans-serif; gap: 15px; margin-top: 10px;">
        <div style="text-align: center; background: #fdfcf9; padding: 15px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-bottom: 10px;">熱塑性塑膠 (鏈狀)</h4>
            <div style="height: 180px; display: flex; flex-direction: column; justify-content: space-around; background: white; border-radius: 8px; border: 1px solid #cbd5e1;">
                <div style="height: 8px; width: 80%; background: #3b82f6; border-radius: 4px; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
                <div style="height: 8px; width: 85%; background: #3b82f6; border-radius: 4px; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
                <div style="height: 8px; width: 75%; background: #3b82f6; border-radius: 4px; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
                <div style="height: 8px; width: 80%; background: #3b82f6; border-radius: 4px; margin: 0 auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);"></div>
            </div>
            <p style="font-size: 14px; color: #64748b; margin-top: 10px;"><b>特徵：獨立長鏈</b><br><span style="color:#059669;">✔ 加熱可熔化、可回收</span></p>
        </div>
        <div style="text-align: center; background: #fdfcf9; padding: 15px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-bottom: 10px;">熱固性塑膠 (網狀)</h4>
            <div style="height: 180px; position: relative; background: white; border-radius: 8px; border: 1px solid #cbd5e1; overflow: hidden;">
                <div style="position: absolute; top: 25%; left: 10%; height: 6px; width: 80%; background: #dc2626; border-radius: 3px;"></div>
                <div style="position: absolute; top: 50%; left: 10%; height: 6px; width: 80%; background: #dc2626; border-radius: 3px;"></div>
                <div style="position: absolute; top: 75%; left: 10%; height: 6px; width: 80%; background: #dc2626; border-radius: 3px;"></div>
                <div style="position: absolute; top: 25%; left: 30%; height: 50%; width: 6px; background: #dc2626;"></div>
                <div style="position: absolute; top: 25%; left: 50%; height: 50%; width: 6px; background: #dc2626;"></div>
                <div style="position: absolute; top: 25%; left: 70%; height: 50%; width: 6px; background: #dc2626;"></div>
            </div>
            <p style="font-size: 14px; color: #64748b; margin-top: 10px;"><b>特徵：橫跨交聯</b><br><span style="color:#dc2626;">✘ 加熱不熔化、不可回收</span></p>
        </div>
    </div>
    """
    components.html(html_code, height=450)
    st.write("---")

    st.write("<br>", unsafe_allow_html=True)
    
    # ==========================================
    # 💥 逆轉法庭交互區 (打臉時刻)
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    # 辯護律師對白
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！檢方對於服裝與舞台道具的指控根本是一派胡言！<br><br><b>【關於戰袍毀損案】</b> 我的當事人拿強效的『鹼性肥皂』去洗那件昂貴的純羊毛戰袍，結果衣服大縮水！這證明了那件衣服根本不是天然的動物纖維，而是便宜的假貨！<br><br><b>【關於舞台弊案】</b> 檢方指控我們的舞台地板極度不環保。但事實上，我們採購的是最高級的『熱固性塑膠』！這種材質不僅堅固，等巡迴演唱會結束後，還可以『加熱熔化、回收重塑』成下一次的舞台道具，這可是最環保的選擇！」</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "⚖️ 第一回合：請指出辯方對「羊毛纖維性質」的無知盲點：",
        [
            "A. 「異議！羊毛的成分是『纖維素』，遇到鹼性本來就會縮水，這證明它是真的植物纖維！」",
            "B. 「異議！羊毛是天然的『蛋白質』！蛋白質最怕的就是強鹼，遇到強鹼縮水變形，恰恰證明了它就是貨真價實的純動物纖維！」",
            "C. 「異議！羊毛燃燒後會有塑膠味，所以它應該不怕鹼性肥皂，辯方在說謊！」"
        ],
        index=None,
        key="q1"
    )

    st.write("<br>", unsafe_allow_html=True)

    q2 = st.radio(
        "⚖️ 第二回合：請指出辯方對「塑膠合約結構」的致命錯誤：",
        [
            "A. 「異議！熱固性塑膠是強烈的『網狀結構』！一旦成型定型，就算加熱也『絕對無法熔化』，根本不可能回收重塑，辯方在公然作偽證！」",
            "B. 「異議！只有熱固性塑膠可以回收，但前提是必須加入強酸溶解，不能用加熱的方式！」",
            "C. 「異議！熱固性塑膠是『鏈狀結構』，加熱後會氣化消失，根本連回收的殘渣都不會剩下！」"
        ],
        index=None,
        key="q2"
    )
    
    if st.button("⚖️ 提出雙重異議 (Objection!)", use_container_width=True):
        if not q1 or not q2:
            st.warning("檢察官，請先完成『兩回合』的反駁論點準備，再拍桌抗議！")
        elif q1.startswith("B") and q2.startswith("A"):
            st.success("💥 異議成立！(OBJECTION!)\n\n法官重重敲下法槌：「檢察官說得完全正確！羊毛是蛋白質畏懼強鹼，而熱固性塑膠是無法熔化的網狀結構！辯方律師的化學常識簡集一塌糊塗！」\n\n✅ 成功戳破所有謊言，審判勝利，準備進入實戰演練！")
            return True
        else:
            # 針對答錯的地方給予個別提示
            error_msg = "❌ 異議駁回！法官認為你的論述有破綻：\n"
            if not q1.startswith("B"):
                error_msg += "\n👉 **【關於戰袍案】** 請重新翻閱卷宗，確認『羊毛』的主要成分與弱點！"
            if not q2.startswith("A"):
                error_msg += "\n👉 **【關於舞台案】** 請仔細觀察證物結構圖，確認『熱固性塑膠』的物理極限！"
            st.error(error_msg)
            
    return False
