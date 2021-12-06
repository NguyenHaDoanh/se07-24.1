pragma solidity ^0.8.2;
//bat dau code dong coin dau tien 
contract Doanlly{
    mapping(address => uint) public balances; // ánh xạ ,lưu địa chỉ ....vd 00dsdsdsds = 10 đồng,... 
    mapping(address => mapping (address => uint)) public allowance; //địa chỉ này sẽ sử dụng 1 số lượng nào đó 
                //trong ví trên


    uint public totalSupply  = 10000 * 10 ** 18 ;//tong so luong dong token la bao nhieu 
    string  public name  = "Doanllyboyzcoin";
    string  public symbol = "DLC";
    uint public decimal = 18;  //định nghĩa độ chia nhỏ của 1 đồng coin 
    event Transfer (address indexed from , address indexed to ,uint value); // tìm kiếm các event theo đia chỉ or địa chỉ nhận
    event Appoval(address indexed owner,address indexed spender, uint value);   //appoved : sự chấp thuận
    //indexed :Các tham số được lập chỉ mục cho các sự kiện đã ghi sẽ cho phép bạn tìm kiếm 
    //         các sự kiện này bằng cách sử dụng các tham số được lập chỉ mục làm bộ lọc.

    constructor() {

        balances[msg.sender] = totalSupply; //khi khoi tạo , tất cả các đồng sẽ chuyển vể ví của chủ trước
        //undeclared : không khai báo  ;indentifier : định danh
    }
    function balanceOf(address owner) public view returns(uint)  { //balanceof : cán cân,  owner : chủ 
        //ham kiem tra so du tai khoan   // voi view là giá trị trả vể 
        return balances[owner];
    }
    function transfer(address to, uint value) public returns(bool){
    //muon co giao dich toi cac vi khac, su dung ham nay  //value : biểu diễn số tiền cần chuyển
        require(balanceOf(msg.sender) >= value, 'Insufficient funds'); //test xem số dư có đủ để chuyển không
        //invalid character to string : ký tự ko hợp lệ thành chuỗi

        // nếu so dư > gt chuyển thì có thể chuyển
        balances[to] +=value;
        balances[msg.sender] -= value;


        //khi biet ham này , mk phải bắn ra 1 sự kienr để u d bên ngoài bắt đc sự kiện đó
        emit Transfer(msg.sender,to,value);
        return true;


    }
    //xong dữ kienj khỏi tạo  đầu tiên :khi khỏi tạo (constructor ) thì sẽ đẩy hét 1000 coin vè vícủa mmk
    // sau đó transfer (chuyển khoản) chuyển coin cho những ví khác

    //--->> tiếp theo cần xày dựng hàm delegettranfer điểm tiên tiến : cho ví khác ddc quyền sử dụng 1
    //số tiền nào đo trong cái ví của mk
    function tranferFrom(address from ,address to ,uint value) public returns(bool){
        //hàm đề cấp quyền ví khác sử dụng 1 số tiền nào  đó trong ví mình
        require(balanceOf(from ) >= value , 'Ko du tien de su dung');
        require(allowance[from][msg.sender] >= value ,'khong du tien' );
        balances[to] += value; //neu dap ưng 2 cai tren 
        balances[from] -= value; //tru value 


        //bắt ra 1 sự kiện chuyen
        emit Transfer(from,to,value);
        return true;

    }
    //1 hàm chấp thuận của g chủ để chuyển tiền
    function appove(address spender,uint value) public returns (bool){ //appove : sự chấp thuận
        allowance[msg.sender][spender] =value;   //spender : người tiêu tiền 
        emit Appoval(msg.sender,spender ,value);
        return true;     
        }
//nhắc lại về msg.sender là một global variable cho chúng ta biết address nào phụ trách việc kích hoạt.
        //   Nó có thể là account hoặc là một smart contract khác.
        // tạo xong đồng , có dấu tích là đã thành công
        
}
