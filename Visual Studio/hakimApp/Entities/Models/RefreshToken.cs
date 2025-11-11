namespace hakimApp.Entities.Models
{
    public class RefreshToken
    {
        public int Id { get; set; }
        public int FK_User_Id { get; set; }
        public string TokenHash { get; set; }
        public string TokenSalt { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime ExpireDate { get; set; }
    }
}
