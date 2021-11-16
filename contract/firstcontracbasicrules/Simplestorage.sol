
pragma solidity ^0.6.0;
contract Simplestorage{
    //uint256 favoriteNumber1 = 5; // gan 1 bien so nguyen  ko dau co kick thuoc la 256 bit 
    //bool favoriteBool = true;
    //string favoriteString = "Hello bro";
    //int256 favoriteInt  = -4;  // gan so so nguyen ko dau co kik thuoc 256 bit
    //address favoritaddress = 0x6dE5465d240434E5184fa7F99553F9254Ed92567; 
    //bytes32   favoritebyte = "coin";
    //uint256 public  favoriteNumb ;// co the goi la bien ben ngoai
    // khoi tao bang 0x6dE5465d240434E5184fa7F99553F9254Ed92567
    //function store(uint256 _favoritenumb) public { // khoi tao 1 ham public      
       // favoriteNumb = _favoritenumb;
        uint256 public   favoriteNumb ;// co the goi la bien ben ngoai n // pulic la trang thai de xuat hien 1 favoriteNumb , 
                           //neu ko co no se khoi tao thanh 1 noi bo ben trong
        bool public favoriteBool;
        bool public favoriteBool2;
    // khoi tao bang 0x6dE5465d240434E5184fa7F99553F9254Ed92567
    
    //struct People { // cau truc luu tru mot muc yeu thic so lien quan den 1 so nguoi 
    //    uint256 favoriteNumb; // cau truc favoriteNumb o chi  muc so 0 khi thuc hien deployy
   //     string name;   //...1
        
   // }
   //chi tao ra 1 nguoi      People public person  = People({favoriteNumb : 2,name : "Doan Nguyen"});
   // tao ra 1 danh sac Person - lam viec voi Arrays
   //b1 tao bien
    struct People {
        uint256 favoriteNumber;
        string name;
    }
    
    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumb; // Anh xa vd tu ten doan nguyen co the tim dc favoriteNumber la 22 ,phan dau tien se la nhap tu keyw va co kha nang hien thi co ten la nameToFavoriteNumb
    // can phai gan nameToFavoriteNumb vao ham addPerson chia khoa se la _name
    
    
    
    //thua hien chuc nang them nguoi 
    //function addPerson(string memory _name,uint256 _favoriteNumb) public { //memory dữ liệu sẽ chỉ được lưu trữ trong thực thi chức năng
    function addPerson(string memory _name,uint256 _favoriteNumb) public {
        people.push(People(_favoriteNumb , _name));
        nameToFavoriteNumb[_name] = _favoriteNumb;
    }
    function store(uint256 _favoritenumb) public //private ,internal
    { // khoi tao 1 ham public      
        favoriteNumb = _favoritenumb;
        
    }
    function retrieve() public view returns(uint256)
    { // thuc hien chuc nang doc 1 so trang thai ngoai chuoi khoi va tra ve 1so co dang  uint256 
        return favoriteNumb;   
    }
   
} // Deploy de trien khai hop dong varun transactions 
// hash : 0x,,,,, da hoan thanh hop dong gidao dicj 
// neu de dang public favoriteNumb khi trien khai se hien 2 nut gom favoriteNumb va  store 
// nut tu khoa cong khai favoriteNumb xac dinh kha nang hien thi cua bien hoac chuc nang hien co, co the dc goi bat cu luc nao
    //tu khoa vung chac vt tat cus smartcontract - tuong tu nhu 1 lop trong java orr bat ky lap trinh 00p nao khac

// struc de xac dinh do ran cua cac chuoi khoi
