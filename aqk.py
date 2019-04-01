#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:56:18 2019

@author: root
"""

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    a, frame = cap.read()
    cv2.imshow(frame)
cv2.destroyAllWindows()
cap.release()