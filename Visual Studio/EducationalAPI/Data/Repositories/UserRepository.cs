using Dapper;
using EducationalAPI.Data.Contracts;
using EducationalAPI.Data.DbContext;
using EducationalAPI.Entities;

namespace EducationalAPI.Data.Repositories
{
    public class UserRepository : IUserRepository
    {
        private readonly DapperContext _context;

        public UserRepository(DapperContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<User>> GetAllUsersAsync()
        {
            var query = "SELECT * FROM Users WHERE IsDeleted = 0";
            using var connection = _context.CreateConnection();
            return await connection.QueryAsync<User>(query);
        }

        public async Task<User?> GetUserByIdAsync(int userId)
        {
            var query = "SELECT * FROM Users WHERE UserID = @UserId AND IsDeleted = 0";
            using var connection = _context.CreateConnection();
            return await connection.QuerySingleOrDefaultAsync<User>(query, new { UserId = userId });
        }

        public async Task<User> CreateUserAsync(User user)
        {
            var query = @"
                INSERT INTO Users (Username, Email, PasswordHash, CreatedAt, IsDeleted)
                VALUES (@Username, @Email, @PasswordHash, @CreatedAt, @IsDeleted);
                SELECT CAST(SCOPE_IDENTITY() as int);";

            using var connection = _context.CreateConnection();
            var id = await connection.QuerySingleAsync<int>(query, user);
            user.UserID = id;
            return user;
        }

        public async Task<bool> UpdateUserAsync(int userId, User updatedUser)
        {
            var query = @"
                UPDATE Users
                SET Username = @Username, Email = @Email, PasswordHash = @PasswordHash, IsDeleted = @IsDeleted
                WHERE UserID = @UserId";

            using var connection = _context.CreateConnection();
            var rowsAffected = await connection.ExecuteAsync(query, new
            {
                updatedUser.Username,
                updatedUser.Email,
                updatedUser.PasswordHash,
                updatedUser.IsDeleted,
                UserId = userId
            });

            return rowsAffected > 0;
        }

        public async Task<bool> DeleteUserAsync(int userId)
        {
            var query = "UPDATE Users SET IsDeleted = 1 WHERE UserID = @UserId";
            using var connection = _context.CreateConnection();
            var rowsAffected = await connection.ExecuteAsync(query, new { UserId = userId });
            return rowsAffected > 0;
        }
    }
}
