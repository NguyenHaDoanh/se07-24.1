# Báo cáo tuần 3

I. Tìm hiểu về RESTFUL API

  1. Định nghĩa
 
   - RESTful API là một tiêu chuẩn dùng trong việc thiết kế API cho các ứng dụng web (thiết kế Web services) để tiện cho việc quản lý các resource. Nó chú trọng vào tài nguyên hệ thống (tệp văn bản, ảnh, âm thanh, video, hoặc dữ liệu động…), bao gồm các trạng thái tài nguyên được định dạng và được truyền tải qua HTTP.
   - API (Application Programming Interface) là một tập các quy tắc và cơ chế mà theo đó, một ứng dụng hay một thành phần sẽ tương tác với một ứng dụng hay thành phần khác. API có thể trả về dữ liệu mà bạn cần cho ứng dụng của mình ở những kiểu dữ liệu phổ biến như JSON hay XML.
   - REST (REpresentational State Transfer) là một dạng chuyển đổi cấu trúc dữ liệu, một kiểu kiến trúc để viết API. Nó sử dụng phương thức HTTP đơn giản để tạo cho giao tiếp giữa các máy. Vì vậy, thay vì sử dụng một URL cho việc xử lý một số thông tin người dùng, REST gửi một yêu cầu HTTP như GET, POST, DELETE, vv đến một URL để xử lý dữ liệu.
![image](https://user-images.githubusercontent.com/92654803/140596770-c6b5d0a0-c450-4307-8286-009712b328c4.png)

    
    
   
  2. Các giao thức hoạt động 
   - REST gửi một request HTTP method như GET, POST, PUT, DELETE,... đến một URI để xử lý dữ liệu.
  |METHOD|ACTION|
  |---|-------|
  |POST|(CREATE) Tạo mới một Resource.|
  |GET|(READ) Trả về một Resource hoặc một danh sách Resource.|
  |PUT|(UPDATE) Cập nhật, thay thế thông tin cho Resource.|
  |DELETE|(DELETE) Xoá một Resource.|
   - Những phương thức hay hoạt động này thường được gọi là CRUD tương ứng với Create, Read, Update, Delete – Tạo, Đọc, Sửa, Xóa. Mỗi phương thức trên phải được API call thông qua để gửi chỉ thị cho server phải làm gì.

    REST hoạt động chủ yếu dựa vào giao thức HTTP. Các hoạt động cơ bản nêu trên sẽ sử dụng những phương thức HTTP riêng.
      ->GET (SELECT): Trả về một Resource hoặc một danh sách Resource.
      ->POST (CREATE): Tạo mới một Resource.
      ->PUT (UPDATE): Cập nhật thông tin cho Resource.
      ->DELETE (DELETE): Xoá một Resource.
    Những phương thức hay hoạt động này thường được gọi là CRUD tương ứng với Create, Read, Update, Delete – Tạo, Đọc, Sửa, Xóa
![image](https://user-images.githubusercontent.com/92654803/140596554-909907bc-103c-4ba7-9bd9-bfcd2f58f8c2.png)

    
  3. Sơ đồ hoạt động
  
![image](https://user-images.githubusercontent.com/92654803/140596543-e6661bbd-6a0b-447b-89fb-d16d3e23c5a0.png)

  4. Ưu điểm của RESTFUL
  
    ->Giúp cho ứng dụng rõ ràng hơn
    ->REST URL đại diện cho resource chứ không phải hành động
    ->Dữ liệu được trả về với nhiều định dạng khác nhau như: xml, html, json….
    ->Code đơn giản và ngắn gọn
    ->REST chú trọng vào tài nguyên của hệ thống
