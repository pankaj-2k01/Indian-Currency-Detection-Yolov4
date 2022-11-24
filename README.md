Indian-Currency-Detection-Yolov4 For Visually Impaired Peoples
=============
I have built the Indian Currency detection using Yolov4.
I have created the Custom Indian Currency Dataset and Trained the Yolov4 on those images.
`Multiple_image` is the Final Dataset which I have used.
`Training.ipyb` is the Notebook file used for the Training and it is done in `Google Colab`
Weights are then generated and used as per the use case.
Image gets Predicted on the basis of the Training and correspoding auido of the Currency gets Played in the background.


Dataset Description
-------

Please Carefully read the Folllowing Instructions
* Dataset consist of 7 classes i,e 10, 20, 50, 100, 200, 500, 2000
* Each class has 450 images both Processed image.
* Those images get labelled with the help of Python `process.py`, `convert.py` and `bbox.py`
* Generated Labels then gets converted into the Yolo Format and trained it using Google Colab
* Due to lack of the resources Yolov4 is only gets trained for 100000 iterations only.
* Then I have create the `test.py` to testing of the YOLOv4 Model.

Testing
-----------

```
pip install -r requirement.txt
```

Paste the image which you have to test in the Testing folder and Change the name of the Testing image in the `testing.py`

```
python testing.py
```

Predicted Image gets saved and Output gets shows in the Terminal.

Usage
-----

Paste the Testing Image in Testing folder and change the Name of the Image:

```python
change the name of the file  img=cv2.imread('Testing/10.jpg')
```

After Running the Code You can see the Predicted Image i,e `predicted.png` and Based on the currency in the Image `audio` gets played in the Background. 
Example :

```
Predicted Note is  10
Playing 10 Note MP3
```

Screenshots
-----------
Change the Name of the Test File You want to test and Run it.
![Sc](https://i.imgur.com/B8RP4vg.png)

Output Generated

![Sc](https://i.imgur.com/usgkAL2.png)

Demo Video
-----------
[Demo Video](https://imgur.com/VnzVFm2)




