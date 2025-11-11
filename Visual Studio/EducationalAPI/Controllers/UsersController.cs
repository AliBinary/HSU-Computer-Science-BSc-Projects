using System.Data;
using EducationalAPI.Data.DbContext;
using EducationalAPI.Entities;
using Microsoft.AspNetCore.Mvc;
using Dapper;

namespace EducationalAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UsersController : ControllerBase
    {
        private readonly DapperContext _context;

        public UsersController(DapperContext context)
        {
            _context = context;
        }

        [HttpPost("CreateUser")]
        public async Task<IActionResult> CreateUser(User user)
        {
            using var connection = _context.CreateConnection();

            await connection.ExecuteAsync(
                "sp_CreateUser",
                new { user.Username, user.Email, user.PasswordHash },
                commandType: CommandType.StoredProcedure
            );

            return Ok("User created successfully");
        }
    }
}
