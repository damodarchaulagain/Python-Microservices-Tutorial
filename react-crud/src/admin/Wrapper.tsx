import React from 'react';
import { Outlet } from 'react-router-dom';
import Menu from '../components/Menu';
import Nav from '../components/Nav';

const Wrapper = () => {
  return (
  <div>
    <Nav/>

    <div className="container-fluid">
    <div className="row">
        <Menu/>
        <Outlet/>
    </div>
    </div>
  </div>);
};

export default Wrapper;
