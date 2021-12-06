pragma solidity   >= 0.7.0 <0.9.0;
contract coin {
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
        uint createtime; //thoi gian tao tinh tu khoang thoi gian nam bao nhieu do ,lay moc thoi gian la 1/1/1970 - hien tai  ket qua tra ve la giay 
    }
    function addPlayer(string memory fullname , uint age , string memory sex ) public{
        players[msg.sender]=   Player(msg.sender ,fullname,Level.Beginer,age,sex,block.timestamp);// dữ liệu phía sau cần phả nhớ nhắt
        countplayer += 1;
    }

    //Bây giờ  bạn cần phải quản lý chúng bằng địa chỉ (address)  //se triên khai o ham Games2
    function getplayer(address diachinguoichoi) public view returns (Level) {
        return players[diachinguoichoi].mylev;
    }
    function chainPlayerlevel(address playeradress) public {
        Player storage player  = players[playeradress];//luu vao bo nho player ,lay ra tk player chon th playerlevel
        if(block.timestamp >= player.createtime + 15){
            player.mylev = Level.Intermediate; // 15 giay sau khi chay no se chuyen cho cua level
        }
    
    }




}
