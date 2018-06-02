import cv2
import time
import datetime


# https://stackoverflow.com/questions/22116071/creating-time-lapse-images-in-python
def capture_image():
    image_time = time.time()
    cap = cv2.VideoCapture(1)
    image0 = cap.read()[1]
    time_str = datetime.datetime.fromtimestamp(image_time).strftime('%Y-%m-%d %H:%M:%S')
    write_text(image0, time_str)

    # compressão
    # https://stackoverflow.com/questions/12216333/opencv-imread-imwrite-increases-the-size-of-png
    # https://stackoverflow.com/questions/40027678/how-to-compress-png-file-with-opencv-in-python
    params = list()
    params.append(cv2.IMWRITE_PNG_COMPRESSION)
    params.append(8)

    cv2.imwrite(f"images/image-{time_str}.png", image0, params)

    return time_str

# https://stackoverflow.com/questions/16615662/how-to-write-text-on-a-image-in-windows-using-python-opencv2
def write_text(image, text):
    font                   = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    bottomLeftCornerOfText = (10,20)
    fontScale              = 0.5
    fontColor              = (255,255,255)
    lineType               = 1
    cv2.putText(image,
                text,
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType
    )

if __name__ == "__main__":
    endTime = time.time() + 0.5*60*60 # 1 hour from now
    while time.time() < endTime:
        photo_at = capture_image()
        print(f"Photo taken at {photo_at}")
        time.sleep(30)
