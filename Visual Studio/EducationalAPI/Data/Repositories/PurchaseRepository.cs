using Dapper;
using EducationalAPI.Data.Contracts;
using EducationalAPI.Data.DbContext;
using EducationalAPI.Entities;

namespace EducationalAPI.Data.Repositories
{
    public class PurchaseRepository : IPurchaseRepository
    {
        private readonly DapperContext _context;

        public PurchaseRepository(DapperContext context)
        {
            _context = context;
        }

        public async Task<IEnumerable<Purchase>> GetAllPurchasesAsync()
        {
            var query = "SELECT * FROM Purchases";
            using var connection = _context.CreateConnection();
            return await connection.QueryAsync<Purchase>(query);
        }

        public async Task<Purchase?> GetPurchaseByIdAsync(int id)
        {
            var query = "SELECT * FROM Purchases WHERE PurchaseID = @Id";
            using var connection = _context.CreateConnection();
            return await connection.QueryFirstOrDefaultAsync<Purchase>(query, new { Id = id });
        }

        public async Task<int> CreatePurchaseAsync(Purchase purchase)
        {
            var query = @"
                INSERT INTO Purchases (UserID, CourseID, PurchaseDate, AmountPaid)
                VALUES (@UserID, @CourseID, @PurchaseDate, @AmountPaid);
                SELECT CAST(SCOPE_IDENTITY() AS INT);";
            using var connection = _context.CreateConnection();
            return await connection.QuerySingleAsync<int>(query, purchase);
        }

        public async Task<bool> UpdatePurchaseAsync(Purchase purchase)
        {
            var query = @"
                UPDATE Purchases
                SET UserID = @UserID, CourseID = @CourseID, AmountPaid = @AmountPaid
                WHERE PurchaseID = @PurchaseID";
            using var connection = _context.CreateConnection();
            var rowsAffected = await connection.ExecuteAsync(query, purchase);
            return rowsAffected > 0;
        }

        public async Task<bool> DeletePurchaseAsync(int id)
        {
            var query = "DELETE FROM Purchases WHERE PurchaseID = @Id";
            using var connection = _context.CreateConnection();
            var rowsAffected = await connection.ExecuteAsync(query, new { Id = id });
            return rowsAffected > 0;
        }

        public Task<IEnumerable<Purchase>> GetPurchasesByUserIdAsync(int userId)
        {
            throw new NotImplementedException();
        }
    }
}
