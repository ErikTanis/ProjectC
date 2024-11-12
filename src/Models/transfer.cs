using System;

namespace ProjectC.Models
{
    public class Transfer
    {
        public required string Reference { get; set; }
        public required string TransferFrom { get; set; }
        public required string TransferTo { get; set; }
        public required string TransferStatus { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.Now;
        public DateTime UpdatedAt { get; set; }

    }

}