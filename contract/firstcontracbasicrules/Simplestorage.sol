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
        uint256   favoriteNumb ;// co the goi la bien ben ngoai
    // khoi tao bang 0x6dE5465d240434E5184fa7F99553F9254Ed92567
    
    struct People { // cau truc luu tru mot muc yeu thic so lien quan den 1 so nguoi 
        uint256 favoriteNumb;
        string name;
        
    }
    People public person  = People({favoriteNumb : 2,name : "Doan Nguyen"});
    function store(uint256 _favoritenumb) public //private ,internal
    { // khoi tao 1 ham public      
        favoriteNumb = _favoritenumb;
        
    }
    function retrieve() public view returns(uint256)
    { // thuc hien chuc nang doc 1 so trang thai ngoai chuoi khoi
        return favoriteNumb;   
    }
   
} // Deploy de trien khai hop dong varun transactions 
// hash : 0x,,,,, da hoan thanh hop dong gidao dicj 
// neu de dang public favoriteNumb khi trien khai se hien 2 nut gom favoriteNumb va  store 
// nut tu khoa cong khai favoriteNumb xac dinh kha nang hien thi cua bien hoac chuc nang hien co, co the dc goi bat cu luc nao
    //tu khoa vung chac vt tat cus smartcontract - tuong tu nhu 1 lop trong java orr bat ky lap trinh 00p nao khac

// struc de xac dinh do ran cua cac chuoi khoi
