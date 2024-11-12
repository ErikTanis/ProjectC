using System;

namespace ProjectC.Models
{
    public class Location
    {
        public required int Id { get; set; }
        public required int WarehouseId { get; set; }
        public required string Code { get; set; }
        public required string Name { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime UpdatedAt { get; set; } = DateTime.Now;
    }
}