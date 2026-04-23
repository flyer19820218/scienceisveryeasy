import streamlit as st
import streamlit.components.v1 as components

def render_reading_and_quiz():
    # 🌟 終極 CSS：統一 20px 大字、並強化法庭設計感
    st.markdown("""
        <style>
        div[class*="stRadio"] > label { font-size: 20px !important; font-weight: bold !important; color: #1e293b !important; line-height: 1.6 !important; margin-bottom: 15px !important; }
        div[class*="stRadio"] p { font-size: 20px !important; font-weight: 500 !important; color: #334155 !important; }
        div[class*="stRadio"] [data-testid="stWidgetSelectionColumn"] { gap: 15px !important; }
        u { text-decoration: underline; text-underline-offset: 4px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### ⚖️ 黎明化學法庭 S02E03：後台的生存法則")
    st.markdown("<div style='background-color: #e0f2fe; padding: 15px; border-radius: 8px; color: #0369a1; border-left: 5px solid #0284c7; font-size: 16px;'>💡 <b>審判長 <u>黎明</u></b>：『檢察官，既然辯方質疑肥皂的洗淨力，請立刻展示【去污四部曲】的動態證物，讓他們看看科學的暴力美學！』</div>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)

    # ... (卷宗內容與前版相同，此處略過節省空間，請保留您原本的閱讀文章) ...
    with st.container():
        st.markdown("#### 📁 檢方機密卷宗：食品保存與皂化反應")
        st.markdown("　　在後台，食材的保存是關鍵。真空包裝透過抽乾空氣來阻絕氧氣（O₂），防止氧化與細菌孳生。醃漬法則利用「滲透壓」原理，以高濃度的鹽或糖將細菌體內水分抽乾，使其脫水死亡。而低溫殺菌法（攝氏 62 到 65 度）則能消滅致病菌並保留鮮奶風味。", unsafe_allow_html=True)
        st.markdown("　　而卸妝用的肥皂，誕生於「皂化反應」。將油脂與強鹼（氫氧化鈉 NaOH）加熱後，會產生肥皂（脂肪酸鈉）與副產物甘油。在反應中，加入「酒精」並非作為催化劑，而是擔任「助溶劑」的角色，讓油脂與鹼水均勻混合。", unsafe_allow_html=True)

    st.write("---")

    # ==========================================
    # 🧬 旗艦版：去污四部曲動態圖解 (HTML5 + CSS Animation)
    # ==========================================
    st.markdown("#### 🧬 呈堂證供：去污機器人的【四步拔除】動畫")
    
    html_code = """
    <div style="font-family: sans-serif; background: #f8fafc; padding: 25px; border-radius: 20px; border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <div style="display: flex; justify-content: space-between; margin-bottom: 30px; text-align: center;">
            <div style="width: 23%;">
                <div style="width: 50px; height: 50px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-weight: bold;">1</div>
                <div style="font-size: 14px; font-weight: bold;">親油端<br>接近油垢</div>
            </div>
            <div style="width: 23%;">
                <div style="width: 50px; height: 50px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-weight: bold;">2</div>
                <div style="font-size: 14px; font-weight: bold;">咬住油污<br>向外拉扯</div>
            </div>
            <div style="width: 23%;">
                <div style="width: 50px; height: 50px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-weight: bold;">3</div>
                <div style="font-size: 14px; font-weight: bold;">乳化包圍<br>拔離表面</div>
            </div>
            <div style="width: 23%;">
                <div style="width: 50px; height: 50px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 10px; font-weight: bold;">4</div>
                <div style="font-size: 14px; font-weight: bold;">隨水沖走<br>恢復潔淨</div>
            </div>
        </div>

        <div style="position: relative; height: 250px; background: white; border-radius: 15px; border: 2px dashed #cbd5e1; overflow: hidden;">
            <style>
                @keyframes molecule-grab {
                    0% { transform: translate(-50px, -50px) rotate(0deg); }
                    30% { transform: translate(10px, 10px) rotate(15deg); }
                    60% { transform: translate(-20px, -40px) rotate(-10deg); }
                    100% { transform: translate(-100px, -150px) rotate(-45deg); opacity: 0; }
                }
                @keyframes oil-shrink {
                    0% { transform: scale(1); }
                    60% { transform: scale(0.8); }
                    100% { transform: scale(0); opacity: 0; }
                }
                .molecule { position: absolute; display: flex; align-items: center; animation: molecule-grab 4s infinite ease-in-out; }
                .oil { position: absolute; top: 50%; left: 50%; width: 80px; height: 80px; background: #f59e0b; border-radius: 50%; margin-top: -40px; margin-left: -40px; z-index: 1; animation: oil-shrink 4s infinite ease-in-out; }
            </style>
            
            <div class="oil" style="display: flex; align-items: center; justify-content: center; font-weight: bold; color: white;">油垢</div>
            
            <div class="molecule" style="top: 55%; left: 55%;">
                <div style="width: 60px; height: 4px; background: #475569;"></div>
                <div style="width: 15px; height: 15px; background: #3b82f6; border-radius: 50%;"></div>
            </div>
            <div class="molecule" style="top: 45%; left: 45%; animation-delay: 0.5s;">
                <div style="width: 60px; height: 4px; background: #475569;"></div>
                <div style="width: 15px; height: 15px; background: #3b82f6; border-radius: 50%;"></div>
            </div>
            
            <div style="position: absolute; bottom: 10px; width: 100%; text-align: center; color: #94a3b8; font-size: 12px;">科學動態演示：清潔劑分子正在將油垢乳化拔除</div>
        </div>
        
        <div style="display: flex; justify-content: center; gap: 30px; margin-top: 20px; font-weight: bold; color: #475569;">
            <span style="color: #475569;">⚫ 灰色：親油端 (咬住油)</span>
            <span style="color: #3b82f6;">🔵 藍色：親水端 (抓水)</span>
        </div>
    </div>
    """
    components.html(html_code, height=520)
    st.write("---")

    # ... (後續法庭交叉詰問內容與前版相同) ...
    # ==========================================
    # 💥 逆轉法庭交互區 (打臉時刻)
    # ==========================================
    st.markdown("#### 💥 交叉詰問：揭穿辯方的連環偽證！")
    
    st.markdown("<div style='background-color: #fee2e2; padding: 15px; border-radius: 8px; color: #991b1b; border-left: 5px solid #dc2626; font-size: 16px;'>🗣️ <b>辯護律師 <u>韓流</u></b>：<br>「法官大人！... (下略)」</div>", unsafe_allow_html=True)
    # ... 保留原本的題目與按鈕邏輯 ...
