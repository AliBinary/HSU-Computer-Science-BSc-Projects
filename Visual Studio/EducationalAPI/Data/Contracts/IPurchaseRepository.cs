using EducationalAPI.Entities;

namespace EducationalAPI.Data.Contracts
{
    public interface IPurchaseRepository
    {
        Task<IEnumerable<Purchase>> GetAllPurchasesAsync();
        Task<Purchase?> GetPurchaseByIdAsync(int id);
        Task<int> CreatePurchaseAsync(Purchase purchase);
        Task<bool> UpdatePurchaseAsync(Purchase purchase);
        Task<bool> DeletePurchaseAsync(int id);
        Task<IEnumerable<Purchase>> GetPurchasesByUserIdAsync(int userId);
    }
}
