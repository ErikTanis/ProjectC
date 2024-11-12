using System;
using System.Collections.Generic;

namespace ProjectC.Models
{
    public class Transfer
    {
        public required int Id { get; set; }
        public required string Reference { get; set; }
        public required int? TransferFrom { get; set; }
        public required int TransferTo { get; set; }
        public required string TransferStatus { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime UpdatedAt { get; set; } = DateTime.Now;
        public required List<ItemInfo> Items { get; set; }
    }
}