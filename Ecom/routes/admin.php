<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Admin\LoginController;
use App\Http\Controllers\Admin\DashboardController;
use App\Http\Controllers\Admin\ProductController;
use App\Http\Requests\ProductSaveRequest;


Route::name('admin.')->group(function(){
    Route::get('admin/login', [LoginController::class,'login'])->name('login');
    Route::post('admin/do-login', [LoginController::class,'doLogin'])->name('do.login');

  Route::middleware('auth:admin')->group(function(){

        Route::get('admin/dashboard', [DashboardController::class,'dashboard'])->name('dashboard');
        Route::get('admin/logout', [LoginController::class,'logout'])->name('logout');

        // route controller class grouping
        // Route::name('product.')->prefix('admin/products')->controller(ProductController::class)->group(function(){

        Route::name('product.')->prefix('admin/products')->group(function(){
            Route::get('/', [ProductController::class,'list'])->name('list');
            Route::get('create', [ProductController::class,'create'])->name('create');
            Route::post('save', [ProductController::class,'save'])->name('save');
            Route::get('delete/{id}',[ProductController::class,'delete'])->name('delete');
            Route::get('edit/{id}',[ProductController::class,'edit'])->name('edit');
            Route::POST('update',[ProductController::class,'update'])->name('update');
        });
    });
});