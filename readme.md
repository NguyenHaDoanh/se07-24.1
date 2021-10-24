# Tổng quan về Blockchain


1. [Blockchain là gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Definition/Blockchain)
2. [Blockchain dùng để làm gì ?](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/Use/%E1%BB%A8ng%20d%E1%BB%A5ng)
3. [Công nghệ Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/tree/main/Tech)
4. [Hệ thống Blockchain](https://github.com/NguyenHaDoanh/se07-24.1/blob/main/System/H%E1%BB%87%20th%E1%BB%91ng)

5. Cấu trúc Blockchain
        Mỗi khối(block) sẽ được lưu trữ gồm 3 phần: 1.Dữ liệu 2.Hash của khối hiện tại 3.Hash khối trước
        
        - Dữ liệu: Dữ liệu sẽ tùy thuộc vào từng loại Blockchain. Dữ liệu giao dịch gồm: Thông tin người gửi, nhận và số lượng coin được gửi.
        - Hash của khối hiện tại: Hash của khối hiện tại như một đặt điểm để nhận dạng. Nó là duy nhất và không trùng nhau giống như vân tay của chúng ta vậy.
        - Hash của khối trước: Nhờ hash này mà các khối(block) liên kết tạo ra một chuỗi (chain). Tuy nhiên khối đầu tiên sẽ không được liên kết với bất cứ khối nào. Vì nó được tạo ra đầu tiên. Khối đầu tiên này được gọi là Genesis block dịch ra tiếng Việt là “Khối nguyên thủy”

6. Công nghệ Blockchain hoạt động như thế nào? Cần có 4 yếu tố
     
        - Phải có giao dịch: nghĩa là phải có hoạt động mua bán, trao đổi diễn ra. Ví dụ: bạn thực hiện mua hàng trên Amazon
        - Giao dịch đó phải được xác minh: mọi thông tin liên quan đến giao dịch như thời gian, địa điểm, số tiền giao dịch, người tham gia… đều phải được ghi lại. Ví dụ: khi xem tình trạng đơn hàng, bạn sẽ biết được mình đã order những gì, tổng tiền là bao nhiêu, khi nào thì nhận được hàng…
        - Giao dịch đó phải được lưu trữ trong block: Bất cứ lúc nào bạn cũng xem lại được thông tin đơn hàng mà mình đã thực hiện. Chúng được lưu trữ trong mục “Quản lý đơn hàng”.
        - Block đó phải nhận được hash (hàm chuyển đổi một giá trị sang giá trị khác): chỉ khi nhận được hash thì một block mới có thể được thêm vào blockchain. 
