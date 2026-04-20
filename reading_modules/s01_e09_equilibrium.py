# 檔案位置：reading_modules/s01_e09_equilibrium.py
import streamlit as st
import json

def render_reading_and_quiz():
    """渲染第九集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：沒有盡頭的延長賽——揭開「動態平衡」的巨蛋之謎")
    st.info("🎧 點擊播放，聽聽曉臻球評為您轉播這場永遠打不完的史詩戰役！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第9集_化學平衡_沒有盡頭的延長賽.mp3") 

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學巨蛋報導】九局上半，比賽進入了永遠打不完的延長賽！在化學大聯盟裡，比賽分為兩種截然不同的賽制：</p>

<p><b>⚾ 露天球場 vs 巨蛋球場</b><br>
🔸 <b>不可逆反應</b>：就像在「<b>露天球場</b>」打球，打者把球轟出全壘打牆飛進太平洋，就永遠回不來了（例如：木材燃燒化為灰燼、氣體逸散），這類比賽只能單向進行，無法回頭。<br>
🔸 <b>可逆反應</b>：必須在屋頂完全關閉的「<b>巨蛋球場（密閉系統）</b>」進行！當氣體撞到屋頂會反彈回來，再次參與比賽。這時場上就會同時出現兩種跑動方向：球員從休息室跑上場守備（<b>正反應</b>），以及場上球員退下場回到休息室（<b>逆反應</b>）！</p>

<p><b>⚾ 賽評八字真言：巨觀靜止，微觀狂奔</b><br>
當裁判大喊「比賽達到平衡」時，從觀眾席看過去，場上與休息室的「總人數」似乎不再改變（這在化學上稱為<b>濃度固定</b>）。但千萬別以為球員們在場上睡覺！<br>
這是一場激烈的「<b>動態平衡</b>」：教練依然在瘋狂進行人員調度，只是<b>上場的球員數量，剛好等於下場的球員數量（正反應速率 = 逆反應速率）</b>。一進一出互相抵銷，造就了這場沒有盡頭的延長賽！</p>
</div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：動態平衡巨蛋模擬器
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧪 戰術模擬中心：巨觀與微觀的雙重視角")
    
    widget_spec = {
      "component": "LlmGeneratedComponent",
      "props": {
        "height": "650px",
        "prompt": "建立一個名為『動態平衡：巨蛋球場模擬器』的互動教學工具。介面分為上下兩區：上方是『微觀球場』，分為左右兩個相連的空間（左：休息室/反應物，右：場上/生成物），有代表球員的粒子在兩邊隨機移動。下方是『巨觀數據圖表』，繪製兩條動態折線圖（分別代表左區與右區的粒子總數，隨時間變化）。提供一個『開始比賽』按鈕。按下後，粒子開始來回移動，下方的兩條曲線會隨著時間變化，最終逐漸趨於平緩並變成『兩條平行的水平線』。當曲線變成水平時，彈出醒目提示：『達到動態平衡：正逆速率相等，總人數不再改變！』。請在圖表區加上重要文字標籤：『注意看！平衡時兩條線的高度(濃度)不一定要一樣，也不一定要剛好是完美的整數比例！』。介面請使用繁體中文。"
      }
    }
    
    st.components.v1.html(f"""
        <script>
            window.parent.postMessage({{
                type: 'streamlit:set_component_value',
                value: {json.dumps(widget_spec)}
            }}, '*');
        </script>
    """, height=0)
    
    st.write("*(請點擊上方的開始按鈕，親眼見證粒子瘋狂跑動時，下方的濃度曲線是如何變成水平直線的！)*")

    st.markdown("""
<div style="background-color: #fff1f2; padding: 15px; border-left: 5px solid #e11d48; margin: 15px 0; border-radius: 4px; font-size: 19px; line-height: 1.8;">
🚨 <b>大聯盟防守警告：段考最愛考的大魔王陷阱！</b><br>
記者發現，很多新秀以為達到平衡時，場上與休息室的人數比例，會剛好等於化學戰術板上寫的「<b>係數比</b>」（例如 N<sub>2</sub> + 3H<sub>2</sub> ⇌ 2NH<sub>3</sub> 就是 1:3:2），這是<b>大錯特錯的致命盲點</b>！<br>
平衡時的濃度比例，有可能是任何數字比（完全取決於一開始帶了多少人進巨蛋）。請把這句話刻在腦海裡：<b>「濃度固定不變」絕對不等於「濃度等於係數比」！</b>
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導並觀察模擬圖表後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據大聯盟專欄報導，關於「化學動態平衡」的敘述，下列哪一個觀念是完全正確的？",
        [
            "(A) 反應達到平衡時，所有分子球員都會停止跑動，這是一場完全靜止的比賽。", 
            "(B) 只要把反應物放在開放的露天球場，最後也一定能順利達到化學平衡。", 
            "(C) 達到平衡時，正反應速率會剛好等於逆反應速率，巨觀上各物質的濃度不再改變。", 
            "(D) 達到平衡時，反應物與生成物的濃度比例，一定會剛好等於化學式的係數比。"
        ],
        index=None,
        key="reading_q9"
    )

    if q1 == "(C) 達到平衡時，正反應速率會剛好等於逆反應速率，巨觀上各物質的濃度不再改變。":
        st.success("✅ 採訪成功！你徹底領悟了「巨觀靜止，微觀狂奔」的動態平衡真諦！正式解鎖賽事挑戰！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者搖頭：嗶嗶！你被大魔王陷阱騙到了！趕快回去看紅色框框與八字真言的防守秘訣！")
        return False
        
    return False
