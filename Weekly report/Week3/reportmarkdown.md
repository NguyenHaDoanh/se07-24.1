# Báo cáo tuần 3

I. Tìm hiểu về RESTFUL API

  1. Định nghĩa
 
   - RESTful API là một tiêu chuẩn dùng trong việc thiết kế API cho các ứng dụng web (thiết kế Web services) để tiện cho việc quản lý các resource. Nó chú trọng vào tài nguyên hệ thống (tệp văn bản, ảnh, âm thanh, video, hoặc dữ liệu động…), bao gồm các trạng thái tài nguyên được định dạng và được truyền tải qua HTTP.
   - API (Application Programming Interface) là một tập các quy tắc và cơ chế mà theo đó, một ứng dụng hay một thành phần sẽ tương tác với một ứng dụng hay thành phần khác. API có thể trả về dữ liệu mà bạn cần cho ứng dụng của mình ở những kiểu dữ liệu phổ biến như JSON hay XML.
   - REST (REpresentational State Transfer) là một dạng chuyển đổi cấu trúc dữ liệu, một kiểu kiến trúc để viết API. Nó sử dụng phương thức HTTP đơn giản để tạo cho giao tiếp giữa các máy. Vì vậy, thay vì sử dụng một URL cho việc xử lý một số thông tin người dùng, REST gửi một yêu cầu HTTP như GET, POST, DELETE, vv đến một URL để xử lý dữ liệu.
![image](https://user-images.githubusercontent.com/92654803/140596770-c6b5d0a0-c450-4307-8286-009712b328c4.png)

    
    
   
  2. Các phương thức hoạt động 
  
   - REST gửi một request HTTP method như GET, POST, PUT, DELETE,... đến một URI để xử lý dữ liệu.
  
  |METHOD|ACTION|
  |---|-------|
  |POST|(CREATE) Tạo mới một Resource.|
  |GET|(READ) Trả về một Resource hoặc một danh sách Resource.|
  |PUT|(UPDATE) Cập nhật, thay thế thông tin cho Resource.|
  |DELETE|(DELETE) Xoá một Resource.|
  - Những phương thức hay hoạt động này thường được gọi là CRUD tương ứng với Create, Read, Update, Delete – Tạo, Đọc, Sửa, Xóa. Mỗi phương thức trên phải được API call thông qua để gửi chỉ thị cho server phải làm gì. Đại đa số web API chỉ cho phép GET request lấy dữ liệu khỏi một externer server. Authencation không bắt buộc, nhưng nên có khi ta cho phép các lệnh khá “nguy hiểm” như PUT hay DELETE.
![image](https://user-images.githubusercontent.com/92654803/140596554-909907bc-103c-4ba7-9bd9-bfcd2f58f8c2.png)

    
  3. Sơ đồ hoạt động
  
 ![image](https://user-images.githubusercontent.com/92654803/140596543-e6661bbd-6a0b-447b-89fb-d16d3e23c5a0.png)

  4. Ưu điểm của RESTFUL
  
   - Giúp cho ứng dụng rõ ràng hơn
   - REST URL đại diện cho resource chứ không phải hành động
   - Dữ liệu được trả về với nhiều định dạng khác nhau như: xml, html, json….
   - Code đơn giản và ngắn gọn
   - REST chú trọng vào tài nguyên của hệ thống
    
    
  5. Các tiêu chí đánh giá 1 API RESTFUL:
   - Một kiến trúc máy khách-máy chủ được tạo thành từ máy khách, máy chủ và tài nguyên, với các yêu cầu được quản lý thông qua HTTP.
  
   - Giao tiếp máy khách-máy chủ không trạng thái , có nghĩa là không có thông tin máy khách nào được lưu trữ giữa các yêu cầu nhận và mỗi yêu cầu là riêng biệt và không      được kết nối.
  
   - Dữ liệu có thể lưu vào bộ nhớ cache giúp hợp lý hóa các tương tác giữa máy khách và máy chủ.
  
   - Một giao diện thống nhất giữa các thành phần để thông tin được truyền ở dạng chuẩn. Điều này yêu cầu rằng:
      +các tài nguyên được yêu cầu có thể nhận dạng được và tách biệt với các đại diện được gửi đến khách hàng.
      +các tài nguyên có thể được thao tác bởi máy khách thông qua biểu diễn mà họ nhận được vì biểu diễn chứa đủ thông tin để làm như vậy.
      +các thông điệp tự mô tả được trả lại cho khách hàng có đủ thông tin để mô tả cách thức khách hàng xử lý nó.
      +có sẵn siêu văn bản / siêu phương tiện, có nghĩa là sau khi truy cập tài nguyên, khách hàng sẽ có thể sử dụng siêu liên kết để tìm tất cả các hành động hiện có khác     mà họ có thể thực hiện.
   - Mặc dù REST API có những tiêu chí này để tuân theo, nó vẫn được coi là dễ sử dụng hơn so với một giao thức được quy định như SOAP (Giao thức truy cập đối tượng đơn giản), có các yêu cầu cụ thể như nhắn tin XML và tuân thủ giao dịch và bảo mật tích hợp sẵn. chậm hơn và nặng hơn.

   - Ngược lại, REST là một tập hợp các nguyên tắc có thể được triển khai khi cần thiết, làm cho các API REST nhanh hơn và nhẹ hơn, với khả năng mở rộng tăng lên — hoàn hảo cho Internet of Things (IoT) và phát triển ứng dụng di động .
