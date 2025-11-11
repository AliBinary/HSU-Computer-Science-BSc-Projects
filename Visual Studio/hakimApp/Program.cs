using hakimApp.Data.Contracts;
using hakimApp.Data.DbContext;
using hakimApp.Data.Repositories;
using hakimApp.Services.Contracts;
using hakimApp.Services.Implementations;
using hakimApp.WebFrameWork.Helpers;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using Microsoft.OpenApi.Models;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
//builder.Services.AddSwaggerGen();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo { Title = "HakimUniversityWebAPI", Version = "v1" });
    c.OperationFilter<RequierdHeaderParameters>();// for header

});
//// add new to program to support cors
builder.Services.AddCors();
builder.Services.AddCors(option => {
    option.AddPolicy("AllowOrigin", builder =>
    {
        builder.AllowAnyOrigin().AllowAnyHeader().AllowAnyMethod();
    });
});
builder.Services.AddSingleton<DapperContext>();
builder.Services.AddTransient(typeof(IRepository<>), typeof(Repository<>));//    Transient: New instance every time it’s requested.
builder.Services.AddTransient<ITokenService, TokenService>();
builder.Services.AddAuthorization();
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(option =>
    {
        option.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = TokenHelper.Issuer,
            ValidAudience = TokenHelper.Audience,
            IssuerSigningKey = new SymmetricSecurityKey(Convert.FromBase64String(TokenHelper.Secret))
        };
    });

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
///add new to program to support cors
app.UseCors();

app.UseAuthorization();

app.MapControllers();

app.Run();