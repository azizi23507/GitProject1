"""
Database Schema Diagram Generator
==================================
Edit this file to customize your database diagram!

Requirements:
- Python 3
- PIL/Pillow library: pip install pillow

Usage:
python create_database_diagram.py
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ============================================
# CONFIGURATION - EDIT THESE!
# ============================================

# Image size
IMAGE_WIDTH = 1800
IMAGE_HEIGHT = 1400
BACKGROUND_COLOR = 'white'

# Colors (RGB format)
PRIMARY_KEY_COLOR = (255, 215, 0)  # Gold
FOREIGN_KEY_COLOR = (135, 206, 250)  # Light blue
TABLE_HEADER_COLOR = (68, 114, 196)  # Blue
TABLE_BODY_COLOR = (240, 240, 240)  # Light gray
BORDER_COLOR = (0, 0, 0)  # Black
TEXT_COLOR = (0, 0, 0)  # Black

# Table dimensions
TABLE_WIDTH = 450
ROW_HEIGHT = 35
HEADER_HEIGHT = 50

# ============================================
# DEFINE YOUR TABLES HERE
# ============================================

# Table 1: doctors
doctors_table = {
    'name': 'doctors',
    'position': (50, 150),
    'columns': [
        {'name': 'doctor_id', 'type': 'INT', 'is_pk': True, 'is_fk': False},
        {'name': 'first_name', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'last_name', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'email', 'type': 'VARCHAR(100)', 'is_pk': False, 'is_fk': False},
        {'name': 'username', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'password', 'type': 'VARCHAR(255)', 'is_pk': False, 'is_fk': False},
        {'name': 'phone', 'type': 'VARCHAR(15)', 'is_pk': False, 'is_fk': False},
        {'name': 'license_number', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'specialization', 'type': 'VARCHAR(100)', 'is_pk': False, 'is_fk': False},
        {'name': 'profile_picture', 'type': 'VARCHAR(255)', 'is_pk': False, 'is_fk': False},
        {'name': 'is_verified', 'type': 'TINYINT(1)', 'is_pk': False, 'is_fk': False},
        {'name': 'created_at', 'type': 'TIMESTAMP', 'is_pk': False, 'is_fk': False},
    ]
}

# Table 2: patients
patients_table = {
    'name': 'patients',
    'position': (1300, 150),
    'columns': [
        {'name': 'patient_id', 'type': 'INT', 'is_pk': True, 'is_fk': False},
        {'name': 'doctor_id', 'type': 'INT', 'is_pk': False, 'is_fk': True},
        {'name': 'first_name', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'last_name', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'date_of_birth', 'type': 'DATE', 'is_pk': False, 'is_fk': False},
        {'name': 'gender', 'type': "ENUM('M','F')", 'is_pk': False, 'is_fk': False},
        {'name': 'blood_group', 'type': 'VARCHAR(5)', 'is_pk': False, 'is_fk': False},
        {'name': 'phone', 'type': 'VARCHAR(15)', 'is_pk': False, 'is_fk': False},
        {'name': 'email', 'type': 'VARCHAR(100)', 'is_pk': False, 'is_fk': False},
        {'name': 'address', 'type': 'TEXT', 'is_pk': False, 'is_fk': False},
        {'name': 'emergency_contact', 'type': 'VARCHAR(100)', 'is_pk': False, 'is_fk': False},
        {'name': 'emergency_phone', 'type': 'VARCHAR(15)', 'is_pk': False, 'is_fk': False},
        {'name': 'profile_picture', 'type': 'VARCHAR(255)', 'is_pk': False, 'is_fk': False},
        {'name': 'created_at', 'type': 'TIMESTAMP', 'is_pk': False, 'is_fk': False},
    ]
}

# Table 3: ehr_records
ehr_table = {
    'name': 'ehr_records',
    'position': (650, 700),
    'columns': [
        {'name': 'ehr_id', 'type': 'INT', 'is_pk': True, 'is_fk': False},
        {'name': 'patient_id', 'type': 'INT', 'is_pk': False, 'is_fk': True},
        {'name': 'doctor_id', 'type': 'INT', 'is_pk': False, 'is_fk': True},
        {'name': 'height', 'type': 'DECIMAL(5,2)', 'is_pk': False, 'is_fk': False},
        {'name': 'weight', 'type': 'DECIMAL(5,2)', 'is_pk': False, 'is_fk': False},
        {'name': 'bmi', 'type': 'DECIMAL(5,2)', 'is_pk': False, 'is_fk': False},
        {'name': 'blood_pressure', 'type': 'VARCHAR(20)', 'is_pk': False, 'is_fk': False},
        {'name': 'heart_rate', 'type': 'INT', 'is_pk': False, 'is_fk': False},
        {'name': 'temperature', 'type': 'DECIMAL(4,2)', 'is_pk': False, 'is_fk': False},
        {'name': 'medical_history', 'type': 'TEXT', 'is_pk': False, 'is_fk': False},
        {'name': 'current_medications', 'type': 'TEXT', 'is_pk': False, 'is_fk': False},
        {'name': 'allergies', 'type': 'TEXT', 'is_pk': False, 'is_fk': False},
        {'name': 'immunization_status', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'lab_results', 'type': 'TEXT', 'is_pk': False, 'is_fk': False},
        {'name': 'diagnosis', 'type': 'TEXT', 'is_pk': False, 'is_fk': False},
        {'name': 'treatment_plan', 'type': 'TEXT', 'is_pk': False, 'is_fk': False},
        {'name': 'xray_image', 'type': 'VARCHAR(255)', 'is_pk': False, 'is_fk': False},
        {'name': 'visit_date', 'type': 'DATE', 'is_pk': False, 'is_fk': False},
        {'name': 'created_at', 'type': 'TIMESTAMP', 'is_pk': False, 'is_fk': False},
    ]
}

# Table 4: login_attempts
login_table = {
    'name': 'login_attempts',
    'position': (50, 700),
    'columns': [
        {'name': 'id', 'type': 'INT', 'is_pk': True, 'is_fk': False},
        {'name': 'username', 'type': 'VARCHAR(50)', 'is_pk': False, 'is_fk': False},
        {'name': 'ip_address', 'type': 'VARCHAR(45)', 'is_pk': False, 'is_fk': False},
        {'name': 'success', 'type': 'TINYINT(1)', 'is_pk': False, 'is_fk': False},
        {'name': 'attempt_time', 'type': 'TIMESTAMP', 'is_pk': False, 'is_fk': False},
    ]
}

ALL_TABLES = [doctors_table, patients_table, ehr_table, login_table]

# ============================================
# DEFINE RELATIONSHIPS (fixed logic)
# ============================================

RELATIONSHIPS = [
    # doctors → patients (one doctor has many patients)
    {
        'from_table': doctors_table,
        'to_table': patients_table,
        'label': 'has many',
        'type': 'one-to-many'
    },
    # doctors → ehr_records (one doctor creates many records)
    {
        'from_table': doctors_table,
        'to_table': ehr_table,
        'label': 'creates',
        'type': 'one-to-many'
    },
    # patients → ehr_records (one patient has many records)
    {
        'from_table': patients_table,
        'to_table': ehr_table,
        'label': 'has many',
        'type': 'one-to-many'
    },
]

# ============================================
# FUNCTIONS
# ============================================

def draw_table(draw, x, y, table_name, columns, fonts):
    title_font, text_font, small_font = fonts
    total_height = HEADER_HEIGHT + (len(columns) * ROW_HEIGHT)

    # Shadow
    draw.rectangle([x + 5, y + 5, x + TABLE_WIDTH + 5, y + total_height + 5], fill=(200, 200, 200))

    # Border
    draw.rectangle([x, y, x + TABLE_WIDTH, y + total_height], outline=BORDER_COLOR, width=3)

    # Header
    draw.rectangle([x, y, x + TABLE_WIDTH, y + HEADER_HEIGHT],
                   fill=TABLE_HEADER_COLOR, outline=BORDER_COLOR, width=3)
    draw.text((x + 15, y + 15), table_name, fill='white', font=title_font)

    # Columns
    current_y = y + HEADER_HEIGHT
    for col in columns:
        bg_color = PRIMARY_KEY_COLOR if col['is_pk'] else FOREIGN_KEY_COLOR if col['is_fk'] else TABLE_BODY_COLOR
        draw.rectangle([x, current_y, x + TABLE_WIDTH, current_y + ROW_HEIGHT],
                       fill=bg_color, outline=BORDER_COLOR, width=1)

        col_text = col['name']
        if col['is_pk']:
            col_text = "🔑 " + col_text + " (PK)"
        elif col['is_fk']:
            col_text = "🔗 " + col_text + " (FK)"

        draw.text((x + 10, current_y + 8), col_text, fill=TEXT_COLOR, font=text_font)
        draw.text((x + TABLE_WIDTH - 150, current_y + 8), col['type'], fill=TEXT_COLOR, font=small_font)
        current_y += ROW_HEIGHT

    return total_height


def draw_relationship(draw, from_table, to_table, label, small_font):
    # Draw line from center bottom of from_table to center top of to_table
    x1 = from_table['position'][0] + TABLE_WIDTH // 2
    y1 = from_table['position'][1] + HEADER_HEIGHT + len(from_table['columns']) * ROW_HEIGHT
    x2 = to_table['position'][0] + TABLE_WIDTH // 2
    y2 = to_table['position'][1]

    # Line
    draw.line([(x1, y1), (x2, y2)], fill=BORDER_COLOR, width=3)
    # Arrow head
    draw.polygon([(x2, y2), (x2 - 10, y2 - 15), (x2 + 10, y2 - 15)], fill=BORDER_COLOR)

    # Label
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2
    bbox = draw.textbbox((0, 0), label, font=small_font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.rectangle([mid_x - w // 2 - 5, mid_y - h // 2 - 2, mid_x + w // 2 + 5, mid_y + h // 2 + 2],
                   fill='white', outline=BORDER_COLOR)
    draw.text((mid_x - w // 2, mid_y - h // 2), label, fill=BORDER_COLOR, font=small_font)


def create_diagram():
    img = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts cross-platform
    try:
        if os.name == 'nt':  # Windows
            title_font = ImageFont.truetype("arialbd.ttf", 36)
            heading_font = ImageFont.truetype("arialbd.ttf", 22)
            text_font = ImageFont.truetype("arial.ttf", 16)
            small_font = ImageFont.truetype("arial.ttf", 14)
        else:  # Linux/Mac
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
            heading_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
            text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
            small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        title_font = heading_font = text_font = small_font = ImageFont.load_default()

    # Title
    draw.text((550, 30), "EHR Database Schema Diagram", fill=TABLE_HEADER_COLOR, font=title_font)
    draw.text((650, 80), "ehr_system Database", fill=TEXT_COLOR, font=heading_font)

    # Draw tables
    for table in ALL_TABLES:
        draw_table(draw, table['position'][0], table['position'][1], table['name'], table['columns'],
                   (heading_font, text_font, small_font))

    # Draw relationships
    for rel in RELATIONSHIPS:
        draw_relationship(draw, rel['from_table'], rel['to_table'], rel['label'], small_font)

    # Legend
    legend_y = 1250
    legend_x = 50
    draw.text((legend_x, legend_y), "LEGEND:", fill=TEXT_COLOR, font=heading_font)
    draw.rectangle([legend_x, legend_y + 40, legend_x + 200, legend_y + 75],
                   fill=PRIMARY_KEY_COLOR, outline=BORDER_COLOR, width=2)
    draw.text((legend_x + 10, legend_y + 47), "🔑 Primary Key (PK)", fill=TEXT_COLOR, font=text_font)
    draw.rectangle([legend_x + 250, legend_y + 40, legend_x + 450, legend_y + 75],
                   fill=FOREIGN_KEY_COLOR, outline=BORDER_COLOR, width=2)
    draw.text((legend_x + 260, legend_y + 47), "🔗 Foreign Key (FK)", fill=TEXT_COLOR, font=text_font)
    draw.rectangle([legend_x + 500, legend_y + 40, legend_x + 700, legend_y + 75],
                   fill=TABLE_BODY_COLOR, outline=BORDER_COLOR, width=2)
    draw.text((legend_x + 510, legend_y + 47), "Regular Field", fill=TEXT_COLOR, font=text_font)

    # Database info
    info_x = 1200
    draw.text((info_x, legend_y), "DATABASE INFO:", fill=TEXT_COLOR, font=heading_font)
    draw.text((info_x, legend_y + 40), "Database Name: ehr_system", fill=TEXT_COLOR, font=text_font)
    draw.text((info_x, legend_y + 70), "Total Tables: 4", fill=TEXT_COLOR, font=text_font)
    draw.text((info_x, legend_y + 100), "Engine: InnoDB", fill=TEXT_COLOR, font=text_font)

    # Save
    img.save('database_schema_diagram.png')
    print("✅ Database schema diagram created: database_schema_diagram.png")


if __name__ == '__main__':
    create_diagram()
    print("\n📝 HOW TO EDIT:")
    print("1. Edit table definitions in the 'DEFINE YOUR TABLES HERE' section")
    print("2. Adjust positions by changing (x, y) coordinates")
    print("3. Add/remove columns in the 'columns' list")
    print("4. Edit relationships in the 'DEFINE RELATIONSHIPS' section")
    print("5. Change colors in the 'CONFIGURATION' section")
    print("6. Run: python create_database_diagram.py")
