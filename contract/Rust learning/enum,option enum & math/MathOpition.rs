//sẽ gọn gàng honw rất nhiều
//khớp là một toán tử luồng điều khiển trong Rust được sử dụng để chuyển điều khiển đến một khối mã
// cụ thể dựa trên giá trị của biến đang được kiểm tra.Toán tử đối sánh nhận vào một biến và so sánh
// giá trị của nó với từng giá trị trường hợp. Nếu có sự trùng khớp, khối mã tương ứng sẽ được thực thi.
//Match :cho phép bạn ssánh một gtrị với một loạt các mẫu và sau đó thực thi mã dựa trên mẫu phù hợp.
// Các mẫu có thể được tạo thành từ các giá trị chữ, tên biến, ký tự đại diện và nhiều thứ khác; 
//compound : phức hợp
fn main() {
    decimals(Coin::Solana);
    decimals(Coin::Bitcoin(Balance::Fish));
}
#[derive(Debug)] //debug lỗi 
enum Balance {
    //Balanece ; thăng bằng , intermediate : trung cấp
    Small,
    Intermediate,
    Fish,
    Shark,
}
enum Coin{
    Solana,
    Ethereum,
    Near,
    Bitcoin(Balance),
}
fn decimals(coin : Coin)-> u8 { //so thap phan : decimals
    match coin {
        Coin::Solana => {
            println!("Solana Math");
            1
        }
        //: Một enum và một matchbiểu thức có các biến thể của enum dưới dạng các mẫu của nó

        Coin::Ethereum =>10,
        Coin::Near =>30,
        Coin::Bitcoin(bala) => { //balance là 1 compuunt
            println!("I am a {:#?}", bala);
            30
        }
    }
}
