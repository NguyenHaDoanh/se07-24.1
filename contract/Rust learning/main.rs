fn main() {
    //println!("Hello, world!");
    //khởi tạo 1 biến 
    let mut x = 10; //mut  - mutable : có thể được biến đổi ,neus ko có sẽ lỗi vì let là biến bất biến

    println!("x = {}",x);
    x = 20;
    println!("x = {}",x);
    //khai báo hằng số trong Rust 
    //const HANG_SO : u32= 100000000000; //u32 là 32 bit 
    //u32 chỉ được hoạt động trong 1 khoảng từ 0 - 4 294 967 295
    //cao hơn thì dùng u128
    const HANG_SO : u128= 100_000_000_000;
    println!("Hằng số  = {}",HANG_SO);
    //có thể sử dụng _ để phân biệt bn chữ số vs u128 = 1000000000 = 1_000_000_000
    
    //shadowing(bóng tối)
    let x = 10;
    println!("x : {}",x);
    let x = "Tiền";
    println!("x ={}",x);
    let outer = 10 ;
    {
        let inner  = 200;
        println!("inner = {}", inner);
        let outer = 300 ; 
        println!("outer = {}",outer); // trong cùng phạm vi , biến cũ sẽ bị che phủ bơi biến mới

    }
    println!("outer = {}",outer); // trong phạm vi này , biến cũ được lôi ra  

    
    // Các kiểu dữ liệu --DATA TyPE
     //+ Scalar Data : 1 biến đơn vd let x = ,,,, , khởi tạo 1 cái dữ liệu duy nhất
    //Integer
    let a: i32 = 111_111; //Demicals
    let b: i32 = 0xff ;//Hex 0 -255 ,thêm 1 số sẽ ko chấp nhận
    let c : i32 = 0o77;//Octal
    let d : i32 = 0b1111_0000;//Binany : mã nhị phân
    let e : u8 = b'A'; //Byte (chỉ có u8 onlu u8)  nhận dienj đc toàn bộ mã đấy
    println!("a = {}",a);
    println!("b = {}",b);
    println!("c = {}",c);
    println!("d = {}",d);
    println!("e = {}",e);
    //Float : Giống hầu hết ngôn ngữ khác
    let f:f64 = 2.0;
    let j:f32 = 3.0;
    let sum : i32 = 3+4;
    let subtraction : i32 = 4-3;      // subtraction : phép trừ
    let multiplication : i32 = 3*5;
    let division :f64 = 20.4 / 10.1;
    let remainder : i32 = 20%3;  //phép lấy phần dư
    println!("f = {}",f);
    println!("j = {}",j);
    println!("sum = {}",sum);
    println!("subtraction= {}",subtraction);
    println!("multiplication = {}",multiplication);
    println!("division = {}",division);
    println!("remainder = {}",remainder);
    //String 

    //Bolean 
    //let i = true;
    //let h :bool = false;
    //Character
    let f = "z"; 
    let r = '😀';//chấp nhận icon ,.. yumicode j đó
    println!("f = {}",f);
    println!("r = {}",r);

    //---------------------------------------------
     //+Compound Data : tổng hop nhieu fkieeur duex liệu trong 1 biến tương tự nhu array,...
    //+ Tuple : là 1 dạng  dữ liệu tích hop nhiều kiểu dữ liệu   trong 1 tuple (th)
    let tupp :(&str,i32) = ("TRaLY",100);
    //println!("{}",tup);  // sẽ lỗi vì ko biết in ra kieurw dữ liệu nào ??
    println!("{:?}",tupp); 
    let (_string, _integer) = tupp;
    let _integer : i32  = tupp.1;
    println!("{}",_integer);
    println!("{}", _string);
    //array : là 1 danh sách có kích thuowcs cố định ,  các dữ liệu đồng nhất 1  dữ liệu
    let number : [i32;3] = [122,204,037];
    let get_number : i32 = number[1];
    println!("number = {}",get_number);
    let _hashing:[i32;32] = [0; 32];
    println!("Hasing = {:?}",_hashing)   ;       //32 sớ
    //c2 dùng forr
    for i in _hashing.iter(){
        //iter lấy ra từng item ở trong _hashing
        print!("{}",i);
    }


}
// file cargo dùng để liệt kê  import vào packeage ,hu viện
