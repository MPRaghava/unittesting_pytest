import cv2
import pytesseract
from PIL import Image

# (Only for Windows users)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = 'blood_report.jpg'  # Change to your image path
image = cv2.imread(image_path)

# Convert to grayscale for better OCR
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Optional: Apply thresholding or denoising for better results
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Extract text using pytesseract
extracted_text = pytesseract.image_to_string(gray)

# Print the output
print("🔍 Extracted Text from Blood Report:\n")
print(extracted_text)
