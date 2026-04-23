import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    st.markdown("### 📜 黎明韓流 S02E01 戰術板：碳基生命的審判")
    st.info("💡 **舞台導師韓流**：『首輪試鏡的標準非常嚴格！練習生們身上的服裝與本質，必須是真正的有機化合物。搞錯定義、認錯家族，就直接淘汰！』")
    
    # ==========================================
    # 📖 完整知識點閱讀區
    # ==========================================
    with st.expander("📖 賽前機密檔案：有機化學全指南 (點擊展開閱讀)", expanded=True):
        st.markdown("""
        #### 一、 有機物的血統證明與四大叛徒
        * **古典 vs 現代**：早期以為只有生物能製造有機物，直到**烏拉**在實驗室用無機物合成出「尿素」，神話才破滅！現在的定義很簡單：**只要含有碳（C）元素，就是有機物。**
        * 🛑 **四大叛徒陷阱**：有四種物質雖然含碳，但性質偏向無機物，直接被歸類為無機物！
          1. **一氧化碳 (CO)**
          2. **二氧化碳 (CO₂)**
          3. **碳酸鹽類** (例如大理石的成分：碳酸鈣 CaCO₃)
          4. **氰化物** (例如劇毒 KCN)

        #### 二、 殘酷檢驗法：乾餾與燃燒
        * **木材乾餾法**：用鋁箔紙包覆物質，**「隔絕空氣加熱」**，逼出極限產物。
          * **氣體**：可燃的 (CO、CH₄、H₂) + 不可燃的 (CO₂)。
          * **液體**：黑色焦油 + **酸性的醋酸** (使石蕊試紙變紅)。
          * **固體**：留在底部的黑色碳顆粒。
        * **燃燒檢驗法**：
          * 氣體讓**澄清石灰水變混濁** 👉 產生 CO₂ 👉 證明有**碳 (C)** 元素。
          * 氣體讓**乾燥藍色氯化亞鈷試紙變粉紅色** 👉 產生 H₂O 👉 證明有**氫 (H)** 元素。

        #### 三、 四大偶像家族 (分組考核)
        1. **烴 (ㄊㄧㄥ) 類**：只含碳、氫。碳數少為氣態 (如甲烷 CH₄ 是天然氣)，碳數變多則轉為液態、固態。
        2. **醇類**：帶有羥基 (-OH)。**乙醇 (C₂H₅OH)** 是安全可消毒的酒精；**甲醇 (CH₃OH)** 是工業用木精，有劇毒，誤食會失明甚至死亡！
        3. **有機酸類**：帶有羧基 (-COOH)，呈酸性。如甲酸 (蟻酸)、乙酸 (醋酸)。
        4. **酯類**：由「有機酸 + 醇類」滴入**濃硫酸 (催化劑/脫水劑)** 製成。有水果香味，密度比水小，難溶於水。

        #### 四、 終極密碼：同分異構物
        * **定義**：分子式完全相同 (原子種類與數量一樣)，但**原子排列的結構式截然不同**！
        * **實例**：乙醇 (液體、可消毒) 與 甲醚 (氣體)。兩者都是 C₂H₆O，但結構不同，物理與化學性質就完全不同！長得一樣，不代表實力一樣！
        """)
        
    st.write("---")

    # ==========================================
    # 🧬 3D 互動：同分異構物視覺化 (自訂藍色氫原子)
    # ==========================================
    st.markdown("#### 🧬 終極密碼：同分異構物 (請動手旋轉看看！)")
    st.write("這兩個傢伙的分子式完全相同（都是 C₂H₆O），也就是說它們用了**一模一樣種類與數量的原子**。但因為「骨架結構」拼法不同，造就了完全不同的命運！")
    
    html_code = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://3Dmol.csb.pitt.edu/build/3Dmol-min.js"></script>
    <div style="display: flex; justify-content: space-around; font-family: sans-serif; gap: 10px;">
        <div style="text-align: center; background: #fdfcf9; padding: 10px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-top: 0; font-size: 18px;">乙醇 (Ethanol)</h4>
            <p style="font-size: 14px; color: #dc2626; font-weight: bold; margin-bottom: 2px;">常溫：液體 (可消毒、飲用)</p>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 8px;">骨架：C - C - O</p>
            <div id="container-ethanol" style="height: 250px; width: 100%; position: relative;"></div>
        </div>
        <div style="text-align: center; background: #fdfcf9; padding: 10px; border-radius: 12px; border: 2px solid #e2e8f0; width: 48%;">
            <h4 style="color: #1e293b; margin-top: 0; font-size: 18px;">甲醚 (Dimethyl Ether)</h4>
            <p style="font-size: 14px; color: #dc2626; font-weight: bold; margin-bottom: 2px;">常溫：氣體 (作為燃料)</p>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 8px;">骨架：C - O - C</p>
            <div id="container-ether" style="height: 250px; width: 100%; position: relative;"></div>
        </div>
    </div>
    <div style="text-align: center; background: #1e293b; color: white; padding: 8px; border-radius: 8px; font-size: 14px; margin-top: 15px;">
        👆 <b>互動提示</b>：按住滑鼠拖曳可 360° 旋轉立體分子，滾輪可縮放。<br>
        <span style="color: #cbd5e1;">( <b>⚫灰球</b>：碳原子 C | <b>🔴紅球</b>：氧原子 O | <b style="color:#60a5fa;">🔵藍球</b>：氫原子 H )</span>
    </div>
    <script>
        $(document).ready(function() {
            // 載入乙醇 (CID: 702)
            let viewer1 = $3Dmol.createViewer("container-ethanol", {backgroundColor: "white"});
            $3Dmol.download("cid:702", viewer1, {}, function() {
                // 先套用標準色
                viewer1.setStyle({}, {stick: {radius: 0.15, colorscheme: 'Jmol'}, sphere: {scale: 0.3, colorscheme: 'Jmol'}});
                // 強制覆寫：把氫原子 (H) 變成藍色 (blue)
                viewer1.setStyle({elem: 'H'}, {stick: {radius: 0.15, color: '#3b82f6'}, sphere: {scale: 0.3, color: '#3b82f6'}});
                viewer1.zoomTo();
                viewer1.render();
            });

            // 載入甲醚 (CID: 8254)
            let viewer2 = $3Dmol.createViewer("container-ether", {backgroundColor: "white"});
            $3Dmol.download("cid:8254", viewer2, {}, function() {
                // 先套用標準色
                viewer2.setStyle({}, {stick: {radius: 0.15, colorscheme: 'Jmol'}, sphere: {scale: 0.3, colorscheme: 'Jmol'}});
                // 強制覆寫：把氫原子 (H) 變成藍色 (blue)
                viewer2.setStyle({elem: 'H'}, {stick: {radius: 0.15, color: '#3b82f6'}, sphere: {scale: 0.3, color: '#3b82f6'}});
                viewer2.zoomTo();
                viewer2.render();
            });
        });
    </script>
    """
    components.html(html_code, height=400)

    st.write("---")
    
    # ==========================================
    # 🔍 素養情境題
    # ==========================================
    st.markdown("#### 🔍 舞台突發狀況 (情境考核)")
    st.write("在服裝材質的『乾餾』檢驗關卡中，五號練習生拿著一瓶標示著 **CH₃OH** 的透明液體，興奮地對鏡頭說：")
    st.write("> *「製作人你看！我把衣服『隔絕空氣加熱』後，流出了會讓石蕊試紙變紅的酸性液體是純水！而且為了慶祝晉級，我要把手上這瓶 CH₃OH 乾杯喝掉！」*")
    
    q1 = st.radio(
        "身為總製作人，請你立刻奪下她的麥克風，並指出她話中**最致命的化學錯誤**：",
        [
            "A. 「乾餾產生的酸性液體是純水沒錯，但妳手上的 CH₃OH 燃燒後會產生碳酸鈣，不能喝！」",
            "B. 「乾餾必須在有氧氣的情況下燃燒！而且同分異構物的性質都一樣，甲醇跟乙醇可以隨便混著喝。」",
            "C. 「淘汰！乾餾產生的酸性液體是『醋酸』；而且妳手上拿的是劇毒的『甲醇 (木精)』，喝了會失明甚至喪命！」",
            "D. 「答對一半。產生的液體是焦油，而妳手上的 CH₃OH 是安全的乙醇酒精，可以拿來消毒與乾杯。」"
        ],
        index=None
    )
    
    if st.button("🛡️ 提交評判", use_container_width=True):
        if q1 is None:
            st.warning("請先選擇一個選項再送出！")
        elif q1.startswith("C"):
            st.success("✅ 評判精準，成功阻止了一場醫療悲劇！乾餾產生的酸性液體是醋酸，而 CH₃OH 是劇毒甲醇。審判通過，準備進入正式挑戰！")
            return True
        else:
            st.error("❌ 評判失誤！請打開上方的『賽前機密檔案』，重新複習【乾餾的液體產物】以及【醇類的致命陷阱】！")
            
    return False
