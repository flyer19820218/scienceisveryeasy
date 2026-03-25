# 🏆 理化別裝了！這場比賽我贏定了 (Science Is Very Easy)

這是一個專為國中生打造的**「沉浸式理化 Podcast 微課平台」**。
我們拋棄了枯燥的教科書與黑板，將微觀的化學世界化作熱血的棒球大聯盟！跟著主播彥君老師與球評曉臻助教的轉播，看穿科學的偽裝，拿回屬於你的分數！

## 🌟 核心理念 (Core Concept)
* **場景化學習：** 將酸、鹼、鹽等生硬的化學名詞，包裝成棒球場上的球隊與球路，降低學習抗拒感。
* **沉浸式聽覺：** 採用高品質 AI 語音 (Edge-TTS) 生成逼真的轉播對話，並輔以精準對拍的真實球場音效（如：群眾歡呼、裁判哨音、金屬擊球聲）。
* **極簡行動體驗：** 使用 Streamlit 打造，針對手機版介面深度優化，讓學生隨時隨地都能像聽球賽一樣複習理化。

## 🚀 平台特色 (Features)
* **📱 手機端完美適配：** 隱藏了預設的 Streamlit 選單與浮水印，呈現乾淨、專注的 App 級視覺體驗。
* **🎧 劇集式展開：** 使用 Expander 結構整理 10 集賽事，最新一集自動展開，歷史集數預設收合，保持版面清爽。
* **📝 戰術板亮點摘要：** 每集皆附有核心知識點的 Markdown 整理（支援 LaTeX 渲染化學式，如 $H_2SO_4$），聽完馬上抓重點。
* **🔗 一鍵分享功能：** 底部內建客製化的 HTML/JS 分享按鈕，點擊即可複製專屬網址，方便學生間互相推廣。

## 🛠️ 技術架構 (Tech Stack)
* **Frontend / Backend:** [Streamlit](https://streamlit.io/) (Python)
* **Audio Generation:** Microsoft Edge-TTS (via Python script)
* **Audio Mixing:** Pydub (Python)
* **UI Components:** Streamlit built-in layout & Custom HTML/CSS/JS via `streamlit.components.v1`

## 📁 專案結構 (Project Structure)
確保您的檔案依照以下結構擺放，才能讓 Streamlit 順利讀取圖片與音檔：

```text
📦 Your-Project-Folder
 ┣ 📂 audio                 # 存放所有 Podcast MP3 音檔
 ┃ ┣ 📜 第一季_化學大聯盟_酸球隊.mp3
 ┃ ┗ 📜 第一季_化學大聯盟_超級新秀_電解質.mp3
 ┣ 📂 images                # 存放所有視覺設計圖
 ┃ ┣ 📜 化學大聯盟.jpg
 ┃ ┗ 📜 理化別裝了！這場比賽我贏定了.png
 ┣ 📜 app.py                # Streamlit 主程式碼
 ┗ 📜 README.md             # 本說明文件
