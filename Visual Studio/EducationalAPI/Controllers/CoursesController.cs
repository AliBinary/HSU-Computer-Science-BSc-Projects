using System.Data;
using EducationalAPI.Data.DbContext;
using EducationalAPI.Entities;
using Microsoft.AspNetCore.Mvc;
using Dapper;

namespace EducationalAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class CoursesController : ControllerBase
    {
        private readonly DapperContext _context;

        public CoursesController(DapperContext context)
        {
            _context = context;
        }

        [HttpPost("CreateCourse")]
        //public async Task<IActionResult> CreateCourse(Course course)
        //{
        //    using var connection = _context.CreateConnection();

        //    await connection.ExecuteAsync(
        //        "sp_CreateCourse",
        //        new { course.Title, course.Description, course.Price },
        //        commandType: CommandType.StoredProcedure
        //    );

        //    return Ok("Course created successfully");
        //}
        public async Task<int> CreateCourse(Course course)
        {
            var query = "INSERT INTO Courses (Title, Description, Price) VALUES (@Title, @Description, @Price)";
            using var connection = CreateConnection();
            return await connection.ExecuteAsync(query, course);
        }

    }
}
