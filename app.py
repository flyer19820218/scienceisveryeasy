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
    st.markdown("<h3 style='font-size: 18px; font-weight: bold; color: #333; margin-top: 20px; margin-bottom: 0px;'>🎧 賽事轉播表 (第一季完結)</h3>", unsafe_allow_html=True)

    # 🌟 NEW! 第十集：賽季大結局，預設展開 🌟
    with st.expander("🔥 EP10 | 完結篇！總裁的唱反調——勒沙特列大魔王與總冠軍之戰", expanded=True):
        st.markdown("**上架日期：2026/03**") 
        st.write("十局下半，滿壘關鍵時刻！大聯盟總裁勒沙特列親自進場干預，發動濃度、溫度、壓力三大試煉！我們將揭開「全體加速、幅度不同」的科學真相，破解催化劑的計時器騙局。跟著曉臻助教揮出再見滿貫全壘打，贏得屬於我們的總冠軍獎盃！")
        
        # 播放器 (音檔路徑對齊下載檔名)
        st.audio("audio/第一季_化學大聯盟_第10集_破壞平衡的大魔王.mp3", format="audio/mp3")
        
        st.markdown("**📌 總冠軍賽戰術板亮點：**")
        st.markdown("- **總裁的「唱反調」原則**：你給我什麼我就消耗什麼。濃度增加（休息室變擠），碰撞機率上升，導致平衡向右移動以恢復秩序。")
        st.markdown("- **濃度試煉的大陷阱**：固體（如食鹽、灰石）與純液體的「濃度」不變。加入固體對氣體碰撞機率毫無影響，絕對不會改變平衡狀態！")
        st.markdown("- **溫度的終極對位思考**：溫度上升，正逆反應速率「同時變快」！但因為分子能量常態分佈基數不同，吸熱方向（跨越高牆）的成長倍數遠大於放熱方向，平衡因而向吸熱端移動。")
        st.markdown("- **催化劑騙局 (投球計時器)**：等比例增加正逆速率。它只能縮短達到平衡的時間，絕對無法破壞平衡，也無法多增加一分一毫的產量！")
        st.markdown("- **自然界的造物奇蹟**：鐘乳石形成的化學式 $CaCO_3 + CO_2 + H_2O \\rightleftharpoons Ca(HCO_3)_2$，就是自然界最完美的動態平衡拉扯。")

    # 第九集
    with st.expander("🌟 EP09 | 化學平衡 (上)！沒有盡頭的延長賽與調度假象", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("比賽進入最緊繃的九局上半！今天我們要探討的是一場永遠打不完的延長賽：「動態化學平衡」！我們將把比賽搬進密閉的巨蛋球場，看穿巨觀靜止與微觀狂奔的假象，並且由曉臻助教揮出大號全壘打，一棒擊碎大考最愛考的「濃度比與係數比」大魔王陷阱！")
        st.audio("audio/第一季_化學大聯盟_第9集_化學平衡_沒有盡頭的延長賽.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **兩種賽制 (可逆與不可逆)**：開放空間氣體逸散是不可逆反應；密閉空間（巨蛋球場）氣體跑不掉，則可發生可逆反應。")
        st.markdown("- **正逆反應定義**：反應物變生成物（上場守備）是正反應；生成物變回反應物（退回休息室）是逆反應。")
        st.markdown("- **動態平衡真面目**：正反應速率 = 逆反應速率（上場人數 = 下場人數）。巨觀總量不變，微觀持續進行。")
        st.markdown("- **大魔王陷阱 (濃度比 $\\neq$ 係數比)**：達到平衡時，反應物與生成物的濃度比「不一定」等於係數比，取決於初始球員帶了多少。")

    # 第八集
    with st.expander("🌟 EP08 | 反應速率與小球戰術！機關槍打線、滿壘壓力與超級教練", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("主場球隊修築了高聳的全壘打牆，企圖利用極高「活化能」封鎖打線。教練團祭出戰術連環計：先用「機關槍打線」（接觸面積）不斷上壘，再請出超級教練「催化劑」，下達小球戰術直接改變反應途徑，順利突破僵局！")
        st.audio("audio/第一季_化學大聯盟_第8集_反應速率與小球戰術.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **機關槍打線（接觸面積）**：注意數學陷阱！邊長變 $1/n$，表面積僅變 $n$ 倍。")
        st.markdown("- **超級教練（催化劑）**：提供「低活化能途徑」，反應後質量性質不變可重複執教。經典例子：哈柏法製氨的鐵粉。")

    # 第七集
    with st.expander("🌟 EP07 | 超音速跑壘測試賽！雙重爆發與反應速率", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("從瞬間爆炸的煙火到花費千百年才形成的石筍，化學反應速率跨度超乎想像！想打出全壘打？你必須掌握「碰撞學說」的兩大絕對條件。還要揭開溫度帶來的「雙重爆發」秘密！")
        st.audio("audio/第一季_化學大聯盟_第7集_超音速跑者與雙重爆發.mp3", format="audio/mp3")
        st.markdown("- **碰撞學說條件**：正確的碰撞方向（甜蜜點）與足夠的能量（突破活化能）。")
        st.markdown("- **溫度雙重爆發**：溫度升高不僅增加碰撞次數，還大幅增加跨越活化能門檻的分子數。")

    # 第六集
    with st.expander("🌟 EP06 | 球場的五大無名英雄與石灰三兄弟變身大秀", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("場務人員清理「鹽類」戰利品。這集我們將開箱大聯盟最強的後勤裝備：從維持生命的食鹽到畫線用的大理石，還有「石灰三兄弟」的終極變身魔術！")
        st.audio("audio/第一季_化學大聯盟_第6集_球場的五大無名英雄.mp3", format="audio/mp3")

    # 第五集
    with st.expander("🌟 EP05 | 五局下半的極限拆彈任務！世紀大決戰與酸鹼中和", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("酸鹼兩大軍團正面對決。這是一場需要屏氣凝神的「滴定實驗」。當兩軍互撞，居然會變成最無害的水？粉紅刺客「酚酞」將精準抓出終極平衡點！")
        st.audio("audio/第一季_化學大聯盟_第5集_極限拆彈.mp3", format="audio/mp3")

    # 第四集
    with st.expander("🌟 EP04 | 進階數據解密！火力密度與神祕的 pH 計分板", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("解密大理化魔王「體積莫耳濃度 (M)」的計算祕訣。破解 pH 值數字越小反而越酸的迷思，以及「加水稀釋」致命陷阱！")
        st.audio("audio/第一季_化學大聯盟_第4集_進階數據_胃酸全壘打.mp3", format="audio/mp3")

    # 第三集
    with st.expander("🌟 EP03 | 球場地下室的無名英雄：鹼性後勤部隊與神奇藥水", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("認識傳奇「鹼性後勤部隊」！介紹三大陣營鑑定神器：石蕊、酚酞、廣用指示劑，以及三大鹼性王牌：氫氧化鈉、氧化鈣與氨氣！")
        st.audio("audio/第一季_化學大聯盟_第3集_鹼性後勤部隊_神奇藥水.mp3", format="audio/mp3")

    # 第二集
    with st.expander("🌟 EP02 | 狂轟猛炸的「酸」球隊強勢踢館", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("大聯盟裡火力最兇猛、脾氣最火爆的「酸球隊」強勢登場！破解強酸王牌的致命球路與實驗室保命守則。")
        st.audio("audio/第一季_化學大聯盟_第2集_酸球隊.mp3", format="audio/mp3")

    # 第一集
    with st.expander("🌟 EP01 | 超級新秀電解質", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("破解『電解質』的基本概念。必須要能「溶於水」且能「導電」的化合物，兩者缺一不可！")
        st.audio("audio/第一季_化學大聯盟_第1集_超級新秀電解質.mp3", format="audio/mp3")

# --- 內容區塊 (籌備中的賽季) ---
else:
    st.markdown("<h3 style='text-align: center; font-size: 20px;'>更多賽季，即將開打 ⚾</h3>", unsafe_allow_html=True)
    st.write("我們的教練團正在規劃下一個賽季戰術（慢工出細活！），請隨時回來查看最新的轉播表！")

# --- 5. 底部互動區 ---
st.write("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 14px;'>不想錯過任何一場致勝關鍵？趕快邀請戰友一起收聽！</p>", unsafe_allow_html=True)

# 分享連結按鈕
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
