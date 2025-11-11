namespace hakimApp.Entities.Dto.TokenDto
{
    public class TokenResponseDto
    {
        public int UserId { get; set; }
        public string AccessToken { get; set; }
        public string RefreshToken { get; set; }

        public string FullName { get; set; }
        public string PhoneNo { get; set; }
    }
}
