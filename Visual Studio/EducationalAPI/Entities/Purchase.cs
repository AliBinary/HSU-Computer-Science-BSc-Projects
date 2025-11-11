namespace EducationalAPI.Entities
{
    public class Purchase
    {
        public int PurchaseID { get; set; }
        public int UserID { get; set; }
        public int CourseID { get; set; }
        public DateTime PurchaseDate { get; set; } = DateTime.UtcNow;
        public decimal AmountPaid { get; set; }
    }
}
