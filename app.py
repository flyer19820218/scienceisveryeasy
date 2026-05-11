import streamlit as st
import streamlit.components.v1 as components 
import json
import os
from datetime import datetime, timezone, timedelta

# --- 從我們剛建好的部門(模組)引入資料 ---
from seasons import season1
from seasons import season2

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
seasons = ["第一季：化學大聯盟 ⚾", "第二季：黎明韓流選秀 🎤", "第三季：籌備中... ⏳"]
selected_season = st.selectbox("📂 選擇你要挑戰的賽季", seasons)

st.write("---")

# --- 4. 內容區塊 (超極簡路由) ---
if selected_season == "第一季：化學大聯盟 ⚾":
    season1.render_season()
elif selected_season == "第二季：黎明韓流選秀 🎤":
    season2.render_season()
else:
    st.markdown("<h3 style='text-align: center; font-size: 20px;'>更多賽季，即將開打 ⚾</h3>", unsafe_allow_html=True)
    st.write("教練團與製作人正在閉關寫稿中（慢工出細活！），請隨時回來查看最新的節目單！")


# --- 5. 底部互動區 ---
st.write("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 14px;'>不想錯過任何一場致勝關鍵？趕快邀請戰友一起收聽！</p>", unsafe_allow_html=True)

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

# ==========================================
# --- 5.5 學習診斷系統推廣區 (總裁指定黃金版位) ---
# ==========================================
st.write("---")
st.markdown("<h3 style='text-align: center; color: #007BFF;'>📊 理化專屬學習診斷系統</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 14px;'>聽完節目還是怕怕的？立刻進行測驗，AI 幫你精準抓出觀念盲區！🎯</p>", unsafe_allow_html=True)

st.link_button("👉 點我進入學習診斷系統", "https://flyer19820218.github.io/scienceisveryeasy/indexforlearningdiag.html", use_container_width=True)


# --- 6. 球迷吐嘈區 (留言板) ---
st.write("---")
st.markdown("<h3 style='text-align: center; color: #E65100;'>💬 賽後記者會：聽眾留言區</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 14px;'>聽完節目有什麼話想說的？直接在這裡開噴吧！</p>", unsafe_allow_html=True)

COMMENT_FILE = "data/comments.json"
TW_TZ = timezone(timedelta(hours=8))

os.makedirs("data", exist_ok=True)

def load_comments():
    if os.path.exists(COMMENT_FILE):
        try:
            with open(COMMENT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_comment(name, text):
    comments = load_comments()
    now_str = datetime.now(TW_TZ).strftime("%Y-%m-%d %H:%M")
    comments.append({"name": name, "text": text, "time": now_str})
    comments = comments[-50:] 
    with open(COMMENT_FILE, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=4)

with st.form("comment_form", clear_on_submit=True):
    col1, col2 = st.columns([1, 3])
    with col1:
        user_name = st.text_input("👤 你的稱呼", placeholder="例如：被化學當掉的阿明", max_chars=20)
    with col2:
        user_text = st.text_input("🎤 留言內容", placeholder="製作人太殘酷了吧！", max_chars=100)
    
    submitted = st.form_submit_button("🚀 送出留言")
    
    if submitted:
        if not user_name.strip() or not user_text.strip():
            st.warning("⚠️ 裁判舉黃牌！暱稱跟留言內容都不能是空白的喔！")
        else:
            save_comment(user_name, user_text)
            st.success("✅ 留言成功！已傳達給製作單位。")
            st.rerun() 

st.write("") 

comments_data = load_comments()

if not comments_data:
    st.info("🪹 觀眾席目前空無一人，搶個頭香吧！")
else:
    with st.container(height=400):
        for comment in reversed(comments_data):
            with st.chat_message("user", avatar="💬"):
                st.markdown(f"**{comment['name']}** <span style='color:#888; font-size:12px;'>({comment['time']})</span>", unsafe_allow_html=True)
                st.write(comment['text'])
