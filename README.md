# 🎙️ 理化別裝了！這場比賽我贏定了 🏆
**— 互動式 Podcast 與學習診斷系統 —**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> 「褪去偽裝，直擊本質。歡迎來到沒有退路的理化生存戰！」

這不僅僅是一個存放音檔的倉庫，而是一個專為國/高中生打造的**「沉浸式理化學習平台」**。本專案將枯燥的理化知識包裝成高規格的「實境選秀廣播劇」與「體育賽事轉播」，並結合 Streamlit 打造出集結**音頻播放、重點筆記、互動留言與學習診斷**於一體的網頁應用程式。

---

## ✨ 核心特色 (Features)

* 🎧 **多賽季 Podcast 播放器**
  * 支援跨賽季切換（如：第一季《化學大聯盟》、第二季《黎明韓流選秀》）。
  * 內建流暢的網頁音頻播放器，隨點隨聽。
* 📝 **製作人評審筆記 (Show Notes)**
  * 每個集數配有專屬的展開式筆記（Expander），將音頻中的重點知識（如：勒沙特列原理、四大官能基、虎克定律）轉化為高密度的考點精華。
* 💬 **即時互動留言板**
  * 內建 JSON 格式的輕量級留言系統，讓聽眾/學生可以在聽完節目後即時「吐嘈」或發問，建立學習社群感。
* 📊 **學習診斷系統 (開發中 / WIP)**
  * 結合節目知識點的互動式測驗與弱點分析，精準打擊學生的理化盲區。
* ⚡ **自動化音頻生成工作流 (Audio Pipeline)**
  * 專案內含基於 `edge-tts` 與 `pydub` 的音軌合成腳本，可將純文本劇本自動轉化為帶有背景音樂、音效、人聲雙軌混音的母帶級 MP3。

---

## 🛠️ 技術棧 (Tech Stack)

* **前端與網頁框架**：[Streamlit](https://streamlit.io/)
* **後端邏輯與資料處理**：Python 3
* **語音合成引擎**：`edge-tts` (Microsoft Edge Text-to-Speech API)
* **音頻混音與剪輯**：`pydub`, `ffmpeg`
* **資料儲存**：JSON (輕量級留言與測驗數據儲存)

---

## 📂 專案目錄結構 (Folder Structure)

```text
├── app.py                  # Streamlit 主程式入口
├── audio/                  # Podcast MP3 音檔存放區
│   ├── 第一季_化學大聯盟_...mp3
│   └── 第二季_黎明韓流_...mp3
├── images/                 # 網頁主視覺與 UI 圖片
│   ├── 化學大聯盟.jpg
│   └── limingdancing.png
├── data/                   # 本地端資料庫 (JSON)
│   └── comments.json       # 留言板數據
├── scripts/                # (可選) 存放音頻生成的 Colab/Python 腳本
├── requirements.txt        # Python 依賴套件清單
└── README.md               # 專案說明文件
