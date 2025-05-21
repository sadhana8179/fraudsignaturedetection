import cv2
from skimage.metrics import structural_similarity as ssim

def compare_signatures(img1_path, img2_path):
    # Load images in grayscale
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        raise ValueError("One or both image paths are invalid or the image could not be read.")

    # Resize images to the same shape
    img1 = cv2.resize(img1, (300, 100))
    img2 = cv2.resize(img2, (300, 100))

    # Calculate SSIM
    similarity, _ = ssim(img1, img2, full=True)

    return similarity * 100  # Return percentage (0–100%)
