//storagefactory -nhà máy lưu trữ SPDX - License_Identifiter :

pragma solidity ^0.6.0;
// trien khai tat ca tinh nang cua hop dong va tuong tac hop dong tu nguoi khac  g
//co the ke thua tat cac cac chuc nag cua luu tru don gian  ma ko can phai soa chep ,gan
import "./Simplestorage.sol" ;
contract StrongFactory is Simplestorage {
    //b1: tao 1 hop dong luu tru don giann duoi dang cong khai
    // dat vao trong 1 danh sach or 1 Array
    Simplestorage[] public simplestoragearray ;
    function createsimplestorageContract() public  {
        Simplestorage simplestorage = new Simplestorage(); // tao 1 doi tuong hop dong luu tru don gian 
        simplestoragearray.push(simplestorage);
    }
    //them 1 ham chuc nang cua hang nha may
    //function storagefactoryStore(uint256 _simpleStorageIndex,uint256 _simpleStorageNumb) public {
        //Dia chi
        //ABI - Application  Binany interface -giao dien nh phan ung dung tu lan nhap truoc don
        // b1 tuong tac voi bo nho don gian 
        
        
        //Simplestorage simplestorage  = Simplestorage(address(simplestoragearray[_simpleStorageIndex]));
      //  simplestorage.store(_simpleStorageNumb);
        
    //}
    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumb) public {
        // Address 
        // ABI 
        Simplestorage(address(simplestoragearray[_simpleStorageIndex])).store(_simpleStorageNumb);
    }
    
    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256) {
        return Simplestorage(address(simplestoragearray[_simpleStorageIndex])).retrieve(); //truy cap dia chi 1 lan nua     
    //truy xuat chuc nang 
        
    }
}
