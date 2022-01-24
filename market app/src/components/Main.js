import React, { Component } from 'react';

class Main extends Component {

  render() {
    return (
      <nav className=" navbar-dark bg-white flex-md-nowrap p-0 shadow">
        <div id= "content">
          <h4><b> Thêm sản phẩm </b></h4>
          <form onSubmit={(event) => {
            event.preventDefault()
            const name = this.productName.value
            const price = window.web3.utils.toWei(this.productPrice.value.toString(), 'Ether')
            this.props.createProduct(name, price)
          }}>
            <div className="form-group mr-sm-2">
              <input
                id="productName"
                type="text"
                ref={(input) => { this.productName = input }}
                className="form-control"
                placeholder="Tên sản phẩm"
                required />
            </div>
            <div className="form-group mr-sm-2">
              <input
                id="productPrice"
                type="text"
                ref={(input) => { this.productPrice = input }}
                className="form-control"
                placeholder="Giá trị sản phẩm"
                required />
            </div>
            <button type="submit" className="btn btn-success"><b> Thêm sản phẩm </b></button>
          </form>
          <p> </p>
          <h4><b> Danh sách sản phẩm </b></h4>
          <table className="table">
            <thead>
              <tr>
                <th scope="col">Stt</th>
                <th scope="col">Tên sản phẩm</th>
                <th scope="col">Giá sản phẩm</th>
                <th scope="col">Chủ sở hữu</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody id="productList">
              { this.props.products.map((product,key) => {
                return (
                  <tr key = {key}>
                    <th scope="row">{product.id.toString()}</th>
                    <td>{product.name}</td>
                    <td>{window.web3.utils.fromWei(product.price.toString(),'Ether') } ETH</td>
                    <td>{product.owner}</td>
                    <td>
                      { !product.purchased
                        ? <button 
                            type="submit" 
                            className="btn btn-success"
                            name={product.id}
                            value={product.price}
                            onClick={(event) => {
                              this.props.purchaseProduct(event.target.name, event.target.value)
                            }}
                          >
                              <b> Mua </b>
                          </button>
                        : <p className= "text-dark"> <em><b> Đã bán </b></em>
                          </p>
                      }
                      </td>
                  </tr>
                  )
              })}

            </tbody>
          </table>
        </div>
      </nav>
    );
  }
}

export default Main;
