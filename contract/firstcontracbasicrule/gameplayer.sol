pragma solidity   >= 0.7.0 <0.9.0;
contract game {
    // bool = true; //false  : khai bao bien tra ve Truee or False
    // uint songuyencuatoi =10;
    // int myinteger ; //so nguyen co the am
    // string myString = "Xin Chao Doan";
    // address pls = mgs.sender();
    uint public countplayer = 0; // hamdem so nguoi da tao ra

    enum Level {Beginer, Intermediate,advande} //người bắt đầu, trung gian , nang cao           // la 1 kieu danh sach han che su dung , chi co the chon 1 trong so cac du lieu da co
    mapping (address => Player) public players ;//Ánh xạ , để lưu trữ truyền dữ liệu 
    struct Player{
        address diachinguoichoi;
        string fullname;  
        Level mylev;
        
        
        uint age ;
        string sex;
        //sau đó khai báo truyền vào 1 Level
        
    }
    function addPlayer(string memory fullname , uint age , string memory sex ) public{
        players[msg.sender]=   Player(msg.sender ,fullname,Level.Beginer,age,sex);// dữ liệu phía sau cần phả nhớ nhắt
        countplayer += 1;
    }

    //Bây giờ  bạn cần phải quản lý chúng bằng địa chỉ (address)  //se triên khai o ham Games2
    function getpleyer(address diachinguoichoi) public returns (Level) {
        return players[diachinguoichoi].mylev;
    }





}
