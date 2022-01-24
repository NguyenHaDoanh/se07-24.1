import React, { Component } from 'react';

class Navbar extends Component {

  render() {
    return (
      <nav className=" navbar-dark bg-success flex-md-nowrap p-0 shadow">


        <a
          className=" navbar navbar-brand col-sm-3 col-md-2 mr-0"
          href="http://https://google.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          <b><em>SE07-24.1</em></b>
        </a>
        <ul className="navbar-nav px-3">
          <li className="nav-item text-nowrap d-none d-sm-none d-sm-block">
            
            <p className= "text-white"> <em><b> Tài khoản: </b></em>
             <small className= "text-white"> <em><span id= "account">{ this.props.account}</span></em></small>
            </p>
          </li>
        </ul>
      </nav>
    );
  }
}
export default Navbar;
