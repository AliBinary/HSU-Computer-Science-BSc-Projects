using Microsoft.Data.SqlClient;
using OnlineStoreAPI.Repositories; // فضای اسمی پروژه‌ی خود را جایگزین کنید
using Dapper;

var builder = WebApplication.CreateBuilder(args);

// اضافه کردن سرویس‌های مورد نیاز به DI Container
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// تنظیم اتصال دیتابیس برای Dapper
builder.Services.AddScoped<SqlConnection>(_ =>
    new SqlConnection(builder.Configuration.GetConnectionString("DefaultConnection")));

// اضافه کردن Repositoryها به DI Container
builder.Services.AddScoped<CustomerRepository>();
builder.Services.AddScoped<OrderRepository>();

var app = builder.Build();

// استفاده از Swagger در حالت توسعه
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
