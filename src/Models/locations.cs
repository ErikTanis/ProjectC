using System;

namespace ProjectC.Models
{
    public class Location
    {
        public int Id { get; set; }
        public int WarehouseId { get; set; }
        public string Code { get; set; }
        public string Name { get; set; }
        public DateTime CreatedAt { get; set; }
        public DateTime UpdatedAt { get; set; }

        public Location(int id, int warehouseId, string code, string name, DateTime createdAt, DateTime updatedAt)
        {
            Id = id;
            WarehouseId = warehouseId;
            Code = code;
            Name = name;
            CreatedAt = createdAt;
            UpdatedAt = updatedAt;
        }
    }
}