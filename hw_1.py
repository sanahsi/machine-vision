import cv2

def zoom_image(image, zoom_factor):
    # محاسبه ابعاد جدید تصویر
    height, width = image.shape[:2]
    new_height = int(height * zoom_factor)
    new_width = int(width * zoom_factor)

    # تغییر اندازه تصویر
    zoomed_image = cv2.resize(image, (new_width, new_height))

    # برش تصویر برای حفظ ابعاد اصلی
    start_x = (new_width - width) // 2
    start_y = (new_height - height) // 2
    cropped_image = zoomed_image[start_y:start_y + height, start_x:start_x + width]

    return cropped_image

def main():
    # بارگذاری تصویر از ورودی
    image_path = input("لطفاً مسیر تصویر را وارد کنید: ")
    image = cv2.imread(image_path)

    if image is None:
        print("تصویر پیدا نشد. لطفاً مسیر صحیح را وارد کنید.")
        return

    # زوم کردن تصویر
    zoom_factor = float(input("لطفاً ضریب زوم را وارد کنید (مثلاً 1.5 برای زوم 50%): "))
    zoomed_image = zoom_image(image, zoom_factor)

    # نمایش تصویر زوم شده
    cv2.imshow("Zoomed Image", zoomed_image)
    
    # ذخیره تصویر زوم شده
    output_path = "zoomed_image.jpg"
    cv2.imwrite(output_path, zoomed_image)
    print(f"تصویر زوم شده در {output_path} ذخیره شد.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
