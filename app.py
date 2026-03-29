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

    # 🌟 NEW! 第八集：最新上架，預設展開 🌟
    with st.expander("🔥 EP08 | 反應速率與小球戰術！機關槍打線、滿壘壓力與超級教練", expanded=True):
        st.markdown("**上架日期：2026/03**") 
        st.write("比賽來到八局上半！主場球隊修築了高聳的全壘打牆，企圖利用極高「活化能」封鎖打線。教練團祭出戰術連環計：先用「機關槍打線」（接觸面積）不斷上壘，再把「壘包塞滿」（濃度與壓力）製造威脅。最後請出超級教練「催化劑」，下達觸擊短打與盜壘的「小球戰術」，直接改變反應途徑，順利突破僵局！")
        
        # 播放器 (音檔路徑對齊截圖檔名)
        st.audio("audio/第一季_化學大聯盟_第8集_反應速率與小球戰術.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **機關槍打線（接觸面積）**：將火力分散切碎。注意數學陷阱：邊長變 $1/n$，表面積僅變 $n$ 倍（切 729 塊表面積僅變 9 倍！）。")
        st.markdown("- **生活實例（表面積）**：嚼碎胃藥錠、揉皺紙錢再燃燒，都能大幅增加與氧氣或藥物的碰撞機會。")
        st.markdown("- **滿壘戰術（濃度與壓力）**：壘包越擠，碰撞機率越高。高濃度鹽酸對決碳酸鈣 ($CaCO_3$)，氣泡反應瞬間炸裂！")
        st.markdown("- **超級教練（催化劑）**：不親自跑壘卻親自指導。提供「低活化能途徑」（小球戰術），反應後質量性質不變可重複執教。")
        st.markdown("- **教練團四大特質**：專一性、反應前後不變、微量即可、可加速亦可減速（負催化劑如甘油）。")
        st.markdown("- **經典教練名單**：哈柏法製氨（鐵粉 $Fe$）、汽車觸媒轉化器（鉑、鈀）、生物酵素（酶）。")

    # 第七集
    with st.expander("🌟 EP07 | 超音速跑壘測試賽！雙重爆發與反應速率", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("比賽進入最熱血的 Lucky 7！今天我們帶上測速槍，看看這群化學新秀的爆發力有多驚人！從瞬間爆炸的煙火、幾個月才生鏽的鐵欄杆，到花費千百年才形成的石筍，化學反應的速度跨度超乎想像！想打出全壘打？你必須掌握「碰撞學說」的兩大絕對條件。還要揭開溫度帶來的「雙重爆發」秘密，以及超音速跑者與不動老將的活性對決！")
        
        st.audio("audio/第一季_化學大聯盟_第7集_超音速跑者與雙重爆發.mp3", format="audio/mp3")
        
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **反應速率的跨度**：煙火（極快） vs. 鐵生鏽（慢） vs. 鐘乳石筍形成（極慢）。")
        st.markdown("- **觀念大陷阱**：反應速率跟時間絕對是「成反比」的關係（速率可以用 $1/t$ 來表示），時間越短，速度越快！")
        st.markdown("- **碰撞學說兩大條件**：必須擊中甜蜜點（正確的碰撞方向）並全力揮擊（突破活化能）。")
        st.markdown("- **溫度的雙重爆發 (二次曲線)**：溫度升高，不僅讓球員跑更快（增加碰撞次數），還讓能量變高（更容易突破活化能門檻），產生相乘效果！")
        st.markdown("- **物質活性的天生差異**：超級快腿金屬鈉 ($Na$) 遇水劇烈反應，不動老將黃金 ($Au$) 則毫無反應。")

    # 第六集
    with st.expander("🌟 EP06 | 球場的五大無名英雄與石灰三兄弟變身大秀", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("六局上半正式開打！場務人員正在清理酸鹼互撞後掉落的「鹽類」戰利品。這集我們將開箱大聯盟最強的後勤裝備：從維持生命的 MVP「食鹽」、醫療團隊最愛的「石膏」，到畫線用的「大理石」！更精彩的是，我們還會目睹「石灰三兄弟」的終極變身魔術，以及最狂救援投手「蘇打兄弟檔」的滅火神技！")
        st.audio("audio/第一季_化學大聯盟_第6集_球場的五大無名英雄.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **維持生命的 MVP**：氯化鈉 ($NaCl$)，中性的食鹽，打點滴必備。")
        st.markdown("- **醫療團隊的最愛**：硫酸鈣 ($CaSO_4$)，微溶於水的白色石膏。")
        st.markdown("- **石灰三兄弟變身閉環**：灰石 ($CaCO_3$) 加熱 $\\rightarrow$ 生石灰 ($CaO$) 加水 $\\rightarrow$ 熟石灰 ($Ca(OH)_2$) 吹入二氧化碳 $\\rightarrow$ 變回白色混濁的灰石！")
        st.markdown("- **最狂蘇打兄弟檔**：硬漢哥哥「碳酸鈉」($Na_2CO_3$) 是鹼性洗滌鹼；怕熱弟弟「碳酸氫鈉」($NaHCO_3$) 則是弱鹼性小蘇打，遇熱會吐出二氧化碳來滅火跟做麵包！")

    # 第五集
    with st.expander("🌟 EP05 | 五局下半的極限拆彈任務！世紀大決戰與酸鹼中和", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("比賽進入最關鍵的五局下半！酸鹼兩大軍團終於要在球場上正面對決。這是一場需要屏氣凝神的「極限拆彈任務」（滴定實驗），由高塔上的鹼性狙擊手對決掩體裡的酸球隊！當兩軍互撞，居然會變成最無害的水？粉紅刺客「酚酞」將再次登場擔任客座裁判，精準抓出戰力歸零的終極平衡點！")
        st.audio("audio/第一季_化學大聯盟_第5集_極限拆彈.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **世紀大決戰通式**：酸 + 鹼 $\\rightarrow$ 水 + 鹽類 + 熱量（放熱反應！）。")
        st.markdown("- **極限拆彈任務（滴定實驗）**：左手控制活塞，右手搖晃錐形瓶，視線平齊液面凹下最底端！")
        st.markdown("- **粉紅刺客的判決**：滴定終點時，只要多一滴鹼液，酚酞就會瞬間解除隱身引爆成紫紅色，宣告比賽結束！")
    
    # 第四集
    with st.expander("🌟 EP04 | 進階數據解密！火力密度與神祕的 pH 計分板", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("歡迎來到大聯盟最機密的「進階數據分析室」！這集將為你拆解理化大魔王「體積莫耳濃度 ($M$)」的計算祕訣。同時公開球場上的終極計分板「pH 值」，破解數字越小反而越酸的迷思，以及「加水稀釋」致命陷阱！")
        st.audio("audio/第一季_化學大聯盟_第4集_進階數據_胃酸全壘打.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **火力密度指標**：體積莫耳濃度 ($M$) = 溶質莫耳數 ÷ 溶液體積（一定要用「公升」！）。")
        st.markdown("- **終極計分板 pH 值**：7 是平手，小於 7 是酸球隊，大於 7 是鹼球隊！")

    # 第三集
    with st.expander("🌟 EP03 | 球場地下室的無名英雄：鹼性後勤部隊與神奇藥水", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("認識大聯盟的傳奇「鹼性後勤部隊」！這集我們要介紹大聯盟最機密的三大陣營鑑定神器，並破解三大鹼性王牌的特殊技能，以及強弱電解質的終極差異！")
        st.audio("audio/第一季_化學大聯盟_第3集_鹼性後勤部隊_神奇藥水.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **三大鑑定神器**：紅藍判官（石蕊試紙）、粉紅刺客（酚酞）、彩虹戰鬥儀（廣用指示劑）。")
        st.markdown("- **王牌成員**：氫氧化納（燒鹼）、氧化鈣（生石灰）、氨水（弱鹼）。")

    # 🌟 第二集 (內容已全面升級擴充) 🌟
    with st.expander("🌟 EP02 | 狂轟猛炸的「酸」球隊強勢踢館", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("二局上半正式開打！大聯盟裡火力最兇猛、脾氣最火爆的「酸球隊」強勢登場！他們最愛投出 $H^+$ 的直球對決，極具腐蝕性的破壞力讓人膽戰心驚。這集我們不僅要破解三大強酸王牌的致命球路與實驗室保命守則，還要看穿他們對決「活性金屬」與「碳酸鹽類」時截然不同的化學反應！")
        st.audio("audio/第一季_化學大聯盟_第2集_酸球隊.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **招牌直球武器**：溶於水必定解離出帶正電的氫離子 ($H^+$)。")
        st.markdown("- **觀念大陷阱（打擊對決）**：遇到「活性金屬」轟出氫氣 ($H_2$) 全壘打；遇到「碳酸鈣」（大理石/貝殼）產生的絕對是二氧化碳 ($CO_2$)！")
        st.markdown("- **王牌一：硫酸 ($H_2SO_4$)**：化學工業之母。具有恐怖「脫水性」（方糖變黑炭）。稀釋絕對守則：務必「將酸緩慢加入水中」！")
        st.markdown("- **王牌二：鹽酸 ($HCl$)**：胃酸主要成分。工業級微黃是因為鐵離子。致命禁忌：洗廁所絕不能與漂白水混用（會產生劇毒氯氣）！")
        st.markdown("- **王牌三：硝酸 ($HNO_3$)**：見光死刺客，遇光分解出有毒紅棕色氣體，需保存在深色瓶。與鹽酸調配出的「王水」連黃金都能溶解！")
        st.markdown("- **弱酸救援老將：醋酸 ($CH_3COOH$)**：純度極高時在 17°C 會結冰，又稱「冰醋酸」。食用醋僅含 3~5%，千萬別以為可以直接喝純冰醋酸！")

    # 第一集
    with st.expander("🌟 EP01 | 超級新秀電解質", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("化學大聯盟的第一位超級新秀強勢登板！我們將破解『電解質』的基本概念。它們在水中的導電球路到底有多刁鑽？會為球場帶來什麼樣的化學變化？")
        st.audio("audio/第一季_化學大聯盟_第1集_超級新秀電解質.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- 電解質與非電解質的世紀對決\n- 看懂阿瑞尼斯的解離暗號\n- 運動飲料裡到底藏了什麼秘密武器？")

    # 第九集到第十集
    for i in range(9, 11):
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
