// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Faucet {
    uint256 public numOfFunders; // không cần quản lý bộ nhớ , lấy ra số người donate
    mapping(uint256 => address) public lutFunders; // ánh xạ , nghĩa là từ 1 số thứ tự bất kỳ lấy ra địa chỉ
    mapping(address => bool) public funders; // ánh xạ từ địa chỉ để xác định  người donnate
    // React to receiving ether
    receive() external payable {}

    //  tạo các chức năng Addfunds, Withdraw, addressIndex, getFunfers
    // địa chỉ cần thanh toán từ server, có chức năng nhận tiền donate, xem địa chỉ tài khoản donnate , kiểm tra địa chỉ ví đã gửi tiền chưa , nếu gửi tiền thì sẽ add vào
    
    function addFunds() external payable {  // nhận tiền từ bên ngoài và có khả năng thanh toán được (được gửi bằng các hợp đồng khác nhau , không thể sử dụng trong call nội bộ 
        address funder = msg.sender; // khi nhập vô địa chỉ ví thì funder được tạo ra bởi người tạo ra nó ( nghĩa là địa chỉ sẽ được tạo ra ở đây)

        if (!funders[funder]) { // xá định nếu chưa có người donnate thì index sẽ +=1 
            uint256 index = numOfFunders++;
            funders[funder] = true;
            lutFunders[index] = funder;
        }
    }
        // chức năng nhập vào 1 số dã cho (số thứ tự ng donnate) đẻ hiển thị địa chỉ tương ứng đã donnate
    function getFundersIndex(uint256 index) external view returns (address) {
        return lutFunders[index];
    }
        // lấy ra tất cả các địa chỉ ví đã donate cho mình
    function getAllFunders() external view returns (address[] memory) {
        address[] memory _funders = new address[](numOfFunders);
        // tạo ra 1 list có địa chỉ có len =  số địa chỉ đã  donnate
        // chỉ lấy những địa chỉ donnate .những địa chỉ chưa donnate thì lược ra
        for (uint256 i = 0; i < numOfFunders; i++) {
            // vòng lặp lấy ra toan bộ thứ tự địa chỉ đã donate 
            _funders[i] = lutFunders[i];
        }
        return _funders;
    }
    //rút tiền :     nhập vào 1 sô tiền để rút
    function withdraw(uint256 withdrawAmount)
        external
        limitWithdraw(withdrawAmount)
    {   // người sử dụng phương thức  thanh toán (payable) để rút tiền
        payable(msg.sender).transfer(withdrawAmount);
    }
    //hàm có chức nang kiếm tra dieu kien truớc khi tiến hành thưc thi-dảm bảo sự an toàn trong hợp đồng
    modifier limitWithdraw(uint256 withdrawAmount) {
           // xét điều kiện rút
        require(
            withdrawAmount <= 1 * (10**18),
            "Khong the rut nhieu hon 1ETH"
        );

        _; // sau kh thỏa mãn các điều kiện trreen thì sẽ trả lại lượng thưc thi cho function nào gọi nó
    }
}
