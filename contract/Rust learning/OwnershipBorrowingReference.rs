//Onership : 1 chức năng ddeeer quan  lí bộ nhớ của Rust
//
///ownership quyền sở hữu
//borrowing vay
//reference quy tắc ,tài liệu tham khảo
//scope : phạm vi
fn main(){
    //fn _x(){
    //    let  mut _a = "hello"; //hello chỉ là 1 dãy ký tự character nằm cạnh nhau chứ ko ph  String
    //    let _b = 100;// cố định
        // muốn thêm vào thì cần thêm mut vào kai báo : let mut _a = "Hello"
    //    _b();
    //}
    //fn _b(){
    //    let  mut _a =String  :: from("wolrd");//là 1 string có thể tăng giảm,.. muốn thay đôi phải thêm mut mutable
        // thêm  vào biến _a.push_str("!")
        //stack & heap  : _x()  các biến trong stack ,  _n thì trong heap 

    //}

    let _s1 = String :: from("Helly");//value borrowed here after move s1 cho s2 mượn nên ko còn s1
    let _s2 = _s1;
    // println!("_s1 = {}",_s1); lỗi
    println!("_s2 = {}",_s2);
    let _s3 = String :: from("XincheoDaoanlly");
    let _s4 =  _s3.clone();//clone 1 bản cũ tạo bản mới
    println!("_s3 = {}",_s3); // khi đó _s3 vẫn có giá trị


    let s  = String :: from("DLY"); //ạo thêm 1 func
    println!("{}",s);
    //take_ownership(s);//nhập hello vào hàm , sẽ looix vì lúc khai báo và chạy take_ownership  nó đã chuyên fn cho take_ownership rồi nên ko cần nữa 

    let s1 = gives_ownership(); // lấy quyền sở hữu
    let s2 =  String :: from("HelloDoanlly");
    let s3 =    takes_and_give_back(s2); //lấ y và trả lại
    println!("{},{}",s1,s3); // s2 đã là chức năng của s3 rôi ( lấy tk s2 trả về cho thằng s3)


}
//tạo 1 func take_nwnership : lấy quyển sở hữu
//fn take_ownership(_string: String){ // giá trị nhập vào là 1 _string
//    println!("{}",_string);
fn gives_ownership() -> String{ // giá trị trả vào là 1 _string
    let some_string = String :: from("Helodoanhe");
    some_string // trả 1 g t là some_string
}
fn takes_and_give_back(some_string: String) -> String{ // Nhập vào 1 giá trị là 1 String vừa nãy trả về 1 Strin
    some_string
} 
// sử dụng biến s1 là gives_ownership có 1 biến là helo (String)
// c2 : nhap 1 giá trị : lấy takes_and_give_back nhập vào s2 để  trả 1 kiểu là SString
//trông rườm rà v cut : lấy rồi trả các thứ @@







