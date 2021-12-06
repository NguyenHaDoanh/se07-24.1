pragma solidity >=0.7.0 <0.9.0;
contract savedata {
    uint public Data;
    function set(uint x) public {
        Data = x;
    }
    function get() public view returns(uint x) {
        return Data;
    }
}
