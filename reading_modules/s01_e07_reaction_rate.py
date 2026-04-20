# 檔案位置：reading_modules/s01_e07_reaction_rate.py
import streamlit as st
import json

def render_reading_and_quiz():
    """渲染第七集閱讀素養，過關回傳 True"""
    
    st.markdown("### 🎙️ 大聯盟專欄：測速槍下的對決——超音速跑壘與雙重爆發")
    st.info("🎧 點擊播放，聽聽曉臻球評為您轉播這場 Lucky Seven 的極速狂飆！")
    
    # 若有音檔，將此行解除註解並確認路徑
    # st.audio("audio/第一季_化學大聯盟_第7集_超音速跑者與雙重爆發.mp3") 

    st.markdown("""
<div style="background-color: #f8fafc; padding: clamp(12px, 3vw, 25px); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 19px; line-height: 1.8; color: #334155; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);">
<p>【特約記者 彥君／化學球場報導】比賽來到 Lucky Seven 第七局！這局記者特別帶上了測速槍，準備來測量這群化學新秀的爆發力，也就是化學上的「<b>反應速率</b>」。雖然我們肉眼無法看見微小分子球員的跑動，但只要球場上出現「<b>氣體狂冒、顏色改變、或沉澱物堆積</b>」，就代表反應正在激烈進行！</p>

<div style="background-color: #fff1f2; padding: 15px; border-left: 5px solid #e11d48; margin: 15px 0; border-radius: 4px; font-size: 18px;">
🚨 <b>大聯盟測速警告：時間與速率的反比陷阱！</b><br>
測速中心特別提醒球迷，千萬別以為「花的時間越久，反應越激烈」！在賽場上，球員跑得越快，抵達本壘花費的「時間」就會越<b>短</b>！因此，反應速率跟時間是完全「<b>成反比</b>」的。我們通常用時間的倒數（<b>1 / t</b>）來代表反應速率，這可是段考最愛吹哨的變化球！
</div>

<p><b>⚾ 得分絕對核心：碰撞學說 (Collision Theory)</b><br>
球員在場上不能只是擦棒被捕，必須發生拳拳到肉的「<b>有效碰撞</b>」才能成功引發反應！這需要滿足兩大嚴格條件：<br>
1. <b>正確的碰撞方向</b>：就像打者揮棒時，必須精準擊中球棒的「甜蜜點」。<br>
2. <b>突破活化能門檻</b>：打者必須全力揮擊，擁有足夠的「能量」才能把球扛出高聳的全壘打牆！</p>

<p><b>⚾ 氣候戰術：溫度的「雙重爆發」加成</b><br>
如果教練團讓球場的溫度飆高，球員的腎上腺素會跟著狂飆，這將帶來可怕的雙重效果：<br>
第一，球員跑得更快，<b>大幅增加了互相碰撞的次數</b>。<br>
第二，球員整體能量變高，<b>更容易突破「活化能」的全壘打牆門檻</b>。<br>
因為「次數」與「達標率」同時增加，產生了相乘的爆發效果，這會讓反應速率像全壘打的仰角一樣，畫出一條向上狂飆的「<b>二次曲線</b>」！</p>
</div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 🧪 互動小工具：碰撞與溫度雙重爆發模擬器
    # ---------------------------------------------------------
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("#### 🧪 戰術模擬中心：溫度與有效碰撞測試")
    
    widget_spec = {
      "component": "LlmGeneratedComponent",
      "props": {
        "height": "650px",
        "prompt": "建立一個名為『溫度與雙重爆發模擬器』的互動教學工具。介面分為兩區：左側是『微觀球場』，顯示一個充滿運動粒子的封閉方塊。右側是『數據圖表』，動態繪製一條曲線圖（X軸為溫度，Y軸為反應速率）。下方提供一個『球場溫度』的滑桿。當使用者調高溫度時，左側粒子運動速度加快，且粒子間發生碰撞時若達到能量門檻會閃爍高亮，代表『有效碰撞』。右側的圖表應隨著溫度的提升，畫出一條向上飆升的非線性曲線（類似二次曲線），展示『雙重加成』的效果。請加上圖例與說明，介面使用繁體中文。"
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
    
    st.write("*(請操作上方的溫度滑桿，親眼觀察粒子跑動的速度，以及右側呈現『雙重加成』的狂飆曲線！)*")

    st.markdown("""
<div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #22c55e; margin: 15px 0; border-radius: 4px; font-size: 19px; line-height: 1.8;">
🛡️ <b>防守秘訣：球員的天生素質（活性）</b><br>
除了改變溫度，球隊挑選的「球員活性」也決定了得分的難易度。例如超級快腿「<b>鈉金屬 (Na)</b>」，活性極大，一碰到水就激烈爆炸；但如果是聯盟不動老將「<b>黃金 (Au)</b>」，因為活性極小，不管教練怎麼催促，他站在打擊區就是不動如山，絕對不會起反應！
</div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    st.markdown("### 🏆 賽後記者提問")
    st.markdown("<span style='color: #64748b; font-size: 18px; font-weight: bold;'>👉 讀完報導並完成模擬演練後，請回答記者提問以領取挑戰通行證：</span>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    q1 = st.radio(
        "Q1. 根據記者的測速報導，如果我們利用觀察「沉澱物完全蓋住本壘板所花費的時間」來測量反應快慢時，下列哪一個觀念是正確的？",
        [
            "(A) 花費的時間越長，代表反應速率越快。", 
            "(B) 花費的時間長短，與反應速率完全無關。", 
            "(C) 溫度越高，球員跑得越快，所以測量到的時間會變長。", 
            "(D) 反應速率與時間成反比，通常用時間的倒數 (1/t) 來代表反應速率。"
        ],
        index=None,
        key="reading_q7"
    )

    if q1 == "(D) 反應速率與時間成反比，通常用時間的倒數 (1/t) 來代表反應速率。":
        st.success("✅ 測速精準！時間越短代表速度越快，你成功避開了反比陷阱，正式解鎖賽事挑戰！")
        return True 
    elif q1 is not None:
        st.error("❌ 記者搖頭：嗶嗶！你踩中曉臻球評被吹哨的陷阱啦！趕快回去看紅色框框的警告！")
        return False
        
    return False
