# ![](https://user-images.githubusercontent.com/92350565/138580656-744676a8-a68d-40c4-aae6-823a798fcc3b.PNG) Tổng quan về Blockchain


1. [Blockchain là gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Blockchain)
2. [Blockchain dùng để làm gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Use/%E1%BB%A8ng%20d%E1%BB%A5ng)
3. [Công nghệ Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/tree/main/Tech)
4. [Hệ thống Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/System/H%E1%BB%87%20th%E1%BB%91ng)
5. [Cấu trúc Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Structure/C%E1%BA%A5u%20tr%C3%BAc)
6. [Công nghệ Blockchain hoạt động như thế nào?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Operation/C%C3%A1ch%20ho%E1%BA%A1t%20%C4%91%E1%BB%99ng)
7. [Tìm hiểu về rest API.](https://www.redhat.com/en/topics/api/what-is-a-rest-api?fbclid=IwAR3LFXGv7ET1Lu9_MdPFU0NxX92vHVXwGm6xNDvXNPOwmImbQeWFX5XUV3o)
  -[Rest API là gì](https://itnavi.com.vn/blog/rest-api-la-gi/)
8.    ![image](https://user-images.githubusercontent.com/86102398/138792758-5fce033c-f88f-4bf4-ba62-db88c5daab83.png)
9.    ![image](https://user-images.githubusercontent.com/86102398/138792800-40880189-0bed-4206-9e5e-405a131cd117.png)


# Tổng quát(Smart contract)
Hợp đồng thông minh chuyển tài sản bao gồm kịch bản mua và bán tài sản có giá trị cao, yêu cầu người kiểm tra và thẩm định. Người bán có thể liệt kê tài sản của họ bằng cách khởi tạo hợp đồng thông minh chuyển tài sản. Người mua có thể đưa ra đề nghị bằng cách thực hiện một hành động trên hợp đồng thông minh và các bên khác có thể thực hiện các hành động để kiểm tra hoặc thẩm định tài sản. Khi tài sản được đánh dấu cả đã được kiểm tra và thẩm định, người mua và người bán sẽ xác nhận việc mua bán một lần nữa trước khi hợp đồng được hoàn tất. Tại mỗi thời điểm trong quá trình, tất cả những người tham gia đều có thể nhìn thấy trạng thái của hợp đồng khi nó được cập nhật. 
![image](https://user-images.githubusercontent.com/86102398/138625413-45b50ebf-0624-4e74-b9f7-c432f29acedb.png)
Có bốn nhân vật trong hợp đồng demo này - người bán với tư cách là người khởi xướng và ba nhân vật khác (người mua, người thẩm định và người kiểm tra) với tư cách là người tham gia. Như đã chỉ ra trong hình trên, tại một số giai đoạn nhất định trong hợp đồng, có nhiều hành động khác nhau mà người tham gia có thể thực hiện. Logic được viết trong hợp đồng thông minh sẽ sửa đổi trạng thái cho phù hợp dựa trên các hành động được thực hiện. 
# Vai trò ứng dụng 
|Tên|Vai trò|
|---|-------|
|Người bán|Một người sở hữu một tài sản và muốn bán tài sản đó. |
|Người mua|Một người có ý định mua tài sản đang được bán bởi người bán. |
|Thanh tra|Người được người mua chọn làm người kiểm tra tài sản được xem xét mua. |
|Người thẩm định|Người được người mua chọn làm người thẩm định tài sản được xem xét mua. |

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
  -*Biểu đồ chuyển đổi trạng thái sau đây trình bày rõ các luồng có thể và các chức năng chuyển đổi khác nhau ở mỗi trạng thái. Mỗi người dùng chỉ được phép thực hiện một số hành động nhất định tùy thuộc vào vai trò ứng dụng. Vai trò phiên bản chỉ ra rằng chỉ người dùng có vai trò ứng dụng được chỉ định cho hợp đồng cụ thể mới có thể thực hiện các hành động trên hợp đồng.* 
