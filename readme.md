# Mục tiêu và Mục đích

  Tìm hiểu về công nghệ Blockchain, xây dựng app kết nối
       
#  Tổng quan về Blockchain


1. [Blockchain là gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Blockchain)
2. [Blockchain dùng để làm gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Use)
3. [Công nghệ Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Tech)
4. [Hệ thống Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/System)
5. [Cấu trúc Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Structure)
       ![image](https://user-images.githubusercontent.com/92350565/150643595-f616cff5-b4e9-4154-8126-c5ccb2a118f1.png)
6. [Công nghệ Blockchain hoạt động như thế nào?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Operation)
      ![image](https://user-images.githubusercontent.com/86102398/150788959-3b9db011-7c9e-46a2-8507-2f18e16ab167.png)
7. [Tìm hiểu về rest API.](https://www.redhat.com/en/topics/api/what-is-a-rest-api?fbclid=IwAR3LFXGv7ET1Lu9_MdPFU0NxX92vHVXwGm6xNDvXNPOwmImbQeWFX5XUV3o)
  -[Rest API là gì](https://itnavi.com.vn/blog/rest-api-la-gi/)
  
    ![image](https://user-images.githubusercontent.com/92350565/150643594-b1edf0e3-f0eb-4dfa-9442-d02f40c6d791.png)



# Tổng quát(Smart contract)
Hợp đồng thông minh chuyển tài sản bao gồm kịch bản mua và bán tài sản có giá trị cao, yêu cầu người kiểm tra và thẩm định. Người bán có thể liệt kê tài sản của họ bằng cách khởi tạo hợp đồng thông minh chuyển tài sản. Người mua có thể đưa ra đề nghị bằng cách thực hiện một hành động trên hợp đồng thông minh và các bên khác có thể thực hiện các hành động để kiểm tra hoặc thẩm định tài sản. Khi tài sản được đánh dấu cả đã được kiểm tra và thẩm định, người mua và người bán sẽ xác nhận việc mua bán một lần nữa trước khi hợp đồng được hoàn tất. Tại mỗi thời điểm trong quá trình, tất cả những người tham gia đều có thể nhìn thấy trạng thái của hợp đồng khi nó được cập nhật. 
![image](https://user-images.githubusercontent.com/86102398/138625413-45b50ebf-0624-4e74-b9f7-c432f29acedb.png)
Có bốn nhân vật trong hợp đồng demo này - người bán với tư cách là người khởi xướng và ba nhân vật khác (người mua, người thẩm định và người kiểm tra) với tư cách là người tham gia. Như đã chỉ ra trong hình trên, tại một số giai đoạn nhất định trong hợp đồng, có nhiều hành động khác nhau mà người tham gia có thể thực hiện. Logic được viết trong hợp đồng thông minh sẽ sửa đổi trạng thái cho phù hợp dựa trên các hành động được thực hiện. 

# App Marketplace
Đây là một thị trường chạy trên blockchain. Cho phép mọi người liệt kê các mặt hàng để bán và cũng cho phép mọi người mua chúng trên trang web bằng tiền điện tử.
Khi nào ai đó mua hàng, họ ngay lập tức trở thành chủ sở hữu.

   #### Đảm bảo tải môi trường đầy đủ 
   #### Đã có tài khoản Metamask
   #### [Cài đặt node js](nodejs.org).
   #### Cài đặt truffle,Ganache
   #### `npm install truffle -g`
### Bắt đầu với việc tạo 1 React App
 Dự án này được khởi động bằng[Create React App](https://github.com/facebook/create-react-app).
 ### `npx create-react-app "name"`
 Khởi tạo liên kết truffle và Ganache
 ### `truffle init`
   
## Tập lệnh có sẵn

Trong thư mục dự án , có thể khởi chạy:

### `npm start`

Chạy ứng dụng ở chế độ nhà phát triển.\
Mở [http://localhost:3000](http://localhost:3000) để xem ứng dụng trên trình duyệt.

Trang sẽ tải lại khi đã thực hiện các thay đổi.\
Lỗi cũng sẽ xuất hiện trên cửa sổ.
###

### `truffle console`

Bảng điều khiển tương tác cơ bản kết nối với bất kỳ ứng dụng khách Ethereum nào
 
### `truffle migrate` 

Triển khai smart contract
### `truffle migrate --reset`

Triển khai lại từ đầu
### `npm test`

 Khởi chạy người chạy thử nghiệm trong chế độ tương tác.\
Truy cập [running tests](https://facebook.github.io/create-react-app/docs/running-tests) để biết thêm thông tin.

### `npm run build`

Xây dựng ứng dụng xuất vào folder `build`.\
Kết hợp chính React trong chế độ sản xuất và tối ưu hóa bản dựng để có hiệu suất tốt nhất.

Bản dựng được rút gọn và tên tệp bao gồm các hàm băm.\
Ứng dụng đã sẵn sàng để triển khai!

### `npm run eject`



  
