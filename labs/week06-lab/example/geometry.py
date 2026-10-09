def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * height * base
    print(f"Triangle with height {height} and width {base}")
    print(f"Area = {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

# -----------------------------------------------------
# -----------------------------------------------------

# เขียน function แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
# THB <-> USD .. 1 USD = 32 THB

# โดยใช้ชื่อและการใช้งาน
# function convert_country(100, "USD")

# แสดงผลออกทางหน้าจอ
# 100 THB = 3.3 USD

# และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

# -----------------------------------------------------

def convert_currency(a, b):
    if b == "USD":
        print(f"{a} THB = {a / 32.0:.1f} USD")
    else:
        print(f"{a} USD = {a * 32.0:.1f} THB")

convert_currency(100, "USD")
convert_currency(100, "THB")
