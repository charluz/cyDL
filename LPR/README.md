# A Study of License Plate Recognition

## How Does It Work?

具體步驟如下：
1. 灰度轉換：將彩色圖片轉換為灰度圖像，常見的R=G=B=像素平均值。
2. 高斯平滑和中值濾波：去除噪聲。
3. Sobel算子：提取圖像邊緣輪廓，X方向和Y方向平方和開根號。
4. 二值化處理：圖像轉換為黑白兩色，通常像素大於127設置為255，小於設置為0。
5. 膨脹和細化：放大圖像輪廓，轉換為一個個區域，這些區域內包含車牌。
6. 通過算法選擇合適的車牌位置，通常將較小的區域過濾掉或尋找藍色底的區域。
7. 標註車牌位置
8. 圖像切割和識別

原文網址：https://kknews.cc/car/xlmvrp8.html


## Raspberry Pi Example - OpenALPR

### References
- [OpenCV: Automatic License/Number Plate Recognition (ANPR) with Python](https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/) by pyimagesearch, 2020-09-21
- [License Plate Recognition using OpenCV Python](https://medium.com/programming-fever/license-plate-recognition-using-opencv-python-7611f85cdd6c) by Praveen @ Medium, 2020-07-08
- [openalpr](https://github.com/imonology/ImonCloud-Doc/wiki/openalpr) by imonology @ github
- [閱讀筆記 – 使用樹莓派建立 DIY 車牌掃描器](https://softnshare.com/note-diy-license-plate-scanner-built-with-a-raspberry-pi/) by 'soft & share' Benjamin Franklin 
- [樹莓派3安裝車牌辨識系統](https://mrsitdownplz.pixnet.net/blog/post/404112983-%e6%a8%b9%e8%8e%93%e6%b4%be3%e5%ae%89%e8%a3%9d%e8%bb%8a%e7%89%8c%e8%be%a8%e8%ad%98%e7%b3%bb%e7%b5%b1) by  標準之旅 2019-07-23
- [[ 實用心得 ] Tesseract-OCR](https://medium.com/@b98606021/%E5%AF%A6%E7%94%A8%E5%BF%83%E5%BE%97-tesseract-ocr-eef4fcd425f0) by Kai Chen, Medium, 2018-11-22

- [ALPR with RPi and BB-AI](https://www.element14.com/community/community/project14/visionthing/blog/2019/11/19/lisence-plate) by crisdeodates, 2019-11-20
- [I built a DIY license plate reader with a Raspberry Pi and machine learning](https://towardsdatascience.com/i-built-a-diy-license-plate-reader-with-a-raspberry-pi-and-machine-learning-7e428d3c7401) by Robert Lucian Chiriac, Medium, 2020-02-17
- [ANPR: Car Spy Raspberry Pi](https://magpi.raspberrypi.org/articles/anpr-car-spy-raspberry-pi) by Lucy Hattersley, The MagPi, 2019




