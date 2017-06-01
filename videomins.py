#!/usr/bin/env python3

import cv2


def get_video_mins(video):
    v = cv2.VideoCapture(video)
    fps = v.get(cv2.CAP_PROP_FPS)

    frame_count = v.get(cv2.CAP_PROP_FRAME_COUNT)

    return frame_count / fps

if __name__ == '__main__':
    import sys
    mins = int(get_video_mins(sys.argv[1]))
    print(str(mins) + 's')
