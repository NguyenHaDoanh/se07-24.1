pragma solidity >= 0.7.2 <= 0.9.1;
contract simpleAuction{ //Auction : đấu giá
    //chức năng 1 : đặt giá tiền (phiên đấu giá nằm ở thời gian nào?,giá trị đặt > nhất ở thời điểm đó
    //+Bid != 0 : giá trị luôn !=0;

    //chức năng 2 : rút tiền 
    // + có thé rút số tiền ra khỏi phiên đấu giá nếu muốn đặt cao hơn hoặc từ bỏ
    // amount >0
    //sau khi rút amount = bid (số tiền đã đặt)
    //sau khi rút :send = 0(giá trị ví bid sẽ = 0)

    //CN3 : khi nào phiên đấu giá kết thưc
    /// sau đó sẽ có skien  tranfer (chuyển tiền cho chu phien va so huu san pham dau gia 

    //Variable khỏi tạo biến cần thiết
    address payable public beneficiary;


    uint public auctionEndTime;
    uint public highestBid;
    address public highestBider;
    bool ended = false;

    mapping (address => uint ) public pendingReturns;
    // tạo 1 sự kiện adđ 1 ng mà gt ng đặt cao nhất tăng lên
    event highestBidincrease (address bidder, uint amount);//ng sec chiến thắng với value là cao nhất
    event auctionEnded(address winner,uint amount);
    // set up thoi gian ket thuc 
    constructor(uint _biddingtime ,address payable _beneficiar) { //payable : phai tra
        //ham dinh san chan 1 lan khi contract dc compli
        beneficiary = _beneficiar ;
        auctionEndTime = block.timestamp + _biddingtime;
    }

    //function
    function bid() public payable{ //payable :o phép function có thể nhận ether ,dạng như 1 lớp bảo mật chắc chắn có 1 transfer thì hàm mới hoạt động 

        //neu thoi gian < thoi gian dau gia ket thuc thì nó sẽ vẫn tiếp tục và ngược lại
        if (block.timestamp > auctionEndTime) {  // dk 1 phải nằm trong thời gian đấu gía
            revert("Phien dau gia ket thuc");
        }
        // nếu giá ng gửi thấp hơn giá cao nhất -> thông báo: 
        if (msg.value <= highestBid) {
            revert("Gia caa ban thap han gia cao nhat!");
        }
        if (highestBid != 0){
            pendingReturns[highestBider] += highestBid ; //giá ng đặt giá cao nhất + = giá cao nhất - vẫn la  ng cũ
        }
        highestBider      = msg.sender;//= vs ng khoi tạo
        highestBid          = msg.value;     
        emit highestBidincrease(msg.sender,msg.value)     ;                            
    }
    function withdraw() public returns(bool){ //withdraw : rút
            //returrn 1 giá trị bool , nếu sai sẽ đc rút , nếu dúng sẽ ko đc rút
            uint amount = pendingReturns[msg.sender]; // vi tri cua ng da khoi tao chuc nang do 
            if(amount >0){
                pendingReturns[msg.sender] = 0;  // kD sau khi rut tien xong thi moi thu se tra ve 0
                //tao 1 du lieu lan the nao de no gui tien ve
                if(!payable(msg.sender).send(amount)) {//msg.sende trar ve 1 gia tri neu thanh cong thi rut , ko tra ve thi ko dungrut dc (khi da dau gia ){
                    // tra ve 1 gia tri neu thanh cong thi se rut tien va nguoc lai  = False                  
                    //Payable cho phép function có thể nhận ether,la 1 modifier
                    pendingReturns[msg.sender] = amount;
                    return false ; 
                }

            
            }
            return true;


    }
    function auctionEnd() public {
            // thoi gian ket thuc
        if(ended ){
            revert("Thoi gian phien dau gia da co the ket thuc!");
        }
        if(block.timestamp < auctionEndTime){ //nho hon thoi gian dau gia ket thuc
            revert(" Phien dau gia chua ket thuc");
        }
        ended  =true ;
        // sự kiện coong bố người chiến thắng
        emit  auctionEnded(highestBider ,highestBid);
        beneficiary.transfer(highestBid); //tra gia tri nguoi thua huong beneficiary - chuc nang tu dong giao dich

    }

    
}
