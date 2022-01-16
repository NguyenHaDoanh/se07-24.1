#[derive(Debug)]
enum IpAddressKind { //option : lựa chọn 
    //ứng dụng nhiều , opion có hàu hết trong các mã nguồn , tránh lỗi ,... 
    //Math + option : ,....
    //enum :từ khóa cho phép việc tạo ra một loại có thể là một trong một vài biến thể khác nhau. 
    //      Bất kỳ biến thể nào có giá trị là  structcũng có giá trị là enum.
    //jong struc : tong hop du lieu cho 1 đối tượng nào đó
    //adres Kind : loại địa chỉ
    L4(String),
    L6(String),

}
#[derive(Debug)]
enum IpAddressKind1 { //option : lựa chọn 

    L1(u8,u8,u8,u8),
    L2(String),

}
#[derive(Debug)]
struct _IPaddress { //kieur và địa chir
    kind : IpAddressKind,
    address : String,

}
//dùng enum để tạo ra 1 kiểu dữ liệu
//dùng struct đẻ thêm kiểu dữ lieuj đó và methob để thêm chức năng
impl _IPaddress {
    fn some_function() {
        println!("Blockchain dvlper");
    }
}
fn main() { //c1 lấy ra bằng 1 biến 
    //let localhost  = _IPaddress {
    //    kind : IpAddressKind::L4,
    //    address :String :: from("12.0.0.1"),
    //};//trait : đặc điểm
    //println!("Localhosst = {:#?}",localhost); //:#? de bugg
    //rút họn -----------------
    let localhost1 = IpAddressKind::L4(String ::from("20.04.01"));
    println!("localhost = {:#?}", localhost1);
    let localhost2 = IpAddressKind1::L1(1,2,3,4);
    println!("localhost = {:#?}", localhost2);



}
//cách 2 
//fn route(ip_kind : IpAddressKind){
    //println!("{:?}",ip_kind);
//}
//rút ngắn , thêm trực tiếp kiểu dữ liệu của kind và addresss
