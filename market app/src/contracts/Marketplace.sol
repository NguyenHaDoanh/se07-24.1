pragma solidity ^0.5.0;

contract Marketplace {
    string public name;
    uint public productCount = 0;
    mapping(uint => Product) public products;
    struct Product {
        uint id;
        string name;
        uint price;
        address payable owner;
        bool purchased;

    }
    event ProductCreated(
        uint id,
        string name,
        uint price,
        address payable owner,
        bool purchased
    );
    event ProductPurchased(
        uint id,
        string name,
        uint price,
        address payable owner,
        bool purchased
    );

    constructor() public {
        name = "Final Marketplace";
    }
    function createProduct(string memory _name,uint _price) public  {
        // Yêu cầu tên hợp lệ
        require(bytes(_name).length > 0);
        // Yêu cầu giá hợp lệ
        require(_price > 0);
        // Số lượng sản phẩm tăng dần
        productCount ++;
        // Tạo sản phẩm
        products[productCount] = Product(productCount, _name, _price,msg.sender, false);
        // Kích hoạt một sự kiện
        emit ProductCreated(productCount, _name, _price, msg.sender, false);
    }

    function purchaseProduct(uint _id) public payable {
        // Tìm nạp sản phẩm
        Product memory _product = products[_id];
        // Tìm nạp chủ sở hữu
        address payable _seller = _product.owner;
        // Đảm bảo sản phẩm có id hợp lệ
        require(_product.id > 0 && _product.id <= productCount);
        // Yêu cầu có đủ Ether trong giao dịch
        require(msg.value >= _product.price);
        // Yêu cầu sản phẩm chưa được mua
        require(!_product.purchased);
        
        // Yêu cầu người mua không phải là người bán
        require(_seller != msg.sender);
        
        // Chuyển quyền sở hữu cho người mua
        _product.owner = msg.sender;
        // Đánh dấu là đã mua
        _product.purchased = true;
        // Cập nhật sản phẩm
        products[_id] = _product;
        // Thanh toán cho người bán bằng cách gửi Ether cho họ
        address(_seller).transfer(msg.value);
        // Kích hoạt một sự kiện
        emit ProductPurchased(productCount, _product.name, _product.price, msg.sender, true);
}
}