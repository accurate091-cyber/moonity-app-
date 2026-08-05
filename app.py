import random
from datetime import datetime
import streamlit as st

# 1. ตั้งค่าหน้าตาของแอป
st.set_page_config(
    page_title="🔮 Moonity - มูนิตี้ ดูดวงออนไลน์",
    page_icon="🔮",
    layout="centered"
)

# 2. ใส่ Custom CSS ตกแต่งให้แน่น สวยงาม สไตล์พรีเมียม
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mitr:wght@300;400;500;600&display=swap');

    html, body, .stApp, p, h1, h2, h3, h4, h5, h6, input, select, textarea, label {
        font-family: 'Mitr', sans-serif !important;
    }

    /* คืนค่าปุ่มกวักเปิด Sidebar */
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
        z-index: 999999 !important;
    }

    /* ซ่อนปุ่มมงกุฎและส่วนเกิน */
    footer, #MainMenu, [data-testid="stDecoration"], .stAppViewerFooter {
        display: none !important;
    }

    /* โลโก้แถบข้าง */
    .sidebar-logo-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #111;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* กล่องข้อมูลส่วนตัว */
    .user-profile-box {
        background: linear-gradient(135deg, #f3e8ff 0%, #fce7f3 100%);
        border: 1px solid #e9d5ff;
        border-left: 5px solid #8b5cf6;
        padding: 14px 18px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(139, 92, 246, 0.08);
    }
    .user-profile-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #4c1d95;
        margin-bottom: 4px;
    }
    .user-profile-detail {
        font-size: 0.9rem;
        color: #6b21a8;
    }

    /* กล่อง Widget สีและเลขมงคลประจำวัน */
    .daily-lucky-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        flex-wrap: wrap;
    }
    .lucky-card {
        flex: 1;
        min-width: 130px;
        background-color: #ffffff;
        border: 1px solid #f1f5f9;
        padding: 10px 14px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        text-align: center;
    }
    .lucky-title {
        font-size: 0.8rem;
        color: #64748b;
        margin-bottom: 2px;
    }
    .lucky-value {
        font-size: 0.95rem;
        font-weight: 600;
        color: #0f172a;
    }

    /* การ์ดคำทำนาย */
    .fortune-card {
        background-color: #ffffff;
        border-left: 5px solid #ec4899;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 14px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .fortune-title {
        font-weight: 600;
        font-size: 1.05rem;
        color: #1e293b;
        margin-bottom: 4px;
    }
    .fortune-desc {
        font-size: 0.92rem;
        color: #475569;
        line-height: 1.5;
    }

    /* การ์ดไพ่ทาโรต์ */
    .tarot-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #7c3aed;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        height: 100%;
    }

    /* กล่องสรุปภาพรวม */
    .summary-box {
        background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
        border: 1px solid #d8b4fe;
        padding: 18px;
        border-radius: 12px;
        color: #3b0764;
        margin-top: 18px;
    }

    /* กล่องคำคมสร้างพลังใจ */
    .quote-box {
        background-color: #f8fafc;
        border: 1px stroke #e2e8f0;
        padding: 14px 18px;
        border-radius: 10px;
        margin-top: 25px;
        text-align: center;
        color: #64748b;
        font-size: 0.88rem;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# 3. โลโก้ Moonity ใน Sidebar
st.sidebar.markdown('<div class="sidebar-logo-title">🔮 Moonity</div>', unsafe_allow_html=True)
st.sidebar.markdown("---")

# 4. ข้อมูลดวงชะตา Sidebar
st.sidebar.header("👤 ข้อมูลดวงชะตา")
user_type = st.sidebar.radio("รูปแบบการใช้งาน:", ["✨ กรอกวัน/เดือน/ปีเกิด", "🎲 ใช้งานแบบชั่วคราว"])

if user_type == "✨ กรอกวัน/เดือน/ปีเกิด":
    name = st.sidebar.text_input("ชื่อ/ชื่อเล่น:", "ดวงดี")
    birth_date = st.sidebar.date_input("วันเกิด:", datetime(1997, 12, 31))
    birth_time = st.sidebar.time_input("เวลาเกิด:", datetime.strptime("09:00", "%H:%M").time())
    user_info = {
        "name": name, 
        "birth_date": birth_date.strftime("%d/%m/%Y"), 
        "birth_time": birth_time.strftime("%H:%M น."),
        "mode": "full"
    }
else:
    user_info = {
        "name": "ผู้มาเยือน", 
        "birth_date": "ไม่ได้ระบุ", 
        "birth_time": "ไม่ได้ระบุ",
        "mode": "guest"
    }

menu = st.sidebar.radio("📌 เลือกโหมดคำทำนาย", ["✨ ดวงรายวันเฉพาะบุคคล", "⛩️ เซียมซีออนไลน์", "🃏 ไพ่ทาโรต์ 3 ใบ"])

# 5. แสดงกล่องข้อมูลส่วนตัวชิดซ้ายด้านบน
if user_info['mode'] == 'full':
    profile_html = f"""
    <div class="user-profile-box">
        <div class="user-profile-title">✨ ข้อมูลดวงชะตา: คุณ{user_info['name']}</div>
        <div class="user-profile-detail">
            📅 <b>วันเกิด:</b> {user_info['birth_date']} &nbsp;|&nbsp; ⏰ <b>เวลาเกิด:</b> {user_info['birth_time']}
        </div>
    </div>
    """
else:
    profile_html = f"""
    <div class="user-profile-box">
        <div class="user-profile-title">✨ ข้อมูลดวงชะตา: คุณ{user_info['name']}</div>
        <div class="user-profile-detail">🎲 โหมดใช้งานแบบชั่วคราว</div>
    </div>
    """

st.markdown(profile_html, unsafe_allow_html=True)

# 6. เพิ่ม Widget สีและเลขมงคลประจำวัน
lucky_widget = """
<div class="daily-lucky-container">
    <div class="lucky-card">
        <div class="lucky-title">🎨 สีมงคลวันนี้</div>
        <div class="lucky-value">ชมพู / ฟ้าเข้ม</div>
    </div>
    <div class="lucky-card">
        <div class="lucky-title">⛔ สีต้องห้าม</div>
        <div class="lucky-value">สีแดง</div>
    </div>
    <div class="lucky-card">
        <div class="lucky-title">🔢 เลขนำโชค</div>
        <div class="lucky-value">16, 89, 95</div>
    </div>
    <div class="lucky-card">
        <div class="lucky-title">🧭 ทิศมงคล</div>
        <div class="lucky-value">ตะวันออกเฉียงเหนือ</div>
    </div>
</div>
"""
st.markdown(lucky_widget, unsafe_allow_html=True)

# 7. เนื้อหาแต่ละโหมด
if menu == "✨ ดวงรายวันเฉพาะบุคคล":
    st.subheader(f"✨ คำทำนายประจำวันสำหรับ: คุณ{user_info['name']}")
    
    if st.button("🔮 ผูกดวงรับคำทำนาย"):
        work_list = [
            "การงานราบรื่น มีผู้ใหญ่คอยซัพพอร์ตและสนับสนุนผลงาน",
            "ไอเดียสร้างสรรค์พุ่งกระฉูด เหมาะสำหรับการเริ่มโปรเจกต์ใหม่",
            "ระวังงานด่วนเข้ามาพร้อมกัน ควรจัดลำดับความสำคัญให้ดี"
        ]
        money_list = [
            "การเงินคล่องตัว มีโชคลาภเข้ามาจากช่องทางใหม่ๆ",
            "มีเกณฑ์ได้รับเงินก้อนพิเศษหรือผลตอบแทนที่รอคอยมานาน",
            "ระวังรายจ่ายกะทันหันเกี่ยวกับสุขภาพหรือของชำรุด"
        ]
        love_list = [
            "คนโสดมีเกณฑ์พบมิตรใหม่ คนมีคู่เสน่ห์แรงน่าหลงใหล",
            "บรรยากาศความรักอบอุ่น เข้าใจและดูแลกันดีขึ้น",
            "ควรระวังเรื่องอารมณ์และคำพูดเล็กๆ น้อยๆ กับคนรัก"
        ]
        
        st.success(f"🔮 **คำทำนายผูกดวงชะตาเรียบร้อยแล้ว**")
        
        st.markdown(f"""
        <div class="fortune-card">
            <div class="fortune-title">💼 ด้านการงานและการเรียน</div>
            <div class="fortune-desc">{random.choice(work_list)}</div>
        </div>
        <div class="fortune-card" style="border-left-color: #10b981;">
            <div class="fortune-title">💰 ด้านการเงินและโชคลาภ</div>
            <div class="fortune-desc">{random.choice(money_list)}</div>
        </div>
        <div class="fortune-card" style="border-left-color: #f43f5e;">
            <div class="fortune-title">💖 ด้านความรักและความสัมพันธ์</div>
            <div class="fortune-desc">{random.choice(love_list)}</div>
        </div>
        """, unsafe_allow_html=True)

elif menu == "⛩️ เซียมซีออนไลน์":
    st.subheader("⛩️ เขย่าเซียมซีตั้งจิตอธิษฐาน")
    st.caption("ตั้งจิตให้นิ่ง นึกถึงสิ่งที่อยากรู้ แล้วกดเขย่ากระบอกเซียมซี")
    
    if st.button("🎯 เขย่ากระบอกเซียมซี"):
        stick = random.randint(1, 5)
        
        fortunes_db = {
            1: {
                "title": "ใบที่ 1: มหาโชคมหาลาภ (ยอดเยี่ยม)",
                "detail": "ดวงชะตาสว่างไสว สิ่งที่คิดหรืออธิษฐานไว้จะประสบความสำเร็จสมปรารถนาทุกประการ มีผู้ใหญ่ให้ความเมตตาอุปถัมภ์",
                "work": "การงานเติบโตก้าวหน้า ได้เลื่อนขั้นเลื่อนตำแหน่ง",
                "money": "การเงินหมุนเวียนดีเยี่ยม มีโชคลาภก้อนโต",
                "love": "ความรักสมหวัง คนโสดจะได้พบคู่บุญ",
                "luck": "เลขมงคล: 1, 9, 19, 89"
            },
            2: {
                "title": "ใบที่ 2: เมตตามหาเสน่ห์ (ดีมาก)",
                "detail": "ดวงมีเสน่ห์เป็นที่รักใคร่ของผู้คนรอบข้าง เดินทางไปไหนมาไหนมีแต่คนคอยช่วยเหลือ อุปสรรคที่มีจะคลี่คลายลงได้ด้วยดี",
                "work": "เหมาะแก่การเจรจา ค้าขาย หรือติดต่อประสานงาน",
                "money": "เงินทองไม่ขาดมือ มีลาภปากลาภลอย",
                "love": "คนมีคู่รักใคร่หวานชื่น คนโสดมีคนมาขายขนมจีบ",
                "luck": "เลขมงคล: 2, 6, 26, 62"
            },
            3: {
                "title": "ใบที่ 3: ชะลอเพื่อรอจังหวะ (ปานกลาง)",
                "detail": "ช่วงนี้ดวงชะตากำลังอยู่ในช่วงทรงตัว อย่าเพิ่งใจร้อนทำการใหญ่ ให้ตั้งสติและทำจิตใจให้สงบ ยึดความซื่อสัตย์เป็นหลักแล้วจะผ่านพ้นไปได้",
                "work": "ควรรักษางานเดิมไว้ก่อน อย่าเพิ่งรีบเปลี่ยนงาน",
                "money": "ควรประหยัดอดออม งดเว้นการเสี่ยงโชคหนักๆ",
                "love": "ประคบประหงมน้ำใจกันให้ดี ระวังความเข้าใจผิด",
                "luck": "เลขมงคล: 3, 5, 35, 53"
            },
            4: {
                "title": "ใบที่ 4: เตือนสติสร้างบุญ (ระวัง)",
                "detail": "ช่วงนี้มีวิบากกรรมหรือมารผจญเล็กน้อย ควรหาเวลาไปทำบุญตักบาตร บริจาคทาน เพื่อเสริมดวงชะตาและสะเดาะเคราะห์",
                "work": "ระวังเรื่องเอกสารผิดพลาด หรือเพื่อนร่วมงานอิจฉา",
                "money": "ระวังรอบคอบเรื่องการกู้ยืมและค้ำประกัน",
                "love": "ลิ้นกับฟันกระทบกันเป็นธรรมดา ควรนิ่งสงบสยบความเคลื่อนไหว",
                "luck": "เลขมงคล: 4, 8, 48, 84"
            },
            5: {
                "title": "ใบที่ 5: ฟ้าหลังฝน (ดี)",
                "detail": "ความทุกข์ความยากลำบากที่เคยเผชิญกำลังจะผ่านพ้นไป สิ่งดีๆ กำลังจะเข้ามาแทนที่ จงมีความเชื่อมั่นและลงมือทำอย่างเต็มที่",
                "work": "ปัญหาอุปสรรคจะได้รับแก้ไข มีช่องทางใหม่ๆ",
                "money": "เริ่มปลดหนี้สินได้ การเงินจะค่อยๆ ดีขึ้นตามลำดับ",
                "love": "จะได้ปรับความเข้าใจกัน ปัญหาหัวใจผ่อนคลาย",
                "luck": "เลขมงคล: 5, 7, 57, 75"
            }
        }
        
        result = fortunes_db[stick]
        st.subheader(f"✨ ผลเซียมซีของคุณ {user_info['name']}")
        st.info(f"📜 **{result['title']}**")
        st.markdown(f"""
        **📖 คำทำนายรวม:** {result['detail']}\n
        * 💼 **การงาน:** {result['work']}
        * 💰 **การเงิน:** {result['money']}
        * 💖 **ความรัก:** {result['love']}
        * 🍀 **{result['luck']}**
        """)

elif menu == "🃏 ไพ่ทาโรต์ 3 ใบ":
    st.subheader("🃏 เปิดไพ่ทาโรต์ 3 ใบ (อดีต - ปัจจุบัน - อนาคต)")
    st.caption("ตั้งจิตอธิษฐานถึงเรื่องที่ต้องการคำตอบ แล้วกดปุ่มทำนาย")
    
    cards_db = [
        {
            "name": "The Sun ☀️",
            "past": "อดีตที่ผ่านมาคุณได้ผ่านช่วงเวลาแห่งความสำเร็จ ได้รับโอกาสดีๆ หรือมีความสุขสมหวังในสิ่งที่ลงมือทำ",
            "present": "ปัจจุบันชีวิตกำลังสว่างไสว ปัญหาที่เคยมีได้รับการคลี่คลาย มีพลังกายและใจเต็มเปี่ยม",
            "future": "อนาคตอันใกล้มีเกณฑ์ประสบความสำเร็จอย่างสูง ได้รับชื่อเสียง โชคลาภ และข่าวดีที่รอคอย",
            "tone": "positive"
        },
        {
            "name": "The Moon 🌙",
            "past": "อดีตคุณเคยเผชิญกับความสับสน ความไม่แน่นอน หรือต้องตกอยู่ในสภาวะกดดันแอบแฝง",
            "present": "ปัจจุบันมีความกังวลใจหรือลังเลในทางเลือก แนะนำให้ใช้สติและอย่าเพิ่งรีบร้อนตัดสินใจ",
            "future": "อนาคตต้องระวังความเข้าใจผิด เอกสารสัญญา หรือสถานการณ์ที่ไม่ชัดเจน ควรตรวจสอบข้อมูลให้รอบคอบ",
            "tone": "caution"
        },
        {
            "name": "The Empress 👑",
            "past": "อดีตสร้างรากฐานไว้ดี มีความอุดมสมบูรณ์ ได้รับการดูแลช่วยเหลือจากผู้ใหญ่หรือครอบครัว",
            "present": "ปัจจุบันอยู่ในสภาวะมั่นคง การงานการเงินเจริญเติบโต ผลผลิตหรือสิ่งที่ลงทุนเริ่มออกดอกออกผล",
            "future": "อนาคตจะมีความสุขสมบูรณ์ มีโอกาสได้ผลตอบแทนก้อนใหญ่ หรือมีความสัมพันธ์ที่มั่นคงแน่นแฟ้น",
            "tone": "positive"
        },
        {
            "name": "The Fool 🎒",
            "past": "อดีตเคยผ่านการเริ่มต้นใหม่ การกล้าเสี่ยง หรือก้าวออกจากพื้นที่เซฟโซนเดิมๆ",
            "present": "ปัจจุบันพร้อมที่จะเปิดรับประสบการณ์ใหม่ มีอิสรภาพในการคิดและตัดสินใจ แต่างอาจขาดความระมัดระวังเล็กน้อย",
            "future": "อนาคตจะได้เริ่มต้นเส้นทางใหม่ การเดินทางใหม่ๆ หรือการลงทุนที่ท้าทายแต่ตื่นเต้น",
            "tone": "neutral"
        },
        {
            "name": "The Wheel of Fortune 🎡",
            "past": "อดีตเคยผ่านจุดเปลี่ยนสำคัญของชีวิต มีทั้งช่วงขึ้นและช่วงลงที่สอนประสบการณ์ให้คุณแข็งแกร่ง",
            "present": "ปัจจุบันจังหวะดวงชะตากำลังหมุนเปลี่ยนไปในทางที่ดีขึ้น จังหวะเวลาแห่งโชคลาภกำลังเข้ามา",
            "future": "อนาคตจะเกิดการเปลี่ยนแปลงครั้งใหญ่ที่เป็นบวก มีโอกาสใหม่เข้ามาอย่างไม่คาดฝัน",
            "tone": "positive"
        }
    ]
    
    if st.button("🔮 สุ่มเปิดไพ่ทำนาย"):
        drawn = random.sample(cards_db, 3)
        st.subheader(f"✨ ผลการทำนายไพ่ทาโรต์ของคุณ {user_info['name']}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="tarot-card">
                <h4 style="color: #6b21a8;">📜 อดีต (Past)</h4>
                <p><b>{drawn[0]['name']}</b></p>
                <p class="fortune-desc">{drawn[0]['past']}</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"""
            <div class="tarot-card">
                <h4 style="color: #6b21a8;">⏳ ปัจจุบัน (Present)</h4>
                <p><b>{drawn[1]['name']}</b></p>
                <p class="fortune-desc">{drawn[1]['present']}</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"""
            <div class="tarot-card">
                <h4 style="color: #6b21a8;">🚀 อนาคต (Future)</h4>
                <p><b>{drawn[2]['name']}</b></p>
                <p class="fortune-desc">{drawn[2]['future']}</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        
        tones = [drawn[0]['tone'], drawn[1]['tone'], drawn[2]['tone']]
        pos_count = tones.count('positive')
        
        if pos_count >= 2:
            summary_text = f"**สรุปภาพรวมดวงชะตา:** แนวโน้มดวงชะตาของคุณ {user_info['name']} อยู่ใน **เกณฑ์ดีเยี่ยมถึงรุ่งโรจน์** สิ่งที่เคยสร้างหรือเผชิญมาในอดีตกำลังส่งผลลัพธ์ที่เป็นบวกในปัจจุบัน และจะส่งผลให้เกิดความสำเร็จอย่างเป็นรูปธรรมในอนาคต ขอให้ลงมือทำด้วยความมั่นใจ"
        elif pos_count == 1:
            summary_text = f"**สรุปภาพรวมดวงชะตา:** ดวงชะตาของคุณ {user_info['name']} อยู่ใน **เกณฑ์ปานกลางทรงตัว** มีทั้งโอกาสและข้อควรระวังควบคู่กัน ปัจจุบันควรตั้งสติ รักษาสภาพคล่องทางการเงินและอารมณ์ แล้วอนาคตจะค่อยๆ ปรับเปลี่ยนไปในทิศทางที่ดีขึ้น"
        else:
            summary_text = f"**สรุปภาพรวมดวงชะตา:** เป็นช่วงเวลาที่คุณ {user_info['name']} **ต้องใช้ความรอบคอบและสติเป็นพิเศษ** อนาคตข้างหน้าอาจมีโจทย์หรือการเปลี่ยนแปลงเข้ามาทดสอบ แนะนำให้รอบคอบเรื่องเอกสาร สัญญา และดูแลสุขภาพกายใจให้ดี"
            
        st.markdown(f"""
        <div class="summary-box">
            <h4>💡 สรุปภาพรวม & คำแนะนำดวงชะตา</h4>
            <p>{summary_text}</p>
        </div>
        """, unsafe_allow_html=True)

# 8. ส่วนท้าย: คำคมพลังบวกประจำวัน
quotes = [
    "✨ 'ดวงชะตาเป็นเพียงเข็มทิศ การลงมือทำคือผู้กำหนดทิศทางชีวิตที่แท้จริง'",
    "🌟 'ทุกวันคือโอกาสใหม่ในการเริ่มต้นสร้างสิ่งดีๆ ให้ตัวเอง'",
    "💖 'ความเชื่อมั่นในตัวเอง คือคาถาเวทมนตร์ที่ดีที่สุด'"
]
st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)
