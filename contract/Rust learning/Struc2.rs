#[derive(Debug)]
struct Hinhchunhat {
    chieudai : u32,
    chieurong : u32,
}
fn main(){
    //có thể taọ 1 kiểu dữ liệu giống tuple (1 kiểu danh sach có nhiều kiểu kywx liệu)
    //struct Color(i32,i32,i32) ; //dữ liệu i32 kiểu số
    //struct Point(i32,i32,i32);
    //vd tạo 1 bài toán sử dụng tính diện tích hình chữ nhật
    let _dodai = 50;
    let _dorong = 30;
    println!("Dien tich cua hinh chu nhat {}",dien_tich(_dodai,_dorong));
    //sau khi update 
    let _hinhchunhat = (30,50);
    println!("Dien tich cua hinh chu nhat {}",dien_tich1(_hinhchunhat));
    
    //a1 
    let _kichthuoc =  Hinhchunhat {chieudai:50,chieurong:30};
    println!("Dien tich hinh chu nhat neu su dung struc có thể dùng đc nhiều làn là: {:?}",dien_tich2(&_kichthuoc));
    println!("Kich thuoc hcn la {:#?}",_kichthuoc);
    //implement :triển khai thực hiện
    //`Hinhchunhat`cannot be formatted with the default formatter:`Hinhchunhat` không thể được định dạng bằng trình định dạng mặc định
    //iplm
    println!("Dien tich hinh chu nhat do la  : {}",_kichthuoc._tinhdientich());
    //Chứa đc hình khác hay không 
    let _kichthuoc2 = Hinhchunhat {
        chieudai :20,
        chieurong : 10,
    };
    let _kichthuoc3 = Hinhchunhat {
        chieudai :60,
        chieurong : 90,
    };
    println!("Hinh chữ nhật cũ chứa được hình mới thứ 2 là {}",_kichthuoc.chua_hcn(&_kichthuoc2));
    println!("Hinh chữ nhật cũ chứa được hình mới thứ 3 là {}",_kichthuoc.chua_hcn(&_kichthuoc3));
    //impl thu hinh vuong triong hinh CN 
    let _z = 30;
    println!("Hinh vuong co  kich thuoc là : {:#?} ",_hinhvuong(_z));



}
fn dien_tich(_dodai :u32,_dorong : u32) -> u32{
    _dodai*_dorong
}
//nâng cấp lên tiếp ; có 1 cachcs tính nhanh hơn\
fn dien_tich1(kichthuoc:(u32,u32)) -> u32{ //nó giống kiểu gọi các phần tử trong 1 array í
    kichthuoc.0*kichthuoc.1
    }
//(a1)có vấn đề nếu chạy thì sẽ ko sử dụng dc quá nhiềulần , dữ liệu cũngthay đổi theo giải pháp -->

fn dien_tich2(_kichthuoc : &Hinhchunhat) -> u32 { //tham chiếu thằng hình chữ nhật
    _kichthuoc.chieudai*_kichthuoc.chieurong
}
//1 phần giống oop , tạo 1 chức năng cho HCN
impl Hinhchunhat {
    //Từ khóa impl dùng để implement một trait(đặc điểm) cho một kiểu dữ liệu bất kỳ,
    // ở đây là chúng ta implement trait có tên là _tinhdientich cho hinhchunhatt
    fn _tinhdientich(&self)-> u32 {
        self.chieudai*self.chieurong // sau đó print lại
    }
    fn chua_hcn (&self,hinhchunhatkhac : &Hinhchunhat) ->bool{ // xem thu no chua dc HCN này ko
        self.chieudai > hinhchunhatkhac.chieudai && self.chieurong > hinhchunhatkhac.chieurong
    } //  nếu chứa thì return True
}
// tạo hình vuông cho HCN 
impl Hinhchunhat {
    fn _hinhvuong(kichthuoc : u32) -> Hinhchunhat {
        Hinhchunhat {
            chieudai : kichthuoc,
            chieurong : kichthuoc,
        }
    }
}
