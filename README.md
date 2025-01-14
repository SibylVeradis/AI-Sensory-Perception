# AI-Vision-Preprocessing

# 🎨 RGBL Image Processing

This is a Python script for processing images by extracting:
- `R` (Red Channel)
- `G` (Green Channel)
- `B` (Blue Channel)
- `L` (Luminance - Grayscale)

It was originally designed for visual perception experiments, such as analyzing the **Hermann Grid illusion**.

## 📌 Features
✅ Convert images into separate RGB and Luminance matrices  
✅ Support for **Hermann Grid Illusions**  
✅ Compatible with any image format supported by OpenCV  

---

## 🚀 How to Use
### **1️⃣ Install Dependencies**
Make sure you have Python installed, then install required libraries:
```bash
pip install -r requirements.tx


2️⃣ Run the Script
bash
複製程式碼
python RGBL.py
3️⃣ Customize Your Image
Modify the image_path variable in RGBL.py to process your own image:

python
複製程式碼
image_path = "test/my_image.jpg"
Ensure the image is inside the test/ directory.

🖼 Example: Hermann Grid Illusion
This script can be used to analyze visual illusions like the Hermann Grid.
You can try using different illusions and observe how they are processed.



📊 Future Improvements
✅ Add support for auditory frequency analysis
✅ Expand to multi-dimensional matrix processing
✅ Improve visualization with Matplotlib
