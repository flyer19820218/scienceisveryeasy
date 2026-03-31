import streamlit as st
import streamlit.components.v1 as components 
import json
import os
from datetime import datetime, timezone, timedelta

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
        st.markdown("- **兩種賽制 (可逆與不可逆)**：開放空間氣體逸散是不可逆反應（全壘打飛出場外回不來）；密閉空間（巨蛋球場）氣體跑不掉，則可發生可逆反應。")
        st.markdown("- **正逆反應定義**：反應物變生成物（球員從休息室上場）是正反應；生成物變回反應物（球員退下場）是逆反應。")
        st.markdown("- **動態平衡的真面目**：正反應速率 = 逆反應速率（上場人數 = 下場人數）。一進一出互相抵銷。")
        st.markdown("- **巨觀靜止 vs. 微觀狂奔**：巨觀下物質總量與濃度不再改變（場上與休息室總人數固定），但在微觀視角下，反應從未停止！")
        st.markdown("- **大魔王陷阱 (濃度比 $\\neq$ 係數比)**：達到平衡時，反應物與生成物的濃度比「不一定」等於戰術板上的係數比，有可能是任何數字比！")

    # 第八集
    with st.expander("🌟 EP08 | 反應速率與小球戰術！機關槍打線、滿壘壓力與超級教練", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("比賽來到八局上半！主場球隊修築了高聳的全壘打牆，企圖利用極高「活化能」封鎖打線。教練團祭出戰術連環計：先用「機關槍打線」（接觸面積）不斷上壘，再把「壘包塞滿」（濃度與壓力）製造威脅。最後請出超級教練「催化劑」，下達觸擊短打與盜壘的「小球戰術」，直接改變反應途徑，順利突破僵局！")
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
        st.markdown("- **世紀大決戰通式**：酸 + 鹼 $\\rightarrow$ 鹽類 + 水 + 熱量（注意：這絕對是一場會讓溫度飆高的「放熱反應」！）。")
        st.markdown("- **隱藏的真正對決 (淨離子反應)**：不管酸鹼陣營派誰上場，真正互毆的永遠是 $H^+$ 加上 $OH^-$，最終抱在一起變成無害的 $H_2O$ (水)。")
        st.markdown("- **大魔王陷阱 (鹽類的真相)**：化學上的「鹽類」只是酸鹼互撞後留下的裝備碎片（金屬離子+酸根離子），絕對不等於可以吃的食鹽 ($NaCl$)！")
        st.markdown("- **極限拆彈裝備 (滴定儀器)**：標準姿勢是「左手控制滴定管活塞，右手搖晃下方錐形瓶」。視線必須平齊液面凹下最底端才準確！")
        st.markdown("- **粉紅刺客的判決 (滴定終點)**：把無色酚酞滴在酸性錐形瓶中，當上方鹼液滴入，只要剛好超過一滴，酚酞瞬間引爆成「紫紅色」且不褪色，比賽(中和)宣告結束！")
    
    # 第四集
    with st.expander("🌟 EP04 | 進階數據解密！火力密度與神祕的 pH 計分板", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("歡迎來到大聯盟最機密的「進階數據分析室」！這集將為你拆解理化大魔王「體積莫耳濃度 ($M$)」的計算祕訣。同時公開球場上的終極計分板「pH 值」，破解數字越小反而越酸的迷思，以及「加水稀釋」致命陷阱！")
        st.audio("audio/第一季_化學大聯盟_第4集_進階數據_胃酸全壘打.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **火力密度指標 (體積莫耳濃度 $M$)**：$M$ = 溶質莫耳數 ÷ 溶液體積。絕對必考大陷阱：體積一定要換算成「公升 (L)」！")
        st.markdown("- **春訓配藥守則 (稀釋公式)**：加水稀釋前後，溶質的「莫耳數」絕對不變！就像一杯珍奶加再多水，裡面的珍珠數量都不會變！($M_1 \\times V_1 = M_2 \\times V_2$)")
        st.markdown("- **終極計分板 (pH 值)**：測量 $H^+$ 濃度的指數。7 是中性平手，小於 7 偏酸，大於 7 偏鹼。數字越小，酸性火力越猛！")
        st.markdown("- **跨界迷思破解**：酸性溶液瘋狂加水稀釋，酸味會變淡（pH 值上升靠近 7），但「絕對不會」跨過 7 變成鹼性（pH 永遠小於 7）！")

    # 第三集
    with st.expander("🌟 EP03 | 球場地下室的無名英雄：鹼性後勤部隊與神奇藥水", expanded=False):
        st.markdown("**上架日期：2026/03**") 
        st.write("認識大聯盟的傳奇「鹼性後勤部隊」！這集我們要介紹大聯盟最機密的三大陣營鑑定神器，並破解三大鹼性王牌的特殊技能，以及強弱電解質的終極差異！")
        st.audio("audio/第一季_化學大聯盟_第3集_鹼性後勤部隊_神奇藥水.mp3", format="audio/mp3")
        st.markdown("**📌 戰術板亮點：**")
        st.markdown("- **共同特徵 (鹼的本性)**：溶於水必解離出氫氧根離子 ($OH^-$)，摸起來有滑膩感，嘗起來有苦味，而且能溶解油脂（洗碗精的原理）！")
        st.markdown("- **三大鑑定神器**：紅藍判官（石蕊試紙遇鹼變藍）、粉紅刺客（酚酞遇鹼變紅）、彩虹戰鬥儀（廣用指示劑遇鹼變藍紫）。")
        st.markdown("- **王牌一：氫氧化鈉 ($NaOH$)**：俗稱「燒鹼」或「苛性鈉」，超級吸水怪獸（潮解現象），能通馬桶、做肥皂，腐蝕性極強！")
        st.markdown("- **王牌二：氧化鈣 ($CaO$ & $Ca(OH)_2$)**：生石灰加水放出高溫（自熱火鍋原理）變身熟石灰（氫氧化鈣），熟石灰水溶液就是用來檢驗二氧化碳的「澄清石灰水」！")
        st.markdown("- **王牌三：氨氣 ($NH_3$)**：唯一不含 $OH$ 卻是鹼性的特例！極易溶於水變成弱鹼性的氨水，帶有刺鼻尿騷味，是做肥料跟玻璃清潔劑的神器。")

    # 第二集
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
        st.write("化學大聯盟的開幕戰，第一位超級新秀『電解質』強勢登板！這集我們不只要破解電解質的基本身家資料，還要帶大家進入大聯盟的『導電測試台』，一窺電流在水中跑壘的真正面貌，以及球隊如何維持『電中性』的終極平衡法則！")
        st.audio("audio/第一季_化學大聯盟_第1集_超級新秀電解質.mp3", format="audio/mp3")
        
        st.markdown("### 📌 戰術板亮點：")
        st.markdown("- **🔬 新秀體檢中心 (導電測試台)**：用燈泡與發光二極體打造的測試儀器！只要把電極放進水溶液中，能讓燈泡亮起、展現出導電實力的，就是大聯盟認可的電解質球員！")
        st.markdown("- **⚾ 選秀絕對標準 (電解質定義)**：必須要能「溶於水」且能「導電」的化合物，兩者缺一不可！例如固體食鹽就像被綁在休息室的球員無法導電，但跳進水裡變成食鹽水就火力全開！")
        st.markdown("- **⚡ 阿瑞尼斯的解離暗號**：球員一下水就會自動拆解，變成帶正電與帶負電的「離子球員」，在水中自由奔跑，這就是溶液導電的核心秘密！")
        st.markdown("- **🌊 跑壘的動力 (電流的定義)**：什麼是電流？在金屬導線裡，是「自由電子」在跑壘；但在電解質水溶液裡，則是帶正電與帶負電的「離子」朝著相反的極點狂奔，所形成的壯觀人潮！")
        st.markdown("- **⚖️ 球隊的完美平衡 (電中性)**：段考最愛投的變化球！一杯電解質溶液中，所有正離子帶的「總正電量」必定等於負離子帶的「總負電量」。請球迷死守一個觀念：是「總電量」相等，不一定是「總人數（個數）」相等喔！")
        st.markdown("- **🛋️ 乖寶寶板凳球員 (非電解質)**：酒精和蔗糖雖然能完美溶於水，但卻像乖寶寶一樣不解離、身上不帶電，所以無法導電，只能坐在板凳上！")
        st.markdown("- **🧃 運動飲料的秘密武器**：為什麼流汗要補充電解質（鈉離子、鉀離子）？因為人體的神經傳導和肌肉收縮，都需要這群帶電的小傢伙來發號施令！")

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

# --- 6. 球迷吐嘈區 (留言板) ---
st.write("---")
st.markdown("<h3 style='text-align: center; color: #E65100;'>💬 賽後記者會：球迷吐嘈區</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 14px;'>聽完轉播有什麼話想對教練或球員說的？直接開噴吧！</p>", unsafe_allow_html=True)

COMMENT_FILE = "data/comments.json"
TW_TZ = timezone(timedelta(hours=8))

# 確保存放留言的資料夾存在
os.makedirs("data", exist_ok=True)

# 讀取留言的函數
def load_comments():
    if os.path.exists(COMMENT_FILE):
        try:
            with open(COMMENT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

# 儲存留言的函數
def save_comment(name, text):
    comments = load_comments()
    now_str = datetime.now(TW_TZ).strftime("%Y-%m-%d %H:%M")
    comments.append({"name": name, "text": text, "time": now_str})
    # 為了避免留言無限長，我們只保留最新 50 則
    comments = comments[-50:] 
    with open(COMMENT_FILE, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=4)

# 建立留言輸入區塊 (使用 st.form 避免每打一個字就重新整理)
with st.form("comment_form", clear_on_submit=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        user_name = st.text_input("👤 你的球衣背號/暱稱", placeholder="例如：理化被當的阿明", max_chars=20)
    with col2:
        user_text = st.text_input("🎤 吐嘈內容", placeholder="勒沙特列太難了吧！曉臻助教救我！", max_chars=100)
    
    submitted = st.form_submit_button("🚀 送出吐嘈")
    
    if submitted:
        if not user_name.strip() or not user_text.strip():
            st.warning("⚠️ 裁判舉黃牌！暱稱跟吐嘈內容都不能是空白的喔！")
        else:
            save_comment(user_name, user_text)
            st.success("✅ 吐嘈成功！已傳達給教練團。")
            st.rerun() # 送出後強制刷新畫面，讓留言立刻顯示！

st.write("") # 空一行

# 顯示歷史留言區塊
comments_data = load_comments()

if not comments_data:
    st.info("🪹 觀眾席目前空無一人，搶個頭香吧！")
else:
    # 使用 container 來限制留言區的高度，並允許捲動
    with st.container(height=400):
        # 將留言反轉，讓最新的顯示在最上面
        for comment in reversed(comments_data):
            # 用 Streamlit 內建的 chat_message UI，看起來超像通訊軟體！
            with st.chat_message("user", avatar="⚾"):
                st.markdown(f"**{comment['name']}** <span style='color:#888; font-size:12px;'>({comment['time']})</span>", unsafe_allow_html=True)
                st.write(comment['text'])
