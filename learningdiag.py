# ==========================================
# --- 1. 模組引入與系統配置 ---
# ==========================================
import streamlit as st
import google.generativeai as genai
import json
import os 
import re
import random
import time
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import streamlit.components.v1 as components
import importlib

st.set_page_config(page_title="科學大聯盟：素養導向學習系統", page_icon="🎓", layout="wide", initial_sidebar_state="collapsed")

TEACHER_API_KEY = st.secrets.get("GEMINI_API_KEY", "")

components.html(
    """
    <script>
    const parentDoc = window.parent.document;
    if (!parentDoc.getElementById('mathjax-script')) {
        const configScript = parentDoc.createElement('script');
        configScript.innerHTML = `
            window.MathJax = {
                tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] },
                startup: { typeset: false }
            };
        `;
        parentDoc.head.appendChild(configScript);

        const script = parentDoc.createElement('script');
        script.id = 'mathjax-script';
        script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
        script.async = true;
        script.onload = () => { if (window.parent.MathJax) window.parent.MathJax.typesetPromise(); };
        parentDoc.head.appendChild(script);
    } else {
        if (window.parent.MathJax && window.parent.MathJax.typesetPromise) {
            window.parent.MathJax.typesetPromise();
        }
    }
    </script>
    """,
    height=0,
    width=0
)

# ==========================================
# --- 2. 核心設定 (CSS) ---
# ==========================================
st.markdown("""
    <style>
    :root { color-scheme: light; }
    html, body, .stApp, p, h1, h2, h3, h4, h5, h6, li {
        font-family: 'Helvetica Neue', Helvetica, Arial, 'PingFang TC', 'Microsoft JhengHei', sans-serif;
    }
    
    .block-container { max-width: 98% !important; padding-top: 2rem !important; padding-bottom: 2rem !important; }

    .stat-box { background-color: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; }
    .stat-label { color: #64748b; font-size: 16px; margin-bottom: 5px; text-align: center;}
    .stat-value { font-size: clamp(28px, 3vw, 36px); font-weight: bold; color: #0f172a; text-align: center; margin: 0;}
    .stat-detail { color: #0f172a; margin: 0; font-size: 15px; line-height: 1.8;}
    
    .analysis-container { background-color: #f0f7ff; padding: 20px; border-radius: 16px; border: 1px solid #d0e7ff; display: flex; align-items: center; justify-content: space-between; margin-bottom: 25px;}
    .analysis-icon { background-color: #0f172a; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 30px; }
    .analysis-text h4 { margin: 0; color: #1e293b; font-size: clamp(20px, 2.5vw, 28px); font-weight: bold; }
    .analysis-text p { margin: 0; color: #64748b; font-size: clamp(17px, 1.8vw, 24px); margin-top: 5px; }
    
    .learning-card { background-color: #fdfcf9; padding: 24px; border-radius: 12px; min-height: 180px; height: auto; margin-bottom: 20px; border: 1px solid #e5e7eb; }
    .learning-card-header { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; }
    .learning-card-icon { background-color: #1e293b; width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 26px;}
    .learning-card-header b { font-size: clamp(20px, 2.5vw, 28px); color: #1e293b; } 
    .learning-card-content { font-size: clamp(17px, 1.8vw, 24px); color: #334155; line-height: 1.8; letter-spacing: 0.5px; text-align: justify; }
    
    .stMarkdown p, .stMarkdown li { font-size: clamp(18px, 1.5vw, 22px) !important; line-height: 1.8; }
    div[role="radiogroup"] label p { font-size: clamp(18px, 1.5vw, 22px) !important; }
    
    .flip-card { 
        background-color: transparent; width: 100%; max-width: 550px; aspect-ratio: 1 / 1; 
        margin: 0 auto 30px auto; display: block; cursor: pointer; 
    }
    .flip-card-checkbox { display: none; }
    .flip-card-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d; }
    .flip-card-checkbox:checked + .flip-card-inner { transform: rotateY(180deg); }
    
    .flip-card-front, .flip-card-back { 
        position: absolute; width: 100%; height: 100%; backface-visibility: hidden; 
        display: flex; flex-direction: column; align-items: center; justify-content: center; 
        border-radius: 20px; padding: 8%; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); border: 1px solid #e2e8f0; 
    }
    .flip-card-front { background-color: #ffffff; color: #1e293b; border-top: 8px solid #3b82f6; }
    .flip-card-back { background-color: #6a2c2a; color: #f8fafc; transform: rotateY(180deg); overflow-y: auto; }
    
    .fc-title { font-size: clamp(20px, 4vw, 28px); font-weight: bold; line-height: 1.4; margin-bottom: 10px; }
    .fc-content { font-size: clamp(16px, 3.5vw, 22px); line-height: 1.6; text-align: left; width: 100%; }
    
    /* 動畫引擎 */
    @keyframes flipPage {
        0% { transform: perspective(1200px) rotateY(-90deg); opacity: 0; }
        100% { transform: perspective(1200px) rotateY(0deg); opacity: 1; }
    }
    @keyframes slidePage {
        0% { transform: translateX(40px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    .quiz-animate { animation: slidePage 0.4s ease-out forwards; }
    div[data-testid="stForm"] { animation: slidePage 0.4s ease-out forwards; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# --- 3. 系統常數與提示詞 ---
# ==========================================
MODEL_ID = "gemini-3.1-flash-lite-preview"

SYSTEM_INSTRUCTION = """
你現在是『化學大聯盟』的最高戰略教練。在給予回饋時，必須嚴格遵守以下「漸進式引導模式」規範：
1. 核心哲學：絕不直接給死板解答！必須強迫學生啟動「思想實驗 (Gedankenexperiment)」與腦內建模。
2. 文字顯示必須使用 Markdown 語法排版，化學式請務必使用標準符號（如 $H_2SO_4$）。
3. 語氣要像資深教練，用加強語氣的肯定句，引導學生自行爬升。
"""

DIFFICULTY_LEVELS = {
    "Level 1-基礎記憶": "基礎觀念題，測驗定義與名詞解釋。",
    "Level 2-觀念應用": "進階應用題，結合多個觀念或判斷陷阱。",
    "Level 3-素養思考": "生活素養與實驗推論題，需要邏輯推導。"
}

FALLBACK_QUIZ = [
    {"topic": "系統防護", "q": "教練尚未在金庫放入這份考卷。這是備用題：電解質必定溶於水嗎？", "options": ["A. 是", "B. 否"], "ans": "A", "diag": "電解質定義要件之一：溶於水。"}
]

# ==========================================
# --- 4. 動態載入資料庫 & 雲端存檔機制 ---
# ==========================================
os.makedirs("data", exist_ok=True)

@st.cache_resource
def get_gsheet_client(force_refresh=False):
    if force_refresh:
        st.cache_resource.clear()
    try:
        info = st.secrets["GCP_SERVICE_ACCOUNT"]
        creds = Credentials.from_service_account_info(
            info, scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        )
        return gspread.authorize(creds)
    except Exception as e:
        if force_refresh:
            st.error(f"❌ 金鑰讀取失敗！錯誤：{e}")
        return None

def sync_cloud_data(worksheet_name, row_data, headers=None):
    client = get_gsheet_client()
    if not client: return
    try:
        sh = client.open_by_key(st.secrets["GSHEET_ID"])
        try:
            worksheet = sh.worksheet(worksheet_name)
        except gspread.exceptions.WorksheetNotFound:
            worksheet = sh.add_worksheet(title=worksheet_name, rows="1000", cols="20")
            if headers: 
                worksheet.append_row(headers)
                
        a_col_len = len(worksheet.col_values(1))
        next_row_index = a_col_len + 1
        worksheet.update(f"A{next_row_index}", [row_data])
    except Exception as e:
        st.toast(f"⚠️ 雲端同步失敗，成績可能未儲存！({e})")

def get_cloud_history():
    client = get_gsheet_client()
    if not client: return pd.DataFrame()
    try:
        sh = client.open_by_key(st.secrets["GSHEET_ID"])
        try:
            worksheet = sh.worksheet("學習戰報")
            raw_data = worksheet.get_all_values() 
            if not raw_data: return pd.DataFrame()
                
            first_row = raw_data[0]
            if "年級" in first_row or "時間" in first_row or "單元" in first_row:
                df = pd.DataFrame(raw_data[1:])
                if not df.empty: df.columns = first_row
            else:
                default_headers = ["時間", "年級", "班級", "座號", "姓名", "單元", "得分", "觀念診斷", "特訓指南"]
                df = pd.DataFrame(raw_data)
                min_len = min(len(df.columns), len(default_headers))
                df = df.iloc[:, :min_len]
                df.columns = default_headers[:min_len]
            return df
        except gspread.exceptions.WorksheetNotFound:
            worksheet = sh.add_worksheet(title="學習戰報", rows="1000", cols="10")
            worksheet.append_row(["時間", "年級", "班級", "座號", "姓名", "單元", "得分", "觀念診斷", "特訓指南"])
            return pd.DataFrame()
    except Exception as e:
        st.toast(f"⚠️ 無法讀取雲端戰報：{e}")
        return pd.DataFrame()

def get_cloud_passwords():
    client = get_gsheet_client()
    if not client: return {}
    try:
        sh = client.open_by_key(st.secrets["GSHEET_ID"])
        try:
            ws = sh.worksheet("學生密碼")
        except gspread.exceptions.WorksheetNotFound:
            ws = sh.add_worksheet(title="學生密碼", rows="1000", cols="2")
            ws.append_row(["學號", "密碼"])
            return {}
        data = ws.get_all_records()
        return {str(row.get('學號','')): str(row.get('密碼','')) for row in data}
    except Exception as e: return {}

def get_coach_accounts():
    client = get_gsheet_client()
    if not client: return {}
    try:
        sh = client.open_by_key(st.secrets["GSHEET_ID"])
        try:
            ws = sh.worksheet("教練名冊")
        except gspread.exceptions.WorksheetNotFound:
            ws = sh.add_worksheet(title="教練名冊", rows="100", cols="3")
            ws.append_row(["教練帳號", "密碼", "管理班級"])
            return {}
        data = ws.get_all_records()
        result = {}
        for row in data:
            if row.get('教練帳號'):
                result[str(row['教練帳號'])] = {
                    'pw': str(row.get('密碼', '')),
                    'classes': [c.strip() for c in str(row.get('管理班級', '')).split(',') if c.strip()]
                }
        return result
    except Exception as e: return {}

def delete_student_password(student_id):
    client = get_gsheet_client()
    if not client: return False
    try:
        sh = client.open_by_key(st.secrets["GSHEET_ID"])
        ws = sh.worksheet("學生密碼")
        cell = ws.find(student_id)
        if cell: ws.delete_rows(cell.row)
        return True
    except Exception as e: return False

def update_student_password(student_id, new_pw):
    client = get_gsheet_client()
    if not client: return False
    try:
        sh = client.open_by_key(st.secrets["GSHEET_ID"])
        ws = sh.worksheet("學生密碼")
        cell = ws.find(student_id)
        if cell: ws.update_cell(cell.row, cell.col + 1, new_pw)
        return True
    except Exception as e: return False

# 🌟🌟 自動攤平合併引擎 🌟🌟
def load_all_quiz_pools():
    merged_pool = {}
    file_candidates = ["quiz_pool.json"] + [f"s{str(i).zfill(2)}_quiz_pool.json" for i in range(1, 10)]
    loaded_count = 0
    for filename in file_candidates:
        filepath = os.path.join("data", filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    raw_data = json.load(f)
                    loaded_count += 1
                    if isinstance(raw_data, dict):
                        for k1, v1 in raw_data.items():
                            if isinstance(v1, dict): 
                                for k2, v2 in v1.items():
                                    merged_pool[f"{k1}_{k2}"] = v2
                            elif isinstance(v1, list): 
                                merged_pool[k1] = v1
            except Exception as e: pass
    st.session_state['debug_pool_keys'] = list(merged_pool.keys())
    st.session_state['debug_file_count'] = loaded_count
    return merged_pool

@st.cache_data
def load_all_flashcards():
    merged_cards = {}
    file_candidates = ["flashcards_db.json"] + [f"s{str(i).zfill(2)}_flashcards_db.json" for i in range(1, 10)]
    for filename in file_candidates:
        filepath = os.path.join("data", filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    merged_cards.update(json.load(f))
            except: pass
    return merged_cards

@st.cache_data 
def load_local_db(filename="season1_db.json"):
    json_path = os.path.join("data", filename)
    try:
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                full_data = json.load(f)
                return {k: v['content'] for k, v in full_data.items()}
        else: return {f"尚未載入賽程 ({filename})": "請確定資料庫檔案存在。"}
    except Exception as e: return {"讀取錯誤": f"錯誤: {str(e)}"}

SEASON_1_DB = load_local_db("season1_db.json")
SEASON_2_DB = load_local_db("season2_db.json") 
FLASH_DB = load_all_flashcards()

# ==========================================
# --- 4.5 答案比對工具函數 ---
# ==========================================
def check_answer(user_choice, correct_ans):
    user_letter = str(user_choice).strip()[0].upper() if user_choice else ""
    correct_letter = str(correct_ans).strip()[0].upper() if correct_ans else ""
    return user_letter == correct_letter

# ==========================================
# --- 5. 狀態管理初始化 ---
# ==========================================
states = [
    "user_api_key", "student_profile", "app_phase", "quiz_data", "user_ans", 
    "ai_analysis", "ai_guide", "attempt_tracker", "current_episode", "current_difficulty", 
    "current_attempt_num", "current_q_index", "q_answered", "card_index", "class_analysis_report", "managed_classes",
    "reading_unlocked", "has_checked_in"
]
for s in states:
    if s not in st.session_state:
        if s == "student_profile": st.session_state[s] = {"grade": "國八", "class": "1班", "seat": "01", "name": ""}
        elif s == "app_phase": st.session_state[s] = "checkin"
        elif s == "user_ans": st.session_state[s] = {}
        elif s == "attempt_tracker": st.session_state[s] = {}
        elif s == "reading_unlocked": st.session_state[s] = {}
        elif s in ["current_q_index", "current_attempt_num", "card_index"]: st.session_state[s] = 0
        elif s == "current_episode": st.session_state[s] = list(SEASON_1_DB.keys())[0] if SEASON_1_DB else ""
        elif s == "current_difficulty": st.session_state[s] = "Level 1-基礎記憶"
        elif s == "managed_classes": st.session_state[s] = []
        elif s == "has_checked_in": st.session_state[s] = False 
        else: st.session_state[s] = None

if st.session_state.user_api_key:
    genai.configure(api_key=st.session_state.user_api_key)

# ------------------------------------------
# 🟢 全域導覽列 (上一頁功能)
# ------------------------------------------
if st.session_state.app_phase != "checkin" and st.session_state.has_checked_in:
    with st.sidebar:
        st.markdown("### 🗺️ 戰區導航")
        
        is_lobby = st.session_state.app_phase == "lobby"
        is_quiz = st.session_state.app_phase == "quiz"
        is_dash = st.session_state.app_phase == "dashboard"
        
        if st.button("🏠 回到賽季大廳", use_container_width=True, disabled=is_lobby):
            st.session_state.app_phase = "lobby"
            st.rerun()
            
        has_quiz = len(st.session_state.quiz_data) > 0 if st.session_state.quiz_data else False
        if st.button("✍️ 進入實戰測試", use_container_width=True, disabled=is_quiz or not has_quiz):
            st.session_state.app_phase = "quiz"
            st.rerun()
            
        st.write("---")
        if st.button("🔌 登出系統", use_container_width=True):
            st.session_state.clear()
            st.rerun()

# ------------------------------------------
# 🛑 終極防呆：未登入硬闖踢回第一頁
# ------------------------------------------
if not st.session_state.has_checked_in and st.session_state.app_phase != "checkin":
    st.session_state.app_phase = "checkin"
    st.rerun()

# ==========================================
# --- 6. 核心引擎 (🚀 雙渦輪防錯版) ---
# ==========================================
def get_smart_flashcards(episode_name):
    # 渦輪 A：完全精準配對 (第二季)
    if episode_name in FLASH_DB: return FLASH_DB[episode_name]
    
    # 渦輪 B：第一季專屬翻譯年糕 (1局下半 -> 第一集)
    if "局" in episode_name:
        match = re.search(r'\d+', episode_name)
        ep_num_str = match.group(0) if match else "1"
        zh_map = {"1": "第一集", "2": "第二集", "3": "第三集", "4": "第四集", "5": "第五集", 
                  "6": "第六集", "7": "第七集", "8": "第八集", "9": "第九集", "10": "第十集"}
        prefix = zh_map.get(ep_num_str, "第一集")
        for k, v in FLASH_DB.items():
            if prefix in k: return v
            
    return []

def get_quiz_data(episode_name, difficulty_key, attempt_num):
    pool = load_all_quiz_pools()
    if not pool:
        st.error("🚨 警告：題庫是空的！請檢查 data 資料夾內的 JSON 檔是否有被正確讀取。")
        return FALLBACK_QUIZ
        
    # 🌟 渦輪 A：完美精準配對 (第二季)
    exact_key = f"{episode_name}_{difficulty_key}_pool"
    if exact_key in pool:
        q_list = pool[exact_key]
        if isinstance(q_list, list): return random.sample(q_list, 10) if len(q_list) >= 10 else q_list

    # 🌟 渦輪 B：第一季專屬翻譯年糕
    if "局" in episode_name:
        match = re.search(r'\d+', episode_name)
        ep_num_str = match.group(0) if match else "1"
        zh_map = {"1": "第一集", "2": "第二集", "3": "第三集", "4": "第四集", "5": "第五集", 
                  "6": "第六集", "7": "第七集", "8": "第八集", "9": "第九集", "10": "第十集"}
        prefix_to_search = zh_map.get(ep_num_str, "第一集")
        diff_level = difficulty_key.split('-')[0]
        
        for p_key, q_list in pool.items():
            if prefix_to_search in p_key and diff_level in p_key:
                if isinstance(q_list, list): return random.sample(q_list, 10) if len(q_list) >= 10 else q_list

    # 🌟 渦輪 C：終極搜救
    for p_key, q_list in pool.items():
        if episode_name[:4] in p_key and difficulty_key.split('-')[0] in p_key:
            if isinstance(q_list, list): return random.sample(q_list, 10) if len(q_list) >= 10 else q_list

    available_keys = st.session_state.get('debug_pool_keys', [])
    st.error(f"🚨 **題庫讀取失敗：單元名稱對不起來！**")
    st.warning(f"系統目前想找的精準鑰匙是：\n`{exact_key}`\n\n🔑 但你的 JSON 檔案裡實際有：\n{available_keys[:10]} ...")
               
    return FALLBACK_QUIZ

def get_ai_report(player_name, score, mistakes, content, podcast_name):
    if not st.session_state.user_api_key: return "API金鑰無效", "請檢查金鑰"
    
    safe_config = {"max_output_tokens": 3500, "response_mime_type": "application/json"}
    model = genai.GenerativeModel(MODEL_ID, system_instruction=SYSTEM_INSTRUCTION, generation_config=safe_config)
    
    prompt = f"""
    球員：{player_name}
    得分：{score}
    錯題清單：{mistakes}
    
    請針對該球員的「錯題清單」給予直接的學習診斷。
    嚴格規範：
    1. 產出純 JSON 格式。
    2. analysis (觀念診斷)：直接點出錯題的核心觀念盲點，字數控制在 250 字左右。
    3. guide (研讀指南)：給予具體建議，字數控制在 250 字左右。最後加上：「想聽教練親自傳授破題密碼？立刻去聽本週《{podcast_name}》Podcast！」
    4. ⚠️ 化學式鐵律：【絕對禁止】使用 LaTeX 語法。強制使用 HTML 標籤 <sub> 及 <sup>。
    5. ⚠️ JSON 格式鐵律：字串中【絕對嚴禁直接按 Enter 換行】，請用「\\n」代替。
    
    輸出格式：
    {{ "analysis": "...", "guide": "..." }}
    """
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            report_json = json.loads(clean_text)
            
            analysis = report_json.get("analysis", "分析生成失敗。")
            guide = report_json.get("guide", "指南生成失敗。")
            
            if isinstance(analysis, list): analysis = "\n\n".join([str(item) for item in analysis])
            if isinstance(guide, list): guide = "\n\n".join([str(item) for item in guide])
            
            final_analysis = str(analysis).replace("$", "").replace("_", "")
            final_guide = str(guide).replace("$", "").replace("_", "")
            return final_analysis, final_guide
        except Exception as e: 
            if "503" in str(e) and attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return f"⚠️ 診斷中斷: {e}", "請稍後再試或重新點擊分析。"

def get_class_analysis(episode, target_class, history_df):
    if not st.session_state.user_api_key: return "API金鑰無效"
    try:
        df_ep = history_df
        if '單元' in df_ep.columns:
            df_ep = df_ep[df_ep['單元'] == episode]
        else:
            df_ep = df_ep[df_ep.apply(lambda row: episode in str(row.values), axis=1)]
            
        if target_class != "全部我的班級" and '班級' in df_ep.columns:
            df_ep = df_ep[df_ep['班級'] == target_class]
        
        if df_ep.empty:
            return f"⚠️ 您的班級目前尚無【{episode}】的挑戰紀錄，無法進行戰情分析。"
        
        data_str = df_ep.to_csv(index=False)
        if len(data_str) > 15000: data_str = data_str[:15000] + "\n...(資料過長已截斷)"
        
        prompt = f"""
        你現在是國中理化『總教練』的專屬 AI 首席分析師。
        請針對單元【{episode}】，分析教練專屬班級的綜合學習狀況。
        以下是近期的原始戰報大數據：
        {data_str}
        請綜合以上數據，產出「綜合弱點分析與課堂複習策略」。字數控制在 1000 字以內，使用 Markdown 豐富排版。
        """
        
        coach_safe_config = {"max_output_tokens": 2000}
        model = genai.GenerativeModel(MODEL_ID, system_instruction=SYSTEM_INSTRUCTION, generation_config=coach_safe_config)

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                if "503" in str(e) and attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    return f"⚠️ 綜合戰情分析生成失敗: {e}"
    except Exception as e:
        return f"⚠️ 綜合戰情分析處理失敗: {e}"

# ==========================================
# --- 7. [介面路由] 球員報到 ---
# ==========================================
if st.session_state.app_phase == "checkin":
    st.write("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2.5, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>科學大聯盟</h1>", unsafe_allow_html=True)
        st.write("---")
        
        tab1, tab2, tab3 = st.tabs(["🧑‍🎓 一般球員報到", "🛡️ 教練專屬通道", "🌟 801 專屬通道"])
        
        with tab1:
            st.markdown("#### 📝 一般通道：填寫報到單")
            c_grade, c_class, c_seat = st.columns(3)
            with c_grade: grade = st.selectbox("年級", ["國七", "國八", "國九"])
            with c_class: cls = st.selectbox("班級", [f"{i}班" for i in range(1, 21)])
            with c_seat: seat = st.selectbox("座號", [str(i).zfill(2) for i in range(1, 51)])
            student_name = st.text_input("姓名 (選填)", placeholder="如果不填姓名，戰報將以座號顯示")
            student_pw = st.text_input("個人綁定密碼 🔒", type="password", placeholder="若為首次登入，將自動綁定此密碼")
            
            st.markdown("#### 🔑 出示裝備通行證")
            st.markdown("<span style='font-size: 14px; color: #64748b;'>👉 <a href='https://aistudio.google.com/app/apikey' target='_blank' style='color: #14b8a6; font-weight: bold;'>點此免費申請 Gemini API 金鑰</a></span>", unsafe_allow_html=True)
            api_input = st.text_input("輸入 Gemini API 金鑰", type="password", placeholder="AIzaSy...", label_visibility="collapsed")
            
            if st.button("🚀 一般報到完成", use_container_width=True):
                clean_key = api_input.strip()
                if not student_pw: st.error("🚨 請務必輸入個人密碼！")
                elif not clean_key: st.error("🚨 必須輸入 API 金鑰！")
                else:
                    cloud_pws = get_cloud_passwords() 
                    student_id = f"{grade}_{cls}_{seat}" 
                    if student_id in cloud_pws:
                        if str(cloud_pws[student_id]) != str(student_pw):
                            st.error("🚨 密碼錯誤！有人已經註冊過這個座號囉！")
                        else:
                            st.session_state.user_api_key = clean_key
                            st.session_state.student_profile = {"grade": grade, "class": cls, "seat": seat, "name": student_name}
                            st.session_state.has_checked_in = True 
                            st.session_state.app_phase = "lobby" 
                            st.rerun()
                    else:
                        sync_cloud_data("學生密碼", [student_id, student_pw], ["學號", "密碼"])
                        st.toast("✅ 密碼已安全寫入雲端資料庫！")
                        st.session_state.user_api_key = clean_key
                        st.session_state.student_profile = {"grade": grade, "class": cls, "seat": seat, "name": student_name}
                        st.session_state.has_checked_in = True 
                        st.session_state.app_phase = "lobby" 
                        st.rerun()

        with tab2:
            st.markdown("#### 🛡️ 教練專屬後台")
            coach_action = st.radio("請選擇操作", ["🔑 教練登入", "📝 註冊新教練 (自動開通專屬後台)"], horizontal=True)
            
            if coach_action == "🔑 教練登入":
                coach_id = st.text_input("教練帳號", placeholder="輸入您註冊的帳號")
                coach_pw = st.text_input("教練密碼 🔒", type="password")
                coach_api = st.text_input("您的 API 金鑰 (選填)", type="password", placeholder="AIzaSy...", key="coach_api")
                
                if st.button("💼 進入專屬總經理室", use_container_width=True, type="primary"):
                    clean_coach_key = coach_api.strip() or TEACHER_API_KEY
                    if not clean_coach_key:
                        st.error("🚨 系統找不到 API 金鑰，請輸入！")
                    else:
                        accounts = get_coach_accounts()
                        master_coach_pw = st.secrets.get("COACH_PASSWORD", "")
                        if not master_coach_pw:
                            st.error("🚨 系統尚未設定教練主密碼 (COACH_PASSWORD)，請聯繫管理員！")
                            st.stop()
                        elif coach_id == "admin" and coach_pw == master_coach_pw:
                            st.session_state.managed_classes = "ALL"
                            st.session_state.user_api_key = clean_coach_key
                            st.session_state.student_profile = {"grade": "🏆", "class": "總教練", "seat": "00", "name": "創辦人"}
                            st.session_state.has_checked_in = True 
                            st.session_state.app_phase = "lobby" 
                            st.rerun()
                        elif coach_id in accounts and str(accounts[coach_id]['pw']) == str(coach_pw):
                            st.session_state.managed_classes = accounts[coach_id]['classes']
                            st.session_state.user_api_key = clean_coach_key
                            st.session_state.student_profile = {"grade": "🏆", "class": "總教練", "seat": "00", "name": f"{coach_id} 教練"}
                            st.session_state.has_checked_in = True 
                            st.session_state.app_phase = "lobby" 
                            st.rerun()
                        else:
                            st.error("🚨 帳號或密碼錯誤！")
            else:
                st.info("💡 註冊後，系統會自動為您隔離學生的學習數據與密碼，打造您的專屬教學後台！")
                new_coach_id = st.text_input("設定教練帳號 (建議用真實姓名)")
                new_coach_pw = st.text_input("設定專屬密碼 🔒", type="password")
                
                grade_opts = ["國七", "國八", "國九"]
                class_opts = [f"{i}班" for i in range(1, 21)]
                all_classes = [f"{g}_{c}" for g in grade_opts for c in class_opts]
                managed = st.multiselect("選擇您任教的班級 (可多選)", all_classes, placeholder="例如：國八_1班")
                
                if st.button("📝 立即註冊開通", use_container_width=True):
                    if not new_coach_id or not new_coach_pw or not managed:
                        st.error("🚨 帳號、密碼與任教班級都必須填寫！")
                    else:
                        accounts = get_coach_accounts()
                        if new_coach_id in accounts or new_coach_id == "admin":
                            st.error("🚨 此帳號已被註冊，請換一個名稱。")
                        else:
                            sync_cloud_data("教練名冊", [new_coach_id, new_coach_pw, ",".join(managed)], ["教練帳號", "密碼", "管理班級"])
                            st.success("✅ 註冊成功！請切換至上方「教練登入」進入您的專屬後台。")

        with tab3:
            st.markdown("#### 🚀 801 班專屬快速通關 (尚未開通)")
            c_seat, c_name = st.columns(2)
            with c_seat: seat_801 = st.selectbox("選擇座號", [str(i).zfill(2) for i in range(1, 38)], key="seat_801")
            with c_name: name_801 = st.text_input("姓名 (選填)", key="name_801")
            
            st.write("<br>", unsafe_allow_html=True)
            st.markdown("#### 🔐 雙重安全認證")
            
            vip_code = st.text_input("① 班級通關密碼 🔑", type="password", placeholder="請輸入教練發布的班級密碼", key="vip_code")
            pw_801 = st.text_input("② 個人專屬密碼 🔒", type="password", placeholder="首次登入將自動綁定，防止同學亂登入", key="pw_801")
            
            st.info("💡 提示：本通道由教練贊助 AI 費用，無需自行輸入金鑰！")
            
            if st.button("🚀 801 專屬登入", use_container_width=True, type="primary"):
                vip_pw = st.secrets.get("VIP_PASSWORD", "")
                if not vip_pw:
                    st.error("🚨 系統尚未設定 VIP 密碼 (VIP_PASSWORD)，請聯繫管理員！")
                elif vip_code != vip_pw:
                    st.error("🚨 班級通關密碼錯誤！這不是 801 班的密碼喔！")
                elif not pw_801:
                    st.error("🚨 請務必輸入個人專屬密碼！")
                elif not TEACHER_API_KEY.strip():
                    st.error("🚨 教練尚未在系統設定 GEMINI_API_KEY，無法使用專屬通道！")
                else:
                    cloud_pws = get_cloud_passwords()
                    student_id = f"國八_1班_{seat_801}" 
                    
                    if student_id in cloud_pws:
                        if str(cloud_pws[student_id]) != str(pw_801):
                            st.error("🚨 個人密碼錯誤！這個座號已經綁定了其他的密碼囉！")
                        else:
                            st.session_state.user_api_key = TEACHER_API_KEY.strip()
                            st.session_state.student_profile = {"grade": "國八", "class": "1班", "seat": seat_801, "name": name_801}
                            st.session_state.has_checked_in = True 
                            st.session_state.app_phase = "lobby" 
                            st.rerun()
                    else:
                        sync_cloud_data("學生密碼", [student_id, pw_801], ["學號", "密碼"])
                        st.toast("✅ 專屬密碼已安全綁定至雲端資料庫！")
                        st.session_state.user_api_key = TEACHER_API_KEY.strip()
                        st.session_state.student_profile = {"grade": "國八", "class": "1班", "seat": seat_801, "name": name_801}
                        st.session_state.has_checked_in = True 
                        st.session_state.app_phase = "lobby" 
                        st.rerun()

# ==========================================
# --- 8. [介面路由] 賽季大廳 ---
# ==========================================
elif st.session_state.app_phase == "lobby":
    profile = st.session_state.student_profile
    is_coach = (profile.get('class') == "總教練") 
    display_name = profile['name'] if profile['name'] else f"{profile['grade']}{profile['class']} {profile['seat']}號"
    
    st.write("<br>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>🏟️ 歡迎{'球員' if not is_coach else ''} {display_name}</h2>", unsafe_allow_html=True)
    st.write("---")
        
    if is_coach:
        managed_classes = st.session_state.get("managed_classes", [])
        st.markdown("### 📈 專屬班級學習戰報")
        
        history_df = get_cloud_history()
        
        if not history_df.empty:
            required = ['年級', '班級', '單元', '得分']
            if all(col in history_df.columns for col in required):
                if managed_classes != "ALL":
                    def filter_logic(row):
                        g_str = str(row['年級']).strip()
                        c_str = str(row['班級']).strip()
                        return f"{g_str}_{c_str}" in managed_classes
                    history_df = history_df[history_df.apply(filter_logic, axis=1)]
                
                if not history_df.empty:
                    st.dataframe(history_df, use_container_width=True)
                    st.download_button("📥 下載戰報", history_df.to_csv(index=False, encoding='utf-8-sig'), "戰報.csv")
                    
                    st.write("---")
                    st.markdown("### 🧠 班級綜合大數據分析")
                    unique_eps = history_df['單元'].unique().tolist() if '單元' in history_df.columns else []
                    c_ep, c_cls, c_btn = st.columns([2, 2, 1])
                    with c_ep: analyze_ep = st.selectbox("📌 選擇單元", unique_eps)
                    with c_cls: analyze_cls = st.selectbox("📌 選擇班級", ["全部我的班級"] + (managed_classes if isinstance(managed_classes, list) else []))
                    with c_btn:
                        if st.button("🚀 產出報告", use_container_width=True, type="primary"):
                            st.session_state.class_analysis_report = get_class_analysis(analyze_ep, analyze_cls, history_df)
                    if st.session_state.class_analysis_report:
                        st.info(f"**🎯 戰情分析：{analyze_ep}**")
                        st.markdown(st.session_state.class_analysis_report)
                else:
                    st.info("您的班級目前尚無紀錄。")
            else:
                st.error("🚨 雲端表頭與程式不符！")
                st.info("💡 建議：刪除雲端『學習戰報』分頁，讓系統依照正確順序自動重建。")
        else:
            st.info("目前尚無任何紀錄。")

        st.write("---")
        st.markdown("### 🔑 密碼管理")
        pws = get_cloud_passwords()
        if pws:
            if managed_classes != "ALL":
                pws = {k: v for k, v in pws.items() if "_".join(k.split("_")[:2]) in managed_classes}
            st.dataframe(pd.DataFrame(list(pws.items()), columns=["學號", "密碼"]), use_container_width=True)
            reset_id = st.selectbox("重置座號", list(pws.keys()))
            if st.button("🗑️ 剔除內鬼", type="primary"):
                if delete_student_password(reset_id): st.rerun()

    else:
        with st.expander("⚙️ 修改資料"):
            new_name = st.text_input("修改姓名", value=profile['name'])
            if st.button("💾 儲存"):
                st.session_state.student_profile['name'] = new_name
                st.rerun()
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("### 🗺️ 選擇賽季與單元")
        
        tab_s1, tab_s2 = st.tabs(["⚾ 第一季：化學大聯盟", "🎙️ 第二季：黎明韓流 (理化生存戰)"])
        
        READING_ROUTES = {
            "S01_1": "reading_modules.s01_e01_electrolyte", "S01_2": "reading_modules.s01_e02_acid_team",
            "S01_3": "reading_modules.s01_e03_alkaline_team", "S01_4": "reading_modules.s01_e04_molarity_ph",
            "S01_5": "reading_modules.s01_e05_titration", "S01_6": "reading_modules.s01_e06_salts",
            "S01_7": "reading_modules.s01_e07_reaction_rate", "S01_8": "reading_modules.s01_e08_tactics",
            "S01_9": "reading_modules.s01_e09_equilibrium", "S01_10": "reading_modules.s01_e10_le_chatelier",
            "S02_1": "reading_modules.s02_e01_organic", "S02_2": "reading_modules.s02_e02_polymers", "S02_3": "reading_modules.s02_e03_soap"     
        }

        def parse_ep_num(ep_str):
            match = re.search(r'第(\d+)集', ep_str)
            if match: return match.group(1)
            match = re.search(r'\d+', ep_str)
            if match: return match.group(0)
            return "1"

        def render_season_lobby(season_prefix, db_data, key_prefix):
            if not db_data or list(db_data.keys())[0].startswith("尚未載入賽程"):
                st.warning(f"🔧 此賽季的資料庫 (`{season_prefix.lower()}_db.json`) 尚未建立，請至 data 資料夾新增。")
                return

            selected_ep = st.selectbox(f"📌 選擇單元", list(db_data.keys()), key=f"sel_ep_{key_prefix}")
            ep_num = parse_ep_num(selected_ep)
            target_module = READING_ROUTES.get(f"{season_prefix}_{ep_num}")
            is_unlocked = st.session_state.reading_unlocked.get(selected_ep, False)

            if target_module and not is_unlocked:
                st.write("---")
                try:
                    module = importlib.import_module(target_module)
                    passed = module.render_reading_and_quiz()
                    if passed:
                        st.session_state.reading_unlocked[selected_ep] = True
                        st.rerun()
                except Exception as e:
                    st.error(f"🚨 系統呼叫戰術板失敗！錯誤訊息：{e}")
                    st.info(f"工程師提示：請確認 reading_modules 資料夾內是否已建立檔案 {target_module.split('.')[-1]}.py")
            
            else:
                if is_unlocked: st.success(f"✅ 機密報告閱讀完畢！準備進入【{selected_ep}】挑戰！")
                selected_diff = st.radio("🔥 選擇挑戰難度", list(DIFFICULTY_LEVELS.keys()), index=None, key=f"diff_{key_prefix}")
                st.write("<br>", unsafe_allow_html=True)
                
                st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: #E65100; color: white; width: 100%; font-size: 20px; font-weight: bold; border-radius: 8px;
                }
                </style>""", unsafe_allow_html=True)
                
                btn_label = "⚾ Play Ball! (化學大聯盟)" if season_prefix == "S01" else "🎙️ Play Ball! (黎明韓流)"
                if st.button(btn_label, use_container_width=True, type="primary", key=f"btn_{key_prefix}"):
                    if selected_diff is None: st.error("🚨 球員請注意！你還沒有選擇「挑戰難度」喔！")
                    else:
                        track_key = f"{selected_ep}_{selected_diff}"
                        st.session_state.attempt_tracker[track_key] = st.session_state.attempt_tracker.get(track_key, 0) + 1
                        st.session_state.current_episode = selected_ep
                        st.session_state.current_difficulty = selected_diff
                        st.session_state.current_attempt_num = st.session_state.attempt_tracker[track_key]
                        st.session_state.quiz_data = [] 
                        st.session_state.current_q_index = 0
                        st.session_state.q_answered = False
                        st.session_state.user_ans = {}
                        st.session_state.card_index = 0 
                        st.session_state.app_phase = "quiz"
                        st.rerun()

        with tab_s1: render_season_lobby("S01", SEASON_1_DB, "s1")
        with tab_s2: render_season_lobby("S02", SEASON_2_DB, "s2")

# ==========================================
# --- 9. [介面路由] 測驗系統 ---
# ==========================================
elif st.session_state.app_phase == "quiz":
    ep_name = st.session_state.current_episode
    diff_name = st.session_state.current_difficulty
    attempt_num = st.session_state.current_attempt_num
    
    st.markdown(f"## ✍️ {ep_name} [{diff_name}] - 第 {attempt_num} 次挑戰")
    st.write("---")
    
    col_lecture, col_main = st.columns([1, 1], gap="large")
    
    with col_lecture:
        st.info("📖 戰術板 (講義複習)") 
        current_db = SEASON_2_DB if ep_name in SEASON_2_DB else SEASON_1_DB
        st.markdown(current_db.get(ep_name, "讀取失敗"))
        
    with col_main:
        # 🌟 呼叫神級學習卡抓取引擎
        cards = get_smart_flashcards(ep_name)
        if cards:
            st.markdown("### 🃏 賽前快速記憶")
            idx = st.session_state.card_index
            current_card = cards[idx]
            wrapper_tag = "div" if idx % 2 == 0 else "section"
            
            st.markdown(f"""
                <{wrapper_tag} class="quiz-animate">
                    <label class="flip-card">
                        <input type="checkbox" class="flip-card-checkbox" autocomplete="off">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                <div class="fc-title">{current_card['front']}</div>
                                <p style='color: #94a3b8; font-size: clamp(14px, 1.5vw, 18px); margin-top: 15px;'>👆 點擊卡片看答案</p>
                            </div>
                            <div class="flip-card-back">
                                <div class="fc-content">{current_card['back']}</div>
                            </div>
                        </div>
                    </label>
                </{wrapper_tag}>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 2, 1])
            with c1:
                if st.button("⬅️ 上一張", use_container_width=True) and idx > 0:
                    st.session_state.card_index -= 1
                    st.rerun()
            with c2:
                st.write(f"<p style='text-align:center; color:#64748b; font-size:16px; padding-top:8px;'>學習卡進度 {idx+1} / {len(cards)}</p>", unsafe_allow_html=True)
            with c3:
                if st.button("下一張 ➡️", use_container_width=True) and idx < len(cards) - 1:
                    st.session_state.card_index += 1
                    st.rerun()
            st.write("<br>", unsafe_allow_html=True)

        st.markdown("### ✍️ 實戰測試")
        
        if not st.session_state.quiz_data:
            with st.spinner(f"🤖 正在從金庫抽取考卷..."):
                st.session_state.quiz_data = get_quiz_data(ep_name, diff_name, attempt_num)
                
        if st.session_state.quiz_data:
            total_q = len(st.session_state.quiz_data)
            curr_idx = st.session_state.current_q_index
            q = st.session_state.quiz_data[curr_idx]
            
            st.progress((curr_idx) / total_q, text=f"進度：第 {curr_idx + 1} 題 / 共 {total_q} 題")
            st.markdown(f"<div class='quiz-animate' style='font-size: clamp(18px, 1.5vw, 22px); font-weight: bold; margin-bottom: 15px;'>Q{curr_idx + 1}: {q.get('q', '題目遺失')}</div>", unsafe_allow_html=True)
            opts = q.get('options', ["A", "B", "C", "D"])
            
            if not st.session_state.q_answered:
                with st.form(f"q_form_{curr_idx}"):
                    choice = st.radio("請選擇答案：", opts, label_visibility="collapsed")
                    if st.form_submit_button("揮棒！(送出答案)", type="primary", use_container_width=True):
                        st.session_state.user_ans[curr_idx] = choice
                        st.session_state.q_answered = True
                        st.rerun()
            else:
                st.radio("你的選擇：", opts, index=opts.index(st.session_state.user_ans[curr_idx]), disabled=True, label_visibility="collapsed")
                
                ans_letter = q.get('ans', '').strip()
                user_choice = st.session_state.user_ans[curr_idx]
                
                st.write("---")
                if check_answer(user_choice, ans_letter):
                    st.success(f"🎉 漂亮的好球！正確答案是 {ans_letter}。")
                else:
                    st.error(f"💥 揮棒落空！正確答案是 {ans_letter}。")
                
                st.info(f"💡 教練即時解析：\n\n{q.get('diag', '無')}")
                st.write("<br>", unsafe_allow_html=True)
                
                if curr_idx < total_q - 1:
                    if st.button("👉 下一題", type="primary", use_container_width=True):
                        st.session_state.current_q_index += 1
                        st.session_state.q_answered = False
                        st.rerun()
                else:
                    if st.button("🏁 完成測驗，看結算戰報！", type="primary", use_container_width=True):
                        st.session_state.app_phase = "dashboard"
                        st.rerun()

# ==========================================
# --- 10. [介面路由] 學習儀表板 ---
# ==========================================
elif st.session_state.app_phase == "dashboard":
    st.markdown(f"<h1 style='text-align: center; color: #1e293b;'>🧪 {st.session_state.current_episode} 診斷報報</h1>", unsafe_allow_html=True)
    st.write("---")
    
    correct_count = 0
    total_q = len(st.session_state.quiz_data)
    mistakes_for_ai = ""
    
    for i, q in enumerate(st.session_state.quiz_data):
        user_choice = st.session_state.user_ans.get(i, "")
        if isinstance(q, dict) and 'ans' in q:
            ans_letter = str(q['ans']).strip()
            if check_answer(user_choice, ans_letter):
                correct_count += 1
            else:
                mistakes_for_ai += f"题目：{q.get('q','無')} (選:{user_choice}，正解:{ans_letter})。 "

    rate = int(correct_count/total_q*100) if total_q > 0 else 0
    
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1: st.markdown(f"<div class='stat-box'><p class='stat-label'>分數</p><p class='stat-value'>{correct_count}/{total_q}</p></div>", unsafe_allow_html=True)
    with col_s2: st.markdown(f"<div class='stat-box'><p class='stat-label'>正確率</p><p class='stat-value'>{rate}%</p></div>", unsafe_allow_html=True)
    with col_s3: st.markdown(f"<div class='stat-box' style='text-align: left;'><p class='stat-detail'><b>正確</b> <span style='float: right;'>{correct_count}</span></p><p class='stat-detail'><b>錯誤</b> <span style='float: right;'>{total_q - correct_count}</span></p><p class='stat-detail'><b>未回答</b> <span style='float: right;'>0</span></p></div>", unsafe_allow_html=True)

    current_ep = st.session_state.current_episode
    match = re.search(r'\d+', current_ep)
    if match: ep_num = int(match.group(0))
    else:
        zh_num = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
        ep_num = 1
        for k, v in zh_num.items():
            if k in current_ep:
                ep_num = v
                break
                
    zh_names = {1:"一", 2:"二", 3:"三", 4:"四", 5:"五", 6:"六", 7:"七", 8:"八", 9:"九", 10:"十"}
    search_targets = [current_ep, f"第{ep_num}集", f"第{ep_num:02d}集", f"第{zh_names.get(ep_num, '一')}集", f"EP{ep_num}", f"EP{ep_num:02d}"]

    audio_path = None
    podcast_name = "化學大聯盟"
    if os.path.exists("audio"):
        for filename in os.listdir("audio"):
            if any(target in filename for target in search_targets) and filename.endswith(".mp3"):
                audio_path = os.path.join("audio", filename)
                parts = filename.split("_")
                if len(parts) >= 2: podcast_name = parts[1] 
                break

    st.write("<br>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class='analysis-container'>
            <div style='display: flex; align-items: center; gap: 20px;'>
                <div class='analysis-icon'>📈</div>
                <div class='analysis-text'>
                    <h4>分析我的學習成效</h4>
                    <p>AI 教練將根據你的表現，找出觀念漏洞並產出專屬研讀指南。</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.ai_analysis:
        if st.button("🚀 開始深度診斷", use_container_width=True, type="primary"):
            with st.spinner("AI 教練正在分析你的戰略失誤..."):
                profile = st.session_state.student_profile
                p_name = profile['name'] if profile['name'] else f"{profile['grade']}{profile['class']} {profile['seat']}號"
                
                analysis, guide = get_ai_report(p_name, f"{correct_count}/{total_q}", mistakes_for_ai, st.session_state.current_episode, podcast_name)
                
                st.session_state.ai_analysis = analysis
                st.session_state.ai_guide = guide
                
                now_time = datetime.now().strftime("%Y-%m-%d %H:%M")
                sync_cloud_data("學習戰報", [now_time, profile['grade'], profile['class'], profile['seat'], profile['name'], st.session_state.current_episode, f"{correct_count}/{total_q}", analysis, guide])
                
                st.rerun()

    if st.session_state.ai_analysis:
        st.markdown("### 📋 繼續學習")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
                <div class='learning-card'>
                    <div class='learning-card-header'>
                        <div class='learning-card-icon'>🛡️</div>
                        <b>觀念不對？哪裡需要加強？</b>
                    </div>
                    <div class='learning-card-content'>{st.session_state.ai_analysis}</div>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
                <div class='learning-card'>
                    <div class='learning-card-header'>
                        <div class='learning-card-icon' style='background-color: #065f46;'>📖</div>
                        <b>專屬研讀指南</b>
                    </div>
                    <div class='learning-card-content'>{st.session_state.ai_guide}</div>
                </div>
            """, unsafe_allow_html=True)

        st.write("---")
        
        dash_col_l, dash_col_r = st.columns([1, 1], gap="large")
        
        with dash_col_l:
            st.markdown("### 🎧 戰術廣播室")
            if audio_path and os.path.exists(audio_path):
                st.markdown(f"""
                    <div style='background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); aspect-ratio: 1 / 0.8; border-top-left-radius: 20px; border-top-right-radius: 20px; color: white; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 10px 20px -5px rgba(0,0,0,0.2); width: 100%; padding: 20px; text-align: center;'>
                        <div style='background: rgba(59, 130, 246, 0.2); width: clamp(60px, 8vw, 80px); height: clamp(60px, 8vw, 80px); border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: clamp(30px, 4vw, 40px); margin-bottom: 20px; box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);'>🎙️</div>
                        <h2 style='color: #3b82f6; font-weight: bold; margin: 0; font-size: clamp(28px, 4vw, 38px); letter-spacing: 2px;'>{podcast_name}</h2>
                        <p style='color: white; margin: 15px 0 0 0; font-size: clamp(18px, 2.5vw, 24px); line-height: 1.4;'>【{current_ep}】<br>專屬破題攻略</p>
                    </div>
                """, unsafe_allow_html=True)
                
                with st.container():
                    st.markdown("""<div style="background-color: #f8fafc; padding: 20px; border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; border: 1px solid #e2e8f0; border-top: none; box-shadow: 0 10px 20px -5px rgba(0,0,0,0.1);">""", unsafe_allow_html=True)
                    st.audio(audio_path, format="audio/mp3")
                    st.markdown("""<p style="text-align: center; color: #64748b; font-size: 15px; margin-top: 15px; font-weight: bold;">👆 點擊播放，讓教練親自講給你聽！</p></div>""", unsafe_allow_html=True)
            else:
                st.info("📻 本單元目前尚未錄製專屬 Podcast，請鎖定最新更新！")

        with dash_col_r:
            st.markdown("### 🔍 戰術覆盤 (錯題詳解)")
            with st.expander("👇 點此收合 / 展開錯題詳解", expanded=True):
                with st.container(height=420, border=False): 
                    has_mistakes = False
                    for i, q in enumerate(st.session_state.quiz_data):
                        user_ans = st.session_state.user_ans.get(i, "")
                        correct_ans = q.get('ans','無').strip()
                        if not check_answer(user_ans, correct_ans):
                            has_mistakes = True
                            st.markdown(f"**Q{i+1}: {q.get('q','無')}**")
                            st.error(f"你的答案：{user_ans}")
                            st.success(f"正確答案：{correct_ans}")
                            st.info(f"💡 診斷：{q.get('diag','無')}")
                            st.write("---")
                    
                    if not has_mistakes:
                        st.success("🎉 太神啦！這張考卷你全對，完全沒有錯題！")

            st.write("<br>", unsafe_allow_html=True)
            if st.button("🔄 回到大廳 (挑戰新局)", use_container_width=True, type="primary"):
                st.session_state.ai_analysis = None
                st.session_state.ai_guide = None
                st.session_state.app_phase = "lobby"
                st.rerun()
