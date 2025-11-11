using Dapper;
using EducationalAPI.Data.Contracts;
using EducationalAPI.Data.DbContext;
using EducationalAPI.Entities;

namespace EducationalAPI.Data.Repositories
{
    public class CourseRepository : ICourseRepository
    {
        private readonly DapperContext _context;

        public CourseRepository(DapperContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<Course>> GetAllCoursesAsync()
        {
            var query = "SELECT * FROM Courses WHERE IsDeleted = 0;";
            using var connection = _context.CreateConnection();
            return await connection.QueryAsync<Course>(query);
        }

        public async Task<Course?> GetCourseByIdAsync(int courseId)
        {
            var query = "SELECT * FROM Courses WHERE CourseID = @CourseID AND IsDeleted = 0;";
            using var connection = _context.CreateConnection();
            return await connection.QuerySingleOrDefaultAsync<Course>(query, new { CourseID = courseId });
        }

        public async Task<Course> CreateCourseAsync(Course course)
        {
            var query = @"
                INSERT INTO Courses (Title, Description, Price, CreatedAt)
                VALUES (@Title, @Description, @Price, @CreatedAt);
                SELECT CAST(SCOPE_IDENTITY() as int);";

            using var connection = _context.CreateConnection();
            var id = await connection.QuerySingleAsync<int>(query, course);
            course.CourseID = id;
            return course;
        }

        public async Task<bool> UpdateCourseAsync(int courseId, Course updatedCourse)
        {
            var query = @"
                UPDATE Courses
                SET Title = @Title, Description = @Description, Price = @Price
                WHERE CourseID = @CourseID AND IsDeleted = 0;";
            using var connection = _context.CreateConnection();
            var rowsAffected = await connection.ExecuteAsync(query, new { updatedCourse.Title, updatedCourse.Description, updatedCourse.Price, CourseID = courseId });
            return rowsAffected > 0;
        }

        public async Task<bool> DeleteCourseAsync(int courseId)
        {
            var query = "UPDATE Courses SET IsDeleted = 1 WHERE CourseID = @CourseID;";
            using var connection = _context.CreateConnection();
            var rowsAffected = await connection.ExecuteAsync(query, new { CourseID = courseId });
            return rowsAffected > 0;
        }
    }
}
