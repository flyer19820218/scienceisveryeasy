import streamlit as st

# --- 網頁頁面配置 ---
st.set_page_config(
    page_title="自然好簡單 - Podcast",
    page_icon="🍃",
    layout="wide", # 使用寬屏模式
    initial_sidebar_state="expanded" # 預設展開側邊欄
)

# --- 側邊欄設計 (賽季導覽) ---
with st.sidebar:
    st.image("path_to_your_logo.png", use_column_width=True) # 放置你的節目 Logo
    st.markdown("---")
    st.title("賽季導覽")
    
    # 這裡預留未來擴充，目前只有第一季
    seasons = ["第一季：化學大聯盟", "其他賽季準備中..."]
    selected_season = st.radio("選擇你想收聽的賽季", seasons)
    
    st.markdown("---")
    st.markdown("### 關於節目")
    st.info("這裡是《理化別裝了！這一場比賽我贏定了》，我們用最簡單、有趣的方式講給你聽複雜的自然科學。")
    st.markdown("### 收聽平台")
    st.markdown("- [Apple Podcasts](#)")
    st.markdown("- [Spotify](#)")
    st.markdown("- [Google Podcasts](#)")

# --- 主頁面設計 ---

# 1. 節目標題與 Logo (如果側邊欄不放 Logo，可以放這裡)
st.title("🍃 理化別裝了！這一場比賽我贏定了")
st.write("---")

# 2. 賽季內容呈現
if selected_season == "第一季：化學大聯盟":
    
    # 使用 columns 來平衡畫面：左邊放賽季圖，右邊放集數
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("第一季：化學大聯盟 🧪⚾️")
        # 放置每一季設計的圖 - 化學大聯盟
        st.image("path_to_season_art.png", use_column_width=True) 
        st.write("""
        本季我們將帶領大家進入微觀的化學世界，將各種化學分子想像成大聯盟的球員，探索物質變化的奧秘！
        共有 10 集精彩內容，敬請期待！
        """)
        st.write("---")
        st.markdown("### 評分與回饋")
        st.write("喜歡我們的節目嗎？請給我們五星好評！")
        st.text_input("留言給我們...", key="feedback")
        st.button("提交回饋")

    with col2:
        st.subheader("集數列表")
        
        # --- 第一集 (詳細設計範例) ---
        with st.expander("EP01 | 超級新秀電解質 ✨", expanded=True):
            st.markdown("#### **本集簡介**")
            st.write("""
            化學大聯盟的第一位超級新秀登場！這集我們將介紹『電解質』的基本概念。
            它們是如何在水中導電的？就像球場上的新秀一樣，它們將為我們帶來什麼樣的物質變化？
            一起來探索這個充滿電力的精彩開場！
            """)
            
            # 互動式播放器 (替換成你實際的音檔連結)
            st.markdown("#### **立即收聽**")
            st.audio("https://www.w3schools.com/html/horse.ogg") # 範例音檔連結
            
            st.markdown("#### **本集亮點**")
            st.markdown("- 電解質與非電解質的區別")
            st.markdown("- 阿瑞尼斯的解離說簡介")
            st.markdown("- 生活中的電解質")
            
        st.write("---")
        
        # --- 預留其他集數占位符 (2-10集) ---
        for i in range(2, 11):
            with st.expander(f"EP{i:02d} | 精彩內容籌備中...", expanded=False):
                st.write(f"第 {i} 集的精彩內容正在錄製中，我們將會盡快與你分享。")
                # 這裡可以預留一個無法點擊的播放器或敬請期待的字樣

else:
    # 處理選擇「其他賽季準備中...」時的呈現
    st.header("敬請期待 🍃")
    st.write("我們正在加緊腳步錄製更多有趣的內容，請持續關注！")
    st.image("理化別裝了！這一場比賽我贏定了.png", width=300)
