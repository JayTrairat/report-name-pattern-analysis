# --*-- coding: utf-8 --*--
import re

def main():
    stop_words = [
        "ต่อ", "และ", "ตาม", "จำแนก",
        "-", "จาก", "ถึง", "ที่", "มี",
        "ราย", "การ", "จำนวน", "ทั่ว",
        "ของ", "ข้อมูล", "จปฐ", "บาท",
        "ราย", "อยู่", "โดย", "เป็น",
        "ใน", "ทั้งสิ้น", "สำเร็จ", "อื่นๆ",
        "ได้รับ", "สะสม", "สังกัด", "เฉพาะ",
        "แห่ง", "เดือน", "ๆ", "หรือ", "กทม.",
        "ช่วง", "ป.", "ท", ".", "แบบ", "ช่วง",
        "พ.ศ.", "พ", "ศ", "ป.ป.ช.", "ฯ", "รอบ",
        "ปี", "ราชอาณาจักร", "(", ")", "ครัวเรือน",
        "มาก", "น้อย",
        "จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์",
        "จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา.",
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน",
        "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม",
        "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.",
        "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค.", "ณ", " "
    ]

    for index in range(1, 9):
        type = 'type_' + str(index)
        with open('assets/%s/original.txt' % type, 'r', encoding='utf8') as file_object:
            content = file_object.readlines()

        with open('assets/%s/removal_output.txt' % type , 'w', encoding='utf8') as file_object_output:
            content = [element.split('|') for element in content]
            for elements in content:
                filtered_elements = ([element for element in elements if element not in stop_words and re.match('^\D+', element)])
                joined_filtered_elements = '|'.join(filtered_elements)
                file_object_output.write(joined_filtered_elements)
            print(type + ' completed')


if __name__ == "__main__":
    main()
