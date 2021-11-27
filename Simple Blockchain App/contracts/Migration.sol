// SPDX-License-Identifier: MIT
//pragma solidity >=0.4.22 <0.8.0;

contract Migrations { //sudi cu {  //để kiểm tra các điều kiện trước khi các đoạn mã code trong phương thức đó được thực thi 
  address public owner = msg.sender; //chu so huu ower se luon co dia chi cua nguoi ban dau
  uint public last_completed_migration;

  modifier restricted() {//Modifier onlyOwner() sẽ đảm bảo cho hàm setCompleted() sẽ hoạt động 
                          //một cách đúng đắn : chỉ có owner của Contract mới được quyền gọi nó.
    require( // yeu cầu
      msg.sender == owner, //  mgs.sender(sender : nguoi gui ) la ng gui  thuc hien chuc
                            // nang cuoc goi va tin nhan  ket noi voi  hop dong đang tạo cuộc gọi
                
      "This function is restricted to the contract's owner"//Chức năng này bị hạn chế đối với chủ sở hữu hợp đồng
    );
    _;
  }

  function setCompleted(uint completed) public restricted {
    last_completed_migration = completed;
  }
}
