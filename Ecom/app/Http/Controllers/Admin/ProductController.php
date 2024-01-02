<?php

namespace App\Http\Controllers\Admin;
use App\Http\Controllers\Controller;
use App\Http\Requests\ProductSaveRequest;
use App\Models\Category;
use App\Models\Product;
use Illuminate\Support\Str;
use Illuminate\Support\Facades\Storage;
use Illuminate\Http\Request;

class ProductController 
{
    public function list(){
        $products = Product::latest()->paginate(15);
        return view('admin.products.list',compact('products'));
    }

    public function create(){
        $categories = Category::all();
        return view('admin.products.create',compact('categories'));
    }

    public function save(ProductSaveRequest $request){
        $input=$request->validated();
        if($request->hasFile('image')){
             $extension = $request->image->extension();
             $filename =Str::random(6)."_".time()."_product.".$extension;
             $request->image->storeAs('images',$filename);
             $input['image'] = $filename;
        }
        
        Product::create($input);
        
        return redirect()->route('admin.product.list')->with('message','Product Saved Successfully');
    }

    public function delete($id){
        $product=Product::find(decrypt($id));
        if(!empty($product->image)){
            Storage::delete('images/'.$product->image);
        }
        $product->delete();
        return redirect()->route('admin.product.list')->with('message','Product Deleted Successfully');
    }

    public function edit($id){
        $product=Product::find(decrypt($id));
        $categories = Category::all();
        return view('admin.products.edit',compact('product','categories'));
    }
    public function update(ProductSaveRequest $request){
        $input=$request->validated();
        $product=Product::find(decrypt($request->product_id));
        if($request->hasFile('image')){
            Storage::delete('images/'.$product->image);
            $extension = $request->image->extension();
            $filename =Str::random(6)."_".time()."_product.".$extension;
            $request->image->storeAs('images',$filename);
            $input['image'] = $filename;

        }
        $product->update($input);
        
        return redirect()->route('admin.product.list')->with('message','Product Updated Successfully!!!');
    }
}


