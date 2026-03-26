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

    # 🌟 NEW! 第五集：最新上架，預設展開 🌟
    with st.expander("🔥 EP05 | 五局下半的極限拆彈任務！世紀大決戰與酸鹼中和", expanded=True):
        st.markdown("**上架日期：2026/03**") 
        st.write("比賽進入最關鍵的五局下半！酸鹼兩大軍團終於要在球場上正面對決。這是一場需要屏氣凝神的「極限拆彈任務」（滴定實驗），由高塔上的鹼性狙擊手對決掩體裡的酸球隊！當兩軍互撞，居然會變成最無害的水？粉紅刺客「酚酞」將再次登場擔任客座裁判，精準抓出戰力歸零的終極平衡點！")
        
        # 播放器 (真實音檔路徑)
        st.audio("audio/第一季_化學大聯盟_極限拆彈.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **世紀大決戰通式**：酸 + 鹼 $\\rightarrow$ 水 + 鹽類 + 熱量（這是一場熱血沸騰的放熱反應！）。")
        st.markdown("- **大魔王陷阱**：化學上的「鹽類」只是球員互撞掉落的裝備碎片，絕對不能隨便拿來當炸薯條的食鹽吃！")
        st.markdown("- **極限拆彈任務（滴定實驗）**：利用已知濃度的部隊，去狙擊並計算未知濃度的敵軍。")
        st.markdown("- **狙擊手標準姿勢**：左手控制活塞，右手搖晃錐形瓶，視線平齊液面凹下最底端！")
        st.markdown("- **粉紅刺客的判決**：滴定終點時，只要多一滴鹼液，酚酞就會瞬間解除隱身引爆成紫紅色，宣告比賽結束！")
    
    # 第四集：改為預設收合
    with st.expander("🌟 EP04 | 進階數據解密！火力密度與神祕的 pH 計分板", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("歡迎來到大聯盟最機密的「進階數據分析室」！這集將為你拆解理化大魔王「體積莫耳濃度 ($M$)」的計算祕訣，還有超直覺的珍珠奶茶比喻！同時公開球場上的終極計分板「pH 值」，破解數字越小反而越酸的迷思，以及考試必考的「加水稀釋」致命陷阱！")
        
        st.audio("audio/第一季_化學大聯盟_進階數據.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **火力密度指標**：體積莫耳濃度 ($M$) = 溶質莫耳數 ÷ 溶液體積（絕對要用「公升」！）。")
        st.markdown("- **春訓配藥守則**：為什麼配製溶液不能一開始就把水加滿？")
        st.markdown("- **終極計分板 pH 值**：7 是平手，小於 7 是酸球隊的天下，大於 7 是鹼球隊的地盤！")
        st.markdown("- **必考大魔王陷阱**：酸性溶液瘋狂加水稀釋，pH 值會跨界變成鹼性嗎？極限到底在哪裡？")

    # 第三集：改為預設收合
    with st.expander("🌟 EP03 | 球場地下室的無名英雄：鹼性後勤部隊與神奇藥水", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("帶大家潛入球場地下室，認識大聯盟的傳奇「鹼性後勤部隊」！只要他們溶於水，就會亮出專屬的 $OH^-$ 臂章！這集我們要介紹大聯盟最機密的三大陣營鑑定神器，並破解三大鹼性王牌的特殊技能，以及強弱電解質的終極差異！")
        
        st.audio("audio/第一季_化學大聯盟_鹼性後勤部隊_神奇藥水.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **三大鑑定神器**：紅藍判官（石蕊試紙）、粉紅刺客（酚酞）、彩虹戰鬥儀（廣用指示劑）。")
        st.markdown("- **重裝水管終結者**：氫氧化鈉（燒鹼/苛性鈉），超強潮解與溶解油脂特性。")
        st.markdown("- **海綿大師**：氧化鈣（生石灰），吸水放熱變身熟石灰，自熱火鍋與檢驗二氧化碳的超級法寶。")
        st.markdown("- **亮光清潔兵**：氨水（弱鹼），刺鼻尿騷味化身玻璃清潔劑與外野草皮肥料。")
        st.markdown("- **戰力解析**：百分之百解離的「強電解質」vs. 部分解離的「弱電解質」。")

    # 第二集：改為預設收合
    with st.expander("🌟 EP02 | 狂轟猛炸的「酸」球隊強勢踢館", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("化學大聯盟中最具攻擊性的「酸球隊」登場！他們最愛投出 $H^+$ 的直球對決，極具腐蝕性的破壞力讓人膽戰心驚。當他們對決上「活性金屬」會擊出氫氣全壘打；碰上「碳酸鹽類」則會炸出二氧化碳！今天帶你深入牛棚，破解三大王牌投手與一位側投老將的致命球路！")
        
        st.audio("audio/第一季_化學大聯盟_酸球隊.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **三大王牌先發**：工業之母「硫酸」($H_2SO_4$) 的恐怖脫水性、穿微黃球衣的「鹽酸」($HCl$)，以及見光死的棕色瓶殺手「硝酸」($HNO_3$)。")
        st.markdown("- **打擊對決**：活性金屬產氫氣 vs. 碳酸鹽類產二氧化碳的必考賽況。")
        st.markdown("- **側投老將**：為什麼純的醋酸（弱酸）會被稱為「冰醋酸」？")
        st.markdown("- **安全警告**：稀釋硫酸的絕對規則與鹽酸混用漂白水的致命禁忌！")

    # 第一集：改為預設收合
    with st.expander("🌟 EP01 | 超級新秀電解質", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("化學大聯盟的第一位超級新秀強勢登板！我們將破解『電解質』的基本概念。它們在水中的導電球路到底有多刁鑽？會為球場帶來什麼樣的化學變化？")
        
        st.audio("audio/第一季_化學大聯盟_超級新秀_電解質.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- 電解質與非電解質的世紀對決\n- 看懂阿瑞尼斯的解離暗號\n- 運動飲料裡到底藏了什麼秘密武器？")

    # 第六集到第十集：收合狀態
    for i in range(6, 11):
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
        dummy.value = "https://scienceisveryeasy-mobile.streamlit.app/"; 
        
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
