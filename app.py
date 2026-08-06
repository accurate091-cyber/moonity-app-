import random
from datetime import datetime
import streamlit as st

# 1. ตั้งค่าหน้าตาของแอป
st.set_page_config(
    page_title="🔮 Moonity | คลินิกฮีลใจสไตล์สายมู",
    page_icon="🔮",
    layout="centered"
)

# เพิ่ม Meta Tags สำหรับแชร์ลิงก์
st.markdown("""
    <head>
        <meta property="og:title" content="🔮 Moonity | คลินิกฮีลใจสไตล์สายมู">
        <meta property="og:description" content="พื้นที่พักใจ ดูดวงรายวัน เซียมซี ไพ่ทาโรต์ ฮีลใจให้พลังบวก">
    </head>
""", unsafe_allow_html=True)

# 2. Custom CSS ตกแต่ง UI (ขยายขนาดวงกลมสีให้ใหญ่ขึ้น)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mitr:wght@300;400;500;600&display=swap');

    html, body, .stApp, p, h1, h2, h3, h4, h5, h6, input, select, textarea, label {
        font-family: 'Mitr', sans-serif !important;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f3e8ff 0%, #fce7f3 100%) !important;
    }

    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
        z-index: 999999 !important;
    }

    footer, #MainMenu, [data-testid="stDecoration"], .stAppViewerFooter {
        display: none !important;
    }

    .sidebar-logo-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #4c1d95;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .sidebar-concept {
        font-size: 0.82rem;
        color: #6b21a8;
        background: rgba(255, 255, 255, 0.6);
        padding: 8px 10px;
        border-radius: 8px;
        margin-bottom: 15px;
        line-height: 1.4;
        border-left: 3px solid #8b5cf6;
    }

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
        padding: 12px 14px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        text-align: center;
    }
    .lucky-title {
        font-size: 0.8rem;
        color: #64748b;
        margin-bottom: 6px;
    }
    .lucky-value {
        font-size: 1rem;
        font-weight: 600;
        color: #0f172a;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-top: 6px;
    }
    .color-circle-large {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: inline-block;
        border: 2px solid #ffffff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }

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

    .tarot-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #7c3aed;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        height: 100%;
    }

    .summary-box {
        background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
        border: 1px solid #d8b4fe;
        padding: 18px;
        border-radius: 12px;
        color: #3b0764;
        margin-top: 18px;
    }

    .quote-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
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

# 3. โลโก้และแนวคิดใน Sidebar
st.sidebar.markdown('<div class="sidebar-logo-title">🔮 Moonity</div>', unsafe_allow_html=True)
st.sidebar.markdown("""
<div class="sidebar-concept">
    ✨ <b>แนวความคิด:</b> โชคชะตาคือเส้นทางของเราเอง ตัวเราต่างหากที่กำหนดอนาคต
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")

# 4. ระบบบันทึกข้อมูลดวงชะตา (Session State)
st.sidebar.header("✨ บันทึกต้นกำเนิดดวงดาว")

if "user_data" not in st.session_state:
    st.session_state.user_data = {
        "name": "ดวงดี",
        "birth_date": "01/01/2000",
        "birth_time": "00:00 น.",
        "mode": "full"
    }

profile_mode = st.sidebar.radio("เลือกวิธีใช้งาน:", ["📝 บันทึกข้อมูลส่วนตัว", "👤 โหมดบุคคลทั่วไป"])

if profile_mode == "📝 บันทึกข้อมูลส่วนตัว":
    input_name = st.sidebar.text_input("ชื่อ/ชื่อเล่น:", st.session_state.user_data["name"])
    input_birth_date = st.sidebar.date_input("วันเกิด:", datetime(2000, 1, 1))
    input_birth_time = st.sidebar.time_input("เวลาเกิด:", datetime.strptime("00:00", "%H:%M").time())
    
    if st.sidebar.button("💾 บันทึกต้นกำเนิดดวงชะตา"):
        st.session_state.user_data = {
            "name": input_name.strip(),
            "birth_date": input_birth_date.strftime("%d/%m/%Y"),
            "birth_time": input_birth_time.strftime("%H:%M") + " น.",
            "mode": "full"
        }
        st.sidebar.success("บันทึกต้นกำเนิดดวงชะตาเรียบร้อย! ✨")

    user_info = st.session_state.user_data
else:
    user_info = {"name": "ผู้มาเยือน", "birth_date": "ไม่ได้ระบุ", "birth_time": "ไม่ได้ระบุ", "mode": "guest"}

st.sidebar.markdown("---")
st.sidebar.subheader("📌 เลือกโหมดคำทำนาย")
menu = st.sidebar.radio("เลือกเส้นทางดวงดาว", ["✨ ดวงรายวันเฉพาะบุคคล", "⛩️ เซียมซีออนไลน์", "🃏 ไพ่ทาโรต์ 3 ใบ"])

# 5. แสดงกล่องข้อมูลดวงชะตาด้านบน
if user_info['mode'] == 'full':
    profile_html = f"""
    <div class="user-profile-box">
        <div class="user-profile-title">✨ ข้อมูลดวงชะตา: {user_info['name']}</div>
        <div class="user-profile-detail">
            📅 <b>วันเกิด:</b> {user_info['birth_date']} &nbsp;|&nbsp; ⏰ <b>เวลาเกิด:</b> {user_info['birth_time']}
        </div>
    </div>
    """
else:
    profile_html = f"""
    <div class="user-profile-box">
        <div class="user-profile-title">✨ ข้อมูลดวงชะตา: {user_info['name']}</div>
        <div class="user-profile-detail">🎲 โหมดบุคคลทั่วไป (เลือกโหมดบันทึกข้อมูลส่วนตัวด้านข้างเพื่อผูกดวงชะตา)</div>
    </div>
    """

st.markdown(profile_html, unsafe_allow_html=True)

# 6. ระบบสุ่มเฉดสีจากโค้ด Hex แบบไดนามิก (ซ่อนโค้ด แสดงเฉพาะวงกลมสีใหญ่ๆ)
today_seed = int(datetime.now().strftime("%Y%m%d"))
random.seed(today_seed)

def get_random_hex():
    r = random.randint(40, 220)
    g = random.randint(40, 220)
    b = random.randint(40, 220)
    return f"#{r:02x}{g:02x}{b:02x}", (r, g, b)

def color_distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])

hex1, rgb1 = get_random_hex()
hex2, rgb2 = get_random_hex()
while color_distance(rgb1, rgb2) < 80:
    hex2, rgb2 = get_random_hex()

hex_forbidden, rgb_forbidden = get_random_hex()
while color_distance(rgb_forbidden, rgb1) < 100 or color_distance(rgb_forbidden, rgb2) < 100:
    hex_forbidden, rgb_forbidden = get_random_hex()

rand_nums = sorted(random.sample(range(10, 99), 3))
lucky_number_text = f"{rand_nums[0]}, {rand_nums[1]}, {rand_nums[2]}"
directions_list = ["ทิศตะวันออกเฉียงเหนือ", "ทิศเหนือ", "ทิศตะวันตก", "ทิศใต้", "ทิศตะวันออก", "ทิศตะวันตกเฉียงใต้", "ทิศตะวันออกเฉียงใต้"]
lucky_direction_text = random.choice(directions_list)

random.seed(None)

lucky_widget = f"""
<div class="daily-lucky-container">
    <div class="lucky-card">
        <div class="lucky-title">🎨 สีมงคลวันนี้</div>
        <div class="lucky-value">
            <span class="color-circle-large" style="background-color: {hex1};"></span>
            <span class="color-circle-large" style="background-color: {hex2};"></span>
        </div>
    </div>
    <div class="lucky-card">
        <div class="lucky-title">⛔ สีต้องห้าม</div>
        <div class="lucky-value">
            <span class="color-circle-large" style="background-color: {hex_forbidden};"></span>
        </div>
    </div>
    <div class="lucky-card">
        <div class="lucky-title">🔢 เลขนำโชค</div>
        <div class="lucky-value" style="font-size: 0.95rem; margin-top: 10px;">{lucky_number_text}</div>
    </div>
    <div class="lucky-card">
        <div class="lucky-title">🧭 ทิศมงคล</div>
        <div class="lucky-value" style="font-size: 0.85rem; margin-top: 10px;">{lucky_direction_text}</div>
    </div>
</div>
"""
st.markdown(lucky_widget, unsafe_allow_html=True)

# 7. ฐานข้อมูลคำทำนาย 100 โควต
work_pool = [
    "การงานราบรื่น มีผู้ใหญ่คอยซัพพอร์ตและสนับสนุนผลงานของคุณอย่างเต็มที่",
    "ไอเดียสร้างสรรค์พุ่งกระฉูด เหมาะสำหรับการเริ่มโปรเจกต์ใหม่หรือนำเสนองาน",
    "ระวังงานด่วนเข้ามาพร้อมกัน ควรจัดลำดับความสำคัญและตั้งสติให้ดี",
    "มีเกณฑ์ได้รับข่าวดีเรื่องงาน เลื่อนขั้น เลื่อนตำแหน่ง หรือเพิ่มเงินเดือน",
    "การเจรจาต่อรองทางธุรกิจหรือการสมัครงานวันนี้มีโอกาสสำเร็จสูงมาก",
    "ความตั้งใจและผลงานที่คุณทุ่มเทมานานกำลังจะส่งผลิดอกออกผลในเร็วๆ นี้",
    "ระวังความขัดแย้งเล็กๆ น้อยๆ กับเพื่อนร่วมงาน ใช้ความใจเย็นสยบปัญหา",
    "งานราบรื่นผ่านฉลุย ไม่มีอุปสรรคใหญ่มารบกวนจิตใจ",
    "วันนี้เหมาะกับการเคลียร์เอกสารและสะสางงานคั่งค้างให้หมดจด",
    "จะมีคนยื่นมือเข้ามาช่วยเหลือในยามที่คุณเจอทางตันเรื่องงาน",
] + [f"พลังงานด้านการงานมั่นคง โดดเด่น และก้าวหน้าในแบบของคุณ (รหัสลับ {i})" for i in range(11, 101)]

money_pool = [
    "การเงินคล่องตัว มีโชคลาภเข้ามาจากช่องทางใหม่ๆ ที่คาดไม่ถึง",
    "มีเกณฑ์ได้รับเงินก้อนพิเศษ หรือผลตอบแทนจากสิ่งที่เคยลงทุนไป",
    "ระวังรายจ่ายกะทันหันเกี่ยวกับสุขภาพหรือของใช้ชำรุดเสียหาย",
    "การบริหารจัดการเงินช่วงนี้ยอดเยี่ยม มีเงินเก็บเหลือเก็บเพิ่มขึ้น",
    "มีโชคลาภจากการเดินทางหรือการเสี่ยงโชคเล็กๆ น้อยๆ พอหอมปากหอมคอ",
    "ระวังคนยืมเงินหรือการค้ำประกันที่จะนำความเดือดร้อนมาให้",
    "การเงินเติบโตมั่นคง สภาพคล่องดีเยี่ยม ไม่มีเรื่องให้ต้องกังวล",
    "มีเกณฑ์เสียเงินไปกับการช้อปปิ้งเพื่อฮีลใจตัวเอง ควบคุมงบให้ดี",
    "การลงทุนมีความเสี่ยง ควรศึกษาข้อมูลให้รอบคอบก่อนตัดสินใจ",
    "เงินทองไหลมาเทมา ค้าขายคล่องตัว กำไรดีเกินคาด",
] + [f"กระแสการเงินไหลลื่น มั่งคั่ง และมีความมั่นคงในระยะยาว (รหัสลับ {i})" for i in range(11, 101)]

love_pool = [
    "คนโสดมีเกณฑ์พบมิตรใหม่ คนมีคู่เสน่ห์แรงน่าหลงใหลเป็นพิเศษ",
    "บรรยากาศความรักอบอุ่น เข้าใจและดูแลเอาใจใส่กันดีขึ้น",
    "ควรระวังเรื่องอารมณ์และคำพูดรุนแรงเล็กๆ น้อยๆ กับคนรัก",
    "คนโสดมีโอกาสเจอคนที่ใช่จากการทำงานหรือเพื่อนแนะนำ",
    "คนมีคู่มีความสุข ความสัมพันธ์แน่นแฟ้นเข้าใจกันลึกซึ้ง",
    "ระวังเรื่องมือที่สามหรือความหึงหวงโดยไม่มีเหตุผล",
    "ความรักราบรื่น หวานชื่น มีเวลาให้กันและกันมากขึ้น",
    "คนโสดเสน่ห์แพรวพราว มีคนแอบส่งขนมจีบและให้ความสนใจ",
    "มีการพูดคุยปรับความเข้าใจกัน ปัญหาหัวใจคลี่คลายลงด้วยดี",
    "ความสัมพันธ์ดำเนินไปอย่างมั่นคง อบอุ่น และปลอดภัยทางใจ",
] + [f"พลังงานความรักอบอุ่น สมหวัง และเข้าใจกันอย่างลึกซึ้ง (รหัสลับ {i})" for i in range(11, 101)]

# 8. เนื้อหาแต่ละโหมด
if menu == "✨ ดวงรายวันเฉพาะบุคคล":
    st.subheader(f"✨ คำทำนายประจำวันสำหรับ: {user_info['name']}")
    
    if st.button("🔮 รับคำทำนาย"):
        selected_work = random.choice(work_pool)
        selected_money = random.choice(money_pool)
        selected_love = random.choice(love_pool)
        
        st.success(f"🔮 **คำทำนายผูกดวงชะตาเรียบร้อยแล้ว**")
        
        st.markdown(f"""
        <div class="fortune-card">
            <div class="fortune-title">💼 ด้านการงานและการเรียน</div>
            <div class="fortune-desc">{selected_work}</div>
        </div>
        <div class="fortune-card" style="border-left-color: #10b981;">
            <div class="fortune-title">💰 ด้านการเงินและโชคลาภ</div>
            <div class="fortune-desc">{selected_money}</div>
        </div>
        <div class="fortune-card" style="border-left-color: #f43f5e;">
            <div class="fortune-title">💖 ด้านความรักและความสัมพันธ์</div>
            <div class="fortune-desc">{selected_love}</div>
        </div>
        """, unsafe_allow_html=True)

elif menu == "⛩️ เซียมซีออนไลน์":
    st.subheader("⛩️ เขย่าเซียมซีตั้งจิตอธิษฐาน")
    st.caption("ตั้งจิตให้นิ่ง นึกถึงสิ่งที่อยากรู้ แล้วกดเขย่ากระบอกเซียมซี")
    
    if st.button("🎯 รับคำทำนาย"):
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
    st.caption("ตั้งจิตอธิษฐานถึงเรื่องที่ต้องการคำตอบ แล้วกดปุ่มรับคำทำนาย")
    
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
            "present": "ปัจจุบันพร้อมที่จะเปิดรับประสบการณ์ใหม่ มีอิสรภาพในการคิดและตัดสินใจ แต่วาจาอาจต้องระวังเล็กน้อย",
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
    
    if st.button("🔮 รับคำทำนาย"):
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
        
        tags = [drawn[0]['tone'], drawn[1]['tone'], drawn[2]['tone']]
        pos_count = tags.count('positive')
        
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

# 9. คำคมพลังบวกประจำวัน
quotes = [
    "✨ 'ทุกวันคือโอกาสใหม่ในการเริ่มต้นสร้างสิ่งดีๆ ให้ตัวเอง'",
    "🌟 'ดวงชะตาเป็นเพียงเข็มทิศ การลงมือทำคือผู้กำหนดทิศทางชีวิตที่แท้จริง'",
    "💖 'ความเชื่อมั่นในตัวเอง คือคาถาเวทมนตร์ที่ดีที่สุด'",
    "🌿 'ไม่มีคำว่าสายเกินไปสำหรับการเริ่มต้นใหม่ในแบบที่เราต้องการ'",
    "☀️ 'ปล่อยวางเรื่องที่ควบคุมไม่ได้ แล้วโฟกัสสิ่งที่เราสร้างได้ในวันนี้'"
]
st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)
