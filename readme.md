# Mục tiêu và Mục đích

  Tìm hiểu về công nghệ Blockchain, xây dựng app kết nối
       
#  Tổng quan về Blockchain


1. [Blockchain là gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Blockchain)
2. [Blockchain dùng để làm gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Use)
3. [Công nghệ Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Tech)
4. [Hệ thống Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/System)
5. [Cấu trúc Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Structure)
       ![image](https://user-images.githubusercontent.com/92654803/138794918-23ca0a04-8ee0-4eaa-9325-6b47699783d6.png)
6. [Công nghệ Blockchain hoạt động như thế nào?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Operation)
      ![image](https://user-images.githubusercontent.com/92654803/138794853-808260b1-f07c-4699-b6a3-d7e203af86cc.png)
7. [Tìm hiểu về rest API.](https://www.redhat.com/en/topics/api/what-is-a-rest-api?fbclid=IwAR3LFXGv7ET1Lu9_MdPFU0NxX92vHVXwGm6xNDvXNPOwmImbQeWFX5XUV3o)
  -[Rest API là gì](https://itnavi.com.vn/blog/rest-api-la-gi/)
  
    ![image](https://user-images.githubusercontent.com/86102398/138792758-5fce033c-f88f-4bf4-ba62-db88c5daab83.png)
    ![image](https://user-images.githubusercontent.com/86102398/138792800-40880189-0bed-4206-9e5e-405a131cd117.png)


# Tổng quát(Smart contract)
Hợp đồng thông minh chuyển tài sản bao gồm kịch bản mua và bán tài sản có giá trị cao, yêu cầu người kiểm tra và thẩm định. Người bán có thể liệt kê tài sản của họ bằng cách khởi tạo hợp đồng thông minh chuyển tài sản. Người mua có thể đưa ra đề nghị bằng cách thực hiện một hành động trên hợp đồng thông minh và các bên khác có thể thực hiện các hành động để kiểm tra hoặc thẩm định tài sản. Khi tài sản được đánh dấu cả đã được kiểm tra và thẩm định, người mua và người bán sẽ xác nhận việc mua bán một lần nữa trước khi hợp đồng được hoàn tất. Tại mỗi thời điểm trong quá trình, tất cả những người tham gia đều có thể nhìn thấy trạng thái của hợp đồng khi nó được cập nhật. 
![image](https://user-images.githubusercontent.com/86102398/138625413-45b50ebf-0624-4e74-b9f7-c432f29acedb.png)
Có bốn nhân vật trong hợp đồng demo này - người bán với tư cách là người khởi xướng và ba nhân vật khác (người mua, người thẩm định và người kiểm tra) với tư cách là người tham gia. Như đã chỉ ra trong hình trên, tại một số giai đoạn nhất định trong hợp đồng, có nhiều hành động khác nhau mà người tham gia có thể thực hiện. Logic được viết trong hợp đồng thông minh sẽ sửa đổi trạng thái cho phù hợp dựa trên các hành động được thực hiện. 
# Vai trò ứng dụng 
|Tên|Vai trò|
|---|-------|
|Người donate|Người sở hữu một tài sản muốn donate cho 1 người nào đó.|
|Người nhận |Người nhận tiền donate từ những người khác|
# Trạng thái
|Tên|Sự miêu tả|
|---|----------|
|Tích cực(Active)|Cho biết rằng một tài sản có sẵn để mua.|
|Phiếu mua đã đặt(Offer Placed )|Cho biết ý định mua của người mua.|
|Chờ kiểm tra(Pending Inspection)|Cho biết yêu cầu của người mua đối với Người kiểm tra để kiểm tra tài sản đang được xem xét.|
|Đã kiêm tra(Inspected)|Cho biết sự chấp thuận của Thanh tra để mua tài sản đang được xem xét.|
|Đã kiểm định(Appraised )|Cho biết sự chấp thuận của Người kiểm định để mua tài sản đang được xem xét. |
|Chấp nhận không bắt buộc(Notional Acceptance )|Cho biết cả Người kiểm tra và Người kiểm định đều chấp thuận mua tài sản đang xem xét. |
|Người bán được chấp nhận(Seller Accepted)|Cho biết sự chấp thuận của chủ sở hữu để chấp nhận đề nghị do người mua đưa ra. |
|Người mua được chấp nhận(Buyer Accepted) |Cho biết sự chấp thuận của người mua đối với sự chấp thuận của chủ sở hữu. |
|Đã chấp nhận(Accepted)|Cho biết rằng cả người mua và người bán đã đồng ý với việc chuyển giao tài sản đang được xem xét. |
|Đã chấm dứt(Terminated)|Cho biết chủ sở hữu không chấp thuận tiếp tục bán tài sản đang được xem xét. |
# Chi tiết quy trình làm việc
  
