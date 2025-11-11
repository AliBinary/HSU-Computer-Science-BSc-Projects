namespace hakimApp.Entities.Dto.User
{
    public class LonginResultDto
    {
        public int Id { get; set; }
        public string LoginHash { get; set; }
        public string SecurityCode { get; set; }
        public string FullName { get; set; }
        public string ContactNumber { get; set; }
    }
}
