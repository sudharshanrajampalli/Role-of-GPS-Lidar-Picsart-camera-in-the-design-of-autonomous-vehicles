import cv2
import numpy as np
from tflite_support.task import processor
from gtts import gTTS
import os
import RPi.GPIO as GPIO 


# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

_MARGIN = 10  # pixels
_ROW_SIZE = 10  # pixels
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_TEXT_COLOR = (0, 0, 255)  # red

def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def CountFreq(li):
    freq = {}
    for items in li:
        freq[items] = li.count(items)
#    print(freq)
    a=str(freq)
    if cv2.waitKey(1) & 0xFF == ord('r'):
       speak(a)
GPIO.cleanup()
cv2.destroyAllWindows()


def visualize(
    image: np.ndarray,
    detection_result: processor.DetectionResult,
) -> np.ndarray:
  """Draws bounding boxes on the input image and return it.

  Args:
    image: The input RGB image.
    detection_result: The list of all "Detection" entities to be visualize.

  Returns:
    Image with bounding boxes.
  """
  list=[]
  for detection in detection_result.detections:
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, _TEXT_COLOR, 3)

    # Draw label and score
    category = detection.categories[0]
    category_name = category.category_name
    list.append(category_name)
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (_MARGIN + bbox.origin_x,
                     _MARGIN + _ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)
  CountFreq(list)
  return image
