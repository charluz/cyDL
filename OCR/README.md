# Study notes of OCR (Optical Character Recognition)

## 參考資料
- [OpenCV OCR and text recognition with Tesseract](https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/) by Adrian, pyimagesearch, 2018-09-17
- [OpenCV Text Detection (EAST text detector)](https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/) by Adrian, pyimagesearch, 2018-08-20
- [[ 實用心得 ] Tesseract-OCR](https://medium.com/@b98606021/%E5%AF%A6%E7%94%A8%E5%BF%83%E5%BE%97-tesseract-ocr-eef4fcd425f0) by Kai Chen, 2018-11-22, Medium

### Tesseract-OCR Overview

- 最先由HP實驗室於1985年開始研發，至1995年時已經成為OCR業內最準確的三款識別引擎之一。然而，HP不久便決定放棄OCR業務，Tesseract也從此塵封。數年以後，HP將Tesseract貢獻給開源軟件業。2005年，Tesseract由美國內華達州信息技術研究所獲得，並求諸於Google對Tesseract進行改進、消除Bug、優化工作。
- Tesseract目前已作為開源項目發佈在Google Project，其最新版本3.0已經支持中文OCR，並提供了一個命令行工具。
- 主要使用在辨識掃描文件/圖片的文字，包含契約、發票等等，能夠輕鬆地減少需要人力的工作。
- The latest release of Tesseract (v4) supports deep learning-based OCR that is significantly more accurate.
- The underlying OCR engine itself utilizes a Long Short-Term Memory (LSTM) network, a kind of Recurrent Neural Network (RNN).


