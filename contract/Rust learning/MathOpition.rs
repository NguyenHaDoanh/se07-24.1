//Một biến kiểu Option<T> sẽ luôn luôn tồn tại một trong hai giá trị None (không có giá trị nào cả) 
//hoặc Some(T) (trả về giá trị kiểu T của biến đó)\
//handle : xử lí
//#[derive(Debug)]
fn  main(){
    let _five  = Some(5);
    let _six  = plus_one(_five);
    println!("six  ={:#?}",_six);
    let _none  = plus_one(None); //lỗi vì trình biên dịch
    println!("None  ={:#?}",_none);

    // cách để rút ngắn 
    let _value = Some(4);
    match _value {
        Some(5) => println!("Bằng 5."),
        _ =>println!("Không có giá trị thỏa mãn = 5"),  //() thì sẽ ko trả lại j , muốn trả lại 1 cái j đó thì dùng Println! như bt

    }
    // cách 2 ngắn hon:
    let _value1 = Some(3);
    if let Some(3) = _value1 {println!("Bằng 3")} //nhưng nếu thêm 1 dòng khác 3 nhu thế thì nó chỉ in ra bằng 3 thôi
    // ví dụ
    let _value1 = Some(2);
    if let Some(3) = _value1 {println!("Bằng 3")}   //không in ra j cả 
}
fn plus_one(x : Option<i32>) ->Option<i32>  { //bđ +1
    match x { // nếu có giá trị thì + 1 , ko thì None
        Some(x) => Some(x+1), 
        _ =>None 
    }
}


