# Patchara Suwanbordin (6636058)

1. รันไฟล์ model.ipynb เป็นไฟล์ที่เขียน code เกี่ยวกับ data cleansing, machine learning
2. (optional) รันไฟล์ api.py ($python api.py) เป็นไฟล์ที่เอาโมเดลมารันเป็น API โดย API จะรัน localhost บน port 1780

## ตัวอย่าง API
**[POST][http://localhost:1780/predict]**

**[BODY][JSON]:**

    "brand": "Apple",
    "cpu": "Core i7",
    "OS": "macOS",
    "graphics": "Integrated",
    "ram": 16, // GB
    "harddisk": 256, // GB
    "screen_size": 14, // Inch
    "price": 1249 // USD

**[RESPONSE][JSON]:** 

    "isReasonable": false,
    "predictedPrice": 2101.4654308434206