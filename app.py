import streamlit as st
import streamlit.components.v1 as components 

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
st.image("images/理化別裝了！這場比賽我贏定了.png", use_container_width=True)

# 霸氣的標題與精神標語 
st.markdown("<h2 style='text-align: center; color: #E65100; font-weight: 900; font-size: 22px; line-height: 1.4;'>理化別裝了！<br>這場比賽我贏定了 🏆</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 14px; font-weight: bold;'>看穿科學的偽裝，拿回屬於你的分數！</p>", unsafe_allow_html=True)
st.write("---")

# --- 3. 賽季選擇區 ---
seasons = ["第一季：化學大聯盟 ⚾", "第二季：籌備中... ⏳"]
selected_season = st.selectbox("📂 選擇你要挑戰的賽季", seasons)

st.write("---")

# --- 4. 內容區塊 (第一季) ---
if selected_season == "第一季：化學大聯盟 ⚾":
    
    # 【圖二】賽季主視覺圖 
    st.image("images/化學大聯盟.jpg", use_container_width=True)
    
    # 副標題
    st.markdown("<h3 style='font-size: 18px; font-weight: bold; color: #333; margin-bottom: 0px;'>🧪 關於本季：化學大聯盟</h3>", unsafe_allow_html=True)
    st.info("微觀世界就像一個巨大的棒球場！那些看似可怕的化學分子，其實都是大聯盟裡的球員。跟著我們的轉播，看穿它們的球路，這場理化比賽，我們贏定了！")
    
    # 副標題 
    st.markdown("<h3 style='font-size: 18px; font-weight: bold; color: #333; margin-top: 20px; margin-bottom: 0px;'>🎧 賽事轉播表 (共 10 集)</h3>", unsafe_allow_html=True)
    
    # 🌟 NEW! 第二集：最新上架，預設展開 🌟
    with st.expander("🔥 EP02 | 狂轟猛炸的「酸」球隊強勢踢館", expanded=True):
        st.markdown("**上架日期：2026/03**") 
        st.write("化學大聯盟中最具攻擊性的「酸球隊」登場！他們最愛投出 $H^+$ 的直球對決，極具腐蝕性的破壞力讓人膽戰心驚。當他們對決上「活性金屬」會擊出氫氣全壘打；碰上「碳酸鹽類」則會炸出二氧化碳！今天帶你深入牛棚，破解三大王牌投手與一位側投老將的致命球路！")
        
        # 播放器 (真實音檔路徑)
        st.audio("audio/第一季_化學大聯盟_酸球隊.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **三大王牌先發**：工業之母「硫酸」($H_2SO_4$) 的恐怖脫水性、穿微黃球衣的「鹽酸」($HCl$)，以及見光死的棕色瓶殺手「硝酸」($HNO_3$)。")
        st.markdown("- **打擊對決**：活性金屬產氫氣 vs. 碳酸鹽類產二氧化碳的必考賽況。")
        st.markdown("- **側投老將**：為什麼純的醋酸（弱酸）會被稱為「冰醋酸」？")
        st.markdown("- **安全警告**：稀釋硫酸的絕對規則與鹽酸混用漂白水的致命禁忌！")

    # 第一集：改為預設收合，保持版面清爽
    with st.expander("🌟 EP01 | 超級新秀電解質", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("化學大聯盟的第一位超級新秀強勢登板！我們將破解『電解質』的基本概念。它們在水中的導電球路到底有多刁鑽？會為球場帶來什麼樣的化學變化？")
        
        # 播放器 
        st.audio("audio/第一季_化學大聯盟_超級新秀_電解質.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- 電解質與非電解質的世紀對決\n- 看懂阿瑞尼斯的解離暗號\n- 運動飲料裡到底藏了什麼秘密武器？")

    # 第三集到第十集：收合狀態
    for i in range(3, 11):
        with st.expander(f"🔒 EP{i:02d} | 精彩賽事轉播準備中...", expanded=False):
            st.write(f"第 {i} 集的戰術正在牛棚熱身中，剪輯完畢就會馬上派上場！敬請期待。")

# --- 內容區塊 (籌備中的賽季) ---
else:
    st.markdown("<h3 style='text-align: center; font-size: 20px;'>更多賽季，即將開打 ⚾</h3>", unsafe_allow_html=True)
    st.write("我們的教練團正在規劃接下來的 16 個賽季戰術（慢工出細活！），請隨時回來查看最新的轉播表！")

# --- 5. 底部互動區 ---
st.write("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 14px;'>不想錯過任何一場致勝關鍵？趕快邀請戰友一起收聽！</p>", unsafe_allow_html=True)

# 單一「分享給你的朋友」複製連結按鈕
components.html(
    """
    <div style="display: flex; justify-content: center; padding: 5px;">
        <button id="shareBtn" onclick="copyLink()" 
            style="width: 100%; max-width: 400px; background-color: #E65100; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; font-weight: bold; font-family: sans-serif; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: 0.3s;">
            🔗 分享給你的朋友
        </button>
    </div>

    <script>
    function copyLink() {
        var dummy = document.createElement("input");
        document.body.appendChild(dummy);
        
        // ⚠️ 等你的網址正式確定後，請把下面這行引號裡的文字換成你的真實網址！
        dummy.value = "https://你的專屬網址.com"; 
        
        dummy.select();
        document.execCommand("copy");
        document.body.removeChild(dummy);
        
        var btn = document.getElementById("shareBtn");
        btn.innerText = "✅ 連結已複製！快去貼給戰友";
        btn.style.backgroundColor = "#4CAF50"; 
        
        setTimeout(function(){ 
            btn.innerText = "🔗 分享給你的朋友"; 
            btn.style.backgroundColor = "#E65100"; 
        }, 2000);
    }
    </script>
    """,
    height=75
)
