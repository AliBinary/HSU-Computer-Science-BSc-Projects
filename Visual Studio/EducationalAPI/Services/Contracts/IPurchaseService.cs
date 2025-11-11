using EducationalAPI.Entities;

namespace EducationalAPI.Services.Contracts
{
    public interface IPurchaseService
    {
        Task<IEnumerable<Purchase>> GetAllPurchasesAsync();
        Task<Purchase?> GetPurchaseByIdAsync(int purchaseId);
        Task<Purchase> CreatePurchaseAsync(Purchase purchase);
        Task<IEnumerable<Purchase>> GetPurchasesByUserIdAsync(int userId);
        Task<bool> DeletePurchaseAsync(int id);
        Task<bool> UpdatePurchaseAsync(Purchase purchase);
    }
}
