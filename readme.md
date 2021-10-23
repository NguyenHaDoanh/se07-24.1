1. Blockchain là gì ?
        
        - Blockchain là một cơ sở dữ liệu phân cấp lưu trữ thông tin trong các khối thông tin được liên kết với nhau bằng mã hóa và mở rộng theo thời gian. 
        - Mỗi khối thông tin đều chứa thông tin về thời gian khởi tạo và được liên kết tới khối trước đó, kèm một mã thời gian và dữ liệu giao dịch.
        
2. Blockchain dùng để làm gì ?

        - Blockchain được dùng để lưu trữ thông tin trong các khối thông tin được liên kết với nhau. Nó được quản lý bởi tất cả mọi người tham gia hệ thống.
        - Cho phép truyền tải dữ liệu một cách an toàn bằng một hệ thống mã hóa phức tạp, và được mở rộng theo thời gian.
        - Công nghệ này được tạo ra để chống lại sự thay đổi dữ liệu trong hệ thống. Thông tin khi được nhập vào trong chuỗi khối blockchain thì sẽ không thể thay đổi và chỉ được bổ sung thêm khi có sự chấp thuận của tất cả mọi người trong hệ thống.
        - Hệ thống đảm bảo sự an toàn rất cao cho các dữ liệu trước các nguy cơ bị đánh cắp.

3. Công nghệ Blockchain

        - Mật mã học: đảm bảo tính minh bạch, toàn vẹn và riêng tư thì công nghệ Blockchain đã sử dụng public key và hàm hash function.
        - Mạng ngang hàng: Mỗi một nút trong mạng được xem như một client và cũng là server để lưu trữ bản sao ứng dụng.
        - Lý thuyết trò chơi: Tất cả các nút tham gia vào hệ thống đều phải tuân thủ luật chơi đồng thuận (giao thức PoW, PoS,…) và được thúc đẩy bởi động lực kinh tế.

4. Hệ thống Blockchain gồm 3 loại chính

        - Public: Bất kỳ ai cũng có quyền đọc và ghi dữ liệu trên Blockchain. Quá trình xác thực giao dịch trên Blockchain này đòi hỏi phải có rất nhiều nút tham gia. Vì vậy, muốn tấn công được vào hệ thống Blockchain này cần chi phí rất lớn và thực sự không khả thi. Ví dụ: Bitcoin, Ethereum,… 
        - Private: Người dùng chỉ được quyền đọc dữ liệu, không có quyền ghi vì điều này thuộc về bên tổ chức thứ ba tuyệt đối tin cậy. Vì đây là một Private Blockchain, cho nên thời gian xác nhận giao dịch khá nhanh vì chỉ cần một lượng nhỏ thiết bị tham gia xác thực giao dịch. Ví dụ: Ripple là một dạng Private Blockchain, hệ thống này cho phép 20% các nút là gian dối và chỉ cần 80% còn lại hoạt động ổn định là được.
        - Permissioned (hay còn gọi là Consortium): một dạng của Private nhưng bổ sung thêm 1 số tính năng khác, đây là sự kết hợp giữa Public và Private. Ví dụ: Các ngân hàng hay tổ chức tài chính liên doanh sẽ sử dụng Blockchain cho riêng mình.

5. Cấu trúc Blockchain
        Mỗi khối(block) sẽ được lưu trữ gồm 3 phần: 1.Dữ liệu 2.Hash của khối hiện tại 3.Hash khối trước
        
        - Dữ liệu: Dữ liệu sẽ tùy thuộc vào từng loại Blockchain. Dữ liệu giao dịch gồm: Thông tin người gửi, nhận và số lượng coin được gửi.
        - Hash của khối hiện tại: Hash của khối hiện tại như một đặt điểm để nhận dạng. Nó là duy nhất và không trùng nhau giống như vân tay của chúng ta vậy.
        - Hash của khối trước: Nhờ hash này mà các khối(block) liên kết tạo ra một chuỗi (chain). Tuy nhiên khối đầu tiên sẽ không được liên kết với bất cứ khối nào. Vì nó được tạo ra đầu tiên. Khối đầu tiên này được gọi là Genesis block dịch ra tiếng Việt là “Khối nguyên thủy”
