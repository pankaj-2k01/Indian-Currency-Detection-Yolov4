import cv2
import numpy as np 
import argparse
import time
import collections
from playsound import playsound
import simpleaudio as sa
from gtts import gTTS 
import os

def load_yolo():
	net = cv2.dnn.readNet("darknet/yolov4-custom_best.weights", "darknet/cfg/yolov4-custom.cfg")
	classes = []
	with open("darknet/data/piford.names", "r") as f:
		classes = [line.strip() for line in f.readlines()] 
	
	output_layers = [layer_name for layer_name in net.getUnconnectedOutLayersNames()]
	colors = np.random.uniform(0, 255, size=(len(classes), 3))
	return net, classes, colors, output_layers

def detect_objects(img, net, outputLayers):			
	blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(832, 832), mean=(0, 0, 0), swapRB=True, crop=False)
	net.setInput(blob)
	outputs = net.forward(outputLayers)
	return blob, outputs

def get_box_dimensions(outputs, height, width):
	boxes = []
	confs = []
	class_ids = []
	for output in outputs:
		for detect in output:
			scores = detect[5:]
			#print(scores)
			class_id = np.argmax(scores)
			conf = scores[class_id]
			if conf > 0.3:
				center_x = int(detect[0] * width)
				center_y = int(detect[1] * height)
				w = int(detect[2] * width)
				h = int(detect[3] * height)
				x = int(center_x - w/2)
				y = int(center_y - h / 2)
				boxes.append([x, y, w, h])
				confs.append(float(conf))
				class_ids.append(class_id)
	return boxes, confs, class_ids

def draw_labels(boxes, confs, colors, class_ids, classes, img): 
	indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
	font = cv2.FONT_HERSHEY_PLAIN
	for i in range(len(boxes)):
		if i in indexes:
			x, y, w, h = boxes[i]
			label = str(classes[class_ids[i]])
			#color = colors[i]
			color = (255,0,0)
			if label=="ifrsuit":
				color = (0,255,0)
			else:
				color = (0,0,255)
			cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
			cv2.putText(img, label, (x, y - 5), font, 2, color, 2)    
	return img

def get_text(img):
	model, classes, colors, output_layers = load_yolo()
	height, width,channels = img.shape
	blob, outputs = detect_objects(img, model, output_layers)
	boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
	finalImg = draw_labels(boxes, confs, colors, class_ids, classes, img)
	# print(class_ids)
	cv2.imwrite("predicted.png",finalImg)
	return class_ids
	
def gts(cls):
    mytext=""
    if cls=="10":
        mytext="10 Rupee Note"
        print('Playing 10 Note MP3')
    if cls=="20":
        mytext="20 Rupee Note"
        print('Playing 20 Note MP3')
    if cls=="50":
        mytext="50 Rupee Note"
        print('Playing 50 Note MP3')
    if cls=="100":
        mytext="100 Rupee Note"
        print('Playing 100 Note MP3')
    if cls=="200":
        mytext="200 Rupee Note"
        print('Playing 200 Note MP3')
    if cls=="500":
        mytext="500 Rupee Note"
        print('Playing 500 Note MP3')
    if cls=="2000":
        mytext="2000 Rupee Note"
        print('Playing 2000 Note MP3')

    if os.path.exists("audio/predicted.mp3"):
        os.remove("audio/predicted.mp3")
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save("audio/predicted.mp3")
    playsound('audio/predicted.mp3')
    os.remove("audio/predicted.mp3")

predicted_cls={0:10, 1:20, 2:50, 3:100, 4:200, 5:500, 6:2000}
hash_map={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

if __name__=="__main__":

        img=cv2.imread('Testing/10.jpg')
        class_ids=get_text(img)
        for key in class_ids:
                hash_map[key]+=1
        Keymax = max(zip(hash_map.values(), hash_map.keys()))[1]
        # print(Keymax)
        print("Predicted Note is ",predicted_cls[Keymax])
        gts(str(predicted_cls[Keymax]))