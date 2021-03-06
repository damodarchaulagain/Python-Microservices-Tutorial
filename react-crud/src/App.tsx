import React from 'react';
import './App.css';
import Products from './admin/Products';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Main from './main/Main';
import ProductsCreate from './admin/ProductsCreate';
import Wrapper from './admin/Wrapper';
import ProductsEdit from './admin/ProductsEdit';
function App() {
  return (
    <div className="App">
      
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Main/>} />
          <Route path="admin" element={<Wrapper/>}>
            <Route path='products' element={<Products/>}/>
            <Route path='products/create' element={<ProductsCreate/>}/>
            <Route path='products/:id/edit' element={<ProductsEdit/>}/>
          </Route>
          
        </Routes>      
      </BrowserRouter>
    </div>
  );
}

export default App;
