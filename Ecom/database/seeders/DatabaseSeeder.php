<?php

namespace Database\Seeders;
use App\Models\Admin;
use App\Models\Product;
// use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        Product::factory(1000)->create();
        $this->call(AdminSeeder::class);
        $this->call(CategorySeeder::class);

    }
}
