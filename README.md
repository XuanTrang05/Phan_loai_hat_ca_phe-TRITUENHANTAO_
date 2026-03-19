# Phan_loai_hat_ca_phe-TRITUENHANTAO_
# BÀI TẬP LỚN MÔN TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY
# ĐỀ TÀI: PHÂN LOẠI QUẢ CÀ PHÊ
Link youtube
[https://youtu.be/X1LCfPGrDl4](https://youtu.be/kbJAUQDTClk)

- HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY CHƯƠNG TRÌNH
- 🔹 Bước 1: Cài đặt Anaconda
- Truy cập: https://www.anaconda.com
- Tải và cài đặt Anaconda
- Sau khi cài xong, mở Anaconda Prompt
- 🔹 Bước 2: Tạo môi trường Python 3.10
- Nhập lệnh sau:
- conda create -n ai_env python=3.10 → Nhấn y để xác nhận cài đặt
- 🔹 Bước 3: Kích hoạt môi trường
- conda activate ai_env → Nếu thấy (ai_env) phía trước dòng lệnh là thành công
- 🔹 Bước 4: Cài đặt các thư viện cần thiết
- Nhập lần lượt các lệnh:
- '''pip install tensorflow
- pip install flask
- pip install pillow
- pip install numpy
- pip install matplotlib
- pip install seaborn
- pip install scikit-learn '''
- 🔹 Bước 5: Mở thư mục chứa project
- Ví dụ project nằm ở ổ D:
- cd D:\Phanloaichomeo
- Hướng dẫn chạy chương trình
- Bước 1: Vào Pycharm chọn vào new project rồi đặt tên và chọn conda rồi chọn môi trường ai_env
image
- 🔹 Bước 6: Tạo thư mục dataset và cho ảnh mèo và cho vào từng thư mục của mỗi ảnh
- Đảm bảo thư mục dataset có dạng:
- ''' dataset/
-  ├── train/
-  │     ├── ripe/
-  │     └── unripe/
-  ├── validation/
-  │     ├── ripe/
-  │     └── unripe/
-  ├── test/
-  │    ├── ripe/
-  │    └── unripe/''' 
- 🔹 Bước 2: Huấn luyện mô hình (train model)
- Chạy lệnh:
- python src/train.py → Sau khi chạy xong sẽ tạo file:
- models/mobilenet_dog_cat.h5
- 🔹 Bước 3: Tạo thư mục lưu ảnh upload
- mkdir static/uploads
- 🔹 Bước 4: Chạy chương trình
- python main.py → Nếu thành công sẽ hiển thị:
- Running on http://127.0.0.1:5000/
- 🔹 Bước 5: Mở trình duyệt và sử dụng
- Truy cập: http://127.0.0.1:5000/
- → Thực hiện:
- Upload ảnh
- Nhận kết quả phân loại (Cà phê chín / cà phê xanh)
