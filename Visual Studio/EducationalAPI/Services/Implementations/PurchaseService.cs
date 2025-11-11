using EducationalAPI.Data.DbContext;
using EducationalAPI.Data.Contracts;
using EducationalAPI.Entities;
using EducationalAPI.Services.Contracts;
using Dapper;

namespace EducationalAPI.Services.Implementations
{
    public class PurchaseService : IPurchaseService
    {
        private readonly IPurchaseRepository _purchaseRepository;
        private readonly DapperContext _context;

        public PurchaseService(IPurchaseRepository purchaseRepository, DapperContext context)
        {
            _purchaseRepository = purchaseRepository;
            _context = context; // تزریق DapperContext
        }

        public async Task<IEnumerable<Purchase>> GetAllPurchasesAsync()
        {
            return await _purchaseRepository.GetAllPurchasesAsync();
        }

        public async Task<Purchase?> GetPurchaseByIdAsync(int purchaseId)
        {
            return await _purchaseRepository.GetPurchaseByIdAsync(purchaseId);
        }

        public async Task<Purchase> CreatePurchaseAsync(Purchase purchase)
        {
            var query = @"
            INSERT INTO Purchases (UserID, CourseID, PurchaseDate, AmountPaid)
            VALUES (@UserID, @CourseID, @PurchaseDate, @AmountPaid);
            SELECT CAST(SCOPE_IDENTITY() as int);";

            using var connection = _context.CreateConnection(); // ایجاد اتصال به دیتابیس
            var id = await connection.QuerySingleAsync<int>(query, purchase);

            purchase.PurchaseID = id; // مقدار PurchaseID را تنظیم کنید
            return purchase;          // شیء کامل را بازگردانید
        }

        public async Task<IEnumerable<Purchase>> GetPurchasesByUserIdAsync(int userId)
        {
            return await _purchaseRepository.GetPurchasesByUserIdAsync(userId);
        }

        public Task<bool> DeletePurchaseAsync(int id)
        {
            throw new NotImplementedException();
        }

        public Task<bool> UpdatePurchaseAsync(Purchase purchase)
        {
            throw new NotImplementedException();
        }
    }
}
