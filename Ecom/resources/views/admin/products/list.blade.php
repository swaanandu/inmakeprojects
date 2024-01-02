@extends('admin.layout.master')
@section('content')
 
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>Products {{$products->total()}}</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">Products</li>
            </ol>
          </div>
        </div>
      </div><!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-header">
                <!-- <h3 class="card-title">Bordered Table</h3> -->
              </div>
              <!-- /.card-header -->
              <div class="card-header">
               <a href="{{route('admin.product.create')}}" class="btn btn-primary">Add Product</a>
              @if(session()->has('message'))<p class="flashmessage">{{session()->get('message')}}</p>@endif
              </div>
              <div class="card-body">
                <table class="table table-bordered">
                  <thead>
                    <tr>
                      <th style="width: 8%">SI No:</th>
                      <th>Image</th>
                      <th>Name</th>
                      <th>Category</th>
                      <th>Price</th>
                      <th>Status</th>
                      <th>Favourite</th>
                      <th style="width: 15%">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                @foreach($products as $product)
                <tr>
                  <td>{{$loop->iteration}}</td>
                  <!-- first edit .env file -->
                  <td><img src="{{ asset('storage/images/'.$product->image)}}" width="100" height="100"alt=""></td>
                  <td>{{$product->name}}</td>
                  <td>{{$product->category->name}}</td>
                  <td>{{number_format($product->price,2)}}</td>
                  <!-- without using accessors -->
                  <!-- <td>@if($product->status ==1)Active @else Inactive @endif</td> -->
                    <td>{{$product->status_text}}</td>

                  <!-- using accessors -->
                  <td>{{$product->is_favourite_text}}</td>
                  <td>
                    <a href="{{route('admin.product.edit',encrypt($product->id))}}" class="btn btn-primary btn-sm">Edit</a>
                    <a href="{{route('admin.product.delete',encrypt($product->id))}}" class="btn btn-danger btn-sm">Delete</a>
                  </td>
                </tr>
                @endforeach
                  </tbody>
                </table>
              </div>
              <!-- /.card-body -->
              <div class="card-footer clearfix">
                <!-- pagination here and edit AppServiceProvider --> 
               {{ $products -> links()}}
              </div>
            </div>
            <!-- /.card -->

           
              <!-- /.card-body -->
          
            <!-- /.card -->
          </div>
        </div>
        <!-- /.row -->
      </div><!-- /.container-fluid -->
    </section>
    <!-- /.content -->
  </div>
  <!-- /.content-wrapper -->
  @endsection