#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

import cvui


def main():
    window_name = 'cvui-double-knob-trackbar'
    cvui.init(window_name)

    trackbar_value1 = [25.0]
    trackbar_value2 = [75.0]

    while True:
        cvuiframe = np.zeros((140, 460, 3), np.uint8)
        cvuiframe[:] = (49, 52, 49)

        cvui.trackbar2(cvuiframe, 30, 30, 400, trackbar_value1,
                       trackbar_value2, 0., 100.)

        cvui.text(cvuiframe, 50, 100,
                  'value1 : ' + "{0:.1f}".format(trackbar_value1[0]))
        cvui.text(cvuiframe, 160, 100,
                  'value2 : ' + "{0:.1f}".format(trackbar_value2[0]))

        cvui.update()

        cv.imshow(window_name, cvuiframe)
        key = cv.waitKey(50)
        if key == 27:  # ESC
            break


if __name__ == '__main__':
    main()
