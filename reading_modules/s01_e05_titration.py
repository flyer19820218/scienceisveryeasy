# 檔案位置：reading_modules/s01_e05_titration.py
import streamlit as st

def render_reading_and_quiz():
    """渲染第五集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：世紀大決戰與極限拆彈——酸鹼中和的終極交鋒")
    st.info("🎧 點擊播放，聽聽曉臻球評為您轉播這場驚心動魄的五局下半！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第5集_極限拆彈_無語助詞強化版.mp3") 

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】五局下半，全場觀眾屏息以待的世紀大決戰正式爆發！酸球隊的王牌「<b>氫離子 (H<sup>+</sup>)</b>」與鹼性部隊的防守大將「<b>氫氧根離子 (OH<sup>-</sup>)</b>」在球場中央展開了毫無保留的正面衝撞。然而，令人驚訝的是，這兩個極度危險的球員互撞後並未引發大爆炸，反而是戰力瞬間歸零，完美結合成全宇宙最和平的物質——「<b>水 (H<sub>2</sub>O)</b>」。這場化敵為友的戰役，在化學上被稱為<b>「中和」</b>。</p>

<p><b>⚾ 裝備碎片與熱血沸騰的球場</b><br>
記者在場邊觀察到兩個重要現象：首先，雙方激烈互撞後，球員斷裂的球棒與手套碎片散落一地，這些殘骸在化學上被統稱為「<b>鹽類</b>」。其次，如果你伸手觸摸裝載這場比賽的燒杯，會發現它變得非常燙手！這證明了酸鹼中和是一場釋放巨大能量的「<b>放熱反應</b>」。</p>

<div style="background-color: #fff1f2; padding: 15px; border-left: 5px solid #e11d48; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>大聯盟安全警告：鹽類的致命誤解</b><br>
聯盟特別發布紅牌警告：千萬別以為化學上的「鹽類」就是速食店炸薯條撒的食鹽（氯化鈉）！鹽類只是酸鹼中和產物的「統稱」，其中有些鹽類含有劇毒，有些甚至能做成烈性炸藥，<b>絕對不可以將球場上的鹽類隨便放進嘴裡！</b>
</div>

<p><b>⚾ 極限拆彈：高塔狙擊與客座裁判</b><br>
為了解析敵方未知陣營的真實戰力，教練團會啟動名為「滴定」的極限拆彈戰術。防守方（未知濃度）潛伏在下方的「<b>錐形瓶</b>」中；而進攻方（已知濃度）則化身狙擊手，躲在上方帶有刻度的「<b>滴定管</b>」裡。<br>
狙擊手必須維持絕對標準的戰術姿勢：<b>左手</b>控制活塞精準滴入溶液，<b>右手</b>持續輕搖錐形瓶使戰況均勻，同時視線必須平齊液面凹下的最底端。</p>
</div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：極限拆彈滴定模擬器
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧪 戰術模擬中心：極限拆彈 (滴定實驗)")
    
    import json
    widget_spec = {
      "component": "LlmGeneratedComponent",
      "props": {
        "height": "600px",
        "prompt": "建立一個名為『極限拆彈：酸鹼滴定模擬器』的互動教學工具。介面分為兩區：左側是實驗視覺化，顯示一個滴定管（包含鹼性溶液）滴入下方的錐形瓶（包含酸性溶液與酚酞指示劑）。右側是圖表區，動態繪製『加入鹼液體積』對應『pH值』的滴定曲線。提供一個按鈕『滴入少許鹼液』與一個按鈕『連續滴加』。隨著鹼液加入，pH曲線應呈現S型上升。當pH值達到7時，標示此處為『當量點(科學平手)』。當pH值跨過8.2時，錐形瓶內的液體必須瞬間從無色變為明顯的紫紅色，並暫停滴加，彈出醒目提示：『達到滴定終點 (指示劑變色)！立即關閉活塞！』。請確保介面直觀，並使用繁體中文。"
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
    
    st.write("*(請操作上方的模擬器，化身狙擊手加入鹼液，親眼觀察曲線的飆升與指示劑變色的震撼瞬間！)*")

    st.markdown("""
<div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 19px; line-height: 1.8;">
🛡️ <b>防守秘訣：當量點 vs 滴定終點</b><br>
這場拆彈任務中，我們請來了客座裁判「酚酞指示劑」（在酸中隱形無色）。當上方溶液滴下，酚酞<b>瞬間變色且搖晃後不再褪色</b>的那一刻，狙擊手必須立刻關閉活塞！這個肉眼可見的變色瞬間，化學上精確稱為「<b>滴定終點</b>」！這與 H<sup>+</sup> 和 OH<sup>-</sup> 數量在科學上達到完美平手的「<b>當量點</b>」定義是截然不同的。許多新秀常在此栽跟頭，請務必牢記兩者的差異！
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導並完成模擬演練後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據記者的專欄報導與您的模擬操作，當我們看到「酚酞指示劑瞬間變色」而立刻關閉活塞停止實驗的那個瞬間，在化學上精確的名稱是什麼？",
        [
            "(A) 沸騰點", 
            "(B) 當量點", 
            "(C) 滴定終點", 
            "(D) 絕對中性點"
        ],
        index=None,
        key="reading_q5"
    )

    if q1 == "(C) 滴定終點":
        st.success("✅ 拆彈成功！你完美分辨了肉眼看見的「滴定終點」與科學平手的「當量點」，正式解鎖賽事挑戰！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者驚呼：活塞沒關緊！這是一個超大變化球陷阱，趕快回去看最後一段綠色的防守秘訣！")
        return False
        
    return False
