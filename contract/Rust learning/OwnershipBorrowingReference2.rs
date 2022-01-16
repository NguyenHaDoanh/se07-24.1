// sử dụng biến s1 là gives_ownership có 1 biến là helo (String)
// c2 : nhap 1 giá trị : lấy takes_and_give_back nhập vào s2 để  trả 1 kiểu là SString
//trông rườm rà v cut : lấy rồi trả các thứ @@
//------------------------------------- 1 chuc năng của Rust làm mọi chuyện đơn giản -----------
fn main() {
    let _d1 = String :: from("HeloLYsa");
    let (d2,len) = caculate_length(_d1);

    let _d3 = String :: from("Chữi"); // có ký tự unicode uft = 8 nên tính là 6
    let len1 =  caculate_length1(&_d3); // tham chiếu đến s1 thôi chứ giá trị của s 1 vẫn giữ nguyên
    
    let  mut _d4 = String :: from("LLLIsalY"); // có ký tự unicode uft = 8 nên tính là 6
    let len2 =  caculate_length2(&mut _d4);

    
    //let _a2 = &mut _a1; // cannot borrow `_a1` as mutable more than once at a time :
    //không thể mượn `_a1` dưới dạng có thể thay đổi nhiều lần tại một thời điểm
    //let _a3 = &mut _a1;
    let a1 = String :: from("Helo Lía");
    let q_1 = & a1; //khi mượn  sẽ ko thay đổi , không bị lỗi vì nó ko làm thay đỏi dữ liệu
    let q_2 = & a1;
    println!("q_1 = {},q_2 = {}",q_1,q_2);


    println!("độ dài của String {} đó là {} ",d2,len);
    println!("độ dài của String -  {} - đó là {} ",_d3,len1);
    println!("độ dài của String sau khi đ push vào là -  {} - đó là {} ",_d4,len2);
    //println!("_a1 = {} , _a2 = {}",_a2,_a3);  gây ra xung đột , 1 thằng sửa 1 tk in sẽ lỗi 
}
fn caculate_length(some_string : String) -> (String,usize){//usize : độ dài của String đó
    //&String : tham chiếu đến nó và trả lại 1 giá trị uszie
    let length = some_string.len();
    (some_string,length) //return lại 2 g tri
}
//c2 tham chiếu ,, nhìn nó ntn để trả lại giá trị
fn caculate_length1(some_string : &String) -> usize{//usize : độ dài của String đó
    //&String : tham chiếu đến nó và trả lại 1 giá trị uszie
    let length = some_string.len();
    length //return lại 2 g tri
}
fn caculate_length2(some_string : &mut String) -> usize{//usize : độ dài của String đó
    //muốn thay đổi string đó thì phải dung push_str() _cần mut(&mut String) để có thể thay đổi đươck
    some_string.push_str("Lovely lis");
    let length = some_string.len();
    length //return lại 2 g tri
}

// 1 vài nguyên tăc,tài liệu tham khảo : reference
// chỉ có thể tham chiếu  1 mutable  cho 1 data rong phạm vi cho phép
// Ko thể tham chiếu mutable neus 1 tham chiếu imutable  đã tồn tài trong 1 phạm vi
//

