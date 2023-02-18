import cv2
from datetime import datetime

# http://www.learningaboutelectronics.com/Articles/How-to-save-a-video-Python-OpenCV.php

class MyVideoCapture:
    def __init__(self, video_source=0):
        self.now = datetime.now()


        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        # self.four_cc = cv2.VideoWriter_fourcc(*'DIVX')
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # self.output_file = cv2.VideoWriter('./bin/history/{}.mp4'.format(self.now.strftime("%Y-%m-%d %H:%M:%S")), self.four_cc, 24, (self.width, self.height))
        # self.output_file = cv2.VideoWriter('./bin/history/a.mp4', self.four_cc, 20, (720, 480))

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # self.output_file.write(frame)
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
