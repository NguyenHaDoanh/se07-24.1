pragma solidity >=0.6.6 <=0.9.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";
contract Fundme{
    using SafeMathChainlink for uint256;
    
    // tao ra 1 anh xa moi  giua cac dia chi va goa stringmapp
    mapping(address => uint256) public addressToAmountFunded;   //dia chi voi so tien tai tro 
    
    address[] public funders;
    address public owner;
    // tao mot chuc nang moi co the chap nha n thanh toan 
    constructor() public {
        owner = msg.sender;
    }
    function fund() public payable {
        uint256 minimumUSD = 50 * 10 ** 18;
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!");
        // tra tien cho 1 thu j do khi goi den ham  
        addressToAmountFunded[msg.sender] += msg.value ;   // msg :message.value la cac tu khoa trong moi cuoc goi hop dong va moi giao dich 
                                                        // va mgs.sender(sender : nguoi gui ) la ng gui chuc nang cuoc goi va tin nhan 
        funders.push(msg.sender);
        
        
        
        
        //bat cu khi nao goi von ai đó có thể gửi 1 só giá trị phải trả và sẽ duoc lưu ở addressToAmountFunded  để lập ,gọi số tiền được tài trợ
//https://eth-converter.com/ doi 1 so cac don vi do luong 
//Payable là một modifier có thể thêm vào các hàm trong solidity
//Payable cho phép function có thể nhận ether ,... trong 1 nut value o phan Deloy and run tran sactions
// 1 cach don gian de tai tro tien thong minh 
//Blockchain la 1 he thong xac dinh va oracles la cầu nối blockchain và thế giới thực 
//a decentralized oracle network - một mạng lưới tiên tri phi tập trung
//data.chain.link  - có nhiều mức định  khác nhau  nguồn cấp dữ liệu và các mạng cung cấp giá cho các quyền hạn định giá
//chaining support the growth of the defi ecosystem   - 
// hỗ trợ sự phát triển của hệ sinh thái defi

    }
    function getVersion() public view returns (uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }
    
    function getPrice() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
         return uint256(answer * 10000000000);
    }
    
    // 1000000000
    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }
    
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
    
    function withdraw() payable onlyOwner public {
        msg.sender.transfer(address(this).balance);
        
        for (uint256 funderIndex=0; funderIndex < funders.length; funderIndex++){
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }


//tạo ra 1 giá trị tối thiểu để tài trợ  -có thể là usd,VND (chuyển đối já) ( tạo ethernum là mẫ thông báo nhung muốn nó bằng tiền USD)
//Cần xác đinh được tỷ lệ chuyển đổi là bao nhiêu 





 
//sau khi gay quỹ , cop link account (fund) thì số tienf moi dc chuyển vào việc       tài trợ )
    
}
