<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\User\HomePageController;



Route::get('/', [HomePageController::class,'home']);