import streamlit as st

# --- 1. 網頁基本設定 (針對手機版優化) ---
st.set_page_config(
    page_title="理化別裝了！這場比賽我贏定了",
    page_icon="🏆",
    layout="centered", 
    initial_sidebar_state="collapsed" 
)

# --- 隱藏 Streamlit 預設的右上角選單與底部浮水印 ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 2. 頂部區塊：節目總視覺 (第一張圖 Logo) ---
# 已經替換為真實路徑：在 images 資料夾下的 png 檔
st.image("images/理化別裝了！這場比賽我贏定了.png", use_container_width=True)

# 霸氣的標題與精神標語
st.markdown("<h2 style='text-align: center; color: #E65100; font-weight: 900;'>理化別裝了！<br>這場比賽我贏定了 🏆</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 16px; font-weight: bold;'>看穿科學的偽裝，拿回屬於你的分數！</p>", unsafe_allow_html=True)
st.write("---")

# --- 3. 賽季選擇區 ---
seasons = ["第一季：化學大聯盟 ⚾", "第二季：籌備中... ⏳"]
selected_season = st.selectbox("📂 選擇你要挑戰的賽季", seasons)

st.write("---")

# --- 4. 內容區塊 (第一季) ---
if selected_season == "第一季：化學大聯盟 ⚾":
    
    # 【圖二】賽季主視覺圖 
    # 已經替換為真實路徑：在 images 資料夾下的 jpg 檔
    st.image("images/化學大聯盟.jpg", use_container_width=True)
    
    st.markdown("### 🧪 關於本季：化學大聯盟")
    st.info("微觀世界就像一個巨大的棒球場！那些看似可怕的化學分子，其實都是大聯盟裡的球員。跟著我們的轉播，看穿它們的球路，這場理化比賽，我們贏定了！")
    
    st.markdown("### 🎧 賽事轉播表 (共 10 集)")
    
    # 第一集：展開狀態，直接迎接超級新秀
    with st.expander("🌟 EP01 | 超級新秀電解質", expanded=True):
        st.markdown("**上架日期：2026/03**") 
        st.write("化學大聯盟的第一位超級新秀強勢登板！我們將破解『電解質』的基本概念。它們在水中的導電球路到底有多刁鑽？會為球場帶來什麼樣的化學變化？")
        
        # 🌟 播放器 (已經替換為真實的音檔路徑) 🌟
        st.audio("audio/第一季_化學大聯盟_超級新秀_電解質.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- 電解質與非電解質的世紀對決\n- 看懂阿瑞尼斯的解離暗號\n- 運動飲料裡到底藏了什麼秘密武器？")

    # 第二集到第十集：收合狀態
    for i in range(2, 11):
        with st.expander(f"🔒 EP{i:02d} | 精彩賽事轉播準備中...", expanded=False):
            st.write(f"第 {i} 集的戰術正在牛棚熱身中，剪輯完畢就會馬上派上場！敬請期待。")

# --- 內容區塊 (籌備中的賽季) ---
else:
    st.markdown("<h3 style='text-align: center;'>更多賽季，即將開打 ⚾</h3>", unsafe_allow_html=True)
    st.write("我們的教練團正在規劃接下來的 16 個賽季戰術（慢工出細活！），請隨時回來查看最新的轉播表！")

# --- 5. 底部互動區 ---
st.write("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>不想錯過任何一場致勝關鍵？記得訂閱並分享給你的戰友！</p>", unsafe_allow_html=True)

# 社交平台按鈕 (等寬排列)
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.button("🍎 Apple", use_container_width=True)
with col_b:
    st.button("🎧 Spotify", use_container_width=True)
with col_c:
    st.button("📺 YouTube", use_container_width=True)
