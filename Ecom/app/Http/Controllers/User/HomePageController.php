<?php

namespace App\Http\Controllers\User;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Models\Product;

class HomePageController 
{
    public function home(){
        $products = Product::latest()->paginate(15);
        return view('users.home',compact('products'));
        }
}
